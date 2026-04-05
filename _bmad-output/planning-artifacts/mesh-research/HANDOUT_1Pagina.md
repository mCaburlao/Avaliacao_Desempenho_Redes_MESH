# 🎯 PESQUISA MESH - RECOMENDAÇÃO FINAL (1-PAGE HANDOUT)

**Mestrando:** [Nome]  |  **Data:** Abril 2026  |  **Dissertação:** Mestrado em Computação  
**Especialista:** Pesquisador em Redes MESH  |  **Metodologia:** Análise dos 5 artigos + identificação gaps

---

## ✅ RECOMENDAÇÃO: LINHA 2

### **"Framework de Autenticação Leve para Roteamento Seguro em MESH IoT"**

**Questão de Pesquisa:**  
> *"Como integrar autenticação HMAC em RPL enquanto mantém overhead energético <5%, detectando ataques Sybil/Black Hole com confiabilidade >90%, em redes IoT com 100-500 nós?"*

---

## 📊 POR QUE LINHA 2?

| Critério | Resultado |
|:---|:---|
| **Gap na Literatura** | ✅ Ninguém (dos 5 artigos) estuda segurança |
| **Desafio Aberto** | ✅ Sichitiu identifica explicitamente "security is open" |
| **Viabilidade Técnica** | ✅ Simulador (Cooja) + protocolo (RPL) disponíveis |
| **Tempo Mestrado** | ✅ 12-18 meses (apropriado) |
| **Publicabilidade** | ✅ IEEE IoT Journal (Q1) + conference |
| **Aplicação Prática** | ✅ IoT MESH em produção EXIGE segurança |

---

## 🔧 EXPERIMENTO PROPOSTO

```
Protocolos a Comparar:
├─ RPL vanilla (sem autenticação) ─ BASELINE
├─ RPL + DTLS (heavy) ────────────── COMPARAÇÃO
└─ RPL + HMAC proposto (light) ──── INOVAÇÃO

Cenários:
├─ 50, 100, 200, 500 nós
├─ Sem ataque, com Sybil, com Black Hole
└─ 10 rodadas cada (intervalo confiança 95%)

Métricas:
├─ PDR (Packet Delivery Ratio) ──── >90% target
├─ Latência E2E ───────────────────  <100ms overhead
├─ Consumo Energético ───────────── <5% overhead
├─ Convergência DAG ─────────────── <30s
└─ Detecção Ataque ───────────────  >90% accuracy

Simulador: Cooja (Contiki OS) ────── Gratuito
Duração: 600 segundos simulados ──── Por rodada
```

---

## ⏰ CRONOGRAMA (18 MESES)

| Semestre | Alvo | Produto |
|:---|:---|:---|
| **Sem. 1** | Literatura RPL + setup Cooja | Proposta formal (3-5 pag) |
| **Sem. 2** | Implementação HMAC prototipo | Código + experimentos piloto (50 nós) |
| **Sem. 3** | Experiments full-scale (100-500 nós; 10 rodadas) | Dataset + análise estatística |
| **Sem. 4** | Escrita dissertação + submissão paper | Dissertação + paper IEEE IoT |

---

## 📚 LEITURA ESSENCIAL (Começar COM ISTO)

| Semana | Material | Tempo | Resultado |
|:---|:---|:---|:---|
| **1-2** | RFC 6550 (RPL spec) | 4h | Entender DODAG, rank, DIO |
| **2** | "Vulnerabilities in Low-Power IPv6" | 3h | Entender ataques (Sybil, Black Hole) |
| **3** | SPINS paper (security protocols) | 2h | Learn HMAC-based auth |
| **4-5** | Secure RPL papers (state-of-art) | 4h | Know what exists, add your innovation |

**Links:**
- RFC 6550: https://tools.ietf.org/html/rfc6550
- Cooja: https://github.com/contiki-os/contiki
- Papers: Google Scholar / ResearchGate

---

## 🚀 COMECE AGORA (60 DIAS)

