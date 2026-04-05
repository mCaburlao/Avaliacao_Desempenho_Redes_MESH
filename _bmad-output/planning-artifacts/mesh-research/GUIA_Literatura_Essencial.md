# GUIA DE LITERATURA ESSENCIAL
## Para Começar a Pesquisa em Redes MESH (Linha 2 - Recomendada)

---

## 📚 LEITURA ESSENCIAL ORDENADA

### **FASE 1: Fundação (Semanas 1-2)**
Ler na sequência abaixo. Total ~10-15 horas.

#### **1.1 Protocolo RPL (RFC 6550)**
- **Título:** "RPL: IPv6 Routing Protocol for Low-Power and Lossy Networks"
- **URL:** https://tools.ietf.org/html/rfc6550
- **Por quê:** É o coração da sua pesquisa; entender DODAG, rank, DIO crucial
- **Foco:** Seções 1-4 (overview, terminologia, algoritmo core)
- **Tempo:** 3-4 horas
- **Notas:**
  - DODAG = Directed Acyclic Graph (não é árvore!)
  - DIO = DODAG Information Object (pacote de controle)
  - Rank = posição na hierarquia
  - Security extensions em Seção 6 (skip detalhes por enquanto)

#### **1.2 Security Threats em Redes de Sensores**
- **Título:** "Vulnerabilities in Low-Power IPv6" 
- **Recomendado:** IEEE article ou paper Tsao et al. (2015)
- **URL:** Procure em Google Scholar: "RPL security vulnerabilities"
- **Por quê:** Entender ataques específicos (Sybil, blackhole, topology)
- **Foco:** Ataques no DAG construction, rank manipulation
- **Tempo:** 2-3 horas
- **Chave:**
  - Sybil attack: nó falso se passa por múltiplas identidades
  - Black hole: nó adota rank baixo mas descarta pacotes
  - Wormhole: nó cria atalho falso na topologia

#### **1.3 CoAP e DTLS para IoT**
- **Título:** "The Constrained Application Protocol (CoAP)" - RFC 7252
- **URL:** https://tools.ietf.org/html/rfc7252
- **E:** "DTLS for IoT" - RFC 6347 (Datagram TLS)
- **Por quê:** CoAP roda sobre DTLS em redes seguras; entender overhead
- **Foco:** Seção sobre DTLS usage, session setup, handshake
- **Tempo:** 2-3 horas
- **Notas:**
  - DTLS = TLS para UDP (pacotes)
  - Handshake DTLS ≈ 2-3 RTTs (latência!)
  - Consumo energia pode ser problema

---

### **FASE 2: Simulador e Ambiente (Semanas 3-4)**
Total ~6-8 horas prática.

#### **2.1 Cooja Simulator Setup**
- **Título:** "Cooja Simulator User Guide"
- **URL:** http://www.contiki-os.org/start.html (buscar Cooja documentation)
- **Por quê:** É sua ferramenta de trabalho; hands-on essencial
- **Instalação:** Linux/Windows (recomendado WSL2 no Windows)
- **Tempo:** 2-3 horas instalação + testes básicos
- **Checklist:**
  - [ ] Java instalado (JDK 8+)
  - [ ] Contiki-OS clone do GitHub
  - [ ] Compile Cooja
  - [ ] Rode simulação exemplo (10 nós)
  - [ ] Veja logs, topologia visual

#### **2.2 Contiki RPL Implementation**
- **Título:** "Contiki RPL Source Code walkthrough"
- **URL:** GitHub: contiki-os/contiki (pasta: core/net/rpl/)
- **Por quê:** Entender como RPL está codificado; vai modificar
- **Tempo:** 2-3 horas
- **Arquivos chave:**
  - `rpl-icmp6.c` — protocolo RPL (DIOs, DAOs)
  - `rpl-dag.c` — DAG management
  - `rpl.h` — estruturas dados
- **Tarefa:** Trace um DIO packet (origem → destino) no código

#### **2.3 Primeiro Experimento: RPL Baseline (10 nós)**
- **Por quê:** Validar setup; coletar baseline de performance
- **Tempo:** 1-2 horas
- **Resultado esperado:**
  - Todos nós conectam em DAG (rank 1-3)
  - PDR ~99% (sem ataques)
  - Convergência <30 segundos

---

### **FASE 3: Segurança em IoT (Semanas 5-7)**
Total ~12-15 horas leitura.

#### **3.1 Lightweight Authentication Schemes**
- **Título:** "SPINS: Security Protocols for Sensor Networks"
- **Autores:** Perrig et al. (2002)
- **URL:** Google Scholar ou http://www.cs.berkeley.edu/~adi/
- **Por quê:** Framework clássico para autenticação leve
- **Foco:** µTESLA (broadcast authentication), key derivation
- **Tempo:** 3-4 horas
- **Conceitos:**
  - Message Authentication Code (MAC)
  - Key chain: chave0 → chave1 → chave2
  - Delayed disclosure para autenticação broadcast

