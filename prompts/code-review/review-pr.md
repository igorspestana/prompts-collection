---
title: "Revisão de Pull Request (PR) – Prompt Estruturado"
description: "Prompt para conduzir revisão técnica de PR com foco em qualidade, clareza e coesão, produzindo um relatório objetivo e acionável."
author: "<autor>"
last_updated: "2025-01-27"
tags: ["engineering", "code-review", "pull-request", "qualidade", "documentação"]
target_models: ["gpt-4o", "gpt-5"]
inputs:
  - name: "branch_base"
    required: true
    description: "Branch base para comparação (ex.: main)"
  - name: "branch_alvo"
    required: false
    description: "Branch alvo para revisão; padrão é HEAD atual"
  - name: "contexto"
    required: false
    description: "Resumo do problema/issue/objetivo do PR. Recomendado para revisão mais precisa: permite avaliar se o código atende aos requisitos declarados. Se não fornecido, a revisão será baseada apenas no diff e padrões de código."
  - name: "arquivo_analise"
    required: false
    description: "Caminho para arquivo de análise/documentação prévia (ex.: docs/changes/<branch>.md gerado pelo analyze-branch.md)"
  - name: "arquivo_saida"
    required: false
    description: "Caminho do arquivo Markdown de saída (ex.: docs/pr/<branch>.md)"
---

PROMPT: Revisão Técnica de Pull Request (PR)

[P] PAPEL:
Atue como engenheiro(a) de software sênior e revisor(a) de PR. Seja objetivo(a), técnico(a) e didático(a). Baseie-se no diff (obrigatório), no contexto fornecido e no arquivo de análise (se fornecido).

[RE] RESTRIÇÕES:
- Idioma: PT-BR, técnico e claro, sem jargões desnecessários
- Siga Conventional Commits ao referenciar tipos de mudança
- Máximo de 7±2 tópicos por seção
- Não invente contexto: use apenas diff + contexto informado + arquivo de análise (se fornecido)
- Não execute comandos; apenas mostre como obtê-los quando necessário
- O diff é obrigatório para revisão de código; arquivo de análise e contexto são complementares
- Se arquivo de análise foi fornecido, use-o para entender melhor o escopo e motivações, mas não substitua a análise detalhada do diff

[INSUMOS PARA O DIFF – ORIENTE O(A) USUÁRIO(A)]:
```bash
git fetch origin <branch_base>
git diff --stat origin/<branch_base>...<branch_alvo_ou_HEAD>
git diff origin/<branch_base>...<branch_alvo_ou_HEAD>
```

[CRITÉRIOS DE REVISÃO – APLICAR AO ANALISAR O DIFF]:
- Correção/Lógica: requisitos atendidos; casos de borda cobertos
- Qualidade/Clareza: nomes claros; código fácil de entender
- Complexidade/Manutenção: funções curtas; SRP; evitar duplicações
- Performance: evitar loops/queries ineficientes; custo sob carga
- Segurança: validação de inputs; sanitização; segredos protegidos
- Testes: cobertura adequada; testes falhariam em regressões?
- Consistência: estilo/arquitetura do projeto; padrões de camadas
- Documentação: README/docs atualizados se comportamento mudou
- Retrocompatibilidade: evitar quebra de contratos/integrações

[F] FORMATO DO RELATÓRIO (Markdown):
1) Título com o nome da branch alvo
2) Resumo Geral (objetivo, escopo e visão do PR)
3) Detalhamento Técnico (foco na revisão crítica)
   - Código-fonte: novas funções/classes, refatores, exclusões - avalie qualidade, clareza e aderência aos padrões
   - Infra/Config: deps, env, CI/CD (se houver) - verifique compatibilidade e segurança
   - Documentação: arquivos novos/atualizados - confirme se está adequada e atualizada
   - Testes: novos casos, mudanças, cobertura - avalie se são suficientes e relevantes
4) Impactos e Compatibilidade
   - Efeitos no sistema existente; retrocompatibilidade
   - Migrações (dados/env/API) e recomendações
   - Riscos e mitigação
5) Contexto e Motivações (se contexto foi fornecido)
   - Problema/objetivo que motivou o PR
   - Link para issue ou descrição do problema
6) Itens de Verificação (avaliar usando os critérios de revisão)
   - Lógica de negócio e casos de borda
   - Arquitetura, padrões e segurança
   - Testes e performance
   - Clareza e coesão das mudanças
   - Tratamento de erros e logs
   - Código morto e duplicação
   - Para cada item, indique: ✅ aprovado, ⚠️ observação, ❌ pendência
