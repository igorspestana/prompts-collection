---
name: pr-plan
description: Use quando o usuário ainda não começou a implementar e quiser planejar como dividir uma feature, tarefa ou refatoração em PRs pequenos antes de escrever código. Produz um plano em markdown com estratégia de integração, ordem de PRs e sugestões de commits. Não toca em código ou branches.
---

# PR Plan

## Objetivo
Transformar uma tarefa de desenvolvimento em um plano prático de execução com PRs menores, ordenados e coerentes, priorizando segurança de integração, clareza de revisão, reversibilidade e baixo acúmulo de conflitos.

## Quando usar
- Quando o usuário ainda não começou a implementar e quiser planejar como dividir uma feature, tarefa ou refatoração em PRs menores.
- Quando houver dúvida entre PRs direto para `main` e uso de `integration branch`.
- Quando o time quiser reduzir risco e facilitar review antes de implementar.
- Quando existir design doc, spec, plano técnico ou lista de áreas impactadas e isso precisar virar um plano de branches/PRs.

## Quando NÃO usar
- Se o código já existe em uma branch e precisa ser dividido em PRs menores, use a skill `pr-splitter` (split de branch existente com execução git).

## Entradas
- `objetivo` (obrigatório)
- `contexto_tecnico` (opcional, mas fortemente recomendado)
- `areas_afetadas` (opcional, mas recomendado)
- `artefatos_de_planejamento` (opcional)
- `restricoes` (opcional)
- `preferencia_de_estrategia` (opcional)
- `convencoes_de_branch` (opcional)
- `convencoes_de_commit` (opcional)
- `arquivo_saida` (opcional)

### Entrada mínima
- objetivo da mudança
- contexto técnico básico
- áreas do sistema afetadas

### Entrada ideal
- descrição detalhada da feature, tarefa ou refatoração
- design doc, feature spec ou plano de desenvolvimento
- módulos, serviços, APIs, banco de dados e interfaces impactadas
- dependências conhecidas
- restrições técnicas e organizacionais
- preferência por PRs direto para `main` ou `integration branch`
- necessidade de feature flags, compatibilidade temporária ou rollout gradual
- convenções de nomes de branches e commits

## Saída esperada
Produzir um plano estruturado em PT-BR seguindo obrigatoriamente `assets/pr-plan-template.md`.

Salvar o plano em `arquivo_saida` quando ele for informado.

Se `arquivo_saida` não for informado, definir um caminho padrão em:
- `agent-artifacts/pr/<nome-sanitizado>/pr-plan.md`

Onde `<nome-sanitizado>` deve ser derivado do objetivo ou identificador principal da tarefa:
- converter para minúsculas
- substituir espaços, barras e separadores por `-`
- remover duplicação desnecessária de hífens
- manter o nome curto, legível e estável

A saída deve incluir:
- estratégia recomendada de integração
- justificativa da estratégia escolhida
- `integration branch`, quando aplicável
- lista ordenada de branches
- lista ordenada de pull requests
- branch de origem e branch de destino de cada PR
- labels esperadas por PR
- objetivo, escopo, dependências e risco de cada PR
- sugestões de commits por branch, quando úteis
- observações de rollout, reversibilidade, compatibilidade e possibilidade de merge direto para `main`
- suposições e pontos em aberto, quando existirem

## Referências
Use conforme necessário:
- `references/strategy-framework.md`: framework principal com as 4 estratégias de integração (trunk-based, encadeado sem integração, paralelos com integração, stacked diffs), tabela comparativa, sequência de decisão e erros comuns.
- `references/expected-input-output.md`: definição de entrada e formato ideal de saída.
- `references/conventional-commits.md`: regras para sugerir commits em inglês com Conventional Commits.
- `references/size-classification.md`: tabela de classificação `PP|P|M|G|GG` por linhas alteradas; use como meta de planejamento ao estimar o tamanho de cada PR proposto.

## Workflow
1. Ler a solicitação e identificar objetivo, contexto técnico, áreas afetadas, restrições e preferências explícitas.
2. Se a entrada estiver incompleta, inferir uma divisão razoável e registrar explicitamente as suposições.
3. Definir o arquivo de saída:
   - usar `arquivo_saida` quando informado
   - caso contrário, gerar `agent-artifacts/pr/<nome-sanitizado>/pr-plan.md`
4. Aplicar o framework de decisão em `references/strategy-framework.md`.
5. Verificar primeiro se a implementação pode ser quebrada em PRs pequenos direto para `main`.
6. Considerar `integration branch` apenas quando houver dependências reais, revisão em camadas ou alto acoplamento entre etapas.
7. Montar PRs que façam sentido de forma isolada, sejam seguros para integrar e preferencialmente reversíveis.
8. Evitar divisões artificiais apenas por camada técnica quando isso gerar dependências ruins ou review sem contexto.
9. Priorizar fatias de integração, por exemplo:
   - preparar estrutura sem ativar comportamento
   - introduzir contrato novo mantendo compatibilidade
   - adaptar backend para suportar antigo e novo
   - adicionar UI atrás de flag
   - ativar comportamento
   - remover legado depois