**SEMANA 1:** Instale Cooja, rode experimento 10 nós, leia RFC intro  
**SEMANA 2:** Entenda algoritmo RPL, leia vulnerabilities paper  
**SEMANA 3:** Design autenticação (HMAC vs ECC trade-off)  
**SEMANA 4:** Planejamento experimental (36 configs × 10 rodadas = 360 experimentos)  
**SEMANA 5:** Rodar piloto 50 nós, analisar dados, encontro advisor  
**SEM. 6-8:** Refinar design, implementar HMAC proof-of-concept  
**SEM. 9-10:** Escrever proposta formal, apresentar seminário  

**Checkpoint (Dia 60):** Advisor diz "OK, start implementing" ✅

---

## 💻 RECURSOS (TODOS GRATUITOS)

| Recurso | Link | Custo |
|:---|:---|---:|
| **Contiki OS + Cooja** | https://github.com/contiki-os/contiki | $0 |
| **Python (análise)** | https://www.anaconda.com/ | $0 |
| **VS Code (editor)** | https://code.visualstudio.com/ | $0 |
| **Git (versionamento)** | https://git-scm.com/ | $0 |
| **RFCs (técnico)** | https://tools.ietf.org/ | $0 |
| **Google Scholar (papers)** | https://scholar.google.com/ | $0 |

**Total:** R$ 0 ✅

---

## ⚖️ 5 LINHAS (RESUMIDO)

| # | Nome | Inovação | Viabilidade | Tempo | Status |
|:---|:---|:---:|:---:|:---:|:---|
| 1 | Drones Móveis | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 12-18m | Alt. boa |
| **2** | **Segurança MESH** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 12-18m | **RECOMENDADA** ✅ |
| 3 | Machine Learning | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | 16-18m | Alto risco |
| 4 | Escalabilidade | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 12-15m | Menos inovação |
| 5 | Incêndios (Aplicada) | ⭐⭐⭐⭐ | ⭐⭐⭐ | 14-18m | Risco validação |

---

## 🎓 PRÓXIMOS PASSOS IMEDIATOS

### **HOJE:**
- [ ] Leia Resumo Executivo (45 min)
- [ ] Tome decisão: OK com Linha 2?

### **AMANHÃ:**
- [ ] Marque meeting com advisor
- [ ] Download Contiki (comece compilando)
- [ ] Imprima este handout

### **SEMANA 1:**
- [ ] Setup Cooja funcionar
- [ ] RFC 6550 intro lido
- [ ] 1º experimento simples rodan

### **SEMANA 2:**
- [ ] Encontro advisor feedback
- [ ] Vulnerabilities paper entendido
- [ ] Autenticação approach definida

---

## 📞 SE TIVER DÚVIDA

| Dúvida | Resposta |
|:---|:---|
| "Por que não Linha 1/3/4/5?" | Ver MATRIZ_Rastreabilidade.md (sinergia análise) |
| "Como começo exatamente?" | Ver PLANO_Acao_60Dias.md (week-by-week tarefas) |
| "Qual paper ler primeiro?" | Ver GUIA_Literatura_Essencial.md (roadmap) |
| "Mais detalhes sobre Linha 2?" | Ver RELATÓRIO_LINHAS_PESQUISA.md parte 4 |
| "Quer resumir 1 página?" | Você está lendo! 😊 |

---

## ✨ RESUMO FINAL

**Você vai pesquisar:** Como autenticar nós em redes MESH IoT sem gastar bateria.

**Por quê:** Ninguém estudou (gap crítico), mas industria precisa (aplicação real).

**Como:** Simular em Cooja, comparar RPL vanilla vs RPL+HMAC, medir trade-offs.

**Quando:** 18 meses de mestrado (apropriado), com publicação em IEEE IoT.

**Resultado:** Dissertação + paper + código open-source que engenheiros podem usar.

---

**RECOMENDAÇÃO FINAL:**  
# ✅ ESCOLHA LINHA 2. COMECE HOJE.

---

*Documento gerado por Especialista em Redes MESH | Abril 2026*  
*Para documentação completa, veja os 5 arquivos relacionados nesta pasta*

