---
name: pr-review-frontend
description: Revisa PRs com foco em frontend usando a checklist review-frontend.txt e o `gh` para entender o PR a partir do identificador, URL ou branch. Use quando o usuário pedir review de PR frontend, revisão técnica orientada por checklist de UI/UX, ou validação de riscos de acessibilidade, responsividade, performance, segurança e consistência visual com contexto extraído do GitHub.
---

# PR Review Frontend Checklist

## Objetivo
Executar um review técnico estruturado para mudanças de frontend usando `references/review-frontend.txt` como checklist base, ancorando a análise no valor de `Entenda o objetivo do PR:` e no contexto obtido via `gh pr view`.

## Entrada
- `entenda_o_objetivo_do_pr` (obrigatório; deve ser número ou URL do PR)

## Workflow
1. Ler `entenda_o_objetivo_do_pr` e validar se é número ou URL de PR; se for branch ou outro formato, retornar erro pedindo número/URL.
2. Antes de qualquer outra análise, executar `gh pr view <identificador> --comments --json title,body,files,author,baseRefName,headRefName,labels,reviewRequests,reviews` para obter contexto do PR.
3. Se tiver problema no sandbox e o `gh` falhar por acesso à API, então repita fora do sandbox para obter o contexto do PR antes de revisar o diff.
4. Se o `gh` retornar erro de autenticação ou problema no sandbox eleve o provilegio, interromper imediatamente e informar apenas que o `gh` não está autenticado.
5. Se a consulta ao `gh` falhar por outro motivo, interromper a análise e informar o motivo; não inferir o objetivo do PR sem esse passo.
6. Salvar um resumo enxuto do PR extraído do `gh` em `agent-artifacts/pr-review-frontend/<identificador-sanitizado>/gh-pr-summary.md`.
7. Resumir a intenção do PR em uma frase usando o material do GitHub.
8. Ler `references/review-frontend.txt` e aplicar os itens relevantes ao contexto.
9. Se houver `diff`, priorizá-lo acima de qualquer resumo ou contexto auxiliar.
10. Verificar o fluxo do usuário, estados vazios, loading, erro e sucesso, além de acessibilidade, responsividade, performance, segurança no frontend, compatibilidade e consistência visual.
11. Se houver `AGENTS.md` aplicável, validá-lo para os arquivos alterados.
12. Classificar achados por severidade e registrar evidência objetiva.
13. Se o contexto for insuficiente, declarar a limitação e evitar conclusões não suportadas.
14. Produzir review em PT-BR.

## Regras
- Use `references/review-frontend.txt` como checklist canônica.
- Use `gh pr view` como fonte primária de contexto do PR.
- Não aceitar branch como identificador de PR.
- Não inventar detalhes não observáveis.
- Persistir sempre um resumo do PR no caminho padrão definido.
- Priorizar riscos de UI, regressões de UX, acessibilidade, responsividade, performance, compatibilidade e falhas de cobertura.
- Se não houver `diff` suficiente, deixar explícito que a revisão é parcial.
- Registrar caminhos relativos quando citar arquivos.
- Manter linguagem direta, objetiva e técnica.

## Template do Resumo do GH
Preencher `agent-artifacts/pr-review-frontend/<identificador-sanitizado>/gh-pr-summary.md` com:

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
