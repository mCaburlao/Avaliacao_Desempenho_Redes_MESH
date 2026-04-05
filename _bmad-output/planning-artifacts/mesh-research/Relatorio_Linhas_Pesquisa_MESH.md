# RELATÓRIO ESTRATÉGICO DE LINHAS DE PESQUISA
## Redes MESH Wireless: Análise de Oportunidades para Dissertação de Mestrado

**Autor:** Especialista em Redes MESH  
**Data:** Abril 2026  
**Contexto:** Análise de 5 artigos fundamentais em redes MESH wireless  
**Destinatário:** Mestrando em Ciência da Computação

---

## PARTE 1: ANÁLISE DE CONTEXTO

### 1.1 Inferências sobre os 5 Artigos

#### **Artigo 1: "Wireless Mesh Networks Design — A Survey" (Benyamina)**
- **Escopo Inferido:** Levantamento panorâmico de arquiteturas e topologias MESH
- **Conteúdo Provável:**
  - Estrutura de redes MESH (tipos: flat, hierarchical/cluster-based)
  - Comparação preliminar entre protocolos (AODV, OLSR, RPL)
  - Desafios fundamentais: escalabilidade, latência, consumo energético
  - Camada física: wireless standards (802.11, 802.15.4, LoRaWAN)
- **Nível:** Introdutório-intermediário
- **Valor:** Baseline e arquitetura conceitual

#### **Artigo 2: "Performance Evaluation of DigiMesh and ZigBee Wireless Mesh Networks" (Khalifeh)**
- **Escopo Inferido:** Comparação experimental dois protocolos proprietários de baixa potência
- **Conteúdo Provável:**
  - ZigBee: protocolo IEEE 802.15.4, aplicações industriais/residenciais
  - DigiMesh: protocolo proprietário Digi International, foco em IoT e automação
  - Cenários de teste: topologia star, tree, mesh completo
  - Métricas: PDR (Packet Delivery Ratio), latência, throughput, consumo de bateria
  - Ambiente: simulação ou testbed indoor
- **Nível:** Técnico-experimental
- **Valor:** Protocolos comerciais em competição direta

#### **Artigo 3: "Research on the Design and Implementation of a Mesh Network Communication System for Fire and Hazardous Gas Detection and Response" (Lee)**
- **Escopo Inferido:** Aplicação específica de detecção de incêndios em ambientes críticos
- **Conteúdo Provável:**
  - Cenário: edifícios, túneis, ambientes underground com atenuação de sinal
  - Requisitos: latência baixa (<500ms), confiabilidade >99%, cobertura em zonas mortas
  - Protocolo provável: protocolo adaptado AODV ou OLSR com QoS
  - Sensores integrados: temperatura, CO, smoke density
  - Desafio: propagação através de materiais (concreto, metal)
  - Atualização em tempo real para painéis de controle
- **Nível:** Aplicada-industrial
- **Valor:** Requisitos do mundo real + validação prática

#### **Artigo 4: "Mesh Network Performance Measurements" (Passo)**
- **Escopo Inferido:** Metodologia de medição e benchmarking de redes MESH
- **Conteúdo Provável:**
  - Ferramentas de medição: iperf, Wireshark, formadores de tráfego
  - Cenários testados: single-hop, multi-hop com diferentes níveis
  - Métricas coletadas: throughput por hop, latência, jitter, perda de pacotes
  - Impacto de fatores ambientais: interferência 2.4GHz, multipath, shadowing
  - Reprodutibilidade: documentação de ambiente, sementes aleatórias
- **Nível:** Metodológico-experimental
- **Valor:** Framework para validar qualquer protocolo MESH

