# PLANO DE AÇÃO EXECUTIVO
## Início da Pesquisa em Linha 2 (Próximos 60 Dias)

**Data Início:** Primeira semana de Abril 2026  
**Data Alvo:** Fim Giugno 2026 (Proposta refinada com advisor)  
**Linhas de Pesquisa Selecionada:** **LINHA 2 - Framework de Autenticação Leve para Roteamento Seguro em MESH IoT**

---

## 🎯 OBJETIVO FINAL (60 DIAS)

```
┌─────────────────────────────────────────────────┐
│  Ter PROPOSTA FORMAL ESCRITA E VALIDADA com    │
│  advisor no final de 60 dias:                   │
│                                                 │
│  ✅ Questão de pesquisa refinada               │
│  ✅ Protocolos a comparar definidos             │
│  ✅ Cenários experimentais descritos            │
│  ✅ Métricas especificadas                      │
│  ✅ Cronograma semestral (4 sprints)            │
│  ✅ Riscos identificados                        │
│  ✅ Simulador validado (Cooja + RPL rodam)     │
│  ✅ Cronograma mestrado realista                │
└─────────────────────────────────────────────────┘
```

---

## 📅 CRONOGRAMA DETALHADO (60 DIAS)

### **SEMANA 1 (Dias 1-7): Nivelamento + Setup**

#### Dia 1-2: Leitura Rápida + Contextualização
- **Atividade:** Ler resumo executivo deste relatório (este arquivo!)
- **Tempo:** 2 horas
- **Entrega:** Anotações: "Por que Linha 2? Quais são os gaps?"

- **Atividade:** Assistir video 10min sobre RPL basics (YouTube: "RPL Protocol Explained")
- **Tempo:** 15 min
- **Objetivo:** Familiaridade visual com DAG, rank, DIO

#### Dia 3-4: Download & Instalação Cooja
- **Atividade:** Instalar Contiki OS + Cooja no PC
- **Referência:** https://github.com/contiki-os/contiki (README)
- **Tempo:** 2-3 horas (inclui troubleshooting)
- **Resultado esperado:**
  - [ ] Clonar repositório: `git clone https://github.com/contiki-os/contiki.git`
  - [ ] Instalar dependências: `apt install build-essential` (Linux) ou MacPorts (Mac)
  - [ ] Compilar Cooja: `cd tools/cooja && ant jar`
  - [ ] Executar: `ant run`

#### Dia 5-7: Primeiro Experimento Cooja
- **Atividade:** Rodar simulação exemplo (10 nós, RPL default, 600 segundos)
- **Passos:**
  1. Abrir Cooja
  2. "New Simulation"
  3. Add 10 motes (tipo: Cooja Mote w/ RPL)
  4. Start simulation → observar convergência DAG
  5. Coletar métricas: # nós com rank, latência DIO

- **Tempo:** 3-4 horas
- **Produto:** Screenshot + log da simulação (salvar)
- **Checkpoint:** Cooja funciona; você entende interface

---

### **SEMANA 2 (Dias 8-14): Literatura Fase 1**

#### Dia 8-10: RFC 6550 (RPL Specification)
- **Material:** https://tools.ietf.org/html/rfc6550
- **Tempo:** 3-4 horas (não precise ler cada detalhe)
- **Estratégia de leitura:**
  1. Seção 1: Introdução (30 min) → entender motivação
  2. Seção 2: Terminologia (20 min) → DAG, DODAG, rank, DIO, DAO
  3. Seção 3: Algoritmo Core (1h) → como DAG é construído
  4. Seção 6: Segurança (20 min) → conhecer o que já existe (skip detalhes)
  5. Rest: skim conforme necessário

- **Entrega:** Documento (1 página) com:
  - Definição: O que é RPL? (3-4 linhas)
  - DODAG formation: step-by-step (5-6 linhas)
  - Current security mechanisms in RPL (3-4 linhas)

#### Dia 11-14: "Vulnerabilities in Low-Power IPv6" Paper
- **Material:** Google Scholar: "Vulnerabilities in Low-Power IPv6" (buscar 2015-2017)
- **Exemplos concretos:**
  - Tsao, T., et al. "Vulnerabilities in RPL..." IEEE Internet-of-Things Journal 2015
  - Ou buscar "RPL security" com ano 2016+

- **Tempo:** 3-4 horas
- **Strategy:**
  1. Ler Abstract + Introduction (20 min)
  2. Ler Related Work section (15 min)
  3. Entender cada attack description (30 min por attack = 2h total)
  4. Estudar proposed countermeasures (20 min)
  5. Ler Discussion/Conclusions (10 min)

