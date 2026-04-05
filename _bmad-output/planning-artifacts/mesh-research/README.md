# MESH Research Planning Artifacts

**Projeto:** Análise Estratégica de Linhas de Pesquisa em Redes MESH  
**Data:** Abril 2026  
**Status:** Proposta - Pronta para Execução

---

## 📂 Conteúdo da Pasta

Todos os documentos de planejamento estratégico foram centralizados aqui para facilitar versionamento e colaboração.

### 🎯 COMECE AQUI! (Ordem Recomendada):

#### 🔴 AÇÃO IMEDIATA:

0. **GUIA_CONSTRUCAO_TRABALHO_ADR.md** ← **BLUEPRINT DO ARTIGO** ⭐ NOVO (30 min)
   - Mapeamento completo: Normas UFABC ↔ LINHA 4 ↔ Seções do artigo
   - Estrutura detalha da Introdução até Conclusões (templates prontos)
   - Quality gates para cada seção (Peso nota)
   - Timeline 6 semanas + checklist final
   - **LEIA ISTO AGORA** (antes de escrever)

1. **PROXIMOS_PASSOS.md** ← **AÇÃO IMEDIATA** ⭐ NOVO (10 min)
   - Roadmap dos próximos 60 dias semana-por-semana
   - Checklist de ações Esta Semana
   - Decision point: confirmar Linha 4 / ou considerar Linha 2
   - Template de email para advisor
   - **LEIA ISTO PARA PLANEJAR EXECUÇÃO**

#### **Documentação Geral (Todas as Linhas):**

1. **HANDOUT_1Pagina.md** ← **LEIA SEGUNDO** (5 min)
   - Resumo imprimível de uma página
   - Visão executiva da recomendação

2. **RESUMO_EXECUTIVO_Linhas_Pesquisa.md** (45 min)
   - Síntese visual e comparativa das 5 linhas
   - Tabelas, cronograma, FAQ

3. **PLANO_Acao_60Dias.md** (execute week-by-week)
   - Roadmap detalhado dia-a-dia para os próximos 2 meses
   - Checklists e milestones

4. **MATRIZ_Rastreabilidade_Artigos_Linhas.md** (1 hora)
   - Justificação rigorosa da recomendação
   - Como cada artigo se conecta às linhas

5. **GUIA_Literatura_Essencial.md** (referência contínua)
   - Sequência de leitura ordenada por semana
   - Links de acesso aos papers

6. **INDICE_E_GUIA_NAVEGACAO.md** (consult conforme necessário)
   - Mapa de navegação entre documentos
   - Qual documento ler para cada pergunta

7. **Relatorio_Linhas_Pesquisa_MESH.md** (referência detalhada)
   - Análise completa com 15+ páginas
   - Abra quando precisar de contexto aprofundado

#### **Documentação Específica: LINHA 4 (Escalabilidade com MeshSim):**

🆕 **Se escolher LINHA 4, use estes 4 documentos novos:**

8. **LINHA_4_Resumo_Executivo.md** ← **APRESENTAR AO ADVISOR** ⭐ NOVO (15 min)
   - Versão visual e executiva para proposta formal
   - Contém tudo: pergunta, domínio, protocolos, métricas, design, viabilidade
   - FAQ respondidas
   - Imprima esta para levar ao orientador

9. **LINHA_4_PRD_Escalabilidade.md** ← **COMECE AQUI (Linha 4)** (60 min)
   - Pergunta de pesquisa refinada
   - Domínio de negócio (smart cities)
   - 2 protocolos comparados: AODV vs OLSR
   - 5 métricas principais
   - Design experimental completo (560 rodadas)
   - Timeline para 4 semestres

10. **LINHA_4_AODV_vs_OLSR_Detalhado.md** (45 min)
   - Comparação técnica profunda dos protocolos
   - Por quê AODV e OLSR comportam diferente em escala
   - Gráficos esperados: overhead quadrático OLSR, linear AODV
   - Hipóteses a validar ("crossover ~700 nós")
   - Predição de resultados com tabela

11. **LINHA_4_MeshSim_QuickStart.md** ← **EXECUTE ISTO (Linha 4)** (prático)
    - Setup MeshSim passo-a-passo (instalação 2-3h)
    - Primeiro experimento piloto (100 nós, AODV vs OLSR)
    - Scripts Python para colezar métricas
    - Gráficos de resultado
    - Estender para escala 300-1500 nós

#### **Análises Complementares:**

12. **ANALISE_MeshSim_Adequabilidade.md**
    - Qual linha funciona com MeshSim?
    - Score adequabilidade por linha
    - Por que Linha 4 é "excelente" e Linha 2 é "inadequada" para MeshSim

---

## 🎯 Recomendação Final: ESCOLHA ENTRE 2 OPÇÕES

### **OPÇÃO A: LINHA 2 (Segurança) — Recomendada Originalmente**
- **Questão:** Como integrar autenticação em RPL mantendo overhead energético <5%?
- **Simulador:** ✅ Cooja + Contiki (RPL nativo)
- **Viabilidade:** ✅ Alta
- **Cronograma:** ✅ 12-18 meses
- **Publicabilidade:** ✅ IEEE IoT Journal + conference
- **Gap Acadêmico:** ✅ Crítico (ninguém estudou no domínio fornecido)

