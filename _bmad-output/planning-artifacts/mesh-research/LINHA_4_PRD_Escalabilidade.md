# LINHA 4: Escalabilidade em Redes MESH
## Product Requirements Document (PRD) Detalhado

**Projeto:** Análise Comparativa de Escalabilidade AODV vs OLSR  
**Simulador:** MeshSim (NS-3 baseado)  
**Data:** Abril 2026  
**Status:** Phase 1 — Problem Formulation

---

## 1️⃣ PERGUNTA DE PESQUISA REFINADA

### 1.1 Questão Principal

> **"Como protocolos de roteamento com diferentes paradigmas (reativo vs proativo) escalam conforme o número de nós cresce de 100 para 1500 em uma rede MESH?**
>
> **Especificamente: Qual é o ponto de degradação em PDR, latência, overhead de roteamento, e qual protocolo é mais adequado para smart cities (escala 1000+ nós)?"**

### 1.2 Decomposição em Sub-questões

1. **Escalabilidade AODV:** Como AODV (reativo) se comporta quando nós crescem?
   - PDR degrada linearmente, exponencialmente ou threshold?
   - Tempo convergência cresce com nós? Como?

2. **Escalabilidade OLSR:** Como OLSR (proativo) se comporta?
   - Overhead de controle (% bandwidth) cresce linear ou quardrático?
   - Quando OLSR "vira inviável" (overhead >30%)?

3. **Ponto de Crossover:** Em qual # nós AODV fica melhor que OLSR?
   - <300 nós: OLSR vence?
   - 300-800 nós: zona cinzenta?
   - >1000 nós: AODV vence?

4. **Recomendação Prática:** Para smart city (N nós esperados), qual usar?
   - Matriz: # nós → protocolo recomendado

---

## 2️⃣ DOMÍNIO DE NEGÓCIO

### 2.1 Contexto: Smart Cities 2026

**Realidade atual (Abril 2026):**
- Cidades começam implantar redes de sensores (1000-10k nós)
- Exemplos: iluminação inteligente, ar, limpeza, tráfego
- **Problema:** Engenheiros não sabem qual protocolo usar em escala

**Oportunidade de pesquisa:**
- Benchmark científico para escolha protocolo
- Recomendações baseadas em dados (não opinion)
- Publicável em IEEE → engenheiros usam resultado

### 2.2 Stakeholders

| Stakeholder | Interesse | Como resulta ajuda |
|:---|:---|:---|
| **Engenheiros IoT** | "Qual protocolo para 500 nós?" | Tabela de recomendações |
| **Administradores Smart City** | "Qual tecnologia economiza CPU?" | Analysis: overhead vs performance |
| **Pesquisadores MESH** | "Entender limites AODV/OLSR" | Baseline científico novo |
| **Você (dissertação)** | "Publicar em IEEE" | Paper benchmark com resultados sólidos |

### 2.3 Aplicações Reais (Motivação)

**Caso 1: Iluminação Inteligente em cidade**
- Esperado: ~3000 luminárias com sensores
- Pergunta: AODV ou OLSR?
- Sua pesquisa: "Para 3000 nós, recomendamos AODV + heurística X"

**Caso 2: Monitoramento de Qualidade de Ar**
- Esperado: ~800 sensores distribuídos
- Pergunta: Latência máxima tolerável?
- Sua pesquisa: "OLSR em 800 nós = latência 250ms média"

**Caso 3: Logística & Asset Tracking**
- Esperado: ~500 tags + gateways
- Pergunta: Convergência rápida?
- Sua pesquisa: "AODV converge em 5-10s; OLSR em 2-3s"

---

## 3️⃣ PROTOCOLOS COMPARADOS

### 3.1 AODV: Ad-Hoc On-Demand Distance Vector

**Tipo:** Reativo (on-demand routing)