#### **Artigo 5: "Wireless Mesh Networks: Opportunities and Challenges" (Sichitiu)**
- **Escopo Inferido:** Análise crítica e prospectiva dos desafios abertos
- **Conteúdo Provável:**
  - Oportunidades em IoT, smart cities, disaster recovery, cobertura rural
  - Desafios não resolvidos: roteamento adaptativo, segurança, consumo energético
  - Trade-offs: velocidade de convergência vs overhead de controle
  - Problemas de pesquisa em aberto: routing loops, aging, topology management
  - Perspectiva: machine learning para otimização de roteamento
- **Nível:** Prospectivo-estratégico
- **Valor:** Roadmap de pesquisa futura

---

### 1.2 Protocolos Provavelmente Estudados

| Protocolo | Camada | Tipo | Aplicação | Características |
|-----------|--------|------|-----------|-----------------|
| **AODV** | Roteamento | Reativo | Genérico MESH | On-demand, baixa latência setup, PDR ~95% |
| **OLSR** | Roteamento | Proativo | Militar, backhaul | Tabelas completas, previsível, overhead ~10-15% |
| **RPL** | Roteamento | Híbrido DAG | IoT/6LoWPAN | Tree upward, source routing, otimizado para bateria |
| **ZigBee** | Stack (2-4) | Protocolar | IoT/Home automation | 802.15.4, baixa potência, topologia configurable |
| **DigiMesh** | Stack | Proprietário | Industrial IoT | Mesh completo, recuperação automática, <2s latência |
| **802.11s** | Link/MAC | Padrão | WiFi MESH | Compatível 802.11, HT, VHT, overhead ~5% |

---

### 1.3 Cenários de Aplicação Emergentes

1. **Disaster Recovery / Emergency Communications**
   - Redes temporárias pós-desastres (terremotos, incêndios, inundações)
   - Latência crítica: <500ms
   - Mobilidade: nós podem ser reposicionados rapidamente

2. **Fire & Hazardous Gas Detection (Confirmado por Lee)**
   - Ambientes indoor complexos (edificios) e underground
   - Atenuação severa de sinal
   - Sensores baixa potência + gateway central

3. **IoT / Smart Cities**
   - Milhares de sensores espalhados
   - Escalabilidade crítica (nós dinamicamente adicionados/removidos)
   - Consumo energético sobre bateria: >1 ano de autonomia

4. **Rural Coverage / Last-mile Networks**
   - Cobertura de áreas sem infraestrutura celular
   - Topologia linear alongada
   - Nós semi-moveis (drones repetidores)

5. **Drone Communication Networks**
   - Mobilidade rápida (>10 m/s)
   - Topologia altamente dinâmica
   - Requisito: <100ms latência para controle

---

### 1.4 Métricas Provavelmente Medidas

| Métrica | Definição | Fórmula | Limiar Crítico |
|---------|-----------|---------|----------------|
| **PDR** | Packet Delivery Ratio | pkts_recebidos / pkts_sent | >90% para aplicações críticas |
| **Latência E2E** | Tempo pacote origem→destino | Σ(delay_hop) | <500ms (tempo real) |
| **Throughput/Hop** | Taxa dados por salto | bits/sec / num_hops | Depende app: 1Kbps (sensores) - 1Mbps (video) |
| **Jitter** | Variação latência | StDev(E2E_latency) | <100ms (voz) |
| **Overhead de Roteamento** | % BW para controle | ctrl_pkts / total_pkts | <10% (aceitável) |
| **Consumo Energético** | Energia por pacote entregue | mJ/pkt_delivered | <5mJ (bateria 1 ano) |
| **Convergência** | Tempo até rede estável | time(first_route_found) | <30s (rede <100 nós) |
| **Escalabilidade** | PDR vs nós | degradation_curve | PDR >85% até 1000 nós |

---

## PARTE 2: MAPA DE PESQUISA (TABELA COMPARATIVA)

