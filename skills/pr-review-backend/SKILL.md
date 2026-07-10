---
name: pr-review-backend
description: Revisa PRs usando a checklist de review.txt e o `gh` para entender o PR a partir do identificador, URL ou branch. Use quando o usuário pedir review de PR, revisão técnica orientada por checklist, ou validação de riscos, segurança, testes e arquitetura com contexto extraído do GitHub.
---

# PR Review Backend

## Objetivo
Executar um review técnico estruturado usando `references/review.txt` como checklist base, ancorando a análise no valor de `Entenda o objetivo do PR:` e no contexto obtido via `gh pr view`.

## Entrada
- `entenda_o_objetivo_do_pr` (obrigatório; deve ser número ou URL do PR)

## Workflow
1. Ler `entenda_o_objetivo_do_pr` e validar se é número ou URL de PR; se for branch ou outro formato, retornar erro pedindo número/URL.
2. Antes de qualquer outra análise, executar `gh pr view <identificador> --comments --json title,body,files,author,baseRefName,headRefName,labels,reviewRequests,reviews` para obter contexto do PR.
3. Se o `gh` retornar erro de autenticação, interromper imediatamente e informar apenas que o `gh` não está autenticado.
4. Se a consulta ao `gh` falhar por outro motivo, interromper a análise e informar o motivo; não inferir o objetivo do PR sem esse passo.
5. Salvar um resumo enxuto do PR extraído do `gh` em `agent-artifacts/pr-review-backend/<identificador-sanitizado>/gh-pr-summary.md`.
6. Resumir a intenção do PR em uma frase usando o material do GitHub.
7. Ler `references/review.txt` e aplicar os itens relevantes ao contexto.
8. Se houver `diff`, priorizá-lo acima de qualquer resumo ou contexto auxiliar.
9. Verificar objetivo, regras de negócio, lógica, edge cases, `null`/`Optional`, exceptions, arquitetura, performance, segurança, testes, compatibilidade, logs, DTOs, responsabilidades, duplicação, clareza e manutenção.
10. Se houver `AGENTS.md` aplicável, validá-lo para os arquivos alterados.
11. Classificar achados por severidade e registrar evidência objetiva.
12. Se o contexto for insuficiente, declarar a limitação e evitar conclusões não suportadas.
13. Produzir review em PT-BR.

## Regras
- Use `references/review.txt` como checklist canônica.
- Use `gh pr view` como fonte primária de contexto do PR.
- Não aceitar branch como identificador de PR.
- Não inventar detalhes não observáveis.
- Persistir sempre um resumo do PR no caminho padrão definido.
- Priorizar riscos, regressões e falhas de cobertura.
- Se não houver `diff` suficiente, deixar explícito que a revisão é parcial.
- Registrar caminhos relativos quando citar arquivos.
- Manter linguagem direta, objetiva e técnica.

## Template do Resumo do GH
Preencher `agent-artifacts/pr-review-backend/<identificador-sanitizado>/gh-pr-summary.md` com:

```md
# PR Summary
- Identificador: <numero-ou-url>
- Título: <title>
- Autor: <author>
- Base: <baseRefName>
- Head: <headRefName>
- Labels: <labels>
- Objetivo resumido: <1 frase objetiva>
- Arquivos alterados:
  - <path1>
  - <path2>
- Comentários e reviews relevantes:
  - <resumo curto>
```

## Saída esperada
- Resumo do objetivo do PR.
- Lista de achados ordenados por severidade.
- Itens validados sem problemas.
