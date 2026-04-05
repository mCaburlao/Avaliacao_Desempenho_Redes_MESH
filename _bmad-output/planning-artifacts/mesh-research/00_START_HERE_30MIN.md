# ⚡ QUICK START — Comece AGORA em 30 Minutos

**Data:** 05 de Abril de 2026  
**Objetivo:** Seu artigo compilável + pronto para escrever  
**Tempo:** 30 minutos

---

## 🚀 PASSO 1: Abra o Artigo (5 min)

```bash
# No terminal:
cd d:\OneDrive\Documentos\UFABC\2026.1\Avaliacao_Desempenho_Redes_MESH
code documento_latex/Template_SBC/template-latex/artigo.tex
```

**Ou:** Simplesmente abra em VS Code → navegue para arquivo

---

## ✏️ PASSO 2: Personalize (5 min)

Procure por estas 3 linhas e substitua:

**Linha 12:**
```tex
\author{Aluno UFABC\inst{1}, Prof. Orientador\inst{1}}
```
➜ Mude para:
```tex
\author{Seu Nome Completo\inst{1}, Prof. Nome Orientador\inst{1}}
```

**Linha 15:**
```tex
  \email{aluno@ufabc.edu.br, orientador@ufabc.edu.br}
```
➜ Mude para:
```tex
  \email{seuemail@ufabc.edu.br, prof.email@ufabc.edu.br}
```

**Salve:** `Ctrl+S`

---

## 📄 PASSO 3: Compile (10 min)

```bash
# Terminal:
cd documento_latex/Template_SBC/template-latex/

# Compile (vai gerar artigo.pdf):
pdflatex artigo.tex
bibtex artigo
pdflatex artigo.tex
pdflatex artigo.tex
```

**Esperado:** Sem erros `!` (warnings são OK)

---

## 👁️ PASSO 4: Visualize (5 min)

```bash
# Abra o PDF gerado:
open artigo.pdf         # macOS
xdg-open artigo.pdf     # Linux
start artigo.pdf        # Windows (Git Bash)
```

**Checklist Visual:**
- [ ] Seu nome aparece como autor ✅
- [ ] Título está centralizado ✅
- [ ] Resumo em português + Abstract em inglês ✅
- [ ] Seções (Intro, Related Work, Methodology, etc) aparecem ✅
- [ ] Referências aparecem no final ✅

**Se tudo OK:** ✅ **PARABÉNS! Seu artigo está compilável.**

---

## 🎯 PASSO 5: Próximos Passos (Semana 1)

| Quando | O Quê | Tempo | Arquivo |
|:---|:---|:---|:---|
| **Amanhã** | Ler Introdução em voz alta | 15 min | `artigo.tex` seção Introdução |
| **Semana 1** | Refinar Metodologia | 2-3h | Use `QUICK_REFERENCE_TEMPLATES.md` |
| **Semana 2** | Inserir Figuras (após simular) | 1-2h | Execute `python3 generate_paper_figures.py` |
| **Semana 3+** | Completar Resultados + Discussão | 4-6h | Templates em `QUICK_REFERENCE_TEMPLATES.md` |

---

## 📚 Documentos de Suporte (Neste Mesmo Folder)

Quando precisar, abra:

| Situação | Abra | Find |
|:---|:---|:---|
| "Por onde começo?" | `QUICK_REFERENCE_TEMPLATES.md` | [TEMPLATE 1] Parágrafo Intro |
| "Quanto tempo vai tomar?" | `ROADMAP_VISUAL_SIMULACAO_ARTIGO.md` | Timeline Semana-a-Semana |
| "Como inserir figura?" | `QUICK_REFERENCE_TEMPLATES.md` | [TEMPLATE 5] Inserir Figura |
| "Qual é meu status?" | `ESTADO_SIMULACAO_E_PREPARACAO_ESCRITA.md` | O Que Você Tem Agora |
| "Preciso rodar análise" | `generate_paper_figures.py` | Python script pronto |

