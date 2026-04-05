# ANÁLISE DE ADEQUABILIDADE: MeshSim vs Linhas de Pesquisa

**Data:** Abril 2026  
**Simulador Analisado:** MeshSim-master (NS-3 baseado)  
**Análise:** Alinhamento com 5 linhas de pesquisa propostas

---

## 📊 RESUMO EXECUTIVO

| Linha | Adequabilidade | Recomendação | Score |
|:---|:---:|:---|:---:|
| **L1: Drones Móveis** | ✅ **BOA** | Viável com customizações mínimas | 8/10 |
| **L2: Segurança MESH (⭐ Recomendada)** | ❌ **INADEQUADA** | NÃO recomendado sem grandes mudanças | 2/10 |
| **L3: Machine Learning** | ⚠️ **MÉDIO** | Possível, mas interface manual | 5/10 |
| **L4: Escalabilidade AODV vs OLSR** | ✅ **EXCELENTE** | Simulador perfeito para isso! | 9/10 |
| **L5: Incêndios (Atenuação crítica)** | ⚠️ **POSSÍVEL** | Viável com configuração WiFi | 6/10 |

---

## 🔍 ANÁLISE DETALHADA DO MESHSIM

### O que MeshSim oferece:

**Componentes:**
1. ✅ **Simulador NS-3 modificado** (v3.30 ICSI, 2019)
2. ✅ **Configuration Generator** (scripts, templates)
3. ✅ **Post-processing tools** (análise de resultados, gráficos)

**Protocolos de Roteamento:**
- ✅ OLSR (Optimized Link State Routing)
- ✅ AODV (Ad-Hoc On-Demand Distance Vector)
- ❌ **RPL (IPv6 Routing Protocol for LLN)** — NÃO SUPORTADO

**Capacidades de Rede:**
- ✅ WiFi (padrões configuráveis)
- ✅ Mobilidade (MobilityHelper)
- ✅ Loss models (path loss, shadowing)
- ✅ Delay models
- ✅ Point-to-Point backhaul
- ✅ Aplicações customizáveis (UDP, TCP)
- ✅ PCAP output (captura de pacotes)
- ✅ Topologia Mesh + STAs + APs

**NÃO tem:**
- ❌ RPL (protocolo 6LowPAN/IoT)
- ❌ Segurança/autenticação
- ❌ Low-power protocol stack (CoAP, DTLS)
- ❌ Energy consumption modeling (bateria)
- ❌ Real-time constraints

---

## 📈 ALINHAMENTO COM CADA LINHA

### **LINHA 1: Roteamento Adaptativo para Drones Móveis**

```
Questão: Como adaptar roteamento para mobilidade >5 m/s?
Protocolos: AODV vs RPL híbrido vs proposto
```

**Adequabilidade:** ✅ **BOA (8/10)**

**Por quê:**
- ✅ Suporta AODV (protocolo reativo para mobilidade)
- ✅ Mobilidade configurável (coordenadas, padrões)
- ✅ Métricas: PDR, latência, convergência (PCAP pode capturar)
- ✅ Escalável (9 a N nós em exemplos)

**Limitações:**
- ⚠️ Não tem RPL nativo (precisaria estender NS-3)
- ⚠️ Versão NS-3 antiga (3.30, de 2019)
- ⚠️ Foco em WiFi, não em 802.15.4 (sensores)

**Recomendação:** ✅ **VIÁVEL**
- Use AODV baseline
- Estenda com "proposto: AODV + mobility prediction"
- Maior trabalho: implementar predição no simulador

**Esforço:** Médio (~4-6 sem de customização NS-3)

---

### **LINHA 2: Segurança em IoT MESH**

```
Questão: Como autenticar nós em RPL com overhead <5%?
Protocolo: RPL + HMAC
```

**Adequabilidade:** ❌ **INADEQUADA (2/10)**

**Por quê:**
- ❌ **NÃO TEM RPL** (core protocol para IoT)
- ❌ Não tem stack 6LowPAN/CoAP
- ❌ Sem foco energético (modelos de bateria)
- ❌ Segurança não está modelada
- ❌ Versão NS-3 antiga (seria preciso atualizar)

**Por que MeshSim não funciona:**
1. RPL é protocolo IPv6 para low-power networks
2. MeshSim suporta AODV/OLSR (IPv4, AD-HOC)
3. RPL construção DODAG é completamente diferente
4. Autenticação em RPL é em DIOs (DODAG Information Objects)
5. MeshSim não modelaria energia → overhead % fica impreciso

**Alternativa:** Usar **Cooja + Contiki** (conforme proposto no PLANO_Acao)
- Cooja tem RPL nativo
- Contiki tem stack IoT
- Melhor alinhamento para Linha 2

**Recomendação:** ❌ **NÃO USE MESHSIM PARA LINHA 2**

---

### **LINHA 3: Machine Learning para Roteamento**

```
Questão: ML pode otimizar seleção de rotas em MESH heterogênea?
```

**Adequabilidade:** ⚠️ **MÉDIO (5/10)**

**Por quê:**
- ✅ NS-3 é extensível em C++
- ✅ Pode estender AODV/OLSR com agent ML
- ✅ Coleta de métricas (PDR, latência) → features ML
- ⚠️ Interface Python ↔ NS-3 C++ é complexa

**Limitações:**
- Integrações ML (TensorFlow, Stable-Baselines) não são nativas
- Seria preciso serializar estado, chamar Python, receber ação
- Overhead computacional pode ser alto

**Esforço:** Alto (~8-12 sem customização + ML integration)

**Recomendação:** ⚠️ **POSSÍVEL MAS NÃO IDEAL**
- Se insistir em MeshSim: use Q-learning simples em C++
- Melhor: usar NS-3 + Python via DM (ns3 gym project)
- OU usar framework específico para ML+redes