| **Artigo** | **Foco Principal** | **Protocolo(s)** | **Camada** | **Aplicação** | **Métricas Prováveis** | **Gap Potencial** |
|:---:|:---|:---|:---|:---|:---|:---|
| **1. Benyamina** | Overview arquitetura MESH | AODV, OLSR, RPL (múltiplos) | Roteamento |  Genérico/educacional | Throughput, latência (média) | Sem contexto de aplicação específica |
| **2. Khalifeh** | Comparação ZigBee vs DigiMesh | ZigBee, DigiMesh | Stack completo (2-4) | IoT industrial / home automation | PDR, latência, consumo bateria | Sem teste em topologia mobile (drones) |
| **3. Lee** | Incêndio/detecção hazmat | AODV adaptado ou RPL | Roteamento + sensores | Emergency response crítico | PDR (>99%), latência (<500ms), alcance | Sem QoS formal ou priorização de mensagens |
| **4. Passo** | Metodologia benchmarking | Genérico (framework) | Todas camadas | Validação experimental | PDR, throughput, latência, jitter, overhead | Sem análise de convergência ou estabilidade |
| **5. Sichitiu** | Desafios abertos / oportunidades | GenéricoWiFi MESH, IoT MESH | Todos | Prospectivo (todas) | Identificação teorética | Sem validação experimental dos desafios enumerados |

---

## PARTE 3: GAPS E OPORTUNIDADES DE PESQUISA

### 3.1 Gaps Identificados (Análise de Aderência)

#### **Gap 1: Falta de Estudos em Redes MESH Móveis com Drones**
- **Problema:** Artigos 2-4 assumem topologia estática ou semi-estática
- **Realidade:** Drones como nós mesh é cenário crescente (cobertura rural, disaster recovery)
- **Lacuna:** Sem protocolo específico para mobilidade >5 m/s
- **Métrica faltante:** Tempo de re-convergência de roteamento, handover latency

#### **Gap 2: Ausência de Análise de Segurança em Redes MESH Abertas**
- **Problema:** Nenhum dos 5 artigos menciona segurança, autenticação ou criptografia
- **Realidade:** Redes MESH multi-hop são vulneráveis a ataques de roteamento (black hole, wormhole, sybil)
- **Lacuna:** Como integrar autenticação sem consumir bateria crítica?
- **Métrica faltante:** Overhead de segurança vs consumo energético

#### **Gap 3: Otimização de Energia para Roteamento Adaptativo**
- **Problema:** RPL (Artigo 1) é otimizado para energia, mas sem teste real em cenários mobile
- **Realidade:** IoT MESH exige >12 meses de operação por bateria
- **Lacuna:** Como balancear consumo de energia local vs entrega de pacotes globalmente?
- **Métrica faltante:** "Lifetime Index" = (nós mortos / nós totais) ao longo do tempo

#### **Gap 4: Escalabilidade em Redes Ultra-Grandes (>1000 nós)**
- **Problema:** Testes dos 5 artigos provavelmente com <200 nós
- **Realidade:** IoT em smart cities tem dezenas de milhares de sensores
- **Lacuna:** OLSR não escala (overhead quadrático), AODV tem convergência lenta
- **Métrica faltante:** PDR vs nós numa escala log-linear, bottleneck identification

#### **Gap 5: Redes MESH em Ambientes com Severa Atenuação (como Lee menciona)**
- **Problema:** Lee menciona edifícios/underground, mas sem investigação sistemática
- **Realidade:** Metalização urbana, túneis, subsolos têm atenuação >40dB
- **Lacuna:** Protocolo + potência TX = trade-off nunca explorado
- **Métrica faltante:** SNR vs PDR em função de obstáculos

#### **Gap 6: QoS (Quality of Service) e Priorização de Tráfego**
- **Problema:** Protocolos básicos tratam todos pacotes iguais
- **Realidade:** Incêndio (alerta crítico) ≠ dados de temperatura (background)
- **Lacuna:** Roteamento consciente de prioridade sem breaking compatibilidade
- **Métrica faltante:** "Message Criticality Delivery Rate" = urgente_delivered / urgente_sent

