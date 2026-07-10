---
name: pr-review-orchestrator
description: Orquestra análise completa de PR em duas fases obrigatórias, executando branch-analyzer antes de pr-reviewer e garantindo passagem de contexto entre elas. Use quando o usuário pedir revisão ponta-a-ponta com documentação técnica da branch e relatório final de revisão.
---

# PR Review Orchestrator

## Objetivo
Coordenar fluxo sequencial obrigatório:
1. Gerar documentação técnica da branch
2. Gerar revisão técnica do PR usando essa documentação como contexto

## Entradas
- `branch_base` (obrigatório; se ausente, assumir `main`)
- `branch_alvo` (opcional, padrão: HEAD atual)
- `contexto` (opcional)
- `arquivo_saida_analise` (opcional)
- `arquivo_saida_review` (opcional)

## Preparação
1. Resolver `branch_base`: usar valor informado; quando ausente, assumir `main`; se `main` não existir no repositório, retornar erro objetivo solicitando base explícita.
2. Resolver `branch_alvo` (ou HEAD).
3. Sanitizar nome da branch (`/` -> `-`).
4. Definir caminhos padrão:
- `docs/pr/<branch-sanitizada>/branch-analysis.md`
- `docs/pr/<branch-sanitizada>/pr-review.md`
5. Resolver saídas:
- usar `arquivo_saida_analise` quando informado; senão usar caminho padrão de `branch-analysis.md`.
- usar `arquivo_saida_review` quando informado; senão usar caminho padrão de `pr-review.md`.
6. Criar diretório pai dos arquivos de saída quando necessário.

## Fase 1 (obrigatória): branch-analyzer
1. Executar `branch-analyzer` com os mesmos parâmetros e `arquivo_saida_analise`.
2. Gerar relatório de análise no caminho resolvido para análise.
3. Validar que o arquivo de análise existe e está legível.

## Fase 2 (obrigatória): pr-reviewer
1. Executar somente após a conclusão da Fase 1.
2. Passar `arquivo_analise` apontando para o caminho resolvido de análise.
3. Repassar `branch_base`, `branch_alvo`, `contexto` e `arquivo_saida_review`.
4. Gerar `pr-review.md` no caminho resolvido para review.

## Regras Críticas
- Executar sempre `branch-analyzer` antes de `pr-reviewer`.
- Validar sempre que o arquivo de análise existe e está legível antes da Fase 2.
- Escrever apenas nos caminhos definidos pelo fluxo (ou nos caminhos explícitos do usuário).
- Atualizar o arquivo-alvo quando já existir; evitar duplicar relatórios.
- Focar exclusivamente em análise e revisão; não incluir sugestões de mudança de código, upgrades ou migrações.
- Prosseguir somente após `branch_base` estar resolvida (informada ou `main`).

## Saída Esperada
- `docs/pr/<branch-sanitizada>/branch-analysis.md`
- `docs/pr/<branch-sanitizada>/pr-review.md`
- Quando `arquivo_saida_analise`/`arquivo_saida_review` forem informados, usar os caminhos explícitos correspondentes.

## Tratamento de Erro
Se qualquer fase falhar, retornar `Status: ERRO`, motivo objetivo e etapa que falhou (preparação, fase 1 ou fase 2).
