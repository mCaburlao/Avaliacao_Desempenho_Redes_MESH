# LINHA 4 + MeshSim: Setup Prático & Quick Start
## Passo-a-Passo para Rodar Primeiro Experimento

**Objetivo:** Você consegue rodar MeshSim e coletar dados em 2 semanas

---

## 📦 PARTE 1: INSTALAÇÃO (2-3 horas)

### Pré-requisitos

```bash
# Ubuntu 20.04+ (distribuição recomendada)
# Ou: WSL2 + Ubuntu (se Windows)

# Packages
sudo apt update
sudo apt install -y \
  build-essential \
  git \
  cmake \
  python3-dev \
  python3-pip \
  wget \
  libboost-all-dev

# Python packages
pip3 install matplotlib numpy scipy pandas
```

### ⚠️ Pré-requisito CRÍTICO: Instalar NS-3

**MeshSim depende de NS-3**. Você precisa compilar NS-3 PRIMEIRO:

```bash
# Clonar NS-3 (versão compatível com MeshSim)
# OPÇÃO 1: URL padrão (tente primeiro)
# git clone https://github.com/nsnam/ns-3-dev ns-3-dev
# cd ns-3-dev

# Se falhar com "Repository not found", tente OPÇÃO 2:
git clone git://github.com/nsnam/ns-3-dev.git ns-3-dev
cd ns-3-dev

# Se ainda falhar, use OPÇÃO 3 (release específica - RECOMENDADA):
# wget https://www.nsnam.org/releases/ns-3.47.tar.bz2
# tar xjf ns-3.47.tar.bz2
# cd ns-3.47

# NS-3 3.47 usa CMake (não WAF). Compile com:
mkdir -p build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release -DNS3_DIR=$(pwd)
make -j8

# Voltar ao diretório ns-3.47 para verificar
cd ..

# Verificar: deve ter lib/ com headers ns3/
ls build/lib/ | head -5
# Deve listar: libns3-core... arquivos
ls build/include/ns3/ | head -5  # Deve listar: log.h, address.h, etc.

# Exportar para PATH (importante!)
export NS3_DIR=$(pwd)/build
export PKG_CONFIG_PATH=$NS3_DIR/lib/pkgconfig:$PKG_CONFIG_PATH
export LD_LIBRARY_PATH=$NS3_DIR/lib:$LD_LIBRARY_PATH
```

### Download & Compilação de MeshSim

```bash
# Voltar ao dir original e compilar MeshSim
cd ../MeshSim  # Ou seja local onde tem MeshSim

# IMPORTANTE: Manter NS3_DIR em PATH
# Se fechou terminal, execute novamente:
export NS3_DIR=/mnt/d/OneDrive/Documentos/UFABC/2026.1/Avaliacao_Desempenho_Redes_MESH/ns-3-dev/build
export LD_LIBRARY_PATH=$NS3_DIR/lib:$LD_LIBRARY_PATH

# Compilar
mkdir build && cd build

# Caso precise recompilar o projeto:
# cd build
# rm -rf *

cmake \
  -DNS3_USE_BUILD_TREE=ON \
  -DNS3_BUILD_TREE=$NS3_DIR \
  -DCMAKE_BUILD_TYPE=Release \
  ..

make -j8  # 8 threads pois tenho 8 cores (pode testar com "nproc" no terminal)

# Resultado: ./sim/mesh_sim (executável)
```

### Teste Básico

```bash
# 1. Ir para onde o executável foi compilado
cd /mnt/d/OneDrive/Documentos/UFABC/2026.1/Avaliacao_Desempenho_Redes_MESH/MeshSim/build/sim

# 2. Configurar LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/mnt/d/OneDrive/Documentos/UFABC/2026.1/Avaliacao_Desempenho_Redes_MESH/ns-3-dev/build/lib:$LD_LIBRARY_PATH

# 3. Copiar as configs de exemplo e criar pasta de saída
cp -r ../../examples/conf .
mkdir -p out

# 4. Verificar o help
./mesh_sim --help

# 5. Rodar a simulação usando defaults: 9 mesh nodes, 9 STAs, 60s
./mesh_sim conf out
```

Checklist:
- [x] Compilou sem erros
- [x] Executável ./sim/mesh_sim existe
- [ ] Resultado em out_test/ (PCAP files)

---

## 🎯 PARTE 2: PRIMEIRA RODADA PILOTO (4 horas)

### Objetivo piloto
Validar: MeshSim roda, coleta dados, métricas fazem sentido

### Configuração Simples

Crie pasta: `experiments/pilot_100nodes/`

