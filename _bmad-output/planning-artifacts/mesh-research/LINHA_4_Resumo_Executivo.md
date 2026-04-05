# LINHA 4: Escalabilidade AODV vs OLSR — Resumo Executivo
## Para Apresentar ao Advisor

**Status:** Proposta pronta para execução  
**Simulador:** MeshSim (NS-3 baseado)  
**Cronograma:** 12-15 meses  
**Data:** Abril 2026

---

## 🎯 PERGUNTA DE PESQUISA

> **"Como protocolos de roteamento com diferentes paradigmas (reativo vs proativo) escalam conforme o número de nós cresce de 100 para 1500 em uma rede MESH?"**

**Subquestões:**
1. Em qual # nós AODV fica melhor que OLSR? (~700 nós?)
2. Qual overhead cresce: linear (AODV) ou quadrático (OLSR)?
3. Qual recomendação prática para smart cities (1000+ nós)?

---

## 💼 DOMÍNIO DE NEGÓCIO

### Contexto Atual (Abril 2026)
- Cidades implantam redes de sensores: 1000-10k nós
- Exemplos: iluminação inteligente, ar, limpeza, tráfego
- **Problema:** Engenheiros não sabem qual protocolo usar em escala

### Motivação Pesquisa
- ✅ Benchmark científico falta (recomendações empíricas, não opinion)
- ✅ Aplicação real em smart cities
- ✅ Publicável em IEEE Transactions (Top journal)

### Stakeholders
| Quem | Interesse | Como ajuda |
|:---|:---|:---|
| Engenheiros IoT | Escolher protocolo | Tabela recomendações por # nós |
| Admin Smart City | Economizar CPU | Análise overhead vs performance |
| Pesquisadores | Entender limites | Baseline científico novo |
| Você | Publicar | Paper + dissertação |

---

## ⚙️ 2 PROTOCOLOS COMPARADOS

### AODV: Reativo (On-Demand)

```
Comportamento:
- Quando X precisa enviar a Z: inunda rede com RREQ
- Z responde com RREP
- X escolhe melhor rota e memorizá
- Se falha: usa RRER

Filosofia: "LAZY" (descobre quando precisa)
Overhead: LINEAR com fluxos (não com topologia)
Escalabilidade: ✅ BOA para >500 nós
```

**Vantagem:** Overhead controlado em escala  
**Desvantagem:** Latência inicial alta

---

### OLSR: Proativo (Table-Driven)

```
Comportamento:
- Mantém tabela COMPLETA de rotas para todos nós
- Inunda continuamente Topology Control (TC)
- Lookup sempre rápido
- Sempre tem rota fresca

Filosofia: "EAGER" (saiba tudo antecipadamente)
Overhead: QUADRÁTICO com # nós (!!!)
Escalabilidade: ❌ RUIM para >800 nós
```

**Vantagem:** Latência baixa, convergência rápida  
**Desvantagem:** Overhead cresce explosivamente

---

## 📊 5 MÉTRICAS PRINCIPAIS

### 1️⃣ PDR (Packet Delivery Ratio)
```
PDR = (packets_received / packets_sent) × 100%

Esperado:
- AODV 100-500 nós: PDR > 95%
- AODV 1000 nós: PDR 91% (degradação lenta)
- OLSR 100-500 nós: PDR > 97% (melhor)
- OLSR 1000 nós: PDR 75% (quebra)
```

### 2️⃣ Latência E2E
```
Latência = time(received) - time(sent)

Esperado:
- AODV 100 nós: 10-20ms
- AODV 1000 nós: 50-150ms (mais hops)
- OLSR 100 nós: 5-15ms (rápido)
- OLSR 1000 nós: 80-250ms (congestão)
```

### 3️⃣ Overhead Roteamento
```
Overhead% = (control_packets / total_packets) × 100%

Esperado:
- AODV 100 nós: 5-10%
- AODV 1000 nós: 20-30% (linear)
- OLSR 100 nós: 10-15%
- OLSR 1000 nós: 50-80%+ (quadrático!)
```

### 4️⃣ Convergência Inicial
```
Convergência = time(primeira_rota) - start

Esperado:
- AODV: 5-60s (aumenta com nós)
- OLSR: 2-20s (controle preemptivo)
```

### 5️⃣ CPU/Memória
```
Computação relativa para rodar simulação

Esperado:
- 100 nós: <10s CPU
- 500 nós: ~50s CPU
- 1000 nós: ~200s CPU
- 1500 nós: ~500s CPU
```

---

## 🔬 DESIGN EXPERIMENTAL

### Variáveis Independentes
```
Nós: 100, 300, 500, 750, 1000, 1250, 1500 (7 níveis)
Protocolo: AODV, OLSR (2 níveis)
Topologia: Random (1 tipo)
Mobilidade: Static (simplificar)

Total: 7 × 2 = 14 combinações
Réplicas: 10 rodadas cada (diferentes seeds)
Total rodadas: 140 rodadas
```

### Parâmetros Simulação
```
Duração: 640s (30s warm-up + 600s medição + 10s cooldown)
Tráfego: UDP 1000 pps (1 sender → 1 receiver)
Área: 1000m × 1000m (Poisson random topology)
WiFi: 802.11g, 20 Mbps (realista)
```

---

## ✅ VIABILIDADE COM MESHSIM

### Checklist: MeshSim suporta tudo?