**Como funciona:**
```
Quando nó X precisa enviar para nó Z (não tem rota):
1. X inunda rede com RREQ (Route Request)
2. Nós que conhecem Z (ou Z mesmo) respondem com RREP
3. X escolhe melhor rota (menor hop count)
4. Nó armazena rota em cache (timeout: 3-5 min)
5. RRER (Route Error) se rota falha

Características:
- Overhead de controle: BAIXO quando poucos fluxos ativos
- Latência inicial: ALTA (inundação RREQ)
- Escalabilidade: ✅ BOA para >500 nós (menos controle preemptivo)
- Convergência: Lenta (~10-30s em rede grande)
- Consumo CPU/memoria: BAIXO (sem tabelas preemptivas)
```

**Foco Escalabilidade:**
- Overhead permanece linear com nós (não cresce com topologia completa)
- Problema: latência inicial cada busca nova
- Vantagem: economia control traffic

**Parâmetros AODV em MeshSim:**
```
- AODV_HELLO_INTERVAL: 1s (keep-alive)
- AODV_ACTIVE_ROUTE_TIMEOUT: 180s (cache)
- RREQ_RETRIES: 3-5 (broadcasts tentativas)
- RREQ_RATELIMIT: para controlar inundação
```

---

### 3.2 OLSR: Optimized Link State Routing

**Tipo:** Proativo (table-driven routing)

**Como funciona:**
```
Estado permanente:
1. Nó envia HELLO periodicamente para descobrir vizinhos
2. Elege MPRs (Multipoint Relays) — subset mínimo que cobre vizinhos
3. OLSR difunde TC (Topology Control) de 1-hop em MPRs
4. Cada nó mantém tabela de rotas COMPLETA para todos

Características:
- Overhead de controle: ALTO (constante flooding TC)
- Latência inicial: BAIXA (tabelas já prontas)
- Escalabilidade: ❌ RUIM para >500 nós (TC quadrático)
- Convergência: Rápida (~2-5s, tabelas prontas)
- Consumo CPU/memoria: ALTO (tabelas todas nós)
```

**Foco Escalabilidade:**
- Overhead cresce com SIZE topologia (cada nó precisa conhecer todos)
- Problema: com 1000 nós, cada TC msg cresce
- Vantagem: dados frescos, rápido responder

**Parâmetros OLSR em MeshSim:**
```
- OLSR_HELLO_INTERVAL: 2s (descoberta vizinhos)
- OLSR_TC_INTERVAL: 5-10s (difusão topologia)
- OLSR_MID_INTERVAL: 5s (multiplas interfaces)
- OLSR_HNA_INTERVAL: 10s (external networks)
```

---

### 3.3 Comparação Teórica (Antes de Simular)

| Aspecto | AODV (Reativo) | OLSR (Proativo) |
|:---|:---:|:---:|
| **Overhead Controle** | Linear com fluxos | Quadrático com nós |
| **Latência Rota** | Alta (1ª busca) | Baixa (lookup) |
| **Convergência** | Lenta (10-30s) | Rápida (2-5s) |
| **Escalabilidade <500 nó** | ✅ BOA | ✅ BOA |
| **Escalabilidade 500-1000** | ✅ BOA | ⚠️ DEGRADAÇÃO |
| **Escalabilidade >1000** | ✅ MELHOR | ❌ RUIM (overhead huge) |
| **Consumo Memória** | ✅ BAIXO | ❌ ALTO |
| **Ideal para** | Redes dinâmicas | Redes estáveis |

---

## 4️⃣ MÉTRICAS A MEDIR

### 4.1 Métrica 1: PDR (Packet Delivery Ratio)

**Definição:**
```
PDR = (packets_received / packets_sent) × 100%
```

**Por quê importante:**
- Métrica mais crítica para redes
- Degradação mostra quando protocolo "quebra"

**Como medir em MeshSim:**
- Fonte: UDP sender em 1 nó
- Destino: múltiplos (or 1 target)
- Log packets sent vs received (PCAP)
- Python script: contar

**Esperado:**
- AODV 100-500 nós: PDR > 95%
- AODV 500-1500 nós: PDR 90-95% (degradação lenta)
- OLSR 100-500 nós: PDR > 97% (melhor, tabelas prontas)
- OLSR 500-1000 nós: PDR 85-95% (congestionamento)
- OLSR >1000 nós: PDR 70-85% (overhead quebra)

