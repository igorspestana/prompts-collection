# Expected Input / Output

## Entrada mínima
- descrição da tarefa, feature ou refatoração
- contexto técnico básico

Exemplo:
> Preciso implementar um novo dashboard com entidades, API e UI. Quero quebrar isso em PRs pequenos e fáceis de revisar.

## Entrada ideal
- objetivo da mudança
- contexto técnico
- áreas ou módulos afetados
- restrições de execução
- estratégia preferida, se houver
- artefatos de planejamento
- dependências conhecidas
- convenções de branches e commits
- `arquivo_saida`, se o time quiser um destino específico para o plano

## Saída esperada
A skill deve produzir um plano de execução em PRs, não código.

O plano deve conter:
- caminho do artefato gerado
- estratégia recomendada
- justificativa
- lista ordenada de branches
- lista ordenada de PRs
- origem e destino de cada PR
- objetivo e escopo
- dependências
- riscos e observações de revisão
- commits sugeridos por branch, quando útil
- observações sobre feature flags, compatibilidade e merge direto para `main`

## Forma mais útil de resposta
1. Recomendação geral
2. `Integration branch`, se necessária
3. Plano de PRs
4. Riscos e observações

## Destino padrão do artefato
Se o usuário não informar `arquivo_saida`, salvar em:

`agent-artifacts/pr/<nome-sanitizado>/pr-plan.md`
