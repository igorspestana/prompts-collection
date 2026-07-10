# Prompts Collection

Repositório para reunir prompts e agent skills curados e reutilizáveis para diversos usos (engenharia de software, produto, design, dados, marketing, escrita, etc.). O objetivo é padronizar, documentar e facilitar a descoberta e evolução desses artefatos.

## Objetivos
- Manter prompts e skills úteis organizados por contexto e finalidade
- Padronizar estrutura, nomenclatura e metadados
- Facilitar contribuição e revisão
- Promover reuso e versionamento evolutivo

## Estrutura sugerida
```
./
├─ README.md
├─ prompts/
│  ├─ engineering/
│  │  ├─ architecture/
│  │  ├─ code-review/
│  │  ├─ refactoring/
│  │  └─ debugging/
│  ├─ product/
│  ├─ design/
│  ├─ data-ml/
│  ├─ marketing-seo/
│  └─ writing/
├─ skills/
└─ templates/
   └─ prompt-template.md         # Modelo para novos prompts
```

- Coloque novos prompts dentro de `prompts/<categoria>/`.
- Coloque novas skills dentro de `skills/<nome-da-skill>/` (ou em um grupo, como `skills/pr-review/`).
- Use nomes de arquivo e pastas descritivos em `kebab-case` (ex.: `feature-spec-outline.md`, `pr-description/`).

## Recomendações para organização em projetos

- Prefira versionar prompts próximos ao código do sistema que os utiliza. Recomenda-se colocar em `docs/prompt` dentro do repositório da aplicação.
- Em monorepos, utilize caminhos coesos por app ou pacote, como `apps/<app>/docs/prompt` ou `packages/<pkg>/docs/prompt`.

Exemplo de estrutura em um projeto de aplicação:
```
my-app/
├─ docs/
│  └─ prompt/
│     ├─ architecture/
│     │  └─ generate-c4.mdc
│     └─ product/
└─ src/
```

## Skills

Agent skills em `skills/` para fluxos de PR, review e handoff técnico. Cada skill vive em uma pasta com `SKILL.md` (e, quando necessário, `agents/`, `assets/`, `references/` e `scripts/`).

| Skill | Caminho | Uso |
| --- | --- | --- |
| PR Description | `skills/pr-description/` | Gera descrição técnica da branch (problema, solução, testes, resultados) |
| PR Plan | `skills/pr-plan/` | Planeja divisão de feature/tarefa em PRs pequenos antes de implementar |
| Branch Analyzer | `skills/pr-review/branch-analyzer/` | Documenta mudanças da branch em relação à base |
| PR Reviewer | `skills/pr-review/pr-reviewer/` | Review técnico pré-merge com riscos e recomendações |
| PR Review Orchestrator | `skills/pr-review/pr-review-orchestrator/` | Orquestra branch-analyzer + pr-reviewer ponta a ponta |
| PR Review Backend | `skills/pr-review-backend/` | Review de PR backend com checklist e contexto via `gh` |
| PR Review Frontend | `skills/pr-review-frontend/` | Review de PR frontend (UI/UX, a11y, responsividade) |
| PR Splitter | `skills/pr-splitter/` | Divide branch grande já implementada em PRs menores |
| Review Reply Comments | `skills/review-reply-comments/` | Rascunhos de comentários inline (Conventional Comments) |

Para usar: abra o `SKILL.md` da skill desejada (ou aponte o agente para ela) e siga as entradas e o workflow descritos.

## Como usar
### Prompts
1. Navegue pelas categorias em `prompts/`.
2. Abra o arquivo `.md` do prompt desejado.
3. Copie e adapte conforme o seu contexto (edite as variáveis entre `< >` ou blocos YAML).

### Skills
1. Navegue por `skills/`.
2. Abra o `SKILL.md` da skill desejada.
3. Informe as entradas pedidas (branch, PR, contexto) e execute o workflow.

## Metadados (Frontmatter)
Inclua metadados para facilitar busca e manutenção.

```yaml
---
title: "<título curto e claro>"
description: "<o que o prompt faz e quando usar>"
author: "<nome ou @handle>"
last_updated: "YYYY-MM-DD"
tags: ["categoria", "subcategoria", "ferramenta"]
target_models: ["gpt-4o", "gpt-4.1", "claude-3.5", "local-llm"]
inputs:
  - name: "<variável>"
    required: true
    description: "<o que preencher>"
---
```

### Por que usar Frontmatter
- Facilita descoberta e filtragem: metadados estruturados permitem busca por `tags`, autores, modelos-alvo e datas.
- Padroniza manutenção: campos explícitos reduzem ambiguidade e facilitam revisão.
- Melhora versionamento: mudanças de propósito e escopo ficam visíveis nos metadados.
- Habilita automação: ferramentas podem indexar, validar e gerar catálogos a partir do YAML.
- Consistência entre prompts: mesma interface (inputs) e documentação mínima garantidas.

### Uso no Cursor (.mdc)
- Para uso no Cursor, prefira a extensão `.mdc` para prompts. Essa extensão habilita o parsing adequado de Frontmatter e recursos específicos do editor (como blocos e anotações de prompt), evitando que o Frontmatter seja tratado como conteúdo comum.
- Na prática, `.mdc` melhora a compatibilidade com agentes e templates do Cursor, preservando metadados, seções de instruções e blocos de código sem conflitos.

## Template para novos prompts
Use o modelo abaixo ao criar um novo arquivo em `prompts/<categoria>/`.

```markdown
---
title: "<título do prompt>"
description: "<contexto e objetivo>"
author: "<autor>"
last_updated: "YYYY-MM-DD"
tags: ["<tag1>", "<tag2>"]
target_models: ["gpt-4o"]
inputs:
  - name: "<input1>"
    required: true
    description: "<descrição>"
---

## Contexto
Explique brevemente o cenário, limitações e suposições.

## Instruções ao modelo
- Seja explícito sobre o papel da IA
- Defina formato de saída (ex.: JSON, Markdown)
- Liste restrições (tom, idioma, limites)

## Prompt
Coloque aqui o corpo do prompt com variáveis entre `< >`.

## Exemplos (opcional)
- Entrada ➜ Saída esperada

## Checklist de qualidade
- [ ] Variáveis claras
- [ ] Metadados preenchidos
- [ ] Exemplo testado
- [ ] Linguagem consistente
```

## Convenções
- Idioma dos arquivos: Português, a menos que o prompt seja para outro idioma.
- Nomes de arquivo: `kebab-case`, curtos e descritivos.
- Preferir instruções explícitas e testáveis (formato de saída, critérios de aceitação).
- Evitar prompts excessivamente genéricos; contextualize.

## Versionamento e commits
Siga rigorosamente Conventional Commits (mensagens em inglês):
- `feat(scope): add <short change>`
- `fix(scope): fix <short change>`
- `docs(scope): update <short change>`
- `refactor(scope): refactor <short change>`
- `chore(scope): update <short change>`

Regras:
- Um commit por mudança atômica
- Descrição no imperativo, até 50 caracteres, sem ponto final
- Escopo opcional e coeso com os arquivos alterados

## Contribuição
- Abra uma Issue descrevendo o problema/necessidade
- Proponha PRs pequenos e coesos
- Adicione/atualize metadados, exemplos e checklist
- Evite incluir mudanças não relacionadas no mesmo PR

## Qualidade e revisão
- Teste o prompt em pelo menos um modelo alvo
- Verifique clareza, neutralidade e ausência de viés
- Documente limitações conhecidas

## Licença
MIT

---

Sugestões de melhoria são bem-vindas! Abra uma Issue para discutirmos.
