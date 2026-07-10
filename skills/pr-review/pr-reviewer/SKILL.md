---
name: pr-reviewer
description: Revisa tecnicamente um pull request com base no diff entre branches e gera relatório estruturado de qualidade, riscos e recomendações. Use quando o usuário pedir code review pré-merge, validação técnica de PR, análise de segurança/performance/testes, ou checklist de aprovação.
---

# PR Reviewer

## Objetivo
Executar revisão técnica abrangente de PR sem alterar o codebase.

## Entradas
- `branch_base` (obrigatório; se ausente, assumir `main`)
- `branch_alvo` (opcional, padrão: HEAD atual)
- `contexto` (opcional)
- `arquivo_analise` (opcional, recomendado)
- `arquivo_saida` (opcional)

## Precedência de contexto
- Priorizar sempre: `diff` > `arquivo_analise` > `contexto`.
- Se houver conflito entre `arquivo_analise` e `diff`, registrar a discrepância e seguir o `diff`.

## Coleta de dados (comandos)
```bash
git fetch origin <branch_base>
git diff --stat <ref_base>...<branch_alvo_ou_HEAD>
git diff <ref_base>...<branch_alvo_ou_HEAD>
```

Onde `<ref_base>` deve ser:
- `origin/<branch_base>` quando existir remoto `origin` e a referência remota estiver disponível.
- `<branch_base>` como fallback quando `origin` não existir ou `fetch` falhar.

## Workflow
1. Validar entradas e definir branch alvo.
2. Sanitizar nome da branch (`/` -> `-`) para caminhos de saída.
3. Definir saída padrão quando ausente: `docs/pr/<branch-sanitizada>/pr-review.md`.
4. Definir `ref_base` (`origin/<branch_base>` ou fallback local `<branch_base>`).
5. Executar `git fetch` da branch base quando `origin` existir.
6. Obter visão geral com `git diff --stat <ref_base>...<branch_alvo_ou_HEAD>`.
7. Obter diff completo com `git diff <ref_base>...<branch_alvo_ou_HEAD>`.
8. Se `arquivo_analise` existir, usar apenas como contexto complementar.
9. Avaliar lógica, arquitetura, segurança, testes, performance, clareza e compatibilidade.
9.1. Aplicar critérios de análise orientados por princípios de design e qualidade:
   - OCP (Open/Closed Principle): se uma nova feature recorrente exige modificar módulo estável sem ponto de extensão claro, marcar indício de violação.
   - SRP (Single Responsibility Principle): validar se a classe/módulo possui apenas uma razão principal para mudar.
   - DRY (Don't Repeat Yourself): identificar blocos repetidos com pequenas variações.
   - Qualidade de código: verificar se nomes (classes, métodos, variáveis) revelam intenção.
   - Project Rules: validar conformidade com seções aplicáveis de `AGENTS.md` para cada arquivo alterado.
   - Segurança: validar entrada/saída (validação e sanitização) e exposição de segredos/dados sensíveis.
   - Testes: avaliar cobertura real dos comportamentos alterados (não apenas execução de linhas).
10. Avaliar segurança de release (feature flag, rollout e rollback) quando aplicável.
11. Avaliar contratos externos (API/eventos/esquemas compartilhados) e versionamento.
12. Avaliar riscos de concorrência/consistência (idempotência, race condition, transações), quando aplicável.
13. Avaliar privacidade/compliance de dados (PII, mascaramento em logs, exposição indevida), quando aplicável.
14. Classificar decisão final: `aprovar`, `aprovar com ressalvas` ou `solicitar mudanças`.
15. Produzir relatório em PT-BR usando o template em `assets/pr-review-template.md`.
16. Salvar no arquivo de saída.

## Formato do Relatório
- Seguir obrigatoriamente a estrutura de `assets/pr-review-template.md`.
- Para cada achado técnico, incluir:
  - classificação de severidade: `bloqueante`, `alto`, `médio` ou `baixo`;
  - evidência com caminho relativo do arquivo afetado;
  - risco objetivo (regressão, segurança, performance, manutenção, compatibilidade).
- Em "Critérios de Severidade", justificar os achados `bloqueante`.
- Em "Itens de Verificação", manter status com `✅`, `⚠️`, `❌`.
- Em "Ações Recomendadas", usar frases curtas no imperativo.
- Incluir seções ou subseções dedicadas a:
  - **Violações SOLID**: SRP (Single Responsibility Principle), OCP (Open/Closed Principle) e demais princípios aplicáveis.
  - **Code Smells**: DRY (Don't Repeat Yourself), acoplamento excessivo e demais indicadores de débito técnico.
  - **Extensibilidade**: pontos de extensão, facilidade de evolução e impacto em mudanças futuras.
- Garantir cobertura explícita de: Lógica, SOLID, Project Rules (`AGENTS.md`), Segurança e Testes.

## Regras
- Priorizar análise do diff sobre qualquer documento auxiliar.
- Usar Conventional Commits para classificar tipos de mudança.
- Focar em riscos, regressões e cobertura de cenários críticos.
- Tratar como `bloqueante` quando houver:
  - quebra confirmada de contrato externo sem estratégia de compatibilidade;
  - falha de segurança com impacto direto (autorização, vazamento de segredo ou exposição indevida de dados sensíveis);
  - regressão funcional crítica sem mitigação;
  - migração destrutiva/irreversível sem rollback viável.
- Para testes, cobrar cobertura mínima dos cenários alterados: caminho feliz, erro esperado e caso de borda crítico.
- Nos critérios OCP/SRP/DRY, evitar julgamento absoluto: registrar hipótese, evidência e impacto observado no diff.
- Se tocar rota hot path, query crítica ou processamento em lote relevante, exigir evidência objetiva de impacto de performance.
- Registrar limitações quando o diff estiver incompleto.
- Usar exclusivamente caminhos relativos do repositório no relatório final.

## Ambiguidade e Suposições
- Sem contexto de negócio, revisar exclusivamente com base no diff e padrões do projeto.
- Com diff parcial/truncado, explicitar limitação e fazer análise de melhor esforço.
- Quando compatibilidade reversa não puder ser confirmada, declarar a incerteza explicitamente.
- Se padrão arquitetural não estiver claro, documentar hipótese e evidência observável.

## Restrições

- Preserve o código existente.
- Entregue análise e orientação conceitual, sem alterações prontas.
- Mantenha upgrades e migrações fora do escopo.
- Baseie achados de segurança em evidências verificáveis.
- Use linguagem precisa e objetiva.
- Estruture a resposta sem incluir prazos ou estimativas.
- Aplicar as instruções do AGENTS.md quando o diff tocar arquivos cobertos.

## Tratamento de Erro
Quando a revisão falhar, retornar:

```text
Status: ERRO

Motivo: <explicação objetiva>

Próximos Passos Sugeridos:
* Verificar repositório git
* Confirmar branch base e branch alvo
* Garantir acesso de leitura
* Fornecer diff manual, se necessário
* Informar contexto do PR para priorização
```