#### **Gap 7: Machine Learning para Adaptação Dinâmica**
- **Problema:** Sichitiu menciona ML como desafio aberto, mas nenhuma implementação
- **Realidade:** Redes reais são heterogêneas (nós diferentes, canais diferentes)
- **Lacuna:** Como treinar modelo ML offline e deploiar on-edge (com low overhead)?
- **Métrica faltante:** Ganho de performance ML vs overhead computacional

---

### 3.2 Combinações Protocolo + Aplicação Faltando

| **Protocolo** | **Aplicação Estudada** | **Aplicação FALTANDO** | **Potencial** |
|---|---|---|:---:|
| AODV | Genérico | Drones em disaster recovery | ★★★★☆ |
| OLSR | WiFi backhaul | Redes rurais com topologia linear | ★★★☆☆ |
| RPL | IoT sensor networks | IoT + mobilidade (ex: asset tracking) | ★★★★★ |
| ZigBee | Home automation | ZigBee + segurança + escala >10k nós | ★★☆☆☆ |
| DigiMesh | Industrial IoT | DigiMesh em ambientes com atenuação | ★★★☆☆ |
| IEEE 802.11s | WiFi mesh | 802.11s com QoS e priorização | ★★★★☆ |

---

## PARTE 4: PROPOSIÇÃO DE LINHAS DE PESQUISA PARA MESTRADO

### Linha 1: **Roteamento Adaptativo para Redes MESH Móveis com Drones**

**Nome:** *"Protocolo de Roteamento Consciente de Mobilidade para MESH Aéreo em Ambientes de Desastre"*

**Questão de Pesquisa:**
- *Como adaptar um protocolo de roteamento MESH (ex: AODV) para cenários de alta mobilidade (drones em disaster recovery) mantendo PDR >90% e convergência <10s?*

**Protocolos a Comparar:**
- AODV (baseline: reactive, não otimizado para mobilidade)
- RPL com ajustes para mobilidade ascendente (AODV+RPL híbrido)
- Protocolo proposto: AODV com predição de movimento (trajectory-aware routing)

**Cenário Experimental:**
- Topologia: 50-100 nós (drones quadcopter + base stations)
- Mobilidade: drones com velocidade 5-15 m/s em padrão de cobertura
- Área: 1km² simulated
- Simulador: NS-3 + drone mobility model (Gauss-Markov ou determinístico)
- Tempo simulação: 600-3600 segundos

**Métricas Principais:**
- PDR global e por hop
- Latência E2E e variância (jitter)
- Tempo de convergência após mudança topologia
- Overhead de roteamento (% packets de controle)
- **Novo:** Re-convergence time quando drone sai de cobertura

**Valor Acadêmico:**
- Aplicação urgente em resgate/disaster recovery
- Contribuição técnica: integração de mobilidade prediction em AODV
- Publicável em: IEEE Wireless Communications, Ad Hoc Networks Journal

**Viabilidade:**
- ✅ Simulador gratuito (NS-3)
- ✅ Código aberto (AODV em NS-3 já existe)
- ✅ Dados de mobilidade de drones públicos (traces UAV)
- ⚠️ Implementação: ~3-4 meses (codificação + validação)

**Escopo para Mestrado:**
- ✅ Apropriado: 12-18 meses
- Semestre 1: Literatura + configuração NS-3
- Semestre 2: Implementação protocolo proposto
- Semestre 3: Experimentos + análise estatística
- Semestre 4: Escrita artigo + dissertação

**Produtos Esperados:**
- 1 artigo em conference (IEEE INFOCOM, ICNP)
- Código fonte em GitHub (open source)
- Dataset de traces de mobilidade padronizado

---

### Linha 2: **Segurança e Autenticação em Redes MESH com Restrição Energética**

**Nome:** *"Framework de Autenticação Leve para Roteamento Seguro em MESH IoT"*

**Questão de Pesquisa:**
- *Como integrar autenticação de nós em protocolo MESH (ex: RPL) sem comprometer o orçamento energético (<5% overhead) e manter convergência <30s?*