---

### **LINHA 4: Escalabilidade AODV vs OLSR (100-1500 nós)**

```
Questão: Como AODV/OLSR escalam em redes >1000 nós?
```

**Adequabilidade:** ✅ **EXCELENTE (9/10)**

**Por quê:**
- ✅ Suporta AMBOS protocolos (AODV e OLSR)
- ✅ Configuração modular → fácil variar nós
- ✅ Post-processing tools já fazem benchmarking
- ✅ Escalabilidade é ponto forte do design MeshSim
- ✅ Exemplos já incluem multiple scales

**Vantagens:**
- Infraestrutura exatamente para este caso de uso
- Scripts já existem para variar # de nós
- PDR vs nós é métrica nativa
- Configuração separada de roteamento = fácil trocar protocol

**Esforço:** **BAIXO** (~1-2 sem apenas setup + runs)

**Recomendação:** ✅ **USE MESHSIM PARA LINHA 4!**
- Este é praticamente "off-the-shelf" para escalabilidade
- Precisa apenas: rodar experimentos, coletar data
- Menor trabalho de customização

---

### **LINHA 5: Incêndios - Atenuação Severa**

```
Questão: Como otimizar MESH subterrâneo com atenuação >40dB?
```

**Adequabilidade:** ⚠️ **POSSÍVEL (6/10)**

**Por quê:**
- ✅ WiFi loss models (path loss, shadowing)
- ✅ Configuração modular de propagation
- ✅ AODV pode ser adaptado para ambiente crítico
- ⚠️ Foco em WiFi, não em 802.15.4 (subterrâneo usa freq. mais baixa)

**Limitações:**
- ⚠️ Modelos propagação para WiFi 2.4GHz (subterrâneo → freq. mais baixa)
- ⚠️ Sem latência QoS garantida (<500ms crítico)
- ⚠️ Sem energy modeling

**Esforço:** Médio (~3-4 sem customizações)

**Recomendação:** ⚠️ **VIÁVEL MAS COM RESSALVAS**
- Use loss models de MeshSim
- Configure AODV com timeout curto (latência)
- NÃO ideal para "testes sobre bateria"
- Melhor para "topologia + atenuação + conectividade"

---

## 🎯 MATRIZ DE RECOMENDAÇÃO

| Línea | MeshSim | Alternativa Recomendada | Razão |
|:---|:---:|:---|:---|
| **L1** | ✅ Viável | NS-3 puro (mais flexível) | MeshSim bom baseline, mas L1 exige mobilidade Avançada |
| **L2** | ❌ Inadequado | **Cooja + Contiki** | RPL é native em Cooja, essencial para L2 |
| **L3** | ⚠️ Possível | **NS-3 + Python (ns3 gym)** | ML integration melhor en framework dedicado |
| **L4** | ✅✅ Excelente | **MeshSim (use direto!)** | Feito para isto; melhor choice |
| **L5** | ⚠️ Possível | NS-3 customizado | MeshSim + custom loss models para subterrâneo |

---

## 💡 RECOMENDAÇÃO FINAL

### **Se você quer usar MeshSim:**

✅ **MUDE PARA LINHA 4** (Escalabilidade)
- É a melhor fit
- Maior probabilidade de sucesso
- Menos customização necessária
- MeshSim foi praticamente feito para isto

### **Se insiste em LINHA 2 (Segurança):**

❌ **NÃ O USE MESHSIM**
- Use **Cooja + Contiki OS** (conforme PLANO_Acao propõe)
- RPL é nativo
- Energy modeling existe
- Segurança em DIOs já estudada em academia

### **Se quer explorar LINHA 1 (Drones):**

⚠️ **MeshSim pode servir como baseline**
- Mas procure também **ns-3 vanilla** + mobility extensions
- OU **SUMO** (mobility simulator) + NS-3
- MeshSim menos flexível para trajectory-aware routing

---

## 🔧 PASSOS PRÓXIMOS

### **Caso 1: Queira manter LINHA 2 (recomendada)**
```
1. Ignore MeshSim
2. Siga PLANO_Acao_60Dias (instalar Cooja)
3. Use Contiki RPL
4. Viabilidade ALTA
```

### **Caso 2: Quer aproveitar MeshSim que encontrou**
```
1. Adapte para LINHA 4 (Escalabilidade AODV vs OLSR)
2. Mantenha PLANO_Acao (setup/literatuar/cronograma)
3. Mude apenas "Linha 2" → "Linha 4"
4. Viabilidade ALTÍSSIMA (MeshSim foi feito para isto)
```

### **Caso 3: Quer explorar ambas**
```
1. Semestres 1-2: Use MeshSim + LINHA 4 (rápido, resultado seguro)
2. Semestres 3-4: Estenda com Cooja/Contiki para segurança
3. Dissertação: "Escalabilidade MESH + extensão segurança"
4. Resultado: 2 contribuições (baseline + security)
```

---

## 📋 CONCLUSÃO

| Aspecto | Parecer |
|:---|:---|
| **MeshSim é bom simulador?** | ✅ Sim, baseado em NS-3, modular, com ferramentas |
| **Serve para LINHA 2 recomendada?** | ❌ Não (falta RPL, IoT stack, energia) |
| **Serve para LINHA 4?** | ✅✅ Sim! Praticamente perfeito |
| **Vale a pena explorar?** | ✅ Sim, se adapter para L4 ou usar como complemento |
| **Recomendação final** | **Mude para LINHA 4** ou use Cooja para L2 |

---

**ANÁLISE DE ADEQUABILIDADE | Pesquisador MESH**  
**MeshSim-master vs 5 Linhas de Pesquisa | Abril 2026**