**Threshold crítico:** PDR <70% = inviável

---

### 4.2 Métrica 2: Latência E2E (End-to-End)

**Definição:**
```
Latência_E2E = time(packet_received) - time(packet_sent)
Média: mean(all latencies)
StDev: sqrt(sum((L_i - mean)^2))
Percentil 95: L_95 (95% pacotes chegam em <L_95)
```

**Por quê importante:**
- Smart city pode ter requisitos latência (ex: tráfego <200ms)
- Mostra "responsiveness" do protocolo

**Como medir em MeshSim:**
- Timestamp em sender (ns3::Now())
- Timestamp em receiver (ns3::Now())
- Diferença = latência per-packet
- Histogram: distribuição

**Esperado:**
- AODV 100 nós: 10-20ms (rápido)
- AODV 1000 nós: 50-200ms (mais hops, queueing)
- OLSR 100 nós: 5-15ms (tabelas prontas)
- OLSR 1000 nós: 100-300ms (overhead TC congestiona)

**Threshold crítico:** Latência99 >1s = inviável tempo-real

---

### 4.3 Métrica 3: Overhead de Roteamento

**Definição:**
```
Overhead_% = (control_packets_bytes / total_bytes) × 100%
           = (RREQ + RREP + RRER + TC + HELLO) / (data + control)
```

**Por quê importante:**
- Budget de BW: se overhead >50%, eficiência cai
- Mostra "scalability tax" de cada protocolo

**Como medir em MeshSim:**
- PCAP output: contar bytes per tipo packet
- Wireshark parser: contar AODV headers vs data

**Esperado:**
- AODV 100 nós: 5-10% overhead (mostly HELLO keep-alive)
- AODV 500 nós: 10-20% (mais RREQs de pesquisa)
- AODV 1000 nós: 20-30% (muita inundação)
- OLSR 100 nós: 8-15% (TC flooding)
- OLSR 500 nós: 25-40% (TC cresce com topologia)
- OLSR 1000 nós: 40-60%+ (INVIÁVEL, overhead quebra)

**Threshold crítico:** Overhead >50% = bandwidth desperdiçado

---

### 4.4 Métrica 4: Tempo Convergência Inicial

**Definição:**
```
Convergência = time(first_route_established) - time(simulation_start)
```

**Por quê importante:**
- Smart city deployment: quanto tempo até funcionar?
- AODV lento, OLSR rápido

**Como medir em MeshSim:**
- Timestamp quando 1ª rota OK
- Timestamp quando >95% nós conectados

**Esperado:**
- AODV 100 nós: 5-15s (lento, muitas RREQs)
- AODV 1000 nós: 30-60s (broadcasting lento)
- OLSR 100 nós: 2-5s (MPRs rápido)
- OLSR 1000 nós: 10-20s (mais TC necessário)

**Implicação:** Deployment longo vs curto

---

### 4.5 Métrica 5: Overhead CPU/Memória

**Definição:**
```
CPU_overhead = time(simulator_runtime) / simulated_time
Memoria = peak_memory_during_sim
```

**Por quê importante:**
- Seu laptop/cluster consegue rodar 1500 nós?
- Custo computacional vs gain research

**Como medir em MeshSim:**
- /usr/bin/time -v ou valgrind
- NS-3 memory stats

**Esperado:**
- 100 nós: <10s CPU (fácil)
- 500 nós: 30-60s CPU (médio)
- 1000 nós: 120-300s CPU (pesado)
- 1500 nós: 300-600s CPU (muito pesado)

**Implicação práti ca:** Viabilidade de rodar testes

---

## 5️⃣ DESIGN EXPERIMENTAL (DoE)

### 5.1 Variáveis Independentes

**PRIMARY: Número de nós**
```
Níveis: 100, 300, 500, 750, 1000, 1250, 1500
Razão: logarítmico spacing para ver curva
```

**PRIMARY: Protocolo**
```
Níveis: AODV, OLSR
Razão: main comparison
```

