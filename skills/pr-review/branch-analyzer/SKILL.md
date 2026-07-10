---
name: branch-analyzer
description: Analisa tecnicamente mudanças de uma branch em relação à branch base e gera documentação estruturada em markdown. Use quando o usuário pedir mapeamento das mudanças, documentação pré-PR, contexto para code review, ou comparação de branch com main/develop.
---

# Branch Analyzer

## Objetivo
Gerar um relatório técnico completo das mudanças da branch sem modificar o codebase.

## Entradas
- `branch_base` (obrigatório; se ausente, assumir `main`)
- `branch_alvo` (opcional, padrão: HEAD atual)
- `contexto` (opcional)
- `arquivo_saida` (opcional)

## Coleta de dados (comandos)
```bash
git branch --show-current
git fetch origin <branch_base>
git diff --stat <ref_base>...<branch_alvo_ou_HEAD>
git diff <ref_base>...<branch_alvo_ou_HEAD>
```

Onde `<ref_base>` deve ser:
- `origin/<branch_base>` quando existir remoto `origin` e a referência remota estiver disponível.
- `<branch_base>` como fallback quando `origin` não existir ou `fetch` falhar.

## Workflow
1. Validar entradas e identificar `branch_alvo`.
2. Obter nome da branch atual com `git branch --show-current` quando necessário.
3. Sanitizar nome da branch para path: substituir `/` por `-`.
4. Definir saída padrão se `arquivo_saida` não for informado: `docs/pr/<branch-sanitizada>/branch-analysis.md`.
5. Definir `ref_base` (`origin/<branch_base>` ou fallback local `<branch_base>`).
6. Executar `git fetch` da branch base quando `origin` existir.
7. Gerar visão geral com `git diff --stat <ref_base>...<branch_alvo_ou_HEAD>`.
8. Gerar diff completo com `git diff <ref_base>...<branch_alvo_ou_HEAD>`.
9. Analisar código, infra/config, docs, testes, impactos e compatibilidade.
10. Inferir motivação quando não houver contexto (`feat`, `fix`, `refactor`, `chore/ci`, `perf`, `docs`).
11. Escrever relatório final em PT-BR usando `assets/branch-analysis-template.md`.
12. Salvar no arquivo de saída.

## Formato do Relatório
- Seguir obrigatoriamente a estrutura de `assets/branch-analysis-template.md`.
- Em "Contexto e Motivações":
  - se `contexto` existir, usar como base;
  - se ausente, inferir a partir do diff e registrar que é inferência.
- Em "Observações e Considerações", cobrir:
  - lógica e casos de borda;
  - arquitetura e padrões;
  - qualidade, testes, performance e manutenibilidade.
- Usar apenas caminhos relativos do repositório.

## Regras
- Basear análise apenas no diff e contexto fornecido.
- Priorizar mudanças significativas e riscos reais.
- Usar caminhos relativos na listagem de arquivos.
- Documentar incertezas quando o diff não permitir conclusão.
- Manter texto objetivo, sem jargão desnecessário.
- Seguir Conventional Commits para categorizar tipos de mudança.
- Manter máximo de 7±2 tópicos por seção.

## Ambiguidade e Suposições
- Se não houver contexto, inferir motivação pelo padrão de mudança no diff.
- Se o diff estiver parcial/truncado, explicitar limitação e analisar por melhor esforço.
- Se houver múltiplos tipos de mudança, documentar por categoria.
- Se compatibilidade reversa não puder ser comprovada, declarar incerteza explicitamente.
- Se padrão arquitetural não estiver claro, registrar hipótese com evidência observável.

## Restrições
- Manter-se em modo leitura; documentar sem alterar código.
- Documentar somente o estado observado; não prescrever upgrades ou migrações.
- Reportar vulnerabilidades apenas quando evidenciadas no diff.
- Usar linguagem objetiva e precisa.
- Focar em análise factual; não incluir estimativas de tempo.
- Basear-se exclusivamente no diff e nos fatos observáveis; não inferir contexto ausente.

## Tratamento de Erro
Quando a análise falhar, retornar:

```text
Status: ERRO

Motivo: <explicação objetiva>

Próximos Passos Sugeridos:
* Verificar repositório git
* Confirmar acesso à branch base
* Fornecer nomes de branch válidos
* Garantir permissões de leitura
* Informar contexto adicional, se necessário
```