**Protocolos a Comparar:**
- RPL vanilla (sem segurança)
- RPL + DTLS (Datagram TLS) padrão
- RPL + esquema autenticação proposto (lightweight MIC-based)

**Cenário Experimental:**
- Topologia: 200-500 sensores IoT (simulado)
- Simulador: Cooja (Contiki) ou NS-3
- Duração: 10 dias virtual (com múltiplos ciclos de join)
- Ataque simulado: Sybil attack, rogue DIOs (DODAG Information Objects)

**Métricas Principais:**
- PDR sob ataque vs baseline
- Consumo energético por pacote criptografado
- Latência de autenticação novo nó
- Overhead de roteamento com validação
- **Novo:** "Security Cost Index" = (energia_overhead / total_energia)

**Valor Acadêmico:**
- IoT security é crítico e subexplorado
- Contribuição: trade-off quantificado segurança % energético
- Publicável em: IEEE Internet of Things Journal, ACM TOSN

**Viabilidade:**
- ✅ Simulador + tools (Cooja disponível)
- ✅ Protocolos (RPL, DTLS standard)
- ✅ Ataques bem documentados (literatura MESH security)
- ⚠️ Implementação: ~2-3 meses

**Escopo para Mestrado:**
- ✅ Apropriado: 12-18 meses total
- Semestre 1: Literatura segurança + RPL deep-dive
- Semestre 2: Implementação + testes ataque
- Semestre 3: Análise estatística + otimizações
- Semestre 4: Escrita

**Produtos Esperados:**
- 1 artigo security-focused (IEEE IoT)
- Código de autenticação open-source
- Benchmark dataset (simulação com 500 nós)

---

### Linha 3: **Roteamento Adaptativo com Machine Learning para Redes MESH Heterogêneas**

**Nome:** *"Aprendizado de Máquina para Seleção Dinâmica de Rotas em MESH Heterogênea"*

**Questão de Pesquisa:**
- *Como usar machine learning (ex: Q-learning, neural network) para treinar um controller que seleciona rotas ótimas em MESH heterogênea, com nós de capacidades diferentes e canais variáveis, reduzindo overhead vs RPL em >15%?*

**Protocolos a Comparar:**
- RPL baseline (determinístico, rank-based)
- AODV vanilla
- Protocolo ML-enhanced (proposto): AODV + Q-learning agent

**Cenário Experimental:**
- Topologia: Heterogênea (mix): 50% sensores baixa potência + 30% relays + 20% full-capability gateways
- Canais: Variáveis (path loss + shadowing simulado)
- Carga: Tráfego dinâmico (bursty, variable packet rate)
- Simulador: NS-3 com agente Python via network simulator backend
- Duração: 5000 simulação seconds

**Métricas Principais:**
- PDR e latência
- Overhead de roteamento (% packets controle)
- Tempo aprendizado da rede (~número episódios)
- **Novo:** "Adaptability Index" = (melhoria_performance / tempo_aprendizado)
- Consumo CPU do agente ML on-device

**Valor Acadêmico:**
- Cruzamento emergente: redes + AI
- Contribuição: quantificar ganho ML vs overhead em redes reais
- Publicável em: IEEE Transactions on Network and Service Management, INFOCOM

**Viabilidade:**
- ✅ Frameworks ML (TensorFlow, Stable-Baselines)
- ✅ NS-3 suporta sim interfacing com Python
- ⚠️ Implementação complexa: ~4-5 meses

**Escopo para Mestrado:**
- ✅ Apropriado: 16-18 meses (complexo)
- Semestre 1: ML basics + redes MESH + simulador
- Semestre 2,5: Design/implementação agente + ambiente
- Semestre 3: Experimentos + tunning hiperparâmetros
- Semestre 4: Escrita + submissão

**Produtos Esperados:**
- 1 artigo AI+Networks (alto impacto)
- Código agente ML open-source (reuso fácil)
- Dataset heterogêneous MESH

