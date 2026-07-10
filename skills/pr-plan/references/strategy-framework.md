# Strategy Framework

## Objetivo
Escolher a estratégia de integração que melhor reduz risco, facilita revisão e mantém o fluxo de integração saudável.

## Ordem de preferência
1. Trunk-based development (PRs pequenos direto para `main`)
2. PRs encadeados sem branch de integração
3. PRs paralelos com integração
4. PRs encadeados (stacked diffs) com branch de integração

Só avance para estratégias mais complexas quando as anteriores não forem adequadas ao contexto.

---

## Estratégia 1: Trunk-based development

Cada PR nasce da `main` e retorna para a `main` assim que estiver pronto. A feature é construída incrementalmente dentro da própria branch principal. Funcionalidades incompletas são isoladas com feature flags ou toggles.

```
main
├── feat-topic-1  ← PR 1 → merge na main
├── feat-topic-2  ← PR 2 → merge na main
└── feat-topic-3  ← PR 3 → merge na main
```

### Use quando
- cada mudança pode ser mergeada sem quebrar o sistema
- a feature pode ficar incompleta, mas escondida (feature flag ou toggle)
- o time tem cadência alta de deploy
- as partes podem ser revisadas e implantadas independentemente
- cada PR pode ser revertido com segurança

### Ordem de merge
Flexível. Cada PR pode ser mergeado assim que estiver aprovado. Se houver dependência funcional, mergear primeiro o que serve de base.

### Ordem de review
Flexível. Priorizar o que está menor, mais pronto e com menor risco de bloqueio.

### Heurística de quebra
Prefira fatias de integração como:
- preparar modelo ou estrutura
- expor contrato novo mantendo compatibilidade
- adaptar backend para suportar antigo e novo
- adicionar UI atrás de flag
- ativar comportamento
- remover legado depois

---

## Estratégia 2: PRs encadeados sem branch de integração

O PR 1 nasce da `main` e aponta para ela. O PR 2 é criado a partir do PR 1 apenas para viabilizar o desenvolvimento — sem branch de integração. Quando o PR 1 é mergeado, o PR 2 é retargetado para `main` via rebase.

```
main
├── feat-topic-1          ← PR 1 → aponta para main
└── feat-topic-2          ← PR 2 → aponta temporariamente para feat-topic-1

Depois que PR 1 é mergeado:
feat-topic-2 → retargetado para main → PR 2 → main
```

### Use quando
- dois PRs têm dependência de curto prazo, mas ambos são pequenos o suficiente para ir diretamente à `main`
- evita criar branch de integração apenas para gerenciar dependência transitória
- uma pessoa começa a construir em cima de uma base ainda sendo desenvolvida por outra

### Ordem de merge
1. PR 1: `feat-topic-1` → `main`
2. Retargetar PR 2: `feat-topic-2` → `main` (rebase sobre main atualizada)
3. PR 2: `feat-topic-2` → `main`

### Ordem de review
O PR 2 pode ser revisado antes mesmo do PR 1 ser mergeado, já que o reviewer avalia apenas o diff do PR 2 em relação ao PR 1. Isso acelera o ciclo sem exigir que o time espere a sequência completa de merges.

---

## Estratégia 3: PRs paralelos com integração

Existe uma branch de integração criada a partir da `main`. Os PRs menores nascem dessa branch e retornam para ela. Só depois que todos estiverem consolidados, um PR final leva tudo para a `main`.

```
main
└── feat-topic-integration   ← branch de integração
    ├── feat-topic-1         ← PR 1 → merge em feat-topic-integration
    ├── feat-topic-2         ← PR 2 → merge em feat-topic-integration
    └── feat-topic-3         ← PR 3 → merge em feat-topic-integration

Depois:
feat-topic-integration → PR integration → main
```

### Use quando
- a feature tem várias partes que podem ser desenvolvidas em paralelo, mas só fazem sentido juntas
- a branch de integração atua como ambiente de validação antes de tudo chegar na `main`
- não há dependência sequencial forte entre os PRs filhos

### Ordem de merge
Os PRs menores podem ser mergeados na branch de integração em qualquer ordem. O PR final só deve ser mergeado depois que todos os filhos estiverem aprovados e consolidados.

### Ordem de review
Revisar primeiro os PRs que definem bases comuns, depois os mais específicos. O PR final para `main` não deve ser revisado antes que os PRs filhos estejam aprovados — ele tende a ser mais uma validação de consolidação do que uma revisão técnica profunda.

### Boas práticas
- manter a `integration branch` viva pelo menor tempo possível
- garantir que cada PR filho tenha escopo claro
- tratar o PR final para `main` como integração, não como revisão do zero
- no PR final para `main`, usar título com prefixo `[integration]` e label `integration`

---

## Estratégia 4: PRs encadeados (stacked diffs) com branch de integração

Cada branch nasce da anterior, criando uma cadeia de dependências explícitas. A branch de integração nasce da `main`; o PR 1 nasce dela; o PR 2 nasce do PR 1; e assim por diante.

```
main
└── feat-topic-integration     ← branch de integração
    └── feat-topic-1           ← PR 1 (base: feat-topic-integration)
        └── feat-topic-2       ← PR 2 (base: feat-topic-1)
            └── feat-topic-3   ← PR 3 (base: feat-topic-2)

Depois da stack inteira aprovada:
feat-topic-integration → PR integration → main
```

### Use quando
- existe dependência real e sequencial entre as partes: o PR 2 só faz sentido depois que o PR 1 for implementado
- comum em refatorações em camadas ou construção de funcionalidade em cima de outra

### Ordem de merge
A ordem não é flexível. Deve respeitar a estrutura de dependência, sempre de cima para baixo:

1. PR 3: `feat-topic-3` → `feat-topic-2`
2. PR 2: `feat-topic-2` → `feat-topic-1`
3. PR 1: `feat-topic-1` → `feat-topic-integration`
4. PR integration: `feat-topic-integration` → `main`

Mergear fora dessa sequência gera conflitos estruturais difíceis de resolver.

### Ordem de review
O review segue a lógica inversa do merge: de baixo para cima, começando pelo PR mais próximo da base. Os PRs seguintes dependem do anterior; entender a fundação é necessário para revisar o topo.

1. PR integration: `feat-topic-integration` → `main`
2. PR 1: `feat-topic-1` → `feat-topic-integration`
3. PR 2: `feat-topic-2` → `feat-topic-1`
4. PR 3: `feat-topic-3` → `feat-topic-2`

### Nota operacional
No PR final da `integration branch` para `main`, usar título com prefixo `[integration]` e label `integration`.

---

## Comparativo rápido

| Critério | Trunk-based | Encadeado sem integração | Paralelos com integração | Encadeados (stacked) |
|---|---|---|---|---|
| Branch de integração | Não | Não | Sim | Sim |
| Dependência entre PRs | Nenhuma | Temporária | Baixa | Explícita |
| Ordem de merge | Flexível | PR 1 antes do PR 2 | Flexível (filhos antes do final) | Obrigatória (cima para baixo) |
| Ordem de review | Flexível | Paralela (PR 2 pode ser revisado antes) | Semi-flexível | Obrigatória (baixo para cima) |
| Exige feature flags | Frequentemente | Raramente | Raramente | Raramente |
| Risco de conflito | Baixo | Baixo após retarget | Médio | Alto se fora de ordem |
| Indicado para | Features independentes em alta cadência | Dependências transitórias entre duas pessoas | Features paralelas com consolidação | Features com dependências em camadas |

---

## Sequência de decisão

**1. As partes da feature têm dependências entre si?**
- Não → trunk-based ou PRs paralelos com integração
- Sim, em sequência → PRs encadeados (com ou sem branch de integração)

**2. O time faz deploy frequente e usa feature flags?**
- Sim → trunk-based
- Não → PRs paralelos ou encadeados

**3. A feature só faz sentido quando todas as partes estiverem juntas?**
- Sim → PRs paralelos com integração
- Não necessariamente → trunk-based

**4. Existe dependência temporária entre dois PRs desenvolvidos por pessoas diferentes, sem necessidade de branch de integração?**
- Sim → PRs encadeados sem branch de integração

---

## Erros comuns ao dividir PRs

**Dividir por arquivo, não por responsabilidade.** O critério de divisão deve ser a responsabilidade, não o arquivo modificado.

**Criar dependências desnecessárias em PRs paralelos.** Se dois PRs supostamente paralelos compartilham código que um modifica e o outro precisa, eles deixam de ser paralelos. Vale reorganizar antes de começar.

**Mergear a branch de integração antes de todos os PRs filhos estarem prontos.** O PR final deve ser o último. Mergear cedo cria uma versão incompleta na `main`.

**Revisar o topo da stack sem ter revisado a base.** Em stacked diffs, revisar o PR 3 sem ter revisado o PR 1 e o PR 2 é ineficiente. O contexto construído na base é necessário para entender o topo.

---

## Princípios

- Mergeabilidade antes de organização visual
- Reversibilidade antes de elegância
- Compatibilidade temporária antes de big bang
- Integração contínua antes de branch longa
- `Integration branch` como exceção útil, não como padrão
