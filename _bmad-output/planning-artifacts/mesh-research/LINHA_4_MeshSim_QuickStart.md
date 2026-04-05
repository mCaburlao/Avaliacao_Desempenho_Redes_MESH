# LINHA 4 + MeshSim: Setup Prático & Quick Start
## Passo-a-Passo para Rodar Primeiro Experimento

**Objetivo:** Você consegue rodar MeshSim e coletar dados em 2 semanas

> **Status (05/04/2026):**
> - ✅ NS-3 dev branch compilado e linkado
> - ✅ MeshSim compilado (todos os erros de API C++20 resolvidos)
> - ✅ `mesh-helper.cc` patchado (canais 2.4 GHz válidos: 1/6/11 em vez de 100)
> - ✅ `apps_manager.cc` corrigido (atributos deprecated `RemoteAddress`/`RemotePort`)
> - ✅ **Piloto rodou com sucesso** — AODV PDR 78.2% / latência 147 ms | OLSR PDR 69.9% / latência 138 ms
> - ✅ `analyze_pilot.py`: 7 métricas (PDR, latência, jitter, perda, latência-max, throughput, hops)
> - ✅ Suite completa criada: `run_all_experiments.sh` + `generate_all_configs.py` + `analyze_all.py`
> - ✅ Warm-up alinhado: `StartTime=90s` em ambos os protocolos (`DURATION=400s`)
> - ⏳ **Próximo:** re-rodar piloto (400s) → gerar e rodar grid-25 e random-50 → `analyze_all.py`

---

## 📦 PARTE 1: INSTALAÇÃO

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

**MeshSim depende de NS-3 dev branch** (branch `master` do repositório oficial). NS-3 usa CMake — **NÃO usa mais WAF**:

```bash
# Clonar branch de desenvolvimento
git clone https://gitlab.com/nsnam/ns-3-dev.git ns-3-dev
cd ns-3-dev

# Compilar com CMake (Release para performance)
mkdir -p build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j$(nproc)
cd ..

# Verificar: bibliotecas em build/lib/, headers em build/include/ns3/
ls build/lib/ | grep 'libns3-dev-mesh'
# Deve listar: libns3-dev-mesh.so (ou libns3-dev-mesh-default.so)

# Exportar variáveis (colocar no ~/.bashrc para persistir)
export NS3_DIR=$(pwd)/build
export PKG_CONFIG_PATH=$NS3_DIR/lib/pkgconfig:$PKG_CONFIG_PATH
export LD_LIBRARY_PATH=$NS3_DIR/lib:$LD_LIBRARY_PATH
```

> **Atenção — breaking changes da API (já aplicados no MeshSim deste repo):**
> - `WifiPhyStandard` → `WifiStandard` (enum renomeado)
> - `YansWifiPhyHelper::Default()` removido → usar `YansWifiPhyHelper()` direto
> - `SetRemoteStationManager` agora aceita só tipo (sem objetos extras)
> - `ChannelSettings` string obrigatória em todas as standards: `"{0, 0, BAND_2_4GHZ, 0}"`
> - `mesh-helper.cc`: canal 100 (5 GHz) não existe em 2.4 GHz — patch aplicado (usa ch 1/6/11)

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
- [x] Executável `./sim/mesh_sim` existe
- [x] `./mesh_sim --help` mostra parâmetros disponíveis
- [x] Resultado em `out/` (arquivos `trace-app-rx-*.txt`, `flowdata.xml`)

---

## 🎯 PARTE 2: PRIMEIRA RODADA PILOTO (4 horas)

### Objetivo piloto
Validar: MeshSim roda, coleta dados, métricas fazem sentido

### Configuração — Formato Real dos Arquivos MeshSim

O piloto está em `experiments/pilot_100_aodv_olsr/` com topologia de **cadeia linear de 9 nós** (1 STA por nó AP, backhaul no nó 0).

Cada experimento fica numa subpasta com 6 arquivos de config:

**apps.txt** — fluxos UDP echo + TCP file transfer

**mesh_wifi.txt** — backbone mesh 802.11g

**apsta_wifi.txt** — link AP ↔ STA

**mesh_mobility.txt** — posições dos nós mesh

**sta_mobility.txt** — posições das STAs

**routing.txt** — protocolo de roteamento

### Rodar o Piloto

```bash
# Sintaxe real: argumentos POSICIONAIS (config_dir, out_dir)
# NÃO usa --config ou --out

export LD_LIBRARY_PATH=/mnt/d/OneDrive/Documentos/UFABC/2026.1/Avaliacao_Desempenho_Redes_MESH/ns-3-dev/build/lib:$LD_LIBRARY_PATH

BASE=/mnt/d/OneDrive/Documentos/UFABC/2026.1/Avaliacao_Desempenho_Redes_MESH
MESHSIM=$BASE/MeshSim/build/sim/mesh_sim
PILOT=$BASE/experiments/pilot_100_aodv_olsr

mkdir -p $PILOT/out_AODV $PILOT/out_OLSR

# AODV
$MESHSIM --meshSize=9 --staSize=9 --simDuration=60 \
    $PILOT/config_AODV_seed42 $PILOT/out_AODV

# OLSR
$MESHSIM --meshSize=9 --staSize=9 --simDuration=60 \
    $PILOT/config_OLSR_seed43 $PILOT/out_OLSR

# Ou use o script pronto:
cd $PILOT && ./run_pilot.sh
```

Para rodar a simulação novamente:
```bash
# Apagar resultados anteriores para não misturar com a nova rodada
rm -rf experiments/pilot_100_aodv_olsr/out_AODV experiments/pilot_100_aodv_olsr/out_OLSR

# Carregar variáveis de ambiente
source /mnt/d/OneDrive/Documentos/UFABC/2026.1/Avaliacao_Desempenho_Redes_MESH/meshsim_environment.sh

# Rodar o piloto (vai demorar mais — ~5–15 min dependendo da máquina)
cd /mnt/d/OneDrive/Documentos/UFABC/2026.1/Avaliacao_Desempenho_Redes_MESH/experiments/pilot_100_aodv_olsr
./run_pilot.sh

# Após concluir, analisar
python3 analyze_pilot.py
```

### Validar Resultados

```bash
ls experiments/pilot_100_aodv_olsr/out_AODV/
# Deve conter:
# - trace-app-rx-echo*.txt  (bytes cumulativos por fluxo, 1 arquivo por cliente)
# - flowdata.xml            (FlowMonitor: PDR, latência por fluxo)
# - *.pcap (se --enablePcap=true)

# Verificar saída rápida:
tail -1 out_AODV/trace-app-rx-echo1-cl.txt
# Formato: <timestamp_us> <bytes_cumulativos>
# ex:  59847291 48320
```

### Analisar

```bash
# Script dedicado — lê trace-app-rx + flowdata.xml e imprime tabela
python3 experiments/pilot_100_aodv_olsr/analyze_pilot.py

# Saída esperada (colunas: Fluxo, Bytes Rx, Throughput, PDR%, Delay ms):
# PROTOCOLO: AODV
# echo1-cl    48320    6.5 kbps
# ...
# PDR medio: 98.5%   Latencia media: 4.2 ms
#
# PROTOCOLO: OLSR
# ...
```

---

## 📊 PARTE 3: ANÁLISE BÁSICA

### Script Python: Extract Metrics

**Arquivo: `analyze_pilot.py`**

### Rodar Simulação e Análise

```bash
cd /mnt/d/OneDrive/Documentos/UFABC/2026.1/Avaliacao_Desempenho_Redes_MESH/experiments/pilot_100_aodv_olsr

source /mnt/d/OneDrive/Documentos/UFABC/2026.1/Avaliacao_Desempenho_Redes_MESH/meshsim_environment.sh

./run_pilot.sh

python3 analyze_pilot.py

# Output esperado:
# Total packets: 587624
# Start time: 10.23
# End time: 600.01
# Duration: 589.78s
# Throughput: 996.3 pps
```

---

## 🔄 PARTE 4: ESTENDER PARA TOPOLOGIAS MAIORES

### Estado Atual (05/04/2026)

