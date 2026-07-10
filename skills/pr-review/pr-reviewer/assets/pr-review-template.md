# Resumo Geral
- Objetivo do PR:
- Escopo das mudanças:
- Tipo(s) principal(is) de mudança (`feat`, `fix`, `refactor`, etc.):

# Detalhamento Técnico
## Código-fonte
- Principais alterações:
- Pontos de atenção:

## SOLID e Extensibilidade
- SRP/OCP e demais princípios aplicáveis:
- Pontos de extensão e impacto em mudanças futuras:

## Code Smells
- Duplicação (DRY), acoplamento e complexidade:
- Débito técnico relevante identificado:

## Project Rules (`AGENTS.md`)
- Regras aplicáveis aos arquivos alterados:
- Conformidades e desvios observados:

## Infra/Config
- Alterações de dependências, ambiente ou CI/CD:
- Riscos identificados:

## Documentação
- Atualizações realizadas:
- Lacunas identificadas:

## Testes
- Testes adicionados/alterados:
- Cobertura de cenários críticos (caminho feliz, erro esperado e borda crítica):

# Impactos e Compatibilidade
- Impacto no comportamento existente:
- Compatibilidade reversa:
- Contratos externos e versionamento (API/eventos/esquemas):
- Migrações necessárias (dados/API/env), se houver:
- Riscos e mitigação:

# Segurança de Release
- Feature flag necessária?:
- Estratégia de rollout:
- Estratégia de rollback:

# Concorrência e Consistência
- Riscos de race condition/idempotência:
- Estratégia transacional/consistência:

# Privacidade e Compliance
- Dados sensíveis/PII impactados:
- Mascaramento em logs e exposição indevida:

# Contexto e Motivações
- Problema/objetivo do PR:
- Issue/referência relacionada:

# Itens de Verificação
- Lógica de negócio e casos de borda: `✅` | `⚠️` | `❌`
- SOLID e extensibilidade: `✅` | `⚠️` | `❌`
- Code Smells e débito técnico: `✅` | `⚠️` | `❌`
- Project Rules (`AGENTS.md`): `✅` | `⚠️` | `❌`
- Arquitetura, padrões e segurança: `✅` | `⚠️` | `❌`
- Testes e performance: `✅` | `⚠️` | `❌`
- Contratos externos e compatibilidade: `✅` | `⚠️` | `❌`
- Release safety (rollout/rollback): `✅` | `⚠️` | `❌`
- Privacidade e compliance de dados: `✅` | `⚠️` | `❌`
- Clareza e coesão das mudanças: `✅` | `⚠️` | `❌`
- Tratamento de erros e logs: `✅` | `⚠️` | `❌`
- Código morto e duplicação: `✅` | `⚠️` | `❌`

# Critérios de Severidade
- `bloqueante`: quebra de contrato sem compatibilidade, falha de segurança crítica, regressão crítica sem mitigação ou migração irreversível sem rollback.
- `alto`: risco relevante com mitigação parcial.
- `médio`: risco moderado, sem impacto crítico imediato.
- `baixo`: melhoria recomendável sem risco relevante.

# Achados
| Severidade | Arquivo | Evidência | Risco |
| --- | --- | --- | --- |
| `bloqueante|alto|médio|baixo` | `path/relativo` | descrição objetiva do trecho/problema | regressão, segurança, performance, manutenção ou compatibilidade |

# Arquivos Modificados
| Arquivo | Descrição breve da mudança |
| --- | --- |
| `path/arquivo` | descrição objetiva |

# Ações Recomendadas
- Corrigir...
- Adicionar teste para...
- Ajustar validação de...

# Decisão Final
- Status: `aprovar` | `aprovar com ressalvas` | `solicitar mudanças`
- Justificativa objetiva:

# Autor e Data
- **Autor:** <nome do usuário git>
- **Data:** <YYYY-MM-DD>
