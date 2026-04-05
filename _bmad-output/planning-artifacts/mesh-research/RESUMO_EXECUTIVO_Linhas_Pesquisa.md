# RESUMO EXECUTIVO
## 5 Linhas de Pesquisa em Redes MESH - Síntese Comparativa

---

## 🎯 ESCOLHA RÁPIDA: Qual Linha Escolher?

```
┌─────────────────────────────────────────────────────────────────┐
│          RECOMENDAÇÃO PRINCIPAL: LINHA 2                        │
│  "Framework de Autenticação Leve para Roteamento Seguro"        │
│                                                                 │
│  ✅ Gap crítico não preenchido (segurança em MESH)              │
│  ✅ Viabilidade alta (Cooja + RPL disponível)                  │
│  ✅ Cronograma perfeito (12-18 meses mestrado)                 │
│  ✅ Publicável IEEE IoT Journal (Q1)                            │
│  ✅ Aplicação prática (IoT crítica em produção)                │
│                                                                 │
│  ⏰ Duração: 12-18 meses                                        │
│  💻 Simulador: Cooja (gratuito, disponível)                    │
│  📊 Experimentos: 200-500 nós virtuais                         │
│  📄 Artigos esperados: 1 journal + 1 conference                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📊 TABELA COMPARATIVA RÁPIDA

| **Aspecto** | **L1: Drones** | **L2: Segurança** | **L3: ML** | **L4: Escalabilidade** | **L5: Incêndios** |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Inovação** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Viabilidade** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Tempo** | 12-18 | **12-18** | 16-18 | 12-15 | 14-18 |
| **Complexidade** | Média | **Baixa** | Alta | Baixa | Média |
| **Risco Técnico** | Médio | **Baixo** | Alto | Baixo | Médio |
| **Publicação** | Journal+Conf | **Journal Seguro** | Top Conf | Benchmark | Aplicada |
| **Gap Literature** | Alto | **Crítico** | Aberto | Alto | Alto |
| **Dados Disponíveis** | ✅ | ✅ | ⚠️ | ✅ | ⚠️ |
| **Trending em 2026** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |

---

## 🗺️ ROADMAP VISUAL: Por que Linha 2?

```
ARTIGOS FORNECIDOS (Estado da Arte):
┌──────────────────────────────────────────────────────────────┐
│ 1. Benyamina    → Overview arquitetura MESH                  │
│ 2. Khalifeh     → Performance DigiMesh vs ZigBee              │
│ 3. Lee          → Detecção incêndios (aplicação específica)  │
│ 4. Passo        → Metodologia benchmarking                   │
│ 5. Sichitiu     → Desafios ABERTOS (incluindo SEGURANÇA) ← │
└──────────────────────────────────────────────────────────────┘
                              ↓
                    GAP IDENTIFICADO
                              ↓
┌──────────────────────────────────────────────────────────────┐
│  NINGUÉM ESTUDA: Segurança em MESH (autenticação, ataques)  │
│  MAS É CRÍTICO PARA: IoT em produção (smart cities, plants) │
│  E VIÁVEL PARA: Mestrado com simulador disponível             │
└──────────────────────────────────────────────────────────────┘
                              ↓
              ✨ LINHA 2: PREENCHE O GAP ✨
