# Plano de Split em <N> PRs

## Objetivo

- Branch fonte: `<branch_origem>`
- Base: `<branch_base>`
- Meta do split: `<resumo>`

## Análise de Tamanho

- Inserções: `<insercoes>`
- Deleções: `<delecoes>`
- Total: `<total_linhas>`
- Classificação original: `<classe>`
- `quantidade_prs` pedida: `<valor ou não informada>`
- Quantidade recomendada: `<valor>`
- Justificativa: `<por que essa quantidade é adequada>`

## Princípios do Split

- `<regra 1>`
- `<regra 2>`
- `<regra 3>`

## Topologia Proposta

1. `<branch-1>`
   Base: `<base-1>`
   Escopo: `<escopo-1>`

2. `<branch-2>`
   Base: `<base-2>`
   Escopo: `<escopo-2>`

## Detalhamento por PR

### PR 1: `<branch-1>`

- Objetivo: `<objetivo>`
- Commits sugeridos:
  - `<commit 1>`
  - `<commit 2>`
- Arquivos principais:
  - `<arquivo>`
  - `<arquivo>`
- Arquivos com stage por hunk:
  - `<arquivo>`
- Testes:
  - `<comando>`
- Classe prevista: `<classe>`

### PR 2: `<branch-2>`

- Objetivo: `<objetivo>`
- Commits sugeridos:
  - `<commit 1>`
  - `<commit 2>`
- Arquivos principais:
  - `<arquivo>`
- Testes:
  - `<comando>`
- Classe prevista: `<classe>`

## Exclusões

- `<mudanças locais ou arquivos que não entram no split>`

## Checklist Final

- Cada PR tem uma responsabilidade funcional central
- Arquivos mistos foram separados com `git add -p`
- Cada branch compila e roda os testes relevantes
- Nenhum PR ficou `GG` sem justificativa explícita
