---
name: pr-splitter
description: Use quando o código já existir em uma branch grande e o usuário pedir para dividir esse trabalho já implementado em PRs menores. Analisa o diff real, classifica o tamanho pelo critério PP/P/M/G/GG, cria branches empilhadas e pode executar o split com git. Não é para planejamento antes de implementar.
---

# PR Splitter

## Objetivo

Quebrar uma branch grande em PRs menores sem perder coesão funcional, legibilidade do histórico e capacidade de validação.

Use a métrica de tamanho por linhas como restrição de review, não como único critério. Priorize responsabilidade funcional clara, mas trate PR `GG` como sinal de que o split ainda está grande demais.

## Entradas

- `branch_origem` (opcional; padrão: `HEAD` atual)
- `branch_base` (opcional; padrão: `main`)
- `quantidade_prs` (opcional)
- `arquivo_saida` (opcional; padrão: `docs/pr/<branch-sanitizada>/pr-split-plan.md`)
- `executar_split` (opcional; padrão implícito: só planejar; executar quando o pedido deixar isso claro)
- `contexto` (opcional)

Leia sempre [size-classification.md](./references/size-classification.md).

## Workflow

1. Resolver `branch_origem`, `branch_base` e o caminho de saída.
2. Sanitizar o nome da branch (`/` -> `-`) para gerar o path padrão de documentação.
3. Medir o diff com `scripts/pr_size_classifier.py <base> <head>`.
4. Classificar o tamanho do PR original usando a tabela `PP`, `P`, `M`, `G`, `GG`.
5. Quando `quantidade_prs` não for informada, decidir a quantidade usando a heurística abaixo.
6. Mapear responsabilidades funcionais, arquivos tocados, dependências entre mudanças e arquivos com mix de responsabilidades.
7. Propor branches empilhadas com objetivo claro por PR.
8. Quebrar cada PR em commits semânticos pequenos.
9. Quando um arquivo misturar responsabilidades de mais de um PR, usar stage parcial com `git add -p`.
10. Escrever ou atualizar `pr-split-plan.md` usando [pr-split-plan-template.md](./assets/pr-split-plan-template.md).
11. Se o pedido incluir execução, criar worktrees fora do diretório atual, montar as branches empilhadas e validar cada etapa com testes direcionados.
12. Ao final, reportar a classificação de tamanho prevista ou observada para cada PR resultante.

## Heurística para decidir `quantidade_prs`

1. Calcular `total_linhas = insercoes + delecoes`.
2. Se `quantidade_prs` foi informada pelo usuário, respeitar como ponto de partida.
3. Se `quantidade_prs` não foi informada:
- calcular `minimo_sem_gg = ceil(total_linhas / 1000)`;
- calcular `alvo_preferido = ceil(total_linhas / 500)`;
- começar por `minimo_sem_gg`;
- aumentar a quantidade quando responsabilidades continuarem misturadas, quando arquivos críticos precisarem de muitos hunks parciais, ou quando a projeção ainda concentrar PRs `GG`;
- usar `alvo_preferido` como referência de granularidade ideal, não como regra rígida.
4. Se a quantidade escolhida pelo usuário implicar média projetada acima de `1000` linhas por PR, registrar que a divisão tende a gerar PRs `GG`.
5. Preferir resultado final em que a maioria dos PRs fique em `P` ou `M`.
6. Aceitar PR `GG` apenas com justificativa explícita de acoplamento funcional ou risco técnico de separar mais.

## Regras Críticas

- Não usar o worktree atual para montar o split quando ele estiver sujo.
- Preferir `git worktree` em `/tmp` para cada PR empilhado.
- Não usar `git reset --hard`.
- Não carregar mudanças locais irrelevantes para o split.
- Não aceitar 1 commit único por branch quando houver responsabilidades diferentes.
- Validar cada branch antes de montar a próxima.
- Manter cada PR com uma responsabilidade funcional central e commits semanticamente coesos.
- Tratar métricas por linhas como critério de reviewabilidade, não como autorização para separar código semanticamente inseparável.

## Saídas Esperadas

- `agent-artifacts/pr/<branch-sanitizada>/pr-split-plan.md`
- lista de PRs propostos com base e head de cada branch
- classificação `PP|P|M|G|GG` do PR original e de cada PR resultante
- quando houver execução, branches empilhadas prontas para review

## Execução do Split

Quando o pedido for de execução, siga esta ordem:

1. Criar a primeira branch a partir de `branch_base`.
2. Criar cada branch seguinte a partir do SHA da branch anterior, não do nome da branch se ela já estiver anexada a outro worktree.
3. Restaurar da branch fonte apenas o conjunto de arquivos candidato daquele PR.
4. Usar `git add -p` em arquivos mistos.
5. Comitar em unidades pequenas e semânticas.
6. Executar testes direcionados em cada worktree.
7. Só prosseguir para o PR seguinte depois de a etapa atual compilar e os testes relevantes passarem.

## Tratamento de Exceções

- Se `main` não existir, exigir `branch_base` explícita.
- Se o diff estiver grande demais para inspeção manual direta, começar por `git diff --stat` e depois detalhar apenas arquivos candidatos por responsabilidade.
- Se o split ótimo exigir mais PRs do que o usuário pediu, documentar o conflito e propor a menor alternativa que evite PRs `GG`.
- Se um arquivo precisar aparecer em mais de um PR, descrever explicitamente quais hunks pertencem a cada etapa.

## Recursos

- `scripts/pr_size_classifier.py`: mede inserções, deleções, total e classificação da faixa.
- `references/size-classification.md`: regra oficial de classificação e critérios de decisão.
- `assets/pr-split-plan-template.md`: template enxuto para o plano de split.