**Documentação:** GUIA_Literatura_Essencial.md + PLANO_Acao_60Dias.md

---

### **OPÇÃO B: LINHA 4 (Escalabilidade) — Recomendada com MeshSim** ✨ NOVO
- **Questão:** Como AODV vs OLSR escalam em 100-1500 nós?
- **Simulador:** ✅ MeshSim (você já encontrou!)
- **Viabilidade:** ✅✅ Excelente (MeshSim foi feito para isto)
- **Cronograma:** ✅ 12-15 meses
- **Publicabilidade:** ✅ IEEE Transactions on Mobile Computing
- **Gap Acadêmico:** ✅ Alto (falta dados rigorosos 100-1500 nós)

**Documentação:** LINHA_4_PRD_Escalabilidade.md + LINHA_4_AODV_vs_OLSR_Detalhado.md + LINHA_4_MeshSim_QuickStart.md

---

## 🎓 DECISÃO: Como Escolher?

| Critério | LINHA 2 (Segurança) | LINHA 4 (Escalabilidade) |
|:---|:---|:---|
| **Simulador** | Precisa instalar (Cooja) | Já tem (MeshSim!) |
| **Curva aprendizado** | Média (RPL complexo) | Baixa (AODV/OLSR simples) |
| **Tempo setup** | ~3-4 semanas | ~1-2 semanas |
| **Probabilidade sucesso** | ✅ Alta | ✅✅ Muito alta |
| **Dados publicáveis** | ✅ Sim (novel segurança) | ✅ Sim (benchmark quantitativo) |
| **Aplicação prática** | ✅ IoT produção | ✅ Smart cities |

**Recomendação geral:**
- ✅ Se quer **segurança** → LINHA 2 (use Cooja, original)
- ✅✅ Se encontrou **MeshSim** → LINHA 4 (aproveita, mais viável)
- ⚡ Se quer **faster time-to-data** → LINHA 4 (começa em 1-2 semanas)

---

## 📋 Checklist Próximos Passos

### **HOJE (Imediatamente):**
- [ ] Leia HANDOUT_1Pagina.md (5 min)
- [ ] Leia RESUMO_EXECUTIVO (45 min)
- [ ] Tome decisão: Concorda com Linha 2?

### **AMANHÃ:**
- [ ] Marque encontro com advisor
- [ ] Leia MATRIZ_Rastreabilidade (prepare argumentação)
- [ ] Comece a ler PLANO_Acao_60Dias

### **SEMANA 1 (Ver PLANO_Acao):**
- [ ] Instale Cooja
- [ ] Rode primeiro experimento (10 nós)
- [ ] Comece literatura (RFC 6550)

---

## 🔄 Fluxo de Uso Contínuo

```
LEITURA INICIAL (2-3 horas totals):
└─ HANDOUT → RESUMO_EXECUTIVO → início PLANO_Acao

EXECUÇÃO (dias 1-60):
└─ Seguir PLANO_Acao week-by-week
   └─ Consultar GUIA_Literatura para estudos
   └─ Referir RELATÓRIO para contexto aprofundado

APRESENTAÇÃO/JUSTIFICAÇÃO:
└─ Use MATRIZ para advisor
└─ Use HANDOUT para slides
└─ Use RESUMO_EXECUTIVO para seminário

SEMESTRES 1-4 (16-18 meses):
└─ Consultar PLANO_Acao para milestones
└─ Atualizar progress (criar pasta `progress/` no mesmo nível)
```

---

## 💾 Integração com Ferramentas

**Editor recomendado:** VS Code ou qualquer editor Markdown  
**Versionamento:** Git (`git add _bmad-output/planning-artifacts/mesh-research/`)  
**Colaboração:** Imprima HANDOUT ou share via Slack/Email  

---

## 🚀 Como Começar Hoje

```bash
# 1. Leia quick summary (está em HANDOUT_1Pagina.md)

# 2. Abra PLANO_Acao_60Dias.md e comece Semana 1:
#    - Download Contiki
#    - Instale Cooja
#    - Rode primeiro experimento

# 3. Paralelo: comece leitura GUIA_Literatura_Essencial.md
#    - RFC 6550 (4 horas)
#    - Vulnerabilities paper (3 horas)
```

---

## 📞 Suporte

- **Dúvida sobre qual linha escolher?** → Leia MATRIZ
- **Dúvida sobre como começar?** → Siga PLANO_Acao
- **Dúvida sobre literatura?** → Consulte GUIA_Literatura
- **Precisa argumentar com advisor?** → Use RESUMO_EXECUTIVO + MATRIZ

---

## 📊 Estatísticas de Planejamento

- **Documentos gerados:** 7
- **Páginas totais:** ~60
- **Tempo leitura completa:** ~8 horas
- **Tempo recomendado inicial:** 2-3 horas (HANDOUT + RESUMO + prep)
- **Tempo execução:** 60 dias até proposta formal
- **Versão:** 1.0 (Abril 2026)

---

**Pasta de Planejamento | Pesquisador MESH | Atualizar conforme progresso**