**SECONDARY: Topologia**
```
Níveis: Random (Poisson point process), Linear (chain)
Razão: realismo
```

**SECONDARY: Mobilidade**
```
Níveis: Static, Low (1 m/s random walk)
Razão: robustness
```

**Total configurações:**
```
7 (nós) × 2 (protocolo) × 2 (topologia) × 2 (mobilidade) = 56 configs
Cada config: 10 rodadas (diferentes random seeds)
Total: 560 rodadas
```

### 5.2 Variáveis Dependentes (Métricas)

- PDR
- Latência E2E (mean, stdev, p95)
- Overhead % roteamento
- Convergência inicial
- CPU/memória

### 5.3 Duração por Rodada

```
Warm-up: 30s (deixar rede estabilizar)
Medição: 600s (10 min sim ulated)
Cool-down: 10s
Total: 640s por rodada
```

**Por quê 600s:** Tempo suficiente para:
- Ver padrão estável
- Coletar 1000+ pacotes (estatística boa)
- Observar falhas/recuperações

---

## 6️⃣ VIABILIDADE COM MESHSIM

### 6.1 Checklist: MeshSim suporta tudo?

- ✅ AODV? SIM (routing_config.h: ROUTING_AODV)
- ✅ OLSR? SIM (routing_config.h: ROUTING_OLSR)
- ✅ Topologia random? SIM (MobilityHelper, Poisson)
- ✅ WiFi? SIM (wifiConfig)
- ✅ Aplicações (UDP/TCP)? SIM (AppsManager)
- ✅ PCAP output? SIM (enablePcap)
- ✅ Variando nós? SIM (meshSize parameter)
- ✅ Seedando random? SIM (NS-3 RNG)

**Conclusão:** ✅ MeshSim tem TUDO que precisa!

### 6.2 Fluxo MeshSim

```
1. Template config:
   - apps.txt (UDP source-sink 1000 packets/sec)
   - mesh_wifi.txt (WiFi padrões)
   - routing.txt (AODV ou OLSR)
   - mesh_mobility.txt (topologia random)

2. Script generation:
   python genconf.py --nodes=100 --proto=AODV → conf/config_100_AODV/

3. Simulação:
   ./mesh_sim --config conf/config_100_AODV/ → out/results.pcap

4. Post-processing:
   python collect_csv.py out/ → data.csv (PDR, latência, overhead)

5. Análise Python:
   pandas + matplotlib → gráficos
   scipy.stats → IC, ANOVA
```

### 6.3 Estimativa Computação

```
560 rodadas × 640s simulado = 358,400 sim-seconds
CPU ratio: ~1 min CPU por 10s sim (estimate)
Total: ~36,000 min CPU = 600 horas CPU

Na seu PC (1 CPU core):
- 600 horas = 25 dias sequencial ❌

Com paralelização:
- 8 cores: 3 dias ✅
- Cloud (24 cores): 1 dia ✅

Recomendação: Use cluster or cloud compute
```

---

## 7️⃣ TIMELINE DETALHADO

### Semestre 1 (13 semanas)

**Semana 1-2: Preparação**
- [ ] Instalar MeshSim + dependências
- [ ] Entender estrutura configs
- [ ] Primeiro experimento 10 nós (pilot)

**Semana 3-5: Design Experimental (DoE)**
- [ ] Definir configs finais
- [ ] Criar templates batch scripts
- [ ] Test com 100-200nós (viabilidade)
- [ ] RFC/Paper relevantes lidos

**Semana 6-9: Proposta Formal**
- [ ] Escrever PRD (este doc + feedback advisor)
- [ ] Refinar métricas
- [ ] Cronograma mestrado

**Semana 10-13: Qualificação**
- [ ] Dar seminário
- [ ] Proposta aprovada

### Semestre 2 (13 semanas)

**Semana 1-4: Setup & Small-Scale**
- [ ] Mount cluster (or cloud)
- [ ] Rodar 100-500nós (validation)
- [ ] Debug bottlenecks
- [ ] Primeiros gráficos