**Arquivo 1: apps.txt** (aplicações)
```
# UDP sender on node 0 → node 99
# Start: 10s, Duration: 590s (deixe 30s warm-up)
0/1000@0:9 1000 10.0 590.0

# Significado:
# 0 = node source
# /1000 = UDP port 1000
# @0:9 = send to node 9
# 1000 = packets/sec
# 10.0 = start time (segundos)
# 590.0 = duration
```

**Arquivo 2: mesh_wifi.txt** (WiFi entre APs/mesh)
```
standard = 802.11g
station_manager type = ns3::ArfWifiManager

# Channel
default_channel = true
delay_model = ns3::ConstantSpeedPropagationDelayModel
loss_model = @ns3::LogDistancePropagationLossModel

# Attributes
phy_attribs = TxPowerStart=20dBm
phy_attribs = TxPowerEnd=20dBm
phy_attribs = TxPowerLevels=1
phy_attribs = RxGain=0dBm
```

**Arquivo 3: mesh_mobility.txt** (Posicionamento)
```
# Random topologia (Poisson point process)
# 100 nodes in 1000m x 1000m area

mobility_type = UniformDiscPositionAllocator
min_x = 0.0
max_x = 1000.0
min_y = 0.0
max_y = 1000.0
num_nodes = 100
seed = 42  # Reprodutível!
```

**Arquivo 4: routing.txt** (Protocolo)
```
protocol = AODV
# Alternativa: OLSR

# AODV params
aodv_hello_interval = 1.0
aodv_active_route_timeout = 180
aodv_rreq_retries = 3
```

### Rodar

```bash
cd experiments/pilot_100nodes/

# Executar MeshSim
../../sim/mesh_sim \
  --config . \
  --duration 600 \
  --out results_aodv_100nodes

# Esperado:
# [INFO] Loading config...
# [INFO] Creating simulation (100 nodes)...
# [INFO] Running simulation...
# Progress: 0% ... 25% ... 50% ... 75% ... 100%
# [INFO] Simulation complete. Time: 45.2s (CPU)
# [INFO] Output: results_aodv_100nodes/
```

### Validar Resultados

```bash
ls results_aodv_100nodes/
# Deve ter:
# - mesh.pcap (captura MESH APs)
# - sta-wifi.pcap (captura STAs)
# - trace.txt (eventos simulação)

# Contar pacotes:
tcpdump -r results_aodv_100nodes/mesh.pcap | wc -l
# Deve ter 100s+ packets (590s × 1000 pps ≈ 590k packets)
```

---

## 📊 PARTE 3: ANÁLISE BÁSICA (2 horas)

### Script Python: Extract Metrics

**Arquivo: `analyze_pilot.py`**

```python
#!/usr/bin/env python3
import subprocess
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

pcap_file = "results_aodv_100nodes/mesh.pcap"

# Parse PCAP com tshark
result = subprocess.run(
    f"tshark -r {pcap_file} -T fields -e frame.time_epoch -e ip.src -e ip.dst -e udp.srcport",
    capture_output=True,
    text=True,
    shell=True
)

# Parse output
packets = []
for line in result.stdout.strip().split('\n'):
    if not line:
        continue
    parts = line.split()
    if len(parts) >= 4:
        try:
            ts = float(parts[0])
            src = parts[1]
            dst = parts[2]
            port = parts[3]
            packets.append({'ts': ts, 'src': src, 'dst': dst, 'port': port})
        except:
            pass

df = pd.DataFrame(packets)

if len(df) > 0:
    # Métricas básicas
    print(f"Total packets: {len(df)}")
    print(f"Start time: {df['ts'].min():.2f}")
    print(f"End time: {df['ts'].max():.2f}")
    print(f"Duration: {df['ts'].max() - df['ts'].min():.2f}s")
    
    throughput = len(df) / (df['ts'].max() - df['ts'].min())
    print(f"Throughput: {throughput:.1f} pps")
    
    # Plot
    plt.figure(figsize=(10, 4))
    plt.hist(df['ts'], bins=100)
    plt.xlabel('Time (s)')
    plt.ylabel('Packets')
    plt.title('Packet Distribution - AODV 100 nodes')
    plt.savefig('packet_distribution.png')
    print("Saved: packet_distribution.png")
```

### Rodar análise

```bash
python3 analyze_pilot.py

# Output esperado:
# Total packets: 587624
# Start time: 10.23
# End time: 600.01
# Duration: 589.78s
# Throughput: 996.3 pps
```

---

## 🔄 PARTE 4: ESTENDER PARA AODV vs OLSR (1 semana)

### Estrutura de Pasta

