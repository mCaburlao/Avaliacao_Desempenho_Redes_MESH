# Próximos Passos — Roadmap Imediato

**Data:** Abril 2026  
**Status:** Planejamento concluído → Execução

---

## 🚀 DECISION POINT: Qual Linha Escolher?

### CENÁRIO: Você tem MeshSim instalado localmente

✅ **RECOMENDAÇÃO = LINHA 4 (Escalabilidade com MeshSim)**

**Por quê?**
- MeshSim já está lá (não precisa instalar Cooja)
- Setup 2 semanas vs 4 semanas
- 95% chance de sucesso vs 85% (Cooja é mais instável)
- Publicável em IEEE Transactions (top-tier)
- Prático + acadêmico (benchmark = bem citado)

---

## 📅 ESTA SEMANA (Semana 1/60)

### ✅ Tarefa 1: Ler Documentação (2 horas)
1. **LINHA_4_Resumo_Executivo.md** → 15 min
2. **LINHA_4_PRD_Escalabilidade.md** → 45 min
3. **LINHA_4_AODV_vs_OLSR_Detalhado.md** → 30 min

**Depois:** Versão visual pronta para levar ao advisor

## 📅 PRÓXIMA SEMANA (Semana 2/60)

### ✅ Tarefa 3: Instalar MeshSim (2-3 horas)

Siga **LINHA_4_MeshSim_QuickStart.md — PARTE 1: Installation**

```bash
# Resumo rapido:
1. Clone: git clone https://github.com/[...]/MeshSim-master.git
2. Dependências: sudo apt-get install build-essential ...
3. Compile: cd MeshSim-master && ./waf configure --build-profile=release
4. Build: ./waf build
5. Test: ./test.py  # Validar instalação
```

**Entrega esperada:** MeshSim compilado e pronto

---

### ✅ Tarefa 4: Rodar Piloto Experimento (2 horas)

Continue **LINHA_4_MeshSim_QuickStart.md — PARTE 2: Pilot Experiment**

```bash
# Esquema:
1. Criar config 100 nós AODV
2. Rodar simulação (~10 minutos)
3. Coletar PCAP
4. Extrair 3 métricas (PDR, latência, overhead)

Esperado: Gráfico simples PDR% vs tempo
```

**Entrega esperada:** 
- Pasta `results_aodv_100nodes/` com PCAP
- CSV com 3 métricas
- Gráfico PNG

---

## 📅 SEMANA 3-4 (Semanas 3-4/60)

### ✅ Tarefa 5: Expandir para OLSR (1 hora)

```bash
# Mudar protocolo em config, replicar Tarefa 4
1. Editar: routing.txt (protocolo = OLSR)
2. Rodar: MeshSim OLSR 100 nós
3. Coletar: PCAP + CSV
```

**Entrega:**
- Comparação AODV vs OLSR (100 nós)
- Tabela de 3 métricas lado-a-lado
- Gráfico comparativo

---

### ✅ Tarefa 6: Escalar para 300 nós (1-2 dias)

Siga **LINHA_4_MeshSim_QuickStart.md — PARTE 3: Batch Scaling**

```bash
# Script Bash: loop para múltiplas configs
for nodes in 100 300 500; do
    for protocol in AODV OLSR; do
        mpirun -np 8 MeshSim --nodes=$nodes --protocol=$protocol ...
    done
done
```

**Entrega:**
- Dados para 6 combinações (3 nós × 2 protocolos)
- **Gráficos iniciais:** PDR vs # de nós

---

## 📅 SEMANA 5-6 (Semanas 5-6/60)

### ✅ Tarefa 7: Escrever Proposta Formal (3-4 horas)

**Documento:** Proposta_Formal_LINHA_4.md (3-5 páginas A4)

**Estrutura:**
1. Problema & Motivação (1 pg)
2. Pergunta de Pesquisa (0.5 pg)
3. Metodologia (1 pg)
4. Cronograma (1 pg)
5. Referências (1 pg)

**Templates:** Copiar seções de LINHA_4_PRD_Escalabilidade.md

**Deadline:** Enviar ao advisor para aprovação formal

---

## 📊 TABELA RESUMIDA: 60 DIAS