- **Entrega:** Tabela (CSV ou Markdown):
  ```
  Attack Name | How It Works | Impact (PDR % loss) | Mitigation
  Sybil       | Nó falso se passa por múltiplos  | 30- 50% | Authentication
  Black Hole  | Rank baixo mas descarta pkts | 80-100% | Monitoring
  ...
  ```

#### Checkpoint Semana 2:
- [ ] RFC 6550 resumo escrito
- [ ] Security attacks table preenchida
- [ ] Arquivo: `/research/week2_literature_summary.md`

---

### **SEMANA 3 (Dias 15-21): Prototipagem + Primeira Proposta**

#### Dia 15-17: Protocolo Baseline (Code Review)
- **Atividade:** Examinar código RPL em Contiki
- **Arquivos:** 
  - `contiki/core/net/rpl/rpl-icmp6.c` (protocolo)
  - `contiki/core/net/rpl/rpl-dag.c` (DAG management)

- **Tempo:** 2-3 horas
- **Tarefa:** Trace um pacote DIO:
  1. Onde é gerado? (source → função)
  2. Como é enviado? (qual socket?)
  3. Como é recebido? (qual handler?)
  4. Como afeta rank? (atualização DAG)

- **Entrega:** Arquivo `week3_rpl_code_trace.md` com diagram ASCII

#### Dia 18-19: Design da Autenticação
- **Atividade:** Esboçar qual esquema usar
- **Opções a considerar:**
  1. **HMAC-based (simples, recomendado):**
     - Chave pré-compartilhada entre nós
     - HMAC-SHA256 de cada DIO
     - Verificação no receptor
     - Trade-off: <5% latência adicional, ~2-3mJ consumo

  2. **ECC-based (mais seguro, mais complexo):**
     - ECDH key agreement
     - ECDSA signatures
     - Trade-off: >10% latência, ~10-15mJ consumo

  3. **PSK + MIC (lightest):**
     - Pre-shared key simple
     - Message Integrity Check (HMAC)
     - Trade-off: <3% overhead, ~1-2mJ

- **Tempo:** 2 horas
- **Entrega:** Documento 1-2 páginas: "Autenticação Approach - Trade-offs"

#### Dia 20-21: Questão de Pesquisa Refinada
- **Atividade:** Escrever questão precisa
- **Template:**
  ```
  Questão: "Como integrar [AUTENTICAÇÃO] em [RPL] 
           mantendo [CONSUMO ENERGÉTICO] < [X%] adicional, 
           e detectando [ATAQUES] com confiabilidade > [Y%],
           em cenário de [N NÓS]?"
  ```

- **Exemplo concreto:**
  ```
  Questão: "Como integrar autenticação HMAC em RPL 
           mantendo overhead energético < 5%, 
           detectando Sybil + Black Hole attacks com >90% cobertura,
           em redes com 100-500 nós IoT?"
  ```

- **Tempo:** 1-2 horas
- **Entrega:** Questão de pesquisa em `/research/research_question.md`

#### Checkpoint Semana 3:
- [ ] Código RPL entendido
- [ ] Autenticação approach definida (HMAC vs ECC vs PSK)
- [ ] Questão de pesquisa escrita formalmente

---

### **SEMANA 4 (Dias 22-28): Metodologia + Planejamento Experimental**

#### Dia 22-24: Experimental Design
- **Atividade:** Desenhar experimentos
- **Componentes:**

1. **Independent Variables (o que você controla):**
   - Número de nós: 50, 100, 200, 500
   - Autenticação: Disabled, HMAC, ECC
   - Ataques simulados: None, 1 Sybil, 2 Black Holes
   - Tempo simulação: 1800 segundos

2. **Dependent Variables (o que você mede):**
   - PDR (Packet Delivery Ratio)
   - Latência E2E média + StDev
   - Overhead energético (mJ/pkt)
   - Convergência DAG (tempo até estável)

3. **Design:**
   - Fatorial completo: 4 (nós) × 3 (auth) × 3 (ataques) × 1 (tempo) = **36 configurações**
   - Cada configuração: **10 rodadas** (diferentes sementes aleatórias)
   - Total: **360 rodadas** × 30 min/rodada = **180 horas CPU** (OK para cluster)

- **Tempo:** 2-3 horas planejamento
- **Entrega:** Arquivo `experiment_design.md` com tabela all combinations

#### Dia 25-26: Setup Métricas em Cooja
- **Atividade:** Adicionar logging no simulador
- **O que coletar:**
  - DIO packets sent/received (PDR)
  - Packet timestamp (latência)
  - Energy consumption (simulador)
  - Rank per node over time (convergência)

- **Tempo:** 2 horas
- **Tarefa:** Editar arquivo Cooja Java para adicionar custom logging
- **Entrega:** Script Python para parser logs → CSV

