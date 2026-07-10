# Classificação de tamanho por linhas

Classifique cada PR pela soma de inserções e deleções do diff `base...head`.

| Classe | Intervalo de linhas |
| --- | --- |
| `PP` | `0` a `50` |
| `P` | `51` a `200` |
| `M` | `201` a `500` |
| `G` | `501` a `1000` |
| `GG` | `1001+` |

## Diretrizes

- Use a classificação para decidir reviewabilidade, não para desmontar fluxos que precisam permanecer juntos.
- `PP` e `P` são PRs de baixo custo de review. Nem todo split precisa chegar neles.
- `M` é o melhor equilíbrio entre contexto funcional e reviewabilidade. É o tamanho máximo preferencial.
- `G` é sinal de alerta: avalie obrigatoriamente se uma subdivisão é viável. Se não for possível dividir, apresente justificativa técnica explícita explicando por que a divisão aumentaria risco, quebraria coesão funcional ou tornaria o review sem contexto suficiente.
- `GG` é exceção absoluta: exige justificativa ainda mais robusta e avaliação de subdivisão adicional antes de aceitar.
- Quando o usuário não informar a quantidade de PRs, use:
  - `minimo_sem_gg = ceil(total_linhas / 1000)`
  - `alvo_preferido = ceil(total_linhas / 500)`
- Use `minimo_sem_gg` como piso pragmático e `alvo_preferido` como alvo ideal, ajustando conforme responsabilidades funcionais e custo operacional do split.