10. Definir ordem dos PRs com justificativa clara.
10a. Para cada PR proposto, estimar a faixa de tamanho esperada (`PP|P|M|G|GG`) e aplicar as diretrizes de `references/size-classification.md`.
11. Nomear branches com nomes curtos, claros e orientados ao objetivo.
12. Se houver `integration branch`, fazer com que as branches filhas estendam o nome da branch principal com numeração coerente.
12a. Se houver `integration branch`, marcar no plano que o PR final para `main` deve usar título com prefixo `[integration]` e label `integration`.
13. Sugerir commits somente quando isso aumentar a clareza do plano e a previsibilidade de execução.
14. Ao sugerir commits, seguir `references/conventional-commits.md` rigorosamente.
15. Produzir a resposta final no formato do template.
16. Salvar o plano no arquivo de saída.

## Critérios de decisão

Consultar `references/strategy-framework.md` para a sequência de decisão completa e a tabela comparativa entre as 4 estratégias.

### Preferir trunk-based (PRs direto para `main`)
Escolha esta opção quando a maior parte das etapas puder:
- ser mergeada sem quebrar o sistema
- permanecer oculta por feature flag
- coexistir temporariamente com o comportamento antigo
- fazer sentido isoladamente
- ser revertida com segurança

### Preferir PRs encadeados sem branch de integração
Escolha quando dois PRs têm dependência de curto prazo, mas ambos são pequenos o suficiente para ir direto à `main` sem branch intermediária.

### Usar `integration branch` (PRs paralelos ou stacked)
`integration branch` é uma branch temporária usada para agrupar PRs dependentes antes do merge final na `main`.

Escolha `integration branch` quando uma ou mais condições forem verdadeiras:
- existem dependências reais entre os PRs
- a revisão precisa acontecer em camadas
- a feature só faz sentido quando o conjunto estiver pronto
- a mudança envolve múltiplas camadas fortemente acopladas
- o plano técnico já define uma sequência natural de implementação
- integrar parcialmente na `main` criaria complexidade ou risco desnecessário

Entre as variações com `integration branch`: usar PRs paralelos quando as partes são independentes entre si; usar stacked diffs quando há dependência sequencial explícita entre os PRs filhos.

Ao recomendar `integration branch`, explicar por que PRs direto para `main` não são a melhor opção naquele contexto.

## Regras
- Priorizar mergeabilidade antes de organização visual.
- Priorizar reversibilidade antes de elegância da quebra.
- Preferir compatibilidade temporária e rollout gradual em vez de big bang.
- Minimizar tempo fora da `main`.
- Tratar `integration branch` como ferramenta temporária, não como `main` paralela.
- Quando houver `integration branch`, o PR final para `main` deve usar prefixo `[integration]` no título e label `integration`.
- Explicar a ordem proposta de forma objetiva.
- Manter títulos, nomes de branch e escopos consistentes entre si.
- Sugerir commits em inglês.
- Usar Conventional Commits quando sugerir commits.
- Não gerar código nem instruções de implementação detalhada além do necessário para explicar a divisão em PRs.

## Convenções de branches
Quando houver `integration branch`, usar um padrão como:
- `integration branch`: `feat-new-dashboard`
- branch dependente 1: `feat-new-dashboard-1-add-entities`
- branch dependente 2: `feat-new-dashboard-2-add-api`
- branch dependente 3: `feat-new-dashboard-3-add-ui`
- branch dependente 4: `feat-new-dashboard-4-enable-feature`

Regras:
- preservar o contexto da `integration branch` nas filhas
- manter numeração coerente
- usar descrições curtas e específicas
- refletir o escopo real do PR

## Convenções de commits
Quando fizer sentido sugerir commits:
- cada commit deve ter escopo atômico
- a mensagem deve seguir Conventional Commits
- a descrição deve estar no imperativo
- a mensagem deve ser curta, específica e em inglês
- evitar commits genéricos ou que misturem responsabilidades

## Ambiguidade e Suposições
- Se faltarem detalhes técnicos, inferir o plano com base no objetivo e declarar as suposições.
- Se o usuário pedir `integration branch`, ainda validar se PRs direto para `main` seriam melhores.
- Se a estratégia preferida pelo usuário aumentar risco claramente, respeitar a preferência, mas registrar a ressalva.
- Se houver artefatos contraditórios, priorizar o material mais específico e mencionar a divergência.
- Se não houver informação suficiente para detalhar commits, sugerir apenas blocos de mudança por PR.

## Restrições
- Não inventar dependências que não estejam razoavelmente implícitas no contexto.
- Não forçar `integration branch` quando `main` for viável.
- Não propor PRs tão pequenos que percam significado.
- Não propor PRs tão amplos que prejudiquem review ou rollback.
- Não assumir existência de feature flags, adapters ou expand/contract sem citar isso como hipótese.

## Tratamento de Erro
Quando não houver contexto suficiente para montar um plano minimamente confiável, retornar:

```text
Status: ERRO

Motivo: contexto insuficiente para propor uma divisão segura e ordenada.

Informações adicionais necessárias:
* objetivo da mudança
* contexto técnico básico
* áreas do sistema afetadas
* restrições ou dependências conhecidas
```