#### Dia 27-28: Planejamento Cronograma Mestrado
- **Atividade:** Detalhar os 4 semestres
- **Output:** Arquivo `dissertation_timeline.md` com:
  - Semestre 1: Qual capítulo dissertação?
  - Semestre 2: Quais experimentos rodando?
  - Semestre 3: Análise + paper draft?
  - Semestre 4: Escrita final + submissão?

- **Tempo:** 1-2 horas
- **Checkpoint:** Viabilidade de 18 meses confirmada

---

### **SEMANA 5 (Dias 29-35): Validação Baseline**

#### Dia 29-31: Primeira Rodada Piloto (50 nós, sem ataque)
- **Atividade:** Rodar Cooja para coletar baseline
- **Config:**
  - 50 sensores em topologia aleatória
  - RPL default (sem autenticação)
  - 600 segundos simulação
  - Coletar logs completos

- **Tempo:** 4-6 horas (dependendo PC)
- **Produto:** Arquivo `baseline_50nodes.log`

#### Dia 32-33: Análise Dados Piloto
- **Atividade:** Processamento com Python
- **Script:**
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  
  # Parse logs
  data = pd.read_csv('baseline_50nodes.log')
  
  # Compute metrics
  pdr = (data['received'] / data['sent']).mean()
  latency_mean = data['latency'].mean()
  latency_std = data['latency'].std()
  
  # Plot
  plt.figure()
  plt.hist(data['latency'], bins=20)
  plt.xlabel('E2E Latency (ms)')
  plt.ylabel('Frequency')
  plt.savefig('latency_distribution.png')
  ```

- **Tempo:** 2 horas
- **Entrega:** Gráficos + tabela resultado

#### Dia 34-35: Refinamento + Revisão com Advisor
- **Atividade:** Convo com advisor sobre progresso
- **Trazer:**
  - Questão de pesquisa escrita
  - Experimento design
  - Dados piloto (gráfico)
  - Cronograma semestral

- **Tempo:** 1-2 horas
- **Checkpoint:** Advisor diz "OK, siga em frente" ou "refine X"

---

### **SEMANA 6-8 (Dias 36-56): Literatura Fase 2 + Refinamento**

#### Dias 36-42: Leitura Aprofundada (SPINS, ECC, DTLS)
- **Material:**
  1. "SPINS: Security Protocols for Sensor Networks" (Perrig et al. 2002) — 30 min
  2. "ECC vs RSA for IoT" paper — 1h
  3. DTLS overhead analysis paper — 1h
  4. 2x "Secure RPL" papers (state of art recentes) — 2h total

- **Tempo total:** 4-5 horas ao longo da semana
- **Entrega:** Literatura notes file com citações + insights

#### Dias 43-49: Refinement Experimental Setup
- **Atividade:** Ajustar design baseado feedback advisor
- **Possíveis mudanças:**
  - Número de nós alterado? (ex: 100-1000 em vez de 50-500)
  - Tipo ataque diferente? (ex: foco em Sybil vs Black Hole)
  - Métrica nova? (ex: adicionar "Detection Rate" do ataque)

- **Tempo:** 2-3 horas
- **Entrega:** Experimental design v2 (final)

#### Dia 50-56: Integração HMAC no Cooja (Proof of Concept)
- **Atividade:** Codificar esquema HMAC leve
- **Passos:**
  1. Adicionar função HMAC-SHA256 (usar biblioteca libcrypto)
  2. Gerar DIO com MAC agregado
  3. Verificar MAC no receiver
  4. Registrar tempo adicional (latência)

- **Tempo:** 6-8 horas (codificação + debug)
- **Entrega:** Código C funcional (pode ter bugs, tudo bem)
- **Resultado:** Uma rodada simples (10 nós) com autenticação funciona

---

### **SEMANA 9-10 (Dias 57-70+): Proposta Formal**

#### Dia 57-60: Escrita Proposal Document
- **Estrutura (3-5 páginas):**
  1. **Introdução** (0.5 pg): O que é RPL, por que segurança importa
  2. **Questão de Pesquisa** (0.5 pg): Formulação precisa
  3. **Objetivos** (0.5 pg): Objetivo geral + específicos
  4. **Metodologia** (1.5 pg): Exp design, protocolos, cenários, métricas
  5. **Cronograma** (0.5 pg): Semestres e milestones
  6. **Referências** (1 pg): 15-20 key papers

- **Tempo:** 4-5 horas escrita
- **Ferramenta:** LaTeX ou Word
- **Entrega:** `dissertation_proposal_formal.pdf`

#### Dia 61-65: Refinement Baseado Feedback
- **Atividade:** Circule draft com advisor
- **Feedback esperado:** "Refine Objetivos Específicos", "Detalhe cronograma", etc.
- **Iteprações:** 1-2 ciclos de refinement

#### Dia 66-70: Apresentação Seminário Pesquisa
- **Atividade:** Preparar slide + apresentar 15 min no seminário (se houver)
- **Slide:**
  - Visual overview (não texto puro)
  - Gráficos dos dados piloto
  - Cronograma claro
  
- **Tempo:** 2-3 horas preparação

#### Checkpoint Final (Dia 60):
- [ ] Proposta formal escrita
- [ ] Advisor aquiescente ("looks good, start implementing")
- [ ] Cronograma realista validado
- [ ] Código proof-of-concept HMAC funciona
- [ ] Dados piloto coletados

---

## 📊 CHECKLIST COMPLETO (60 Dias)

### Semana 1: Nivelamento
- [ ] Lido resumo executivo relatório
- [ ] Assistido video RPL basics
- [ ] Cooja instalado + funcionando
- [ ] Primeiro experimento Cooja 10 nós rodan

### Semana 2: Literatura 1
- [ ] RFC 6550 resumo escrito
- [ ] Vulnerabilities paper lido
- [ ] Tabela ataques preenchida

### Semana 3: Proto + Proposta
- [ ] Código RPL entendido (trace DIO completo)
- [ ] Autenticação approach definida (HMAC/ECC/PSK)
- [ ] Questão de pesquisa formal

### Semana 4: Metodologia
- [ ] Experiment design completo (36 configs, tableau)
- [ ] Métricas definidas e explicadas
- [ ] Cronograma mestrado 4 semestres

### Semana 5: Baseline
- [ ] Piloto coletado (50 nós, sem ataque)
- [ ] Análise python + gráficos
- [ ] Advisor meeting + feedback OK

### Semana 6-8: Literatura 2 + Refinement
- [ ] SPINS + ECC + DTLS papers lidos
- [ ] Experimental design v2 ajustado
- [ ] HMAC proof-of-concept funciona (10 nós test)

### Semana 9-10: Proposal
- [ ] Proposta formal escrita (3-5 páginas)
- [ ] Advisor feedback loops completos
- [ ] Apresentação seminário pronta (se aplica)
- [ ] **FINAL STATUS:** Ready to Implement


---

## 🎓 RECURSOS NECESSÁRIOS

### Hardware
- PC/Laptop: i5+ / 8GB RAM / 256GB storage (você provavelmente já tem)

### Software (Todos gratuitos)
- Contiki OS — https://github.com/contiki-os/contiki
- Cooja — Incluído em Contiki
- Python 3 + Pandas + Matplotlib — https://www.anaconda.com/
- VS Code — https://code.visualstudio.com/
- Git — https://git-scm.com/

### Custos:
- **Total: R$ 0** ✅

---

## 🆘 TROUBLESHOOTING COMUM

### "Cooja não compila no Windows"
→ Usar WSL2 (Windows Subsystem for Linux 2) com Ubuntu
→ Referência: https://docs.microsoft.com/en-us/windows/wsl/

### "RFC 6550 é muito denso"
→ Normal! Assista video ("RPL Protocol Explained" YouTube) 1ªe então releia
→ Ou pule seções de matemática; foco em algorithm description

### "Não acho paper sobre vulnerabilidades"
→ Procure em: Google Scholar, ResearchGate, ArXiv
→ Email author directamente "Can you share your paper?"
→ 10/10 vezes responde em 24h

### "Meu advisor quer linha diferente"
→ OK! Adapte este plano:
  - Linha 1 (Drones): substitua "RPL" por "AODV + mobility prediction"
  - Linha 4 (Escalabilidade): mude literatura para "AODV scaling"
  - Resto do plano = mesmo framwork

---

## 📢 FINAL: PRÓXIMOS PASSOS IMEDIATOS

### **HOJE (Quando ler este documento):**
1. Forme uma pasta: `/research/mesh-security-dissertation/`
2. Copie os 4 relatórios para lá
3. Crie arquivo `progress_log.md` (vá atualizando)

### **AMANHÃ:**
1. Ler Resumo Executivo (1 hora)
2. Download GitHub Contiki (colocar compilando, pode demorar)
3. Marcar reunião com advisor para "discutir tópicos dissertação"

### **Próxima Semana:**
1. Completar checklist Semana 1
2. Enviar RFC 6550 summary para advisor (feedback)
3. Primeiro experimento Cooja pronto

---

## 📞 CONTATOS ÚTEIS

- **Contiki OS Support:** GitHub Issues em contiki-os/contiki
- **RPL Experts:** Procure pesquisadores que publicaram sobre RPL; email diretamente
- **Your advisor:** (preenchimento automático após encontro)

---

**Plano de Ação Executivo | Especialista em Redes MESH**  
**Linha 2 - Segurança em MESH IoT**  
**Válido por: 60 dias (até fim Junho 2026)**  
**Próxima revisão: 14 dias após início (ajustes conforme necessário)**

