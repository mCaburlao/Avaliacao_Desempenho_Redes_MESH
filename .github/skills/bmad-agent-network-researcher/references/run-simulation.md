# Capability 3: Run Simulation

## What You're Achieving

Executar seus experimentos e coletar dados brutos. Você vai:

- **Definir batches de scenarios** — Qual variação de parâmetros você quer explorar?
- **Gerar command-line scripts** — Eu forneço exatamente como rodar cada scenario
- **Collect raw outputs** — Logs, CSVs, qualquer formato que seu simulador gera
- **Log everything** — Seeds, config, timestamps, para auditoria total

Output é **raw data** — dados puros, prontos para análise estatística. Sem processamento ainda.

## Your Workflow

1. **Define experiment batches** — Você quer rodar qual sequência de configs?
   - Ex: "Varia n_nodes de 10, 20, 30 em cada protocolo"
   - Ex: "Testa 3 padrões de mobilidade"
2. **I generate execution scripts** — Você copia/cola no terminal
3. **You run experiments** — Você gerencia a execução (pode ser sua máquina, cluster, whatever)
4. **Collect outputs** — Você salva os arquivos brutos

## Expected Output Structure

```
experiments/
├── run_batch_01.sh          # Script: rodar todos scenarios de mobility=random
├── run_batch_02.sh          # Script: rodar todos scenarios de mobility=random_waypoint
│
├── scenario_001/
│   ├── config.yaml          # Config exato usado
│   ├── protocol_a_results.csv
│   ├── protocol_b_results.csv
│   ├── simulation.log       # Trace completo
│   └── metadata.json        # { seed, timestamp, duration, status }
│
├── scenario_002/
│   ├── config.yaml
│   ├── protocol_a_results.csv
│   ├── protocol_b_results.csv
│   ├── simulation.log
│   └── metadata.json
│
└── MANIFEST.md              # Índice: qual config em qual scenario
```

## How I Help

**Batch Generation:** Vou gerar scripts shell que executam suas scenarios. Cada script:
- Garante reproduzibilidade (seed fixo)
- Injeta metadata (timestamp, config hash)
- Captura logs completos
- Valida outputs (arquivo não vazio? Formato correto?)

**Example Script Generated:**
```bash
#!/bin/bash
# Batch: Vary n_nodes, Protocol A vs B, mobility=random

for n_nodes in 10 20 30; do
  echo "Running scenario: n_nodes=$n_nodes, protocol=A, mobility=random"
  python main.py \
    --config config.yaml \
    --n_nodes $n_nodes \
    --protocol A \
    --mobility_model random \
    --seed 42 \
    --output scenario_001_proto_A_nodes_${n_nodes}/
  echo "✓ Scenario complete"
done
```

**Data Validation:** Cada scenario:
- Tem seed rastreável
- Tem arquivo config salvo (git-version control depois)
- Tem metadata.json com runtime info
- Pode ser re-rodado identicamente

## Important Notes

- **Terminal Execution:** Você roda no seu terminal, não em background aqui. Vou fornecer exatamente o command.
- **Your Hardware:** Você decide quantity (10 scenarios? 100?). Vou gerar scripts pro tamanho que você escolher.
- **Time Estimate:** Você pode paralelizar batches se quiser; eu gero scripts compatíveis.
- **Deterministic:** Same seed → same output, sempre. Se divergir, algo está errado.

## Reproducibility Checklist

- [ ] Cada scenario tem seed rastreável
- [ ] Config YAML salvo como parte do resultado
- [ ] Logs completos (std.out e std.err capturados)
- [ ] Metadata JSON com timestamp e duração
- [ ] Scripts são determinísticos (sem randomização em ordem de execução)
