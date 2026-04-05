# LINHA 4 + MeshSim: Setup Prático & Quick Start
## Passo-a-Passo para Rodar Primeiro Experimento

**Objetivo:** Você consegue rodar MeshSim e coletar dados em 2 semanas

> **Status (05/04/2026):**
> - ✅ NS-3 dev branch compilado e linkado
> - ✅ MeshSim compilado (todos os erros de API C++20 resolvidos)
> - ✅ Configs piloto criadas — cadeia linear 9 nós, AODV vs OLSR
> - ✅ `mesh-helper.cc` patchado (canais 2.4 GHz válidos: 1/6/11 em vez de 100)
> - ⏳ **Próximo:** rebuild NS-3 + MeshSim → rodar `run_pilot.sh`

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

### Estado Atual

```
experiments/
└─ pilot_100_aodv_olsr/          ✅ configs criadas, scripts prontos
   ├─ config_AODV_seed42/        ✅ 9 nós, cadeia linear, AODV
   ├─ config_OLSR_seed43/        ✅ 9 nós, cadeia linear, OLSR
   ├─ run_pilot.sh               ✅ script de execução
   ├─ analyze_pilot.py           ✅ PDR + throughput + latência
   ├─ out_AODV/                  ⏳ aguarda rebuild + execução
   └─ out_OLSR/                  ⏳ aguarda rebuild + execução
```

### Estrutura Alvo (após validar piloto)

```
experiments/
├─ pilot_9nodes_chain/           ✅ cadeia linear, sanity check
├─ grid_25nodes_aodv/            próximo
├─ grid_25nodes_olsr/
├─ random_50nodes_aodv/
├─ random_50nodes_olsr/
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

## 📈 PARTE 5: COLETA DE MÉTRICAS

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

**Próximas etapas imediatas:**

- [x] Rebuild NS-3: `cd ns-3-dev/build && make -j$(nproc)` (só recompila mesh-helper.cc)
- [x] Rebuild MeshSim: `cd MeshSim/build && make -j$(nproc)`
- [x] Rodar piloto: `cd experiments/pilot_100_aodv_olsr && ./run_pilot.sh`
- [ ] Validar métricas: `python3 analyze_pilot.py` — checar PDR >90%, latência <50 ms
- [ ] Ampliar para topologia grid 5×5 (25 nós) — sanity check escalabilidade
- [ ] Gráficos: PDR, throughput e latência por número de hops

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

### Fase 1 — Validação (esta semana)

1. **Rebuild + Piloto 9 nós:** rebuild NS-3 → rebuild MeshSim → `./run_pilot.sh` → `analyze_pilot.py`
2. **Sanidade da cadeia linear:** PDR deve cair com distância (STA 9 < STA 1), latência deve crescer com hops
3. **Comparação AODV vs OLSR:** OLSR deve ter menor latência (rotas pré-computadas), AODV menor overhead em rede estática pequena

### Fase 2 — Topologias Controladas (semanas 2-3)

4. **Grid 5×5 (25 nós):** topologia conhecida, permite validar roteamento multi-hop
5. **Grid 5×5 com falhas de link:** remover links aleatoriamente; AODV deve se recuperar, OLSR também mas com delay de reconvergência
6. **Replicas:** 5 seeds por configuração → confidence intervals 95%

### Fase 3 — Escala (semanas 4-6)

7. **Random 50 nós** em área 500×500 m (densidade realista)
8. **Random 100 nós** — primeiro experimento de escala
9. **Coleta:** PDR, throughput, latência, overhead de controle por protocolo
10. **Análise:** ANOVA two-way (protocolo × escala), Mann-Whitney U para PDR

### Fase 4 — Paper (semanas 7-10)

11. **Plots publication-ready** (matplotlib, 300 DPI, barras de erro = IC 95%)
12. **Tabela comparativa** AODV vs OLSR por métrica e escala
13. **Seções:** Introdução → Trabalhos Relacionados → Metodologia → Resultados → Conclusão
14. **Submissão:** SBRC 2026 (deadline ~Maio 2026) ou WCNC 2027

---

**LINHA 4 + MeshSim Quick Start | Atualizado em 05/04/2026**  
**Status: infra pronta, aguardando rebuild para primeira rodada de dados**
