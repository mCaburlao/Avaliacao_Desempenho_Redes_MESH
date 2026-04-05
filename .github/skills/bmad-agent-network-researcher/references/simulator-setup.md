# Capability 2: Setup Simulator

## What You're Achieving

Converter sua especificação de problema (PRD) em um simulador executável. Você vai:

- **Explorar opções de simulador** — Qual é o melhor fit? (ns-3, OMNET++, SimPy, custom Python?)
- **Desenhar arquitetura experimental** — Como seu simulador vai ler config e gerar logs?
- **Preparar código executável** — Framework pronto para rodar
- **Criar configuration template** — YAML que parametriza scenarios sem tocar o código

Output é **reproducível** — qualquer pessoa com seu code + config gera mesmos resultados.

## Your Workflow

1. **We decide on simulator** — Você tem preferência? Vou recomendar vantagens/trade-offs.
2. **We design experiment flow** — Como os dados fluem entrada → processamento → saída?
3. **I generate skeleton code** — Estrutura base pronta para você preencher lógica de protocolo
4. **We define config format** — Template YAML que parametriza tudo (n_nodes, mobility_model, etc)

## Expected Output Structure

```
simulator-architecture.md
├── Simulador Escolhido (+ justificativa)
├── Fluxo Experimental
│   ├── Input: Config YAML
│   ├── Processamento: [etapas chave]
│   └── Output: CSV/logs com formato
├── Implementação
│   ├── Estrutura de pastas
│   ├── Entry point (main.py ou equivalente)
│   └── Dependências (requirements.txt)
└── Config Template

simulator-code/
├── main.py                    # Entry point
├── config.yaml               # Example configuration
├── protocol_a.py             # Protocolo A skeleton
├── protocol_b.py             # Protocolo B skeleton
├── event_engine.py           # Event dispatcher
├── network_topology.py       # Topology builder
├── results_writer.py         # Log formatter
└── requirements.txt
```

## How I Help

**Skill Activation:** Uso `bmad-create-architecture` pra documentar design, `bmad-quick-dev` pra gerar código skeleton.

**Simulator Selection:**
- **ns-3** ✓ Se você quer fidelidade total (real wireless effects)
- **OMNET++** ✓ Se você já conhece, ou quer simpler syntax
- **SimPy** ✓ Se você quer controle total, Python-friendly
- **Custom Python** ✓ Se você quer máxima customização

**Config-Driven Design:** Seu simulator lê `config.yaml`, não hardcodes. Isso permite:
- Múltiplos scenarios sem mudar código
- Batch experiments (variar um param por vez)
- Auditoria: `git log config.yaml` mostra que cenários você rodou

**Reproducibility Checklist:**
- [ ] Random seed fixado por scenario
- [ ] All parameters in config file
- [ ] Entry point documented
- [ ] Dependencies pinned (version locked)

## Remember

- **Your Decision:** Qual simulador funciona pra você?
- **My Recommendation:** Vou sugerir based on trade-offs (speed vs accuracy vs learning curve)
- **Code is Skeleton:** Você vai preencher lógica dos protocolos; eu forneço structure
- **Mutation Risk:** Código gerado aqui é base para todo experimento; versione bem