- ✅ AODV? SIM (routing_config.h)
- ✅ OLSR? SIM (routing_config.h)
- ✅ Topologia random? SIM (MobilityHelper)
- ✅ WiFi? SIM (wifiConfig)
- ✅ Aplicações (UDP)? SIM (AppsManager)
- ✅ PCAP output? SIM (enablePcap)
- ✅ Variação nós? SIM (meshSize parameter)
- ✅ Reprodutibilidade? SIM (RNG seeds)

**Conclusão:** ✅ MeshSim tem TUDO que você precisa!

### Fluxo MeshSim
```
1. Gerar configs (script Python)
2. Rodar simulations (parallel, cluster)
3. Coletar PCAP + logs
4. Post-processing (Python pandas)
5. Gráficos + análise estatística
```

### Estimativa CPU
```
140 rodadas × 640s tempo simulado = 89,600 sim-seconds
CPU ratio: ~1 min por 10s simulado = 8,960 min CPU

Com 8 cores em paralelo: 1,120 min = ~18-24 horas
Com cluster/cloud: <12 horas viável
```

---

## 📅 TIMELINE: 4 SEMESTRES

### Semestre 1: Fondações (13 semanas)
- ✅ Literatura: AODV, OLSR, papers escalabilidade
- ✅ Setup MeshSim + primeiro experimento (100 nós)
- ✅ Proposta formal escrita + advisor validation
- **Entrega:** PRD + proposta formal + primeiros dados piloto

### Semestre 2: Execução (13 semanas)
- ✅ Setup cluster/cloud compute
- ✅ Rodar 100-500 nós (validação inicial)
- ✅ Debug, optimize, troubleshoot
- ✅ Paper draft começado
- **Entrega:** Dataset preliminar + gráficos iniciais

### Semestre 3: Análise (13 semanas)
- ✅ Rodar 750-1500 nós (full scale)
- ✅ Post-processing completo
- ✅ Análise estatística (IC 95%, ANOVA)
- ✅ Gráficos publication-ready
- **Entrega:** Paper done + resultados conclusivos

### Semestre 4: Escrita (13 semanas)
- ✅ Dissertação (70-80 páginas)
- ✅ Aperfeiçoar paper (IEEE format)
- ✅ Submit conference
- **Entrega:** Dissertação + paper submetido

---

## 🏆 BENEFÍCIOS DESSA LINHA

### Acadêmico
- ✅ Baseline científico (dados não existem em escala 100-1500)
- ✅ Publicável em IEEE (top journal)
- ✅ Dataset público (replicável)

### Prático
- ✅ Tabela recomendações (engenheiros usam)
- ✅ Entendimento: quando AODV vira melhor?
- ✅ Smart city engineering decisions

### Pessoal
- ✅ Viável em 18 meses (sem risco)
- ✅ MeshSim já encontrou (aproveita!)
- ✅ Menor curva aprendizado que outras linhas

---

## 📊 GRÁFICO ESPERADO (Ilustração)

```
% Overhead
    |
 80 |                                    OLSR (quadrático)
 70 |                                   /
 60 |                                /
 50 |                            /
 40 |                        /    ← Crossover ~700 nós
 30 |                    /
 20 |                /
 10 |          AODV (linear) ───────────
  5 |        /
  0 |____/___________________
    100    300    500    800   1000   1500  (nós)
    
Conclusão: AODV escalável; OLSR não
```

---

## 🚀 PRÓXIMOS PASSOS (IMEDIATOS)

### Esta semana:
- [ ] Ler LINHA_4_PRD_Escalabilidade.md (1 hora)
- [ ] Ler LINHA_4_AODV_vs_OLSR_Detalhado.md (45 min)
- [ ] Marcar meeting com advisor

### Próxima semana:
- [ ] Começar LINHA_4_MeshSim_QuickStart.md
- [ ] Instalar MeshSim (2-3 horas)
- [ ] Rodar primeiro piloto 100 nós AODV (2 horas)

### Semana 3-4:
- [ ] Piloto OLSR (validação comparação)
- [ ] Gráficos básicos
- [ ] Escrever proposta formal

---

## ❓ FAQ

**P: Por quê preferir Linha 4 sobre Linha 2 (segurança)?**
A: Você JÁ TEM MeshSim! Linha 4 usa direto, Linha 2 precisa instalar Cooja. Viabilidade muito maior.

**P: Dados de 100-1500 nós já não existem?**
A: Existem artigos, mas desatualizados (NS-3 versão antiga, metodologia inconsistente). Você faz baseline rigoroso, moderno, reproduzível.

**P: 140 rodadas é muito?**
A: Computação pode rodar paralelo. 8 cores = 18-24 horas total. Viável.

**P: Preciso de novel protocolo?**
A: Não! Você descobre comportamento AODV/OLSR em escala → já é contribuição (benchmark papers são citados!).

**P: Vai publicar onde?**
A: IEEE Transactions on Mobile Computing, Computer Networks, ou Ad Hoc Networks (todas top-tier).

---

## ✨ RECOMENDAÇÃO FINAL

### Para você:
**LINHA 4 com MeshSim é excelente escolha**

- ✅ Viabilidade altíssima (MeshSim ready)
- ✅ Resultado garantido (AODV/OLSR comportam diferente)
- ✅ Publicável (quantitativo + prático)
- ✅ Cronograma realista (12-15 meses)
- ✅ Aplicação real (smart cities precisam desta info)

**Start:** MeshSim Quick Start (2 semanas)  
**Prize:** Dissertação + IEEE paper + dataset público

---

**LINHA 4 Resumo Executivo | Escalabilidade AODV vs OLSR**  
**Pronto para apresentar ao advisor | Abril 2026**