---

### Linha 4: **Escalabilidade e Performance em Redes MESH Ultra-Grandes**

**Nome:** *"Análise Comparativa de Escalabilidade: AODV vs OLSR em Redes de 1000+ Nós"*

**Questão de Pesquisa:**
- *Como protocolos reativos (AODV) e proativos (OLSR) escalam em redes com >1000 nós? Qual é o ponto de quebra em PDR, latência e overhead, e qual protocolo é mais adequado para IoT em smart cities?*

**Protocolos a Comparar:**
- AODV escalado
- OLSR escalado
- Híbrido (ex: OLSR com clustering hierárquico)

**Cenário Experimental:**
- Topologia: Gerada aleatoriamente (Poisson point process), área 10km² simulada
- Nós: 100, 300, 500, 750, 1000, 1500
- Mobilidade: Nula (estática) + Low (1m/s) cenários
- Simulador: NS-3 ou OMNeT++
- Duração por experimento: 1000-5000 seg simulado

**Métricas Principais:**
- PDR vs número de nós (curva de degradação)
- Latência E2E vs nós
- Overhead de roteamento (% control packets)
- Tempo convergência inicial
- Consumo memória / CPU simulador

**Valor Acadêmico:**
- Baseline sistemático para escalabilidade
- Recomendações práticas para deployment smart city
- Publicável em: IEEE Transactions on Mobile Computing, Computer Networks

**Viabilidade:**
- ✅ Simulador disponível
- ✅ Protocolos bem implementados
- ✅ Dados: geração topologia automática
- ⚠️ Computação: ~100-300 horas CPU (cluster needed)

**Escopo para Mestrado:**
- ✅ Apropriado: 12-15 meses
- Semestre 1: Revisão + setup simulador
- Semestre 2: Planejamento experimentos (DoE) + validação pequena escala
- Semestre 3: Rodadas full-scale + análise
- Semestre 4: Escrita

**Produtos Esperados:**
- 1 artigo caracterização (benchmark paper)
- Dataset público (traces 1000+ nós)
- Recomendações de protocolo por escala

---

### Linha 5: **Mitigação de Atenuação em Redes MESH para Detecção de Incêndios (Aplicado)**

**Nome:** *"Otimização de Potência e Topologia em MESH Subterrânea para Monitoramento de Incêndios"*

**Questão de Pesquisa:**
- *Como otimizar localização de nós relay e potência de transmissão em MESH subterrâneo/blind spots (ex: mines, túneis) para garantir cobertura >95% e latência <500ms com orçamento energético limitado?*

**Protocolos a Comparar:**
- AODV padrão
- AODV + power control adaptativo
- Protocolo proposto: AODV com informed placement heuristic

**Cenário Experimental:**
- Ambiente: Simulado (modelo pátio-based para atenuação indoor/underground)
- Path loss: Friis + shadowing (standard deviation 10-15dB)
- Obstáculos: Concreto, metal, água (modelos material específico)
- Topologia: Testes com 50-100 nós em layout 2D/3D realista
- Simulador: NS-3 com propagation models customizados

**Métricas Principais:**
- PDR global e por setor
- Latência crítica de alerta
- Consumo energético total
- Número nós necessários para cobertura >95%
- **Novo:** "Coverage Cost Index" = (energia_total / área_coberta)

**Valor Acadêmico:**
- Aplicação crítica do mundo real (incêndios, vidas humanas)
- Contribuição: framework de otimização topologia + potência
- Publicável em: IEEE Sensors Journal, Fire Safety Journal

**Viabilidade:**
- ✅ Simulador + modelos propagação
- ⚠️ Validação em campo difícil (parece impraticável para mestrado)
- ✅ Dados: Literatura sobre atenuação indoor/underground

