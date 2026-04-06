#!/usr/bin/env python3
"""
analyze_all.py — Analise agregada: AODV vs OLSR em 3 topologias

Metricas por experimento (FlowMonitor):
  1. PDR %           Packet Delivery Ratio  (normalizado por N_STAS*PKTS_PER_STA)
  2. Latencia media  Delay E2E medio (ms)
  3. Jitter medio    Variacao do delay (ms)
  4. Taxa de perda % (1 - PDR)
  5. Latencia max    Pior caso (ms)
  6. Throughput      kbps (rxBytes das flows forward / janela de medicao)
  7. Hops medios     timesForwarded / rxPkts — proxy de overhead de roteamento

Correcoes implementadas:
  - Somente flows STA->backhaul UDP (forward) sao contadas via FlowClassifier,
    excluindo echo-replies (backhaul->STA) e flows TCP.
  - PDR normalizado contra N_STAS * PKTS_PER_STA para comparacao justa
    entre AODV (que tenta enviar e falha) e OLSR (que silencia para destinos
    inalcancaveis, resultando em tx=0 no FlowMonitor).
  - Throughput calculado a partir de rxBytes do FlowMonitor, nao de trace files
    (que apenas rastreavam o TCP para a STA mais distante, frequentemente
    inalcancavel).

Saida:
  - Tabela comparativa no terminal
  - experiments/results.csv
"""

import xml.etree.ElementTree as ET
from pathlib import Path
import csv

BASE = Path("/mnt/d/OneDrive/Documentos/UFABC/2026.1/Avaliacao_Desempenho_Redes_MESH")
EXPERIMENTS = BASE / "experiments"

# Experimentos definidos: (topo_label, exp_subdir, duration_s, num_nodes, warmup_s)
# warmup_s: instante de inicio dos fluxos de medicao; flows antes disso sao probes
# duration_s = warmup_s + 105  (25s stagger+tcp + 50s medicao + 30s buffer)
SUITE = [
    ("grid-25",      "grid_25nodes",          240,    25,  120),
    ("random-50",    "random_50nodes",        300,    50,  180),
    ("random-75",    "random_75nodes",        330,    75,  210),
    ("random-100",   "random_100nodes",       360,   100,  240),
    ("random-150",   "random_150nodes",       390,   150,  270),
    ("random-200",   "random_200nodes",       420,   200,  300),
    ("random-300",   "random_300nodes",       450,   300,  330),
    ("random-500",   "random_500nodes",       480,   500,  360),
    ("random-750",   "random_750nodes",       510,   750,  390),
    ("random-1000",  "random_1000nodes",      540,  1000,  420),
]

# Mapa rapido: label → num_nodes (usado no CSV)
TOPO_NODES = {label: n for label, _, _, n, _ in SUITE}

PROTOCOLS = ["AODV", "OLSR"]

# Parametros da suite de medicao — devem coincidir com generate_all_configs.py
N_STAS       = 5    # FIXED_N_STAS: STAs por topologia
PKTS_PER_STA = 100  # MaxPackets no echo_client de cada STA
STA_SUBNET   = "10.4.128."   # Prefixo IP das STAs
BACKHAUL_IP  = "10.1.1.1"   # IP do backhaul (no 0 mesh)


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------
def _ns3_time_to_ns(s):
    """'+3.30011e+08ns' → float nanosegundos."""
    cleaned = (s or "0").lstrip("+").rstrip("ns").strip()
    try:
        return float(cleaned)
    except ValueError:
        return 0.0


def parse_flowclassifier(fpath):
    """Retorna dict {flowId (int) -> {'src': str, 'dst': str, 'protocol': int}}.

    Usado para distinguir flows forward (STA->backhaul) de echo-replies
    (backhaul->STA) e flows TCP, que nao devem ser contados no PDR."""
    if not fpath.exists():
        return {}
    classifier = {}
    for flow in ET.parse(fpath).findall(".//Ipv4FlowClassifier/Flow"):
        fid = int(flow.get("flowId"))
        classifier[fid] = {
            "src":      flow.get("sourceAddress"),
            "dst":      flow.get("destinationAddress"),
            "protocol": int(flow.get("protocol")),
        }
    return classifier