#### **3.2 ECC (Elliptic Curve Cryptography) para Constrained Devices**
- **Título:** "ECC over F_p for Embedded Systems"
- **Procure:** Papers sobre ECDH, ECDSA em sensores
- **URL:** Google Scholar: "elliptic curve cryptography wireless sensor networks"
- **Por quê:** ECC é mais eficiente que RSA em dispositivos baixa potência
- **Tempo:** 3-2 horas (matemática pode ser densa; ok skip provas)
- **Prático:**
  - ECC 256-bit ≈ RSA 3072-bit em segurança
  - Menos computação, menos energia

#### **3.3 HMAC-based Key Derivation**
- **Título:** "HKDF: A Simple and Flexible Approach to Key Derivation"
- **RFC:** 5869
- **URL:** https://tools.ietf.org/html/rfc5869
- **Por quê:** Usar HMAC + salt para derivar múltiplas chaves de 1 seed
- **Tempo:** 1-2 horas
- **Aplicação:** Derivar chave autenticação por nó sem guardar muitos secrets

#### **3.4 State-of-Art: Secure RPL**
- **Título:** "Secure RPL" ou "RPL with built-in security"
- **Procure:** Papers recentes (2018-2022) sobre "RPL security extensions"
- **URL:** IEEE Xplore, Google Scholar
- **Exemplos:**
  - "Enhanced RPL with Authentication" (buscar 2019-2020)
  - "Detecting Sybil Attacks in RPL" (buscar 2017+)
- **Tempo:** 4-5 horas (ler 3-4 papers)
- **Nota:** Estude o estado da arte; sua inovação é adicionar **eficiência energética** ao que já existe

---

### **FASE 4: Metodologia Experimental (Semanas 8-9)**
Total ~5-7 horas leitura + prática.

#### **4.1 Experimental Design for Wireless Networks**
- **Título:** "Designing and Conducting Network Experiments"
- **Procure:** Methodology papers (IEEE Communications Surveys & Tutorials)
- **Foco:** Factorial design, replication, statistical rigor
- **Tempo:** 2-3 horas
- **Conceitos:**
  - Independent variable: # nós, ataque presente/não
  - Dependent variable: PDR, latência, energy
  - Replication: 10-20 rodadas diferentes sementes

#### **4.2 Statistical Analysis for Networking**
- **Livro curto:** "Statistics for Engineers" (Seção inference)
- **Online:** Khan Academy "Inferential Statistics"
- **Foco:** 
  - Intervalo confiança 95%
  - ANOVA (análise variância)
  - Box plots + error bars
- **Tempo:** 2-3 horas
- **Prático:** Você usará Python (scipy, statsmodels)

#### **4.3 Reprodutibilidade e Validação**
- **Título:** "How to Ensure Your Simulation Results are Trustworthy"
- **Procure:** Paper Tobagi ou "Wireless simulation best practices"
- **Foco:**
  - Mesmas sementes aleatórias = mesmos resultados
  - Documentar parâmetros do simulador
  - Disponibilizar código no GitHub
- **Tempo:** 1-2 horas

---

## 📖 REFERÊNCIAS AGRUPADAS POR TÓPICO

### **RPL & Roteamento em IoT**
1. RFC 6550 — "RPL: IPv6 Routing Protocol for Low-Power and Lossy Networks" ⭐⭐⭐
2. RFC 6206 — "The Trickle Algorithm" (broadcast RPL)
3. "Performance Evaluation of RPL in Wireless Sensor Networks" — IEEE IoT Journal 2017
4. "RPL Protocols: A Comparison" — Ad Hoc Networks Journal 2018

### **Segurança em Redes de Sensores**
1. "SPINS: Security Protocols for Sensor Networks" — Perrig et al. ⭐⭐⭐
2. RFC 7748 — "Elliptic Curves for Security" (ECC)
3. "Vulnerabilities in Low-Power IPv6" — IEEE/IETF 2015 ⭐⭐⭐
4. "Authentication and Authorization in Wireless Sensor Networks" — Survey IEEE 2014

### **DTLS & Segurança IoT**
1. RFC 6347 — "Datagram Transport Layer Security (DTLS)" ⭐⭐
2. RFC 7252 — "The Constrained Application Protocol (CoAP)"
3. "DTLS in Wireless Sensor Networks: Overhead Analysis" — IEEE IoT Journal 2016

### **Simulação em NS-3 / Cooja**
1. "NS-3 Simulator User Manual" — https://www.nsnam.org/docs/ ⭐⭐
2. "Cooja Simulator Tutorial" — Contiki documentation
3. "Validation of Wireless Network Simulators" — IEEE SEPEDS 2010
4. "Best Practices for Network Simulation" — IEEE Communications Magazine 2011

### **Metodologia Experimental**
1. "Designing Experiments in Computer Science" — David Rosenblum, UC Berkeley
2. "Statistical Methods for Engineers" — Montgomery & Runger (Cap. Inference)
3. "Wireless Network Measurement Campaigns" — IEEE Survey 2017