**Escopo para Mestrado:**
- ✅ Apropriado: 14-18 meses
- Semestre 1: Modelos propagação + calibração simulador
- Semestre 2: Implementação heurísticas de placement
- Semestre 3: Experimentos em múltiplos cenários
- Semestre 4: Escrita + validação com dados reais (se possível)

**Produtos Esperados:**
- 1 artigo aplicado (IEEE Sensors)
- Ferramenta planejamento rede (aberta)
- Recomendações construtivas para engenheiros

---

## PARTE 5: MATRIZ DE DECISÃO E RECOMENDAÇÃO FINAL

### 5.1 Matriz de Avaliação

| **Critério** | **Linha 1** | **Linha 2** | **Linha 3** | **Linha 4** | **Linha 5** |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Impacto Acadêmico** | ⭐⭐⭐⭐☆ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐☆☆ | ⭐⭐⭐⭐☆ |
| **Aplicação Prática** | ⭐⭐⭐⭐☆ | ⭐⭐⭐⭐◯ | ⭐⭐⭐☆☆ | ⭐⭐☆☆☆ | ⭐⭐⭐⭐⭐ |
| **Viabilidade Técnica** | ⭐⭐⭐⭐🞆 | ⭐⭐⭐⭐☆ | ⭐⭐⭐☆☆ | ⭐⭐⭐⭐☆ | ⭐⭐⭐☆☆ |
| **Tempo Estimado** | 12-18 meses | 12-18 meses | 16-18 meses | 12-15 meses | 14-18 meses |
| **Complexidade ML/Inovação** | ⭐⭐⭐☆☆ | ⭐⭐☆☆☆ | ⭐⭐⭐⭐⭐ | ⭐☆☆☆☆ (caracterização) | ⭐⭐⭐⭐☆ |
| **Potencial Publicação** | Journal + Conference | Journal Seguro | Conference top | Journal Benchmark | Journal Aplicada |
| **Risco Técnico** | Baixo-médio | Baixo | Alto | Baixo | Médio |
| **Dados/Recursos Disponíveis** | ✅ Simulador + traces UAV | ✅ Protocolo open-source | ⚠️ Framework ML externo | ✅ Todas ferramentas | ⚠️ Modelos propagação |

---

### 5.2 Análise de Sinergia com Artigos Fornecidos

- **Linha 1** se conecta a: Artigos 1, 3, 5 (mobilidade disaster recovery)
- **Linha 2** se conecta a: Artigos 1, 5 (desafios abertos em segurança)
- **Linha 3** se conecta a: Artigos 5 (ML para otimização)
- **Linha 4** se conecta a: Artigos 1, 4 (benchmarking, escalabilidade)
- **Linha 5** se conecta a: Artigos 3, 4 (medições em cenário específico)

---

## 📋 RECOMENDAÇÃO FINAL

### **Recomendação Prioritária: LINHA 2 - "Framework de Autenticação Leve para Roteamento Seguro em MESH IoT"**

---

### **Por que Linha 2?**

#### **1. Lacuna Crítica Não Preenchida**
Nenhum dos 5 artigos menciona segurança em redes MESH. É um gap **estrutural** na literatura fornecida e na comunidade de redes MESH. Segurança é requisito funcional crescente em IoT.

#### **2. Escopo Fortemente Alinhado com Mestrado**
- **12-18 meses:** Tempo ideal (não muito simples, não excessivamente ambicioso)
- **Viabilidade Alta:** Simulador Cooja já tem suporte para RPL, múltiplos nós, e ataques simulados
- **Risco Técnico Baixo:** RPL e DTLS são bem documentados; não requer inovação radical

#### **3. Impacto Acadêmico Relevante**
- Publicaria em IEEE Internet of Things Journal ou ACM TOSN (journals Q1)
- Crossover com segurança e redes (temas "em voga")
- Contribuição original: quantificar trade-off segurança × energia

#### **4. Aplicação Prática Imediata**
- IoT MESH em smart cities, industrial settings, healthcare (todos requerem autenticação)
- Resultado: recomendações concretas para engenheiros
- Potencial spin-off: consultoria/produto em segurança IoT