**Semana 5-9: Large-Scale Runs**
- [ ] Rodar 500-1500 nós (full DoE)
- [ ] Monitoramento (logs, CPU)
- [ ] Troubleshoot timeouts
- [ ] Raw data collected

**Semana 10-13: Analysis & Paper Draft**
- [ ] Post-processing (PDR, latência, overhead)
- [ ] Statistical analysis (IC 95%, ANOVA)
- [ ] Gráficos publicáveis
- [ ] Paper draft escrito

### Semestre 3 (13 semanas)

**Semana 1-5: Refinement**
- [ ] Rerun problematic configs
- [ ] Sensitivity analysis
- [ ] Cross-validation

**Semana 6-10: Escrita Paper + Dissertação**
- [ ] IEEE formato paper
- [ ] Dissertação (70-80 páginas)
- [ ] Figuras high-DPI

**Semana 11-13: Submissions + Defense Prep**
- [ ] Submit conference
- [ ] Final defense prep

### Semestre 4: Defense

---

## 8️⃣ RECOMENDAÇÕES ESPERADAS

### Matriz de Protocolo Recomendado

Baseado em resultados esperados:

| # Nós | Latência Crítica? | Overhead Crítico? | Recomendação |
|:---|:---|:---|:---|
| **<300** | Não | Não | OLSR (rápido, BW OK) |
| **300-500** | Não (talvez sim) | <30% | OLSR (ainda OK) |
| **500-800** | Sim (<200ms) | <30% | **HÍBRIDO** |
| **800-1200** | Sim (<300ms) | <40% | AODV (escalável) |
| **>1200** | Sim (<500ms) | <50% | **AODV + hierárquico** |

Isto será a **CONCLUSÃO prática** do seu trabalho.

---

## 9️⃣ PRODUTOS ESPERADOS

1. **Paper IEEE:**
   - Título: "Scalability Analysis of AODV vs OLSR in Mesh Networks: A Comparative Study up to 1500 Nodes"
   - Target journal: IEEE Transactions on Mobile Computing ou IEEE Transactions on Wireless Communications
   - ~12 páginas, dados científicos rigorosos

2. **Dataset Público:**
   - GitHub: `mesh-scalability-benchmark`
   - Includes: traces PCAP, configs, scripts post-processing
   - Citation-able (Zenodo DOI)

3. **Dissertação:**
   - ~80 páginas
   - Capítulo 1: Introdução (motivação MESH)
   - Capítulo 2: Estado da arte (AODV, OLSR, escalabilidade)
   - Capítulo 3: Metodologia (DoE, MeshSim setup)
   - Capítulo 4: Resultados (PDR vs nós, gráficos)
   - Capítulo 5: Análise & recomendações
   - Capítulo 6: Conclusões & trabalho futuro

4. **Recomendações Prática:**
   - Tabela: "Para smart city com N nós, use X protocolo"
   - Implementável em produção

---

## 🔟 RISCOS & MITIGAÇÃO

| Risco | Probabilidade | Impacto | Mitigação |
|:---|:---:|:---:|:---|
| MeshSim não roda 1500 nós | Média | Alto | Testar cedo com 500-1000 nós |
| Cluster acesso limitado | Média | Alto | Use cloud (AWS, Google) |
| Overhead CPU > estimate | Média | Médio | Rodar pequenininha paralela primeiro |
| OLSR overhead tão alto that inviável | Baixa | Médio | Ok, é descoberta válida |
| Semestre 2 sem resultados | Baixa | Alto | Começar rodadas cedo (sem 1) |

---

## 📋 CHECKLIST PRÉ-COMEÇAR

- [ ] Leu este documento
- [ ] Entende diferença AODV (reativo) vs OLSR (proativo)
- [ ] Concorda com pergunta de pesquisa
- [ ] Aprova as 5 métricas
- [ ] Design experimental (56 configs, 560 rodadas) OK
- [ ] Computação: cluster/cloud planejado
- [ ] Advisor: validou questão
- [ ] Pronto começar semestre 1

---

**LINHA 4 PRD | Escalabilidade MESH com MeshSim**  
**Versão 1.0 | Abril 2026 | Ready for advisor review**
