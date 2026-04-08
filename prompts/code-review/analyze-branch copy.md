---
title: "Análise de Mudanças da Branch Atual"
description: "Gera documentação técnica e estruturada das alterações desta branch para estudo e registro das mudanças."
author: "<autor>"
last_updated: "2025-01-27"
tags: ["engineering", "code-review", "diff", "documentação", "branch-analysis"]
target_models: ["gpt-4o", "gpt-5"]
inputs:
  - name: "branch_base"
    required: true
    description: "Branch base para comparação (ex.: main)"
  - name: "branch_alvo"
    required: false
    description: "Branch alvo para análise; padrão é HEAD atual"
  - name: "contexto"
    required: false
    description: "Contexto adicional sobre o objetivo/motivação das mudanças (issue, problema, etc.)"
  - name: "arquivo_saida"
    required: false
    description: "Caminho do arquivo Markdown de saída (ex.: docs/changes/<branch>.md)"
---

PROMPT: Análise técnica de mudanças na branch a partir do diff do repositório

[P] PAPEL:
Atue como engenheiro(a) de software sênior e documentador(a) técnico(a). Seja objetivo(a), técnico(a) e didático(a), documentando mudanças relevantes e seus impactos.

[RE] RESTRIÇÕES:
- Idioma: PT-BR (teórico e prático, sem jargões desnecessários)
- Siga Conventional Commits ao se referir a tipos de mudanças
- Não invente contexto inexistente; baseie-se apenas no diff e no contexto fornecido (se houver)
- Máximo de 7±2 tópicos por seção para facilitar leitura
- Não execute comandos; apenas indique como obtê-los
- Se não houver contexto fornecido, infira motivações a partir das mudanças no código (padrões, correções, novas features)

[F] FORMATO:
1) Relatório em Markdown com as seções a seguir
2) Tabela de arquivos modificados com breve descrição
3) Estrutura clara e organizada para facilitar leitura

[COMANDOS PARA O DIFF]:
```bash
# Obter nome da branch atual (necessário para salvar arquivo de saída)
BRANCH_NAME=$(git branch --show-current)

# Buscar atualizações da branch base
git fetch origin <branch_base>

# Visualizar estatísticas das mudanças (visão geral - execute primeiro)
git diff --stat origin/<branch_base>...<branch_alvo_ou_HEAD>

# Obter diff completo para análise detalhada
git diff origin/<branch_base>...<branch_alvo_ou_HEAD>
```

[TAREFA]: Gere uma documentação técnica das mudanças da branch a partir do diff acima e salve (ou oriente a salvar) em `docs/changes/<nome-da-branch>.md` com as seções abaixo.

[NOTA SOBRE USO POSTERIOR]:
O arquivo gerado pode ser usado como contexto adicional no prompt de revisão de PR (review-pr.md), fornecendo informações pré-estruturadas sobre escopo, motivações e impactos das mudanças.

# 📦 Alterações nesta Branch

## 🧩 Resumo Geral
Explique o objetivo da branch, escopo e visão geral das mudanças.

## 🔍 Detalhamento Técnico
- Código-fonte: novas funções, classes, refatorações e exclusões
- Infra/Config: alterações em ambiente, dependências, CI/CD
- Documentação: arquivos novos/atualizados
- Testes: novos casos, alterações de cobertura

## ⚙️ Impactos e Compatibilidade
- Efeitos no sistema existente e compatibilidade reversa
- Migrações necessárias (dados, env, API)
- Riscos e recomendações de mitigação

## 🧠 Contexto e Motivações
Por que as mudanças foram propostas; problema/objetivo que motivou as alterações nesta branch.

**Como inferir quando não há contexto fornecido:**
- Analise os tipos de mudanças no diff seguindo Conventional Commits:
  - `fix`: correção de bugs → problema: comportamento incorreto
  - `feat`: nova funcionalidade → objetivo: adicionar capacidade X
  - `refactor`: refatoração → objetivo: melhorar estrutura/legibilidade
  - `chore/ci`: infraestrutura → objetivo: atualizar deps/configurações
  - `perf`: performance → objetivo: otimizar tempo/memória
  - `docs`: documentação → objetivo: atualizar/clarificar informações
- Identifique padrões no código: correções de erros, adição de validações, novos endpoints, mudanças de schema
- Se contexto foi fornecido, use-o como base e complemente com inferências do diff

## 📋 Observações e Considerações

### Lógica e Casos de Borda
- Lógica de negócio alterada e casos de borda identificados
- Tratamento de erros e validações

### Arquitetura e Padrões
- Aderência à arquitetura existente
- Consistência com padrões do projeto
- Considerações de segurança

### Qualidade e Manutenibilidade
- Cobertura de testes e performance
- Clareza de código e coesão das mudanças
- Complexidade e manutenibilidade

## 📄 Arquivos Modificados
| Arquivo | Descrição breve da mudança |
| --- | --- |
| `<path/arquivo>` | `<descrição objetiva>` |

## ✍️ Autor e Data
- **Autor:** <nome do autor ou usuário git>
- **Data:** <data no formato YYYY-MM-DD>

---

[MODELO DE SAÍDA – EXEMPLO]:
```markdown
# 📦 Alterações nesta Branch

## 🧩 Resumo Geral
<explique o objetivo da branch, escopo e visão geral das mudanças>

## 🔍 Detalhamento Técnico
- Código-fonte: <novas funções, classes, refatorações e exclusões>
- Infra/Config: <alterações em ambiente, dependências, CI/CD>
- Documentação: <arquivos novos/atualizados>
- Testes: <novos casos, alterações de cobertura>

## ⚙️ Impactos e Compatibilidade
- Efeitos no sistema existente: <descrição>
- Compatibilidade reversa: <mantida?/riscos>
- Migrações necessárias (dados, env, API): <detalhes>
- Riscos e recomendações de mitigação: <pontos críticos>

## 🧠 Contexto e Motivações
<por que as mudanças foram propostas; problema/objetivo que motivou>

## 📋 Observações e Considerações
### Lógica e Casos de Borda
<observações sobre lógica e casos de borda>

### Arquitetura e Padrões
<observações sobre arquitetura, padrões e segurança>

### Qualidade e Manutenibilidade
<observações sobre testes, performance, clareza e coesão>

## 📄 Arquivos Modificados
| Arquivo | Descrição breve da mudança |
| --- | --- |
| `<path/arquivo>` | `<descrição objetiva>` |

## ✍️ Autor e Data
- **Autor:** <nome do autor ou usuário git>
- **Data:** <data no formato YYYY-MM-DD>
```

[CONVENTIONAL COMMITS – REFERÊNCIA]:
- feat/fix/refactor/docs/test/chore/ci/perf/style (escopo opcional)
- Mensagem curta (≤ 50 caracteres), no imperativo, sem ponto
- Commits coesos: uma mudança atômica por commit