# Recomendação Geral
- Artefato:
- Estratégia recomendada:
- Justificativa:
- Critério principal da decisão:

# Contexto Considerado
- Objetivo da mudança:
- Contexto técnico:
- Áreas afetadas:
- Restrições e preferências:
- Artefatos usados no planejamento:

# Suposições
- Suposições adotadas:
- Pontos em aberto:

# Integration Branch
- Necessária?: `sim` | `não`
- Nome sugerido:
- Papel da `integration branch`:
- Motivo para não ir direto para `main`, se aplicável:
- Convenção operacional do PR final (quando aplicável): título com prefixo `[integration]` e label `integration`

# Plano de Branches
| Ordem | Branch | Base | Objetivo |
| --- | --- | --- | --- |
| `1` | `nome-da-branch` | `main|integration-branch|outra` | objetivo curto |

# Plano de PRs
## PR 1
- Título sugerido:
- Branch de origem:
- Branch de destino:
- Labels esperadas:
- Objetivo:
- Escopo:
- Tamanho estimado: `PP` | `P` | `M` | `G` | `GG`
- Dependências:
- Risco:
- Motivo da ordem:
- Merge direto para `main`?: `sim` | `não` | `parcialmente`
- Compatibilidade temporária / feature flag / rollout:

Commits sugeridos:
- `type(scope): short description`

## PR N
- Título sugerido:
- Branch de origem:
- Branch de destino:
- Labels esperadas:
- Objetivo:
- Escopo:
- Tamanho estimado: `PP` | `P` | `M` | `G` | `GG`
- Dependências:
- Risco:
- Motivo da ordem:
- Merge direto para `main`?: `sim` | `não` | `parcialmente`
- Compatibilidade temporária / feature flag / rollout:

Commits sugeridos:
- `type(scope): short description`

# Riscos e Observações
- Riscos de integração:
- Riscos de conflito:
- Estratégia de reversão:
- Compatibilidade e transição:
- Oportunidades para simplificar ainda mais:

# Resumo Executivo
- Estratégia final:
- Quantidade sugerida de PRs:
- Melhor próximo passo para começar:
