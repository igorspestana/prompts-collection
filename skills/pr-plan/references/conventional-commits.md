# Conventional Commits

Use Conventional Commits rigorosamente ao sugerir commits.

## Regras
- Cada commit deve ser atômico e coeso.
- Use o formato `<type>(optional scope): short imperative description`.
- A descrição deve estar no imperativo.
- A mensagem deve ser curta, específica e em inglês.
- Evite misturar responsabilidades no mesmo commit.

## Tipos mais comuns
- `feat`
- `fix`
- `chore`
- `docs`
- `style`
- `refactor`
- `test`
- `perf`
- `ci`

## Exemplos
- `feat(auth): add JWT expiration validation`
- `fix(api): prevent crash on null user email`
- `refactor(order): simplify discount calculation`
- `test(ui): cover dashboard empty state`