```
experiments/
├─ pilot_100_aodv/      (✅ já fez)
├─ pilot_100_olsr/      (próximo)
├─ scale_300_aodv/
├─ scale_300_olsr/
├─ scale_500_aodv/
├─ scale_500_olsr/
└─ analysis/
   ├─ compare_aodv_olsr.py
   └─ results.csv
```

### Script Batch: Rodar Múltiplas Configs

**Arquivo: `run_experiments.sh`**

```bash
#!/bin/bash

CONFIGS=(100 300 500)
PROTOCOLS=("AODV" "OLSR")

for config in "${CONFIGS[@]}"; do
    for proto in "${PROTOCOLS[@]}"; do
        echo "Running: nodes=$config, proto=$proto"
        
        mkdir -p experiments/scale_${config}_$(echo $proto | tr A-Z a-z)/
        cd experiments/scale_${config}_$(echo $proto | tr A-Z a-z)/
        
        # Setup config files
        cp ../../templates/apps.txt .
        cp ../../templates/mesh_wifi.txt .
        cp ../../templates/mesh_mobility.txt .
        
        # Customize
        sed -i "s/num_nodes = 100/num_nodes = $config/" mesh_mobility.txt
        sed -i "s/protocol = AODV/protocol = $proto/" routing.txt
        sed -i "s/seed = 42/seed = $(($RANDOM))/" mesh_mobility.txt
        
        # Run
        ../../../sim/mesh_sim --config . \
            --out results_${config}_${proto} \
            --duration 600
        
        cd ../../..
    done
done

echo "All experiments done!"
```

### Rodar

```bash
chmod +x run_experiments.sh
./run_experiments.sh

# Roda ~6 simulações
# Tempo total: ~5-10 minutos
```

---

## 📈 PARTE 5: COLETA DE MÉTRICAS (3 horas)

### Script: PDR, Latência, Overhead

**Arquivo: `extract_all_metrics.py`**

```python
import subprocess
import pandas as pd
import re
from pathlib import Path

def analyze_pcap(pcap_file, config_name):
    """Extract PDR, latency, overhead from PCAP"""
    
    # PDR: count UDP packets
    result = subprocess.run(
        f"tshark -r {pcap_file} -Y 'udp.port==1000' -T fields -e frame.time_epoch",
        capture_output=True,
        text=True,
        shell=True
    )
    
    received = len(result.stdout.strip().split('\n')) - 1
    expected = 590 * 1000  # 590s @ 1000 pps
    pdr = (received / expected) * 100.0 if expected > 0 else 0
    
    # Overhead: count control packets
    result_ctrl = subprocess.run(
        f"tshark -r {pcap_file} -Y 'aodv || olsr' -T fields -e frame.len",
        capture_output=True,
        text=True,
        shell=True
    )
    
    ctrl_bytes = sum([int(x) for x in result_ctrl.stdout.strip().split('\n') if x])
    
    # Total bytes
    result_total = subprocess.run(
        f"tshark -r {pcap_file} -T fields -e frame.len",
        capture_output=True,
        text=True,
        shell=True
    )
    total_bytes = sum([int(x) for x in result_total.stdout.strip().split('\n') if x])
    
    overhead_pct = (ctrl_bytes / total_bytes) * 100.0 if total_bytes > 0 else 0
    
    # Latency: parse timestamps
    result_latency = subprocess.run(
        f"tshark -r {pcap_file} -Y 'udp.port==1000' -T fields -e frame.time_epoch",
        capture_output=True,
        text=True,
        shell=True
    )
    
    times = [float(x) for x in result_latency.stdout.strip().split('\n') if x]
    if len(times) > 1:
        latencies = [times[i+1] - times[i] for i in range(len(times)-1)]
        avg_latency = sum(latencies) / len(latencies)
    else:
        avg_latency = 0
    
    return {
        'config': config_name,
        'pdr_percent': pdr,
        'overhead_percent': overhead_pct,
        'avg_latency_ms': avg_latency * 1000
    }

# Processá experiments
metrics = []
for pcap in Path("experiments/").rglob("*.pcap"):
    config_name = str(pcap.parent)
    result = analyze_pcap(str(pcap), config_name)
    metrics.append(result)

# Save
df = pd.DataFrame(metrics)
df.to_csv('results.csv', index=False)
print(df.to_string())
```

### Rodar

```bash
python3 extract_all_metrics.py

# Output exemplo:
#                          config  pdr_percent  overhead_percent  avg_latency_ms
# 0    scale_100_aodv/results... 97.3          7.2           8.5
# 1    scale_100_olsr/results... 99.1          11.4          5.2
# 2    scale_300_aodv/results... 94.8          14.3          22.1
# 3    scale_300_olsr/results... 92.1          26.7          18.9
# 4    scale_500_aodv/results... 91.2          19.8          45.3
# 5    scale_500_olsr/results... 87.5          38.1          62.1
```

