#!/usr/bin/env python3
"""
analyze_pilot.py — Analise dos resultados piloto AODV vs OLSR

Metricas calculadas (todas sobre fluxos com tx > 0):
  1. PDR              — Packet Delivery Ratio (%)
  2. Latencia media   — Delay E2E medio (ms)
  3. Jitter medio     — Variacao do delay (ms), proxy de estabilidade
  4. Taxa de perda    — Pacotes perdidos / transmitidos (%)
  5. Latencia maxima  — Pior caso de delay (ms)
  6. Throughput total — Bytes de dados recebidos / duracao (kbps)
  7. Hops medios      — timesForwarded / rxPackets, proxy de overhead
"""

import os
import math
import xml.etree.ElementTree as ET
from pathlib import Path

BASE = Path("/mnt/d/OneDrive/Documentos/UFABC/2026.1/Avaliacao_Desempenho_Redes_MESH")
PILOT = BASE / "experiments/pilot_100_aodv_olsr"
DURATION = 60  # segundos simulados


def _ns3_time_to_ns(attr_str):
    """Converte string NS-3 de tempo ('+3.30011e+08ns' ou '+12345678ns') para float nanosegundos."""
    s = (attr_str or "0").lstrip("+").rstrip("ns").strip()
    try:
        return float(s)
    except ValueError:
        return 0.0


def parse_trace_rx(filepath):
    """Le trace-app-rx e retorna bytes totais recebidos e throughput."""
    tag_tx = "?"
    bytes_total = 0
    t_start = None
    t_end = None

    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line.startswith("# tags_tx"):
                tag_tx = line.split("=")[-1].strip()
            elif line and not line.startswith("#"):
                parts = line.split()
                if len(parts) == 2:
                    t_us = int(parts[0])
                    b = int(parts[1])
                    if t_start is None:
                        t_start = t_us
                    t_end = t_us
                    bytes_total = b  # cumulativo — ultima linha e o total

    duration_s = (t_end - t_start) / 1e6 if (t_start and t_end and t_end > t_start) else DURATION
    throughput_kbps = (bytes_total * 8) / duration_s / 1000
    return {"tag_tx": tag_tx, "bytes_total": bytes_total, "throughput_kbps": throughput_kbps}


def parse_flowmonitor(filepath):
    """
    Extrai metricas por fluxo do flowdata.xml.
    Retorna lista de dicts com: tx, rx, lost, pdr_pct, avg_delay_ms,
    avg_jitter_ms, max_delay_ms, loss_pct, avg_hops.
    Apenas fluxos com tx > 0 sao incluidos.
    """
    if not os.path.exists(filepath):
        return []

    tree = ET.parse(filepath)
    flows = []
    for flow in tree.findall(".//Flow"):
        tx       = int(flow.get("txPackets", 0))
        rx       = int(flow.get("rxPackets", 0))
        lost     = int(flow.get("lostPackets", 0))
        fwd      = int(flow.get("timesForwarded", 0))
        tx_bytes = int(flow.get("txBytes", 0))
        rx_bytes = int(flow.get("rxBytes", 0))

        if tx == 0:
            continue  # fluxo vazio (segunda passagem do FlowMonitor)

        delay_ns     = _ns3_time_to_ns(flow.get("delaySum",  "0ns"))
        jitter_ns    = _ns3_time_to_ns(flow.get("jitterSum", "0ns"))
        max_delay_ns = _ns3_time_to_ns(flow.get("maxDelay",  "0ns"))

        avg_delay_ms  = (delay_ns  / rx / 1e6) if rx > 0 else 0.0
        avg_jitter_ms = (jitter_ns / max(rx - 1, 1) / 1e6) if rx > 1 else 0.0
        max_delay_ms  = max_delay_ns / 1e6
        pdr_pct       = (rx / tx * 100) if tx > 0 else 0.0
        loss_pct      = (lost / tx * 100) if tx > 0 else 0.0
        avg_hops      = (fwd / rx) if rx > 0 else 0.0

        flows.append({
            "tx": tx, "rx": rx, "lost": lost,
            "pdr_pct":       pdr_pct,
            "loss_pct":      loss_pct,
            "avg_delay_ms":  avg_delay_ms,
            "avg_jitter_ms": avg_jitter_ms,
            "max_delay_ms":  max_delay_ms,
            "avg_hops":      avg_hops,
            "rx_bytes":      rx_bytes,
        })
    return flows


