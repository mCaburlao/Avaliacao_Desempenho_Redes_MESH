#!/usr/bin/env python3
"""
analyze_all.py — Analise agregada: AODV vs OLSR em 3 topologias

Topologias:
  chain-9   (9 nos, linear)
  grid-25   (25 nos, grid 5x5)
  random-50 (50 nos, aleatorio)

Metricas por experimento (FlowMonitor + trace-app-rx):
  1. PDR %           Packet Delivery Ratio
  2. Latencia media  Delay E2E medio (ms)
  3. Jitter medio    Variacao do delay (ms)
  4. Taxa de perda % lostPkts / txPkts
  5. Latencia max    Pior caso (ms)
  6. Throughput      kbps de dados recebidos
  7. Hops medios     timesForwarded / rxPkts — proxy de overhead de roteamento

Saida:
  - Tabela comparativa no terminal
  - experiments/results.csv
"""

import xml.etree.ElementTree as ET
from pathlib import Path
import csv

BASE = Path("/mnt/d/OneDrive/Documentos/UFABC/2026.1/Avaliacao_Desempenho_Redes_MESH")
EXPERIMENTS = BASE / "experiments"

# Experimentos definidos: (label, out_dir, duration_s)
# (topo_label, exp_subdir, duration_s, num_nodes)
SUITE = [
    ("chain-9",     "pilot_100_aodv_olsr",  400,     9),
    ("grid-25",     "grid_25nodes",          500,    25),
    ("random-50",   "random_50nodes",        600,    50),
    ("random-100",  "random_100nodes",       700,   100),
    ("random-200",  "random_200nodes",       800,   200),
    ("random-500",  "random_500nodes",       700,   500),
    ("random-1000", "random_1000nodes",      800,  1000),
    ("random-2000", "random_2000nodes",      900,  2000),
]

# Mapa rapido: label → num_nodes (usado no CSV)
TOPO_NODES = {label: n for label, _, _, n in SUITE}

PROTOCOLS = ["AODV", "OLSR"]


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


def parse_traces(out_dir):
    """Soma bytes e calcula throughput de todos os trace-app-rx-*.txt."""
    total_bytes = 0.0
    total_kbps  = 0.0
    for fpath in sorted(out_dir.glob("trace-app-rx-*.txt")):
        t_start = t_end = None
        last_bytes = 0
        with open(fpath) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                parts = line.split()
                if len(parts) == 2:
                    t_us = int(parts[0])
                    b    = int(parts[1])
                    if t_start is None:
                        t_start = t_us
                    t_end     = t_us
                    last_bytes = b
        if t_start is not None and t_end is not None and t_end > t_start:
            dur_s = (t_end - t_start) / 1e6
        else:
            dur_s = None   # sem dados
        total_bytes += last_bytes
        if dur_s and dur_s > 0:
            total_kbps += (last_bytes * 8) / dur_s / 1000
    return total_bytes, total_kbps


def parse_flowmonitor(fpath):
    """Extrai metricas por fluxo. Retorna lista de dicts (apenas fluxos com tx>0)."""
    if not fpath.exists():
        return []
    flows = []
    for flow in ET.parse(fpath).findall(".//Flow"):
        tx   = int(flow.get("txPackets", 0))
        rx   = int(flow.get("rxPackets", 0))
        lost = int(flow.get("lostPackets", 0))
        fwd  = int(flow.get("timesForwarded", 0))
        if tx == 0:
            continue

        delay_ns     = _ns3_time_to_ns(flow.get("delaySum",  "0ns"))
        jitter_ns    = _ns3_time_to_ns(flow.get("jitterSum", "0ns"))
        max_delay_ns = _ns3_time_to_ns(flow.get("maxDelay",  "0ns"))

        flows.append({
            "tx":            tx,
            "rx":            rx,
            "lost":          lost,
            "pdr":           rx / tx * 100,
            "loss":          lost / tx * 100,
            "avg_delay_ms":  (delay_ns  / rx / 1e6) if rx > 0 else 0.0,
            "avg_jitter_ms": (jitter_ns / max(rx - 1, 1) / 1e6) if rx > 1 else 0.0,
            "max_delay_ms":  max_delay_ns / 1e6,
            "avg_hops":      fwd / rx if rx > 0 else 0.0,
        })
    return flows


def _weighted_mean(vals, weights):
    w = sum(weights)
    return sum(v * wt for v, wt in zip(vals, weights)) / w if w > 0 else 0.0


def compute_metrics(out_dir):
    """Retorna dict de metricas para um diretorio de saida, ou None se vazio."""
    fmon = out_dir / "flowdata.xml"
    flows = parse_flowmonitor(fmon)
    if not flows:
        return None

    tx_total   = sum(f["tx"]   for f in flows)
    rx_total   = sum(f["rx"]   for f in flows)
    lost_total = sum(f["lost"] for f in flows)
    rx_counts  = [f["rx"] for f in flows]

    _, total_kbps = parse_traces(out_dir)

    return {
        "pdr":          rx_total / tx_total * 100,
        "loss":         lost_total / tx_total * 100,
        "avg_delay_ms": _weighted_mean([f["avg_delay_ms"]  for f in flows], rx_counts),
        "avg_jitter_ms":_weighted_mean([f["avg_jitter_ms"] for f in flows], rx_counts),
        "max_delay_ms": max(f["max_delay_ms"] for f in flows),
        "throughput_kbps": total_kbps,
        "avg_hops":     _weighted_mean([f["avg_hops"]      for f in flows], rx_counts),
        "tx": tx_total, "rx": rx_total, "lost": lost_total,
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
    print("Analise AODV vs OLSR — Suite escalabilidade 9-2000 nos")
    print("chain-9 | grid-25 | r-50 | r-100 | r-200 | r-500 | r-1000 | r-2000")

    all_results = {}

    for topo_label, exp_subdir, _duration, _num_nodes in SUITE:
        exp_path = EXPERIMENTS / exp_subdir
        results  = {}
        for proto in PROTOCOLS:
            out_dir = exp_path / f"out_{proto}"
            results[proto] = compute_metrics(out_dir) if out_dir.exists() else None
        all_results[topo_label] = results
        print_comparison(topo_label, results)

    export_csv(all_results, EXPERIMENTS / "results.csv")
    print()