---

## 📊 PARTE 6: GRÁFICOS (1 hora)

### Script: Plot Resultados

**Arquivo: `plot_results.py`**

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('results.csv')

# Parse config para extrair # nós e protocolo
df['num_nodes'] = df['config'].str.extract('(\d+)').astype(int)
df['protocol'] = df['config'].str.extract('(aodv|olsr)', expand=False).str.upper()

# Separar protocols
aodv = df[df['protocol'] == 'AODV'].sort_values('num_nodes')
olsr = df[df['protocol'] == 'OLSR'].sort_values('num_nodes')

# Plot 1: PDR vs Nodes
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.plot(aodv['num_nodes'], aodv['pdr_percent'], 'o-', label='AODV', linewidth=2)
plt.plot(olsr['num_nodes'], olsr['pdr_percent'], 's-', label='OLSR', linewidth=2)
plt.xlabel('Number of Nodes')
plt.ylabel('PDR (%)')
plt.ylim([70, 100])
plt.legend()
plt.grid(True, alpha=0.3)
plt.title('PDR vs Scale')

# Plot 2: Overhead vs Nodes
plt.subplot(1, 3, 2)
plt.plot(aodv['num_nodes'], aodv['overhead_percent'], 'o-', label='AODV', linewidth=2)
plt.plot(olsr['num_nodes'], olsr['overhead_percent'], 's-', label='OLSR', linewidth=2)
plt.xlabel('Number of Nodes')
plt.ylabel('Overhead (%)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.title('Control Overhead vs Scale')

# Plot 3: Latency vs Nodes
plt.subplot(1, 3, 3)
plt.plot(aodv['num_nodes'], aodv['avg_latency_ms'], 'o-', label='AODV', linewidth=2)
plt.plot(olsr['num_nodes'], olsr['avg_latency_ms'], 's-', label='OLSR', linewidth=2)
plt.xlabel('Number of Nodes')
plt.ylabel('Latency (ms)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.title('E2E Latency vs Scale')

plt.tight_layout()
plt.savefig('comparison_aodv_olsr.png', dpi=150)
print("Saved: comparison_aodv_olsr.png")
```

### Rodar

```bash
python3 plot_results.py

# Resultado: comparison_aodv_olsr.png (3 gráficos lado-a-lado)
```

---

## ✅ CHECKLIST: SEMANA 1-2

Fim de semana 2, você terá:

- [ ] MeshSim compilado e testado
- [ ] Piloto 100 nós (AODV): dados coletados
- [ ] Piloto 100 nós (OLSR): dados coletados
- [ ] Extensão: 300 e 500 nós (ambos protocolos)
- [ ] Gráficos: PDR, overhead, latência
- [ ] Validação: "Dados fazem sentido?"

---

## 🐛 TROUBLESHOOTING

| Problema | Solução |
|:---|:---|
| **fatal error: ns3/log.h: No such file** | ❌ NS-3 não está instalado. Execute seção "Instalar NS-3" acima ANTES de MeshSim. Ou: `export NS3_DIR=/path/to/ns-3-dev/build` antes de cmake |
| **cmake error: ns3 not found** | 1. `cmake .. -DNS3_DIR=/path/to/ns-3-dev/build` ou 2. `export PKG_CONFIG_PATH=$NS3_DIR/lib/pkgconfig:$PKG_CONFIG_PATH` |
| **MeshSim não compila (outros erros)** | Checklist: ns3 compilado com `./waf build`? Boost 1.70+? CMake 3.10+? |
| **Simulação sehr lento** | WiFi loss model complexo? Reduzir nós piloto |
| **PCAP vazio** | Aplicações configuradas? routing.txt correto? |
| **Python script error** | tshark instalado? (`sudo apt install tshark`) |
| **Métricas não fazem sentido** | Verificar: tempo warm-up (30s), duration (600s) |

---

## 🚀 PRÓXIMO: Semana 3-10

Uma vez que este piloto (100-500 nós AODV vs OLSR) funciona e produz dados razoáveis:

1. **Escale:** Rodar 750, 1000, 1500 nós
2. **Replicas:** 10 rodadas cada config (diferentes seeds)
3. **Análise:** ANOVA, confidence intervals, plots publication-ready
4. **Paper draft:** Começar escrita com resultados

---

**LINHA 4 + MeshSim Quick Start | Pronto para executar**  
**Estimate: 2 weeks até primeiro resultado concreto | Abril 2026**