#### **5. Evolução Natural da Literatura**
- **Benyamina (Artigo 1):** Fornece overview arquitetura
- **Khalifeh (Artigo 2):** Valida desempenho (baseline)
- **Passo (Artigo 4):** Metodologia benchmarking
- **SUA PESQUISA (Linha 2):** Adiciona segurança ao baseline
- **Sichitiu (Artigo 5):** Identifica desafio; você resolve!

---

### **Abordagem Recomendada (Metodologia)**

```
Semestre 1: Fundação
├─ Revisão: RPL (RFC 6550) + ataques DODAG + DTLS basics
├─ Setup: Cooja + Contiki + 3-4 prototypes pequenos (10-20 nós)
└─ Alinhamento advisor: questão de pesquisa refinada

Semestre 2: Implementação
├─ Desenho esquema autenticação leve (MIC-based ou ECC-based)
├─ Codificação em Contiki C
├─ Testes ataque: injetar DIOs falsos, monitore PDR & consumo

Semestre 3: Validação Experimental
├─ 5-7 experimentos escalando: 50, 100, 200, 500 nós
├─ 10 rodadas por experimento (intervalo confiança 95%)
├─ Análise estatística: ANOVA, box plots, regressão

Semestre 4: Escrita
├─ Artigo IEEE IoT (objetivo)
├─ Dissertação: 60-80 páginas
└─ Apresentação banca
```

---

### **Por que NÃO as outras linhas?**

| Linha | Razão de Não-Prioridade |
|:---:|:---|
| **1 (Drones)** | Excelente, mas requer integração drone simulator + NS-3 (complexidade extra); seria 2ª escolha |
| **3 (ML)** | Muito complexa para 1º mestrado em redes; risco alto de não convergir em 18 meses |
| **4 (Escalabilidade)** | Contribuição mais "caracterização" que "inovação"; publicável mas menos impactante |
| **5 (Incêndios)** | Aplicada mas difícil validar em campo; risco: resultados apenas simulados |

---

### **Próximos Passos (Imediatos)**

1. **Encontro com Advisor:**
   - Apresentar Linha 2 como proposta
   - Validar acesso a Cooja + versão Contiki
   - Afinar questão de pesquisa

2. **Leitura Obrigatória (2-3 semanas):**
   - RFC 6550 (RPL specification)
   - "Vulnerabilities in Low-Power IPv6" (IEEE IoT 2015)
   - "DTLS in Constrained Devices" (IETF RFC 7252 - CoAP)

3. **Prototyping Rápido (1 mês):**
   - Setup Cooja com 20 nós
   - Reproduzir RPL baseline
   - Documentar setup (será base para experimentos)

4. **Define Métricas e Design Experimental (Semana 5-6):**
   - Especificar ataques Sybil/black hole simulados
   - Definir "autenticação leve" (qual algoritmo: HMAC? ECC?)
   - Planejar factorial design (combinações de parâmetros)

---

## CONCLUSÃO

A dissertação em **Linha 2** posiciona o mestrando em uma **fronteira acadêmica real**—segurança em redes MESH IoT—enquanto mantém viabilidade técnica, cronograma realista e potencial de publicação em periódicos de qualidade. 

A combinação de:
- ✅ Protocolo bem-estabelecido (RPL)
- ✅ Simulador robusto (Cooja)
- ✅ Gap não preenchido (segurança)
- ✅ Aplicação prática relevante (IoT)
- ✅ Escopo manuseável (18 meses)

...torna esta a escolha **mais equilibrada** entre inovação, viabilidade e impacto.

---

**Documento preparado com rigor metodológico por: Especialista em Redes MESH**  
**Referencial: Estado da arte em protocolo RPL, IoT security, network simulation**  
**Data: Abril 2026 | Validade: Julho 2026 (recomenda-se revisão de literatura a cada semestre)**
