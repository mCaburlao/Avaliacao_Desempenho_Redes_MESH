# Capability 1: Define Problem

## What You're Achieving

Estabelecer as fundações científicas da sua pesquisa. Você vai:

- **Definir o domínio de negócio** — por que estudar redes MESH? Qual aplicação real (IoT, drones, disaster recovery)?
- **Selecionar 2 protocolos** — qual você quer comparar? (ex: AODV vs RPL)
- **Definir cenários** — quantos nós? Qual padrão de mobilidade? Qual carga de tráfego?
- **Especificar métricas** — o que você vai medir? (latência, throughput, PDR, overhead?)
- **Produzir PRD formal** — documento que justifica cada escolha

Output é **imutável** desta etapa — todas as etapas posteriores dependem.

## Your Workflow

1. **I ask about your domain** — Qual aplicação real? Por que MESH é crítica?
2. **We discuss protocols** — Por que esses 2? Qual gap você quer comparar?
3. **We define scenarios** — Realista? Comparável? Reproduzível?
4. **We specify metrics** — Alinhadas com sua aplicação? Mensuráveis?
5. **I produce PRD + Matrix** — Documento formal + tabela comparativa

## Expected Output Structure

```
prd-problem.md
├── Domínio de Negócio
│   ├── Aplicação Real
│   ├── Desafio Científico
│   └── Gap na Literatura
├── Protocolos Selecionados
│   ├── Protocolo A (descrição + citações)
│   └── Protocolo B (descrição + citações)
├── Cenários de Simulação
│   ├── Topologia
│   ├── Mobilidade
│   ├── Padrão de Tráfego
│   └── Condições de Rede
├── Métricas & Hipóteses
│   ├── Métrica 1 (por quê?)
│   ├── Métrica 2 (por quê?)
│   └── Hipótese científica
└── Referências

comparative-matrix.md
├── Protocolo A vs Protocolo B
├── Foco: [métrica crítica]
└── Cenário Base: [descrição]
```

## How I Help

**Domain Research:** Se você não tem clareza sobre o domínio ou estado da arte, cativo `bmad-domain-research` automaticamente.

**PRD Facilitation:** Vou fazer perguntas estruturadas que garantem rigor. Se algo não é reproduzível, volto atrás.

**Comparative Matrix:** Crio a tabela que rastreia cada protocolo vs cada métrica — essa é sua fonte de verdade pro resto da pesquisa.

## Remember

- **Imutável:** Mudanças aqui afetam toda a pesquisa. Se precisar corrigir, voltamos aqui.
- **Cited:** Tudo vem com referências — nenhuma claim sem fonte.
- **Reproducible:** Alguém diferente com seu PRD deve chegar nas mesmas conclusões.