```
experiments/
├─ pilot_100_aodv_olsr/          ✅ piloto rodou com sucesso
│  ├─ config_AODV_seed42/        ✅ 9 nós, cadeia linear, AODV  (warm-up 90s)
│  ├─ config_OLSR_seed43/        ✅ 9 nós, cadeia linear, OLSR  (warm-up 90s)
│  ├─ run_pilot.sh               ✅ DURATION=400s
│  ├─ analyze_pilot.py           ✅ 7 métricas — FlowMonitor + trace-app-rx
│  ├─ out_AODV/                  ✅ flowdata.xml + trace gerados
│  └─ out_OLSR/                  ✅ flowdata.xml + trace gerados
├─ generate_all_configs.py       ✅ gera grid-25 e random-50 automaticamente
├─ run_all_experiments.sh        ✅ roda as 6 simulações em 1 comando
├─ analyze_all.py                ✅ análise agregada + exporta results.csv
├─ grid_25nodes/                 ⏳ configs geradas ao rodar generate_all_configs.py
└─ random_50nodes/               ⏳ configs geradas ao rodar generate_all_configs.py
```

### Rodar Suite Completa

```bash
cd /mnt/d/OneDrive/Documentos/UFABC/2026.1/Avaliacao_Desempenho_Redes_MESH/experiments
source ../meshsim_environment.sh

# 1. Gerar configs das novas topologias (rápido, ~5s)
python3 generate_all_configs.py

# 2. Dry-run para conferir antes de executar
./run_all_experiments.sh --dry-run

# 3. Rodar tudo (~30-60 min)
./run_all_experiments.sh

# 4. Analisar todos os resultados + gerar results.csv
python3 analyze_all.py
```

### Rodar Topologias Individualmente

```bash
./run_all_experiments.sh chain-9           # só piloto 9 nós
./run_all_experiments.sh grid-25           # só grid 5x5
./run_all_experiments.sh grid-25 random-50 # grid + random
```

### Topologias e Parâmetros

| Topologia | Nós | Warm-up | Duration | Descrição |
|:---|:---:|:---:|:---:|:---|
| `chain-9` | 9 | 90s | 400s | Cadeia linear — sanity check |
| `grid-25` | 25 | 120s | 500s | Grid 5×5, 50m spacing — multi-hop controlado |
| `random-50` | 50 | 180s | 600s | Aleatório 420×420m — densidade realista |

---

## 📈 PARTE 5: ANÁLISE AGREGADA

### Script: `analyze_all.py`

Lê `flowdata.xml` e `trace-app-rx-*.txt` de **todas as topologias** e exporta `results.csv`.

