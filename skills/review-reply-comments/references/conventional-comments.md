# Conventional Comments Reference

Use esta referência para escolher a tag e calibrar o tom do comentário.

## Tags

| Tag | Significado | Exemplo |
| --- | --- | --- |
| `[nit]` / `[nitpick]` | Detalhe pequeno, geralmente não bloqueante | `[nit] poderia quebrar essa linha para melhorar leitura` |
| `[minor]` | Ajuste pequeno, baixa severidade | `[minor] esse nome poderia ser mais específico` |
| `[suggestion]` | Sugestão de melhoria | `[suggestion] talvez extrair isso para uma função` |
| `[question]` | Dúvida real, não necessariamente pedido de mudança | `[question] esse caso pode chegar nulo?` |
| `[issue]` | Problema que provavelmente precisa ser corrigido | `[issue] aqui pode lançar NullPointerException` |
| `[bug]` | Bug identificado | `[bug] esse cálculo falha quando a lista está vazia` |
| `[security]` | Risco de segurança | `[security] validar melhor essa URL para evitar SSRF` |
| `[performance]` | Possível impacto de performance | `[performance] isso faz uma query por item da lista` |
| `[praise]` | Elogio / reforço positivo | `[praise] boa separação de responsabilidade aqui` |
| `[thought]` | Reflexão, ideia ou ponto para considerar | `[thought] no futuro talvez isso vire uma strategy` |
| `[todo]` | Algo a fazer, agora ou depois | `[todo] adicionar teste para esse cenário` |
| `[typo]` | Erro de escrita | `[typo] "recieve" -> "receive"` |

## Guia rápido de tom

- Tom base:
  tente ser o mais amigável possível sem perder objetividade técnica
- Sugestões negociáveis:
  use formulações como `Fiquei com uma dúvida sobre...`, `talvez faça sentido...`, `o que você acha?` e `faz sentido para você?`
- Variação:
  não repita mecanicamente a mesma fórmula em comentários diferentes; alterne aberturas, transições e fechamentos para manter o texto natural
- Dúvidas reais:
  prefira `[question]` com uma formulação como `Fiquei com uma dúvida sobre...` ancorada no comportamento observado
- Problemas obrigatórios:
  mantenha a gravidade explícita, mas ainda com linguagem amigável, propositiva e aberta à contrapartida; não esconda bug, risco de segurança ou quebra de regra de negócio, mas também não feche a conversa
- Elogios:
  quando possível, adicione um reconhecimento curto e concreto antes do ponto principal; use `[praise]` apenas quando o elogio for o próprio comentário, não como filler

## Mapeamento prático

- detalhe pequeno de estilo ou legibilidade: `[nit]` ou `[minor]`
- melhoria de design, clareza ou manutenção: `[suggestion]`
- dúvida autêntica sobre comportamento ou premissa: `[question]`
- falha concreta, regressão, quebra funcional: `[issue]` ou `[bug]`
- vulnerabilidade ou validação insuficiente: `[security]`
- custo desnecessário de CPU, memória, I/O ou query: `[performance]`
- reflexão arquitetural sem urgência: `[thought]`
- ação pendente explicitamente desejada: `[todo]`
- erro de escrita: `[typo]`
