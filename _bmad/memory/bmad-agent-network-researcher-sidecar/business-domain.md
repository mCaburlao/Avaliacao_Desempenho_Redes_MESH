# Domínio de Negócio — LINHA 4 Escalabilidade MESH

**Status:** ✅ FINAL  
**Created:** Abril 2026  
**Last Updated:** Abril 2026 (com guia construção)

---

## Aplicação Real

**Contexto/Domínio:** Smart Cities 2026 — Redes de Sensores em Larga Escala
- **Real use case:** Iluminação Inteligente em cidade de 50km²
  - Regional Central: 200 nós
  - Regional Suburbana: 800 nós
  - Regional Periférica: 3000 nós
- **Other scenarios:** Air quality (800 nós), asset tracking (500 nós)
- **Economic impact:** Protocolo errado = custos extras ou falhas de comunicação

**Pergunta Central:**
> "Como protocolos reativo (AODV) vs proativo (OLSR) escalam de 100 para 1500 nós?"

**Sub-Perguntas:**
1. Ponto de transição: em qual # nós AODV fica melhor? (~750 nós?)
2. Modelo de overhead: linear (AODV) vs quadrático (OLSR)?
3. Recomendação prática para smart cities (1000+ nós)?

---

## Interesse

| Quem | Interesse | Benefício |
|:---|:---|:---|
| **IoT Engineers** | Qual protocolo usar? | Tabela recomendações por escala |
| **Smart City Admins** | Eficiência computacional | Overhead vs performance analysis |
| **MESH Researchers** | Baseline científica | Benchmark moderno 100-1500 nós |
| **You (Dissertand)** | Publicação + grau | IEEE paper + dissertação |

---

## Restrições Críticas (O que Importa)

1. **Escalabilidade:** Como overhead cresce com # nós?
2. **Confiabilidade:** PDR mantém >90% em todas escalas?
3. **Convergência:** Quanto tempo para rede pronta após boot?
4. **Viabilidade Computacional:** Protocolo executável em edge/IoT?

---

## Lacuna Literária (Por que Pesquisar?)

| Trabalho Anterior | Faixa | NS-3 Version | IC 95% | Sua Contribuição |
|:---|:---|:---|:---|:---|
| RFC 3561/3626 | Theory | N/A | N/A | Validação empírica |
| Lee et al. 2015 | 50-500 | Old | No | Estender até 1500 |
| Passo et al. 2018 | Var | v3.24 (2015) | No | NS-3 v3.30 (2024) |
| **This work** | **100-1500** | **v3.30** | **Yes** | **Modern + Rigorous** |

---

## Critérios de Sucesso

✅ **Científico:**
- Intervalo confiança 95% em todas métricas
- Hipóteses testadas (crossover point, overhead models)
- Reproduzível (RNG seeds, toolchain exact)
- Publicável (IEEE Transactions or equiv)

✅ **Prático:**
- Recomendação quantificada: "Use OLSR até 500 nós, AODV após 750"
- Guidelines implementáveis para engenheiros reais

✅ **Acadêmico (Norma UFABC):**
- Artigo 6-10 páginas SBC format
- Níveis: ANÁLISE, AVALIAÇÃO, CRIAÇÃO
- Apresentação ao vivo 10min + código público
- Nota ≥ 8/10

## Protocolos Selecionados

### Protocolo A: [Name]

**Categoria:** [Reactive | Proactive | Hybrid]

**Referência Completa:**
- RFC/Paper: [Citation]
- Link: [URL]

**Descrição Breve:**
[2-3 linhas sobre o protocol; como funciona?]

**Por que você escolheu?**
[Motivação de pesquisa]

**Vantagens Esperadas:**
- [...]
- [...]

**Desvantagens Esperadas:**
- [...]
- [...]

---

### Protocolo B: [Name]

**Categoria:** [Reactive | Proactive | Hybrid]

**Referência Completa:**
- RFC/Paper: [Citation]
- Link: [URL]

**Descrição Breve:**
[2-3 linhas]

**Por que você escolheu?**
[Motivação de pesquisa]

**Vantagens Esperadas:**
- [...]
- [...]

**Desvantagens Esperadas:**
- [...]
- [...]

---

## Hipótese Científica

[Sua predição. O que você acha que vai encontrar?]

**Exemplo:**
"Em cenários de alta mobilidade, AODV mantém latência mais baixa por causa de sua abordagem reativa.
Em cenários estáticos, RPL converge mais rápido e usa menos overhead de roteamento."

---

## Cenários de Teste

### Cenário 1: [Nome Descritivo]

**Tipo:** [Static | Mobile | Disaster | Other]

**Topologia:**
- Número de nós: [N]
- Distribuição: [Grid | Random | Custom]
- Área (km²): [X × Y]
- Raio de transmissão: [range]

**Mobilidade:**
- Modelo: [Static | Random Waypoint | Gauss-Markov | Disaster Churn]
- Velocidade: [min-max] m/s
- Pausa entre movimentos: [seconds]

**Padrão de Tráfego:**
- Tipo: [CBR | Poisson | Bursty | Trace]
- Taxa: [packets/sec ou data rate]
- Tamanho de pacote: [bytes]
- Fonte → Destino: [num flows]

**Duração:** [seconds]

**Justificativa:** [Por que esse cenário é representativo?]

---

### Cenário 2: [Nome Descritivo]

[Repita estrutura]

---

### Cenário 3: [Nome Descritivo]

[Repita estrutura]

---

## Métricas de Interesse

Para cada métrica, defina POR QUÊ você quer medir:

| Métrica | Unidade | Definição | Por Quê? | Meta |
|---------|---------|-----------|---------|------|
| Latência P50 | ms | Mediana do delay packet | Responsividade | <100ms |
| Latência P95 | ms | 95º percentil | Outliers | <500ms |
| PDR | % | Packet Delivery Ratio | Confiabilidade | >95% |
| Overhead | % | Tráfego de controle / tráfego total | Eficiência | <20% |
| Convergence | sec | Tempo para encontrar primeira rota | Inicialização | <10s |
| Route Stability | changes/min | Quantas vezes a rota muda? | Previsibilidade | <5 changes/min |

---

## Reprodutibilidade

Seu compromisso com rigor científico:

✅ **Random Seeds Fixas:** Múltiplas corridas com seeds diferentes, resultados agregados
✅ **Configuração em Versionamento:** Arquivo config.yaml em git
✅ **Código do Simulador:** Publicado em repositório
✅ **Dados Brutos:** Disponíveis para auditors
✅ **Scripts de Análise:** Reproduzíveis e versionados

---

## Referências

[Lista completa de RFCs, papers, tools que você vai usar]

1. [RFC 3561] Perkins, C., et al. "Ad hoc On-Demand Distance Vector..."
2. [RFC 6550] Winter, T., et al. "RPL: IPv6 Routing Protocol..."
3. [Your tool]: ns-3 Documentation, http://...
4. [Related work]: [Citation]

---

## Status de Preenchimento

- ✅ Contexto definido?
- ✅ Protocolos A & B defin​idos?  
- ✅ Hipótese escrita?
- ✅ Cenários 1, 2, 3 descritos?
- ✅ Métricas justificadas?
- ✅ Proposição de reprodutibilidade?

**Pronto para Capability 2 (Simulator Setup)?** [SIM | NÃO — revise acima]