```python
import xml.etree.ElementTree as ET
import csv
from pathlib import Path
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

## 📊 PARTE 6: GRÁFICOS

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

**Concluído:**

- [x] NS-3 dev branch compilado (CMake, sem WAF)
- [x] MeshSim compilado — todos os erros de API C++20 resolvidos
- [x] `Findns3.cmake` corrigido (nomes `libns3-dev-mesh.so` sem sufixo)
- [x] `configureWifiPhy` define `ChannelSettings` para todas as standards (2.4/5 GHz)
- [x] `mesh-helper.cc` patchado — canais 2.4 GHz válidos (1/6/11 em vez de 100)
- [x] Configs piloto criadas: `config_AODV_seed42/` e `config_OLSR_seed43/`
- [x] `run_pilot.sh` e `analyze_pilot.py` prontos

**Concluído (semana 1):**
- [x] Rebuild NS-3 + MeshSim
- [x] Piloto rodou: AODV PDR 78.2%, latência 147 ms | OLSR PDR 69.9%, TCP throughput 0 (sem warm-up)
- [x] Bug latência corrigido (notação científica `+3.30e+08ns`)
- [x] Warm-up alinhado: `StartTime=90s`, `DURATION=400s` em ambos os protocolos
- [x] `analyze_pilot.py` com 7 métricas (FlowMonitor + trace)
- [x] Scripts `generate_all_configs.py`, `run_all_experiments.sh`, `analyze_all.py` criados

**Próximas etapas:**
- [ ] Re-rodar piloto com 400s: `cd experiments/pilot_100_aodv_olsr && ./run_pilot.sh`
- [ ] Rodar suite completa: `cd experiments && ./run_all_experiments.sh`
- [ ] Validar métricas: `python3 analyze_all.py` — verificar PDR, latência e hops por topologia
- [ ] Gráficos: `plot_results.py` — PDR, latência e hops médios vs topologia

---

## 🐛 TROUBLESHOOTING

| Problema | Solução |
|:---|:---|
| **fatal error: ns3/log.h: No such file** | `export NS3_DIR=/path/to/ns-3-dev/build` antes do cmake do MeshSim |
| **cmake error: ns3 not found** | `cmake .. -DNS3_USE_BUILD_TREE=ON -DNS3_BUILD_TREE=$NS3_DIR ..` |
| **linker: -lns3 not found** | `Findns3.cmake` busca `libns3-dev-*.so` — versão corrigida já inclusa |
| **MeshSim não compila (API NS-3)** | NS-3 usa CMake, não WAF. Boost 1.70+, CMake 3.16+, gcc 9+ |
| **`WifiPhyOperatingChannel: No unique channel found`** | ✅ Já corrigido: `mesh-helper.cc` patchado para 2.4 GHz (canais 1/6/11). Rebuild NS-3 necessário. |
| **`unordered_map::at` (runtime)** | `apps.txt` referencia IPs de 9 STAs mas rodou com `--staSize=2`. Use `--staSize=9`. |
| **`Cannot change standard` (abort)** | `ConfigureStandard()` chamado duas vezes com standards diferentes. Verificar `mesh_wifi.txt` vs `apsta_wifi.txt`. |
| **trace-app-rx vazio** | Aplicações não iniciaram? Verificar `StartTime` em `apps.txt` < `simDuration`. |
| **flowdata.xml ausente** | FlowMonitor habilitado por padrão — checar se saída está no diretório correto. |
| **Simulação muito lenta** | LogDistance é leve. Verifique debug build: recompilar com `-DCMAKE_BUILD_TYPE=Release`. |
| **Python script error** | `pip3 install numpy scipy pandas matplotlib` + módulo padrão `xml.etree.ElementTree` (built-in). |

---

## 🚀 PRÓXIMO: Roteiro de Experimentos

### Fase 1 — Validação ✅ CONCLUÍDA

1. ✅ **Piloto chain-9:** NS-3 compilado, MeshSim compilado, piloto rodou com sucesso
2. ✅ **Sanidade da cadeia linear:** OLSR TCP = 0 bytes (sem warm-up, TCP colapsou) — achado diagnosticado
3. ✅ **Warm-up corrigido:** `StartTime=90s` → OLSR tem 90s para convergir antes do tráfego
4. ✅ **7 métricas implementadas:** PDR, latência, jitter, perda, latência-max, throughput, hops

### Fase 2 — Suite Completa (agora)

5. **Re-rodar chain-9 com 400s:** `./run_pilot.sh` → verificar OLSR TCP com warm-up adequado
6. **Grid 5×5 (25 nós):** `./run_all_experiments.sh grid-25` → validar roteamento multi-hop
7. **Random 50 nós:** `./run_all_experiments.sh random-50` → densidade realista
8. **Análise agregada:** `python3 analyze_all.py` → tabela comparativa + `results.csv`

### Fase 3 — Análise Estatística e Paper (semanas 2-4)

9. **IC 95%:** 5 seeds por configuração → `scipy.stats.t.interval()` por métrica
10. **Plots publication-ready** (matplotlib, 300 DPI, barras de erro = IC 95%)
11. **Tabela comparativa** AODV vs OLSR: PDR, latência, jitter, hops por topologia
12. **Seções do artigo:** Introdução → Relacionados → Metodologia → Resultados → Conclusão
13. **Submissão:** SBRC 2026 (deadline ~Maio 2026)

---

**LINHA 4 + MeshSim Quick Start | Atualizado em 05/04/2026**  
**Status: piloto concluído, suite pronta para rodar grid-25 e random-50**