```

---

## 📋 DESCRIÇÃO RESUMIDA DE CADA LINHA

### **LINHA 1: Drones + Mobilidade**
```
Questão: Como adaptar roteamento MESH para drones em movimento?
Protocolos: AODV vs RPL vs proposto hybrid
Cenário: 50-100 drones cobrindo 1km² em disaster recovery
Valor: Aplicação urgente (resgate), mas exige integrador drone+NS-3
Risco: Médio (integração complexa)
Resultado: 1 journal + 1 conference paper
```

### **LINHA 2: Segurança em IoT MESH ✅ RECOMENDADA**
```
Questão: Como autenticar nós em MESH sem consumir bateria?
Protocolos: RPL vanilla vs RPL+DTLS vs RPL+lightweight MIC
Cenário: 200-500 sensores, com ataques simulados (Sybil, black hole)
Valor: Lacuna crítica; aplicação imediata em produção
Risco: Baixo (tudo já existe, só combina)
Resultado: 1 journal IEEE IoT (Q1) + 1 conference
```

### **LINHA 3: Machine Learning**
```
Questão: ML pode otimizar seleção de rotas em MESH heterogênea?
Protocolos: AODV vs Q-learning AODV vs neural network routing
Cenário: Mix nós (sensores fracos + relays + gateways), canais variáveis
Valor: Muito trending; crossover redes + AI
Risco: Alto (ML é árduo; pode não convergir em 18 meses)
Resultado: Top conference (se conseguir) ou journal regional
```

### **LINHA 4: Escalabilidade**
```
Questão: AODV vs OLSR em redes >1000 nós? Qual escala melhor?
Protocolos: AODV vs OLSR vs OLSR hierárquico
Cenário: 100, 300, 500, 750, 1000, 1500 nós (área 10km²)
Valor: Benchmark definitivo para smart cities; recomendações práticas
Risco: Baixo; muita computação mas bem-definido
Resultado: 1 benchmark journal + recomendações para engenheiros
```

### **LINHA 5: Incêndios (Aplicada)**
```
Questão: Como otimizar MESH subterrâneo para detectar incêndios?
Protocolos: AODV + power control adaptativo
Cenário: Túneis, minas, edifícios com atenuação severa (>40dB)
Valor: Aplicação crítica (vidas humanas); muito prático
Risco: Médio-alto (hard validar em campo; dados publicados faltam)
Resultado: 1 journal aplicada + ferramenta planejamento rede
```

---

## 🎓 CRONOGRAMA (LINHA 2, Recomendado)

```
SEMESTRE 1 (13 semanas):
├─ Semanas 1-2:   Literatura (RFC 6550, DTLS, ataques MESH security)
├─ Semanas 3-4:   Setup Cooja + Contiki no seu PC
├─ Semanas 5-7:   Prototyping pequeno (10-20 nós, RPL baseline)
├─ Semanas 8-10:  Refinamento questão de pesquisa com advisor
├─ Semanas 11-13: Qualificação / apresentação proposta seminário
└─ Entrega: Proposta formal de dissertação

SEMESTRE 2 (13 semanas):
├─ Semanas 1-4:   Design esquema autenticação (MIC-based vs ECC)
├─ Semanas 5-9:   Implementação em C/Contiki
├─ Semanas 10-12: Testes ataque (injetar DIOs falsos, medir impacto)
└─ Entrega: Código + experimento piloto 50 nós

SEMESTRE 3 (13 semanas):
├─ Semanas 1-2:   Planejamento experimentos (factorial design)
├─ Semanas 3-8:   Rodadas completas (50, 100, 200, 500 nós)
├─ Semanas 9-11:  Análise estatística (ANOVA, regressão, gráficos)
└─ Entrega: Dataset + resultados preliminares + draft paper

SEMESTRE 4 (13 semanas):
├─ Semanas 1-6:   Escrita artigo (IEEE IoT target)
├─ Semanas 7-10:  Escrita dissertação (60-80 páginas)
├─ Semanas 11-12: Submissão conference + revisão final
└─ Entrega: Dissertação + artigo submetido + apresentação banca
```

---

## 🔧 SETUP TÉCNICO (LINHA 2)

### Ferramentas Necessárias (Gratuitas):
```
✅ Cooja Simulator        → Contiki OS, simula redes wireless
✅ Contiki C compiler     → Código dos nós, implementar RPL
✅ Python 3 + NumPy/SciPy → Análise estatística dos resultados
✅ Matplotlib/Seaborn     → Gráficos publicáveis
✅ Git + GitHub           → Versionamento código + open source
✅ LaTeX                  → Dissertação + paper
```

### Recursos Computacionais:
```
💻 PC Desktop:    Suficiente (CPU: i5+ ; RAM: 8GB+)
⏱️  Tempo CPU:     ~50-100 horas (rodas paralelas simulador)
🗄️  Armazenamento: ~10GB (logs + datasets)
```

### Dados Iniciais:
```
✅ RFC 6550 (RPL spec)               → IETF public
✅ Ataque Sybil em DAG               → IEEE papers
✅ DTLS RFC 6347                     → IETF public
✅ Contiki RPL implementation        → GitHub open source
```

---

## 📊 MÉTRICAS PRINCIPAIS (LINHA 2)

```
Métrica 1: PDR (Packet Delivery Ratio)
├─ Definição: pkts_recebidos / pkts_enviados
├─ Esperado: >90% com autenticação; degradação <5% vs baseline
└─ Threshold crítico: >85% (senão, não é viável)