def _mean(vals):
    return sum(vals) / len(vals) if vals else 0.0


def _weighted_mean(vals, weights):
    total_w = sum(weights)
    return sum(v * w for v, w in zip(vals, weights)) / total_w if total_w > 0 else 0.0


def analyze(proto):
    print(f"\n{'='*55}")
    print(f"  PROTOCOLO: {proto}")
    print(f"{'='*55}")
    out_dir = PILOT / f"out_{proto}"

    if not out_dir.exists():
        print(f"  AVISO: {out_dir} nao encontrado. Rode run_pilot.sh primeiro.")
        return

    # --- Throughput total dos trace files ---
    traces = sorted(out_dir.glob("trace-app-rx-*.txt"))
    total_bytes = 0
    total_throughput_kbps = 0.0
    for t in traces:
        r = parse_trace_rx(t)
        total_bytes += r["bytes_total"]
        total_throughput_kbps += r["throughput_kbps"]

    # --- Metricas agregadas do FlowMonitor ---
    fmon = out_dir / "flowdata.xml"
    flows = parse_flowmonitor(fmon)

    if not flows:
        print("  FlowMonitor: flowdata.xml nao encontrado ou sem fluxos.")
        return

    tx_total   = sum(f["tx"]   for f in flows)
    rx_total   = sum(f["rx"]   for f in flows)
    lost_total = sum(f["lost"] for f in flows)

    # PDR e taxa de perda globais (por pacote, nao media de medias)
    pdr_global  = (rx_total / tx_total * 100) if tx_total > 0 else 0.0
    loss_global = (lost_total / tx_total * 100) if tx_total > 0 else 0.0

    # Latencia e jitter: media ponderada pelo numero de pacotes recebidos
    rx_counts = [f["rx"] for f in flows]
    avg_delay_ms  = _weighted_mean([f["avg_delay_ms"]  for f in flows], rx_counts)
    avg_jitter_ms = _weighted_mean([f["avg_jitter_ms"] for f in flows], rx_counts)
    max_delay_ms  = max(f["max_delay_ms"] for f in flows)
    avg_hops      = _weighted_mean([f["avg_hops"] for f in flows], rx_counts)

    # --- Impressao do resumo ---
    W = 38
    print(f"\n  {'Metrica':<{W}} {'Valor':>12}")
    print(f"  {'-'*W} {'-'*12}")
    print(f"  {'1. PDR (Packet Delivery Ratio)':<{W}} {pdr_global:>11.1f}%")
    print(f"  {'2. Latencia media E2E':<{W}} {avg_delay_ms:>10.2f} ms")
    print(f"  {'3. Jitter medio':<{W}} {avg_jitter_ms:>10.2f} ms")
    print(f"  {'4. Taxa de perda':<{W}} {loss_global:>11.1f}%")
    print(f"  {'5. Latencia maxima (pior caso)':<{W}} {max_delay_ms:>10.2f} ms")
    print(f"  {'6. Throughput total (dados)':<{W}} {total_throughput_kbps:>9.1f} kbps")
    print(f"  {'7. Hops medios por pacote':<{W}} {avg_hops:>11.2f}")
    print(f"  {'-'*W} {'-'*12}")
    print(f"  {'   Pacotes TX / RX / Perdidos':<{W}} "
          f"  {tx_total} / {rx_total} / {lost_total}")


if __name__ == "__main__":
    print("Analise Piloto: AODV vs OLSR — Cadeia Linear 9 nos")
    analyze("AODV")
    analyze("OLSR")
    print()