| Semana | Tarefa | Tempo | Entrega |
|:---|:---|:---|:---|
| 1 | Ler docs + marcar advisor | 2h | Resumo executivo |
| 2 | Instalar MeshSim + piloto AODV | 4h | Resultados 100 nós AODV |
| 3 | Piloto OLSR + comparação | 2h | Gráficos AODV vs OLSR (100) |
| 4 | Batch 300-500 nós | 8h | Dados preliminares 3 escalas |
| 5 | Análise inicial + proposta formal | 6h | **Proposta formal aprovada** |
| 6-8 | Refinamento setup, literatura, análise | 20h | Plano detalhado semestres 1-4 |
| 9-10 | Buffer | - | Ajustes finais |

**Meta:** Final semana 6 = Proposta formal aprovada + primeiros dados visualizados

---

## ⚠️ RISCOS & CONTINGÊNCIAS

### Risco A: MeshSim não compila
**Solução:** LINHA_4_MeshSim_QuickStart.md tem troubleshooting section
- Se falhar: try NS-3 vanilla install (mais estável)
- Timeline: +1 semana

### Risco B: Advisor quer LINHA 2 (Segurança)
**Solução:** Mantenha LINHA_2_docs prontos; pivote para Cooja
- Se isso: timeline +4 semanas (Cooja setup mais complexo)
- Documentação pronta em `Relatorio_Linhas_Pesquisa_MESH.md`

### Risco C: Dados piloto não fazem sentido
**Solução:** Ajuste parâmetros (duration, tráfego, topologia)
- FAQ em LINHA_4_MeshSim_QuickStart.md resp

### Risco D: Cluster não tem acesso
**Solução:** Rodar em máquina local (mais lento)
- 140 rodadas em 1 máquina: ~3 dias (aceitável)
- Ou: AWS/GoogleCloud ($ mas rápido)

---

## 📋 CHECKLIST: SEMANA 1

- [ ] Ler LINHA_4_Resumo_Executivo.md
- [ ] Ler LINHA_4_PRD_Escalabilidade.md
- [ ] Ler LINHA_4_AODV_vs_OLSR_Detalhado.md
- [ ] Enviar email ao advisor (marcar reunião)
- [ ] Receber aprovação: "Voto prosseguir com Linha 4"

### After Week 1 Success:
- [ ] Imprimir & levar LINHA_4_Resumo_Executivo.md à reunião
- [ ] Discutir: cronograma, recursos, expectativas
- [ ] Receber feedback refinado

---

## 🎯 PRÓXIMAS QUESTÕES: Responda Agora

### P1: Você tem acesso a cluster/cloud?
- ✅ SIM → 140 rodadas em 12h viáveis (AWS, XSEDE, etc)
- ❌ NÃO → 140 rodadas em 3 dias (máquina local, paciência)

### P2: Qual seu nível experiência com Linux/Bash?
- ✅ Fluente → MeshSim rápido (1-2 dias setup)
- ⚠️ Intermediário → +3-5 dias (debugging)
- ❌ Iniciante → +1-2 semanas (tutorial necessário)

### P3: Precisa cumprir outras disciplinas?
- ✅ SIM → Planejar 10h/semana ao invés de 15h
- ❌ NÃO → Full time = possível em 12-15 meses

---

## 💬 PRÓXIMA AÇÃO

**Responda em 1 frase:**

> "Vou seguir Linha 4. Estou pronto para começar Semana 1."

**Ou se dúvida:**

> "Quero conversar sobre Linha 2 vs Linha 4 antes de decidir."

---

**Documentos de Referência Rápida:**
- ↳ LINHA_4_PRD_Escalabilidade.md — design completo
- ↳ LINHA_4_AODV_vs_OLSR_Detalhado.md — protocolo teoria
- ↳ LINHA_4_MeshSim_QuickStart.md — installation + first run
- ↳ PLANO_Acao_60Dias.md — detailed weekly plan (all lines)

---

## 📞 Support

Se travar em qualquer ponto:
1. Consulte FAQ section de cada documento
2. Leia troubleshooting em MeshSim QuickStart
3. Volte para consultar o agente MESH researcher

---

**Roadmap LINHA 4 — Ready for Execution**  
**Data: Abril 2026 | Status: Go/No-Go Decision Pending**