**Localização:** `_bmad-output/planning-artifacts/mesh-research/`

---

## ⚙️ Tl;dr: O Que Você Tem

```
✅ Artigo estruturado (8 seções)
✅ Resumo + Abstract
✅ Introdução completa
✅ Trabalhos Relacionados (6 papers integrados)
✅ Metodologia detalhada
✅ Tabela piloto 100 nós
✅ 4 guias de escrita
✅ Script para gerar figuras
✅ Dados brutos coletados (flowdata.xml)

Faltando:
❌ Sua personalização (autor/email) — 5 min
❌ Figuras finais — quando terminar simulação (semana 2)
❌ Sua escrita criativa — começa amanhã!
```

---

## ✅ Checklist Hoje (30 min)

- [ ] Abra artigo.tex
- [ ] Personalize linhas 12 e 15 (seu nome + email)
- [ ] Compile: `pdflatex + bibtex + pdflatex`
- [ ] Abra PDF e verifique formato
- [ ] Leia Introdução em voz alta (5 minutos)
- [ ] PRONTO! Arquivo compilável = ✅

---

## 🎓 Estrutura do Seu Artigo

```latex
1. Título + Autores              ← Já preenchido
2. Abstract (English)            ← Já preenchido
3. Resumo (Português)            ← Já preenchido
├─ Introdução                    ← Já preenchido (pode refinar)
├─ Trabalhos Relacionados        ← Já preenchido (6 papers)
├─ Metodologia                   ← Já preenchido (completo)
├─ Resultados Preliminares       ← Já preenchido (piloto)
├─ Discussão                     ← Já preenchido (draft)
├─ Conclusão                     ← Já preenchido (draft)
└─ Referências (BibTeX)          ← Automático
```

**Todas seções têm conteúdo base. Você só refinais + estende com seus dados.**

---

## 💡 Primeira Sessão de Escrita (Após Hoje)

```
[ ] Abra QUICK_REFERENCE_TEMPLATES.md
[ ] Leia [TEMPLATE 1] Parágrafo de Introdução
[ ] Copie template
[ ] Substitua [PLACEHOLDERS] por SEU conteúdo
[ ] Cole no artigo-LINHA4.tex
[ ] Compile → check visual
```

**Tempo:** 10-15 minutos por parágrafo

---

## 🚨 Se Algo Errar

| Erro | Solução |
|:---|:---|
| `pdflatex: command not found` | Instale LaTeX (`apt install texlive-full` ou MiKTeX) |
| `! Undefined control sequence` | Sintaxe LaTeX errada. Google o erro. |
| PDF não aparece formatado | Rode 3× (`pdflatex` 2×, então `bibtex`, então `pdflatex` 1×) |
| Referências não aparecem | Certifique que `Mesh.bib` está no mesmo folder |

---

## 📞 Próximo Passo Após Hoje

**Amanhã (06/04):** Leia [Introdução do seu artigo] em voz alta:
- Pergunta: O fluxo lógico faz sentido?
- Pergunta: Textos estão claros?
- Pergunta: Faltam dados ou referências?

Se sim em qualquer pergunta → Refine usando QUICK_REFERENCE_TEMPLATES.md

---

## 🎯 Meta Semana 1

**Objetivo:** Ter Introdução + Metodologia refinadas + prontas para advisor ver

**Entrega Esperada:**
- Pdf com seções 1-3 bem preenchidas
- Referências formatadas
- Nenhum TODO pendente

---

**Você tem tudo. Vá compilar! 🚀**

```bash
cd documento_latex/Template_SBC/template-latex/
pdflatex artigo.tex
```

---

**Dúvidas?** Consulte:
- `QUICK_REFERENCE_TEMPLATES.md` (templates prontos)
- `ROADMAP_VISUAL_SIMULACAO_ARTIGO.md` (timeline)
- `GUIA_REFINAMENTO_ARTIGO_LATEX.md` (checklist completo)

**Good luck! ✍️✨**