Métrica 2: Latência de Autenticação
├─ Definição: time(packet_auth_ok) - time(packet_sent)
├─ Esperado: <100ms adicional por autenticação
└─ Threshold: <10% overhead latência

Métrica 3: Consumo Energético por Pacote
├─ Definição: (energia_CPU + energia_radio) / pkts_entregues
├─ Esperado: <5% overhead vs RPL vanilla
└─ Threshold crítico: <10% (senão morre bateria)

Métrica 4: Detecção de Ataque (Sybil/Black Hole)
├─ Definição: ataque_detectado / ataque_injected
├─ Esperado: >95% dos ataques detectados
└─ Threshold: >80%

Métrica 5: Security Cost Index (Novo)
├─ Definição: overhead_energia / energia_total (%)
├─ Esperado: <5%
└─ Contribuição original
```

---

## 💡 DÚVIDAS FREQUENTES

### **P: Por que não ML (Linha 3)?**
R: ML é complexo + incerto. Se errar no design do agente, não converge até dezembro. Linha 2 é "safer bet" com garantia de sucesso.

### **P: Posso combinar duas linhas?**
R: Não recomendado em 18 meses de mestrado. Foco é melhor. (Mas Linha 2 + Linha 1 seria uma doutorado interessante!)

### **P: Preciso de drone real para Linha 1?**
R: Não. Simulador NS-3 + mobility traces de drones públicos é suficiente para mestrado.

### **P: Meu advisor quer que estude incêndios (Linha 5). Problema?**
R: Não problema. Linha 5 é viável. Mas avise que validação em campo pode ser restrita (segurança, acesso). Ênfase em simulação é recomendada.

### **P: Como publico logo? (Linha 4)**
R: Linha 4 é mais fácil publicar em benchmark journal (ex: Computer Networks). But Linha 2 publica em security journal + conference (mais impacto).

---

## ✅ CHECKLIST PRÉ-COMEÇAR (LINHA 2)

- [ ] Ler RFC 6550 (RPL) — entender DAG construction
- [ ] Ler "Vulnerabilities in Low-Power IPv6" — entender ataques típicos
- [ ] Instalar Cooja + Contiki no seu PC
- [ ] Rodar exemplo simples Cooja (10 nós, RPL padrão)
- [ ] Encontrar 3 papers sobre DTLS em constrained devices
- [ ] Definir "autenticação leve": qual esquema? (HMAC? ECC? PSK?)
- [ ] Conversar com advisor sobre questão de pesquisa refinada
- [ ] Escrever proposta formal (2 páginas) para seminário

---

## 📞 PRÓXIMOS PASSOS

1. **Semana 1:** Leia este relatório + recomendação final
2. **Semana 2:** Discuta com seu advisor; refine questão de pesquisa
3. **Semana 3:** Instale Cooja e rode experimento piloto
4. **Semana 4:** Comece literatura formal; escreva proposta
5. **Semana 5:** Apresente no seminário de pesquisa

---

**Documento de Síntese | Especialista em Redes MESH**  
**Complementar ao: Relatório_Linhas_Pesquisa_MESH.md**  
**Recomendação: Leia este documento primeiro; depois o relatório completo para detalhes**