### **Trabalhos Relacionados (Recomendado ler depois)**
- "Lightweight Authentication for Wireless Sensor Networks" — IEEE Security 2015
- "Energy-Efficient Key Management for Wireless Sensor Networks" — ACM TOSN 2012
- "Detecting and Preventing Sybil Attacks in Wireless Networks" — IEEE TMC 2011

---

## 🎯 SEQUÊNCIA RECOMENDADA DE LEITURA (RESUMO)

```
SEMANA 1-2 (Fundação Teórica):
├─ RFC 6550 (RPL specification)              [CRÍTICO]
├─ "Vulnerabilities in Low-Power IPv6"       [CRÍTICO]
├─ RFC 5869 (HKDF - key derivation)          [Importante]
└─ RFC 7748 (ECC curves)                     [Contexto]

SEMANA 3-4 (Prática: Setup):
├─ Cooja Simulator tutorial + instalação     [HANDS-ON]
├─ Contiki RPL source code walkthrough       [HANDS-ON]
└─ Experiment #1: RPL baseline 10 nós        [DELIVERABLE]

SEMANA 5-7 (Segurança em Profundidade):
├─ SPINS: Security Protocols                 [Clássico]
├─ ECC para Constrained Devices              [Técnico]
├─ State-of-Art: Secure RPL papers           [Pesquisa]
└─ Literature notes: threats vs. mitigation  [síntese]

SEMANA 8-9 (Metodologia):
├─ Experimental design for wireless          [Framework]
├─ Statistical analysis 101                  [Ferramentas]
└─ Reprodutibility best practices            [Rigor]

SEMANA 10-13:
└─ Refinamento proposta com advisor
```

---

## 🔗 ONDE ACHAR OS ARTIGOS

### **Acesso Gratuito (Recomendado)**
- **RFCs:** https://tools.ietf.org/ (TODOS públicos, livre)
- **Google Scholar:** https://scholar.google.com/ (procure + "find full text")
- **ResearchGate:** https://www.researchgate.net/ (autores compartilham)
- **ArXiv:** https://arxiv.org/ (preprints, muita boa qualidade)
- **GitHub:** Procure "wireless mesh network research" (muitos dados públicos)

### **Acesso Institucional**
- IEEE Xplore (via UFABC)
- ACM Digital Library (via UFABC)
- Springer Link (via UFABC)
- Wiley InterScience (via UFABC)

### **Se Não Achar:**
- Email author: "Dear Dr. X, could you share your paper on Y? I'm researching..."
- 90% das vezes responde em 24h!

---

## 💡 DICAS DE LEITURA EFICIENTE

### **Para Papers Científicos:**
1. **Não leia sequencial.** Comece:
   - Título + Abstract (5 min)
   - Seção 1: Introdução + Related Work (10 min)
   - Seção 2: Abordagem proposta (20 min)
   - Seção 4: Resultados (15 min)
   - Discussão + Conclusão (10 min)
   - **Detalhes técnicos:** só se relevante

2. **Faça anotações (Markdown):**
   ```markdown
   # Paper X: "Título"
   - Problema: ...
   - Solução: ...
   - Metrics: PDR, latência, energia
   - Key insight: ...
   - Limitations: ...
   - Relevância para minha pesquisa: 7/10
   ```

3. **Tempo recomendado por paper:** 
   - 1ª leitura: 45 min
   - 2ª leitura (se importante): 1.5h
   - Implementar insights: depende

### **Para RFCs:**
- RFCs são spec formais; longas. Estratégia:
  1. Tabela conteúdo (1 min)
  2. Seção relevante para você (20-30 min)
  3. Exemplos pseudocódigo (10 min)
  4. Volta rapidamente seções anteriores se confuso

---

## 📊 ROADMAP DE PESQUISA

```
LITERATURA ──┐
             ├─→ QUESTÃO DE PESQUISA refinada
SIMULADOR ──┤
             ├─→ DESIGN EXPERIMENTAL
METODOLOGIA─┘
              ↓
         PROPOSTA FORMAL
              ↓
  Semestres 2-4: Implementação + Escrita
```

**Checkpoint Semana 9-10:**
- [ ] Li RFC 6550 (RPL)
- [ ] Li "Vulnerabilities" paper
- [ ] Entendo diferença SPINS vs minha abordagem
- [ ] Setup Cooja funciona
- [ ] Pergunta de pesquisa refinada no papel
- [ ] Metodologia esboçada (n de nós, ataques, métricas)

---

## 🚀 PRÓXIMO PASSO

1. **Esta semana:** Imprima ou salve RFC 6550 + "Vulnerabilities" paper
2. **Comece leitura:** 2-3h/dia durante 2 semanas
3. **Instale Cooja:** Em paralelo (não espere terminar leitura)
4. **Semana 3:** Combine: leitura teórica + prática Cooja
5. **Semana 5:** Encontro formal com advisor com proposta refinada

---

**Guia de Literatura | Especialista em Redes MESH**  
**Complementar aos outros relatórios desta pesquisa**  
**Atualizado: Abril 2026**