def _is_fwd_udp(flow_id, classifier):
    """True se o flow e STA->backhaul UDP (forward de medicao).

    Exclui echo-replies (backhaul->STA) e flows TCP (file transfer).
    Fluxos sem entrada no classifier sao descartados (controle/ARP)."""
    info = classifier.get(flow_id)
    if info is None:
        return False
    return (
        info["src"].startswith(STA_SUBNET)
        and info["dst"] == BACKHAUL_IP
        and info["protocol"] == 17  # UDP
    )


def parse_flowmonitor(fpath, min_start_ns=0, classifier=None):
    """Extrai metricas apenas de flows STA->backhaul UDP com tx>0.

    min_start_ns: descarta flows cujo primeiro pacote foi anterior a este
                  instante (ns) — filtra probe flows de warmup.
    classifier:   dict retornado por parse_flowclassifier(); se None, aceita
                  todos os flows (compatibilidade retroativa)."""
    if not fpath.exists():
        return []
    flows = []
    for flow in ET.parse(fpath).findall(".//FlowStats/Flow"):
        fid = int(flow.get("flowId"))
        tx  = int(flow.get("txPackets", 0))
        rx  = int(flow.get("rxPackets", 0))
        if tx == 0:
            continue
        if classifier is not None and not _is_fwd_udp(fid, classifier):
            continue
        if min_start_ns > 0 and _ns3_time_to_ns(flow.get("timeFirstTxPacket", "0ns")) < min_start_ns:
            continue

        lost     = int(flow.get("lostPackets", 0))
        fwd      = int(flow.get("timesForwarded", 0))
        rx_bytes = int(flow.get("rxBytes", 0))

        delay_ns     = _ns3_time_to_ns(flow.get("delaySum",  "0ns"))
        jitter_ns    = _ns3_time_to_ns(flow.get("jitterSum", "0ns"))
        max_delay_ns = _ns3_time_to_ns(flow.get("maxDelay",  "0ns"))

        flows.append({
            "tx":            tx,
            "rx":            rx,
            "rx_bytes":      rx_bytes,
            "lost":          lost,
            "avg_delay_ms":  (delay_ns  / rx / 1e6) if rx > 0 else 0.0,
            "avg_jitter_ms": (jitter_ns / max(rx - 1, 1) / 1e6) if rx > 1 else 0.0,
            "max_delay_ms":  max_delay_ns / 1e6,
            "avg_hops":      fwd / rx if rx > 0 else 0.0,
        })
    return flows


def _weighted_mean(vals, weights):
    w = sum(weights)
    return sum(v * wt for v, wt in zip(vals, weights)) / w if w > 0 else 0.0


def compute_metrics(out_dir, warmup_s=0, duration_s=0):
    """Retorna dict de metricas para um diretorio de saida, ou None se vazio.

    Apenas flows STA->backhaul UDP (forward) sao contados.
    PDR e perda sao normalizados contra N_STAS * PKTS_PER_STA para que
    AODV e OLSR sejam comparaveis (OLSR nao enfileira para destinos
    inalcancaveis, resultando em tx=0 que o FlowMonitor exclui).
    Throughput e calculado a partir de rxBytes do FlowMonitor dividido
    pela janela de medicao (duration_s - warmup_s)."""
    fmon = out_dir / "flowdata.xml"
    classifier = parse_flowclassifier(fmon)
    flows = parse_flowmonitor(fmon, min_start_ns=warmup_s * 1e9, classifier=classifier)

    # Sem flows STA->backhaul = simulacao nao gerou dados de medicao
    if not flows:
        return None

    rx_total    = sum(f["rx"]       for f in flows)
    rx_bytes    = sum(f["rx_bytes"] for f in flows)
    # tx contado pelo FlowMonitor pode diferir entre protocolos (OLSR omite
    # flows onde nao ha rota); usa denominador fixo para comparacao justa.
    expected    = N_STAS * PKTS_PER_STA
    lost_norm   = expected - rx_total
    rx_counts   = [f["rx"] for f in flows]

    measurement_s = max(duration_s - warmup_s, 1)
    throughput_kbps = rx_bytes * 8 / measurement_s / 1000

    # tx/rx/lost no CSV refletem os valores brutos do FlowMonitor (forward flows)
    tx_raw   = sum(f["tx"]   for f in flows)
    lost_raw = sum(f["lost"] for f in flows)

    return {
        "pdr":             rx_total / expected * 100,
        "loss":            lost_norm / expected * 100,
        "avg_delay_ms":    _weighted_mean([f["avg_delay_ms"]  for f in flows], rx_counts),
        "avg_jitter_ms":   _weighted_mean([f["avg_jitter_ms"] for f in flows], rx_counts),
        "max_delay_ms":    max(f["max_delay_ms"] for f in flows),
        "throughput_kbps": throughput_kbps,
        "avg_hops":        _weighted_mean([f["avg_hops"]      for f in flows], rx_counts),
        "tx": tx_raw, "rx": rx_total, "lost": lost_raw,
    }