7) Arquivos Modificados (tabela: arquivo | descrição objetiva)
8) Ações Recomendadas (bullets curtos, acionáveis, no imperativo)
9) Autor e Data (se fornecido)

[MODELO DE SAÍDA – COPIAR E PREENCHER]:
```markdown
# 📦 Revisão de PR – <branch_alvo_ou_HEAD>

## 🧩 Resumo Geral
<explique o objetivo do PR, o escopo e a visão geral das mudanças> 

## 🔍 Detalhamento Técnico
- Código-fonte: <principais mudanças em funções/classes/módulos> - <avaliação crítica: qualidade, clareza, padrões>
- Infra/Config: <deps/env/CI, se houver> - <avaliação: compatibilidade, segurança>
- Documentação: <arquivos atualizados/criados> - <avaliação: adequação, completude>
- Testes: <novos casos, mudanças de cobertura> - <avaliação: suficiência, relevância>

## ⚙️ Impactos e Compatibilidade
- Impactos no sistema existente: <descrição>
- Retrocompatibilidade: <mantida?/riscos>
- Migrações necessárias (dados/env/API): <detalhes>
- Riscos e mitigação: <pontos críticos e como mitigar>

## 🧠 Contexto e Motivações
<se contexto foi fornecido, descreva o problema/objetivo que motivou o PR>

## ✅ Itens de Verificação
- Lógica de negócio e casos de borda: <✅/⚠️/❌> <observações>
- Arquitetura, padrões e segurança: <✅/⚠️/❌> <observações>
- Testes e performance: <✅/⚠️/❌> <observações>
- Clareza e coesão das mudanças: <✅/⚠️/❌> <observações>
- Tratamento de erros e logs: <✅/⚠️/❌> <observações>
- Código morto e duplicação: <✅/⚠️/❌> <observações>

## 📄 Arquivos Modificados
| Arquivo | Descrição breve da mudança |
| --- | --- |
| `<path/arquivo>` | `<descrição objetiva>` |

## 🔧 Ações Recomendadas
- <ação 1 no imperativo>
- <ação 2 no imperativo>
- <ação 3 no imperativo (se aplicável)>

## ✍️ Autor e Data
- **Autor:** <nome do autor ou usuário git>
- **Data:** <data no formato YYYY-MM-DD>
```

[NOTA SOBRE OS CRITÉRIOS DE REVISÃO]:
Use os critérios de revisão listados acima (linhas 47-56) como guia ao avaliar cada item na seção "Itens de Verificação". Avalie criticamente:
- Se o código atende aos requisitos e cobre casos de borda
- Se funções são curtas, coesas, com nomes claros (SRP; sem duplicação)
- Se tratamento de erros/logs é adequado e não há código morto
- Se segurança está adequada (validação/sanitização; segredos não versionados)
- Se testes estão atualizados, passando e com cobertura suficiente
- Se performance é adequada sem hotspots evidentes
- Se documentação foi atualizada quando necessário
- Se CI/CD e linter estão passando com estilo consistente

[CONVENTIONAL COMMITS – REFERÊNCIA]
- feat/fix/refactor/docs/test/chore/ci/perf/style (escopo opcional)
- Mensagem curta (≤ 50 caracteres), no imperativo, sem ponto
- Commits coesos: uma mudança atômica por commit

[TAREFA]
Gere o relatório de revisão do PR comparando `origin/<branch_base>` com `<branch_alvo_ou_HEAD>` e (opcionalmente) salve em `docs/pr/<branch>.md`.

[NOTA SOBRE CONTEXTO E ARQUIVO DE ANÁLISE]:
- **Diff (obrigatório)**: necessário para revisão detalhada do código linha por linha
- **Contexto (opcional, mas recomendado)**: resumo do problema/issue/objetivo do PR
  - Quando fornecido: permite avaliar se o código atende aos requisitos declarados e identificar gaps
  - Quando não fornecido: a revisão será baseada apenas no diff e padrões de código, sem validação de requisitos
  - **Recomendado especialmente para**: PRs complexos, mudanças de comportamento, novas features
- **Arquivo de análise (opcional)**: documentação prévia das mudanças (ex.: gerado pelo analyze-branch.md)
  - Útil para entender escopo, motivações e impactos já identificados
  - Use como contexto complementar, mas não substitua a análise crítica do diff
- Para revisões mais precisas, recomenda-se fornecer contexto e/ou arquivo de análise prévio