# ---------------------------------------------------------------------------
# Impressao
# ---------------------------------------------------------------------------
METRIC_LABELS = [
    ("pdr",           "PDR (%)",                    "{:6.1f}%"),
    ("avg_delay_ms",  "Latencia media E2E (ms)",    "{:8.2f}"),
    ("avg_jitter_ms", "Jitter medio (ms)",           "{:8.2f}"),
    ("loss",          "Taxa de perda (%)",           "{:6.1f}%"),
    ("max_delay_ms",  "Latencia max, pior caso (ms)","{:8.2f}"),
    ("throughput_kbps","Throughput (kbps)",          "{:8.1f}"),
    ("avg_hops",      "Hops medios por pacote",      "{:7.2f}"),
]


def print_comparison(topo_label, results):
    """results = {'AODV': dict|None, 'OLSR': dict|None}"""
    print(f"\n{'━'*62}")
    print(f"  Topologia: {topo_label}")
    print(f"{'━'*62}")

    aodv = results.get("AODV")
    olsr = results.get("OLSR")

    if aodv is None and olsr is None:
        print("  (sem resultados — rode run_all_experiments.sh primeiro)")
        return

    W = 32
    print(f"\n  {'Metrica':<{W}}  {'AODV':>10}  {'OLSR':>10}")
    print(f"  {'-'*W}  {'-'*10}  {'-'*10}")

    for key, label, fmt in METRIC_LABELS:
        a_str = fmt.format(aodv[key]) if aodv else "     —"
        o_str = fmt.format(olsr[key]) if olsr else "     —"
        print(f"  {label:<{W}}  {a_str:>10}  {o_str:>10}")

    print(f"  {'-'*W}  {'-'*10}  {'-'*10}")
    for proto, m in [("AODV", aodv), ("OLSR", olsr)]:
        if m:
            print(f"  {proto} TX/RX/Lost: {m['tx']} / {m['rx']} / {m['lost']}")


# ---------------------------------------------------------------------------
# Exportar CSV
# ---------------------------------------------------------------------------
def export_csv(all_results, csv_path):
    rows = []
    for topo, results in all_results.items():
        for proto, m in results.items():
            if m is None:
                continue
            row = {"topology": topo, "num_nodes": TOPO_NODES.get(topo, 0), "protocol": proto}
            row.update({k: m[k] for k, _, _ in METRIC_LABELS})
            row["tx"] = m["tx"]
            row["rx"] = m["rx"]
            row["lost"] = m["lost"]
            rows.append(row)

    if not rows:
        return

    fields = (["topology", "num_nodes", "protocol"]
              + [k for k, _, _ in METRIC_LABELS]
              + ["tx", "rx", "lost"])
    with open(csv_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    print(f"\n  CSV salvo em: {csv_path.relative_to(BASE)}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("Analise AODV vs OLSR — Suite escalabilidade")
    print(f"PDR normalizado: {N_STAS} STAs x {PKTS_PER_STA} pkts = {N_STAS*PKTS_PER_STA} pkts esperados")
    print("Somente flows STA->backhaul UDP (forward) contados")

    all_results = {}

    for topo_label, exp_subdir, duration_s, _num_nodes, warmup_s in SUITE:
        exp_path = EXPERIMENTS / exp_subdir
        results  = {}
        for proto in PROTOCOLS:
            out_dir = exp_path / f"out_{proto}"
            results[proto] = (
                compute_metrics(out_dir, warmup_s=warmup_s, duration_s=duration_s)
                if out_dir.exists() else None
            )
        all_results[topo_label] = results
        print_comparison(topo_label, results)

    export_csv(all_results, EXPERIMENTS / "results.csv")
    print()
