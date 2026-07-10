---
name: review-reply-comments
description: Gera rascunhos de comentários inline para achados de code review usando Conventional Comments, com o tom mais amigável possível, sempre propositivo e aberto à conversa. Use quando o usuário quiser transformar achados de PR em comentários não publicados, cada um com tag apropriada, texto colaborativo, formulações que convidem à participação do autor e indicação explícita de arquivo e linha.
---

# Review Reply Comments

## Objetivo
Transformar achados de review em rascunhos de comentários inline claros e colaborativos, prontos para copiar para um PR ou ferramenta de review, sem publicar nada automaticamente.

Leia `references/conventional-comments.md` antes de redigir os comentários.

## Quando usar
Use esta skill quando o usuário:
- pedir para converter achados de review em comentários de resposta;
- quiser manter um tom amigável, sugestivo e objetivo;
- precisar indicar em qual arquivo e linha cada comentário deve ser inserido;
- quiser aplicar Conventional Comments de forma consistente;
- não quiser publicar os comentários, apenas gerar rascunhos.

Não use esta skill para publicar comentários em GitHub, GitLab ou qualquer outra ferramenta. A saída desta skill é sempre um rascunho.

## Entrada esperada
Idealmente receba:
- uma lista de achados;
- o diff, patch, trecho de codigo, PR ou arquivos alterados;
- contexto suficiente para localizar cada achado em arquivo e linha.

Se o usuário não fornecer localização precisa, procure no diff ou no código local. Se ainda assim não for possível determinar uma linha defensável, deixe isso explícito e não invente numeração.

## Workflow
1. Ler todos os achados e o contexto técnico disponível.
2. Para cada achado, classificar a natureza do ponto: bug, segurança, regra de negócio, performance, dúvida, melhoria, typo, elogio ou detalhe pequeno.
3. Escolher a tag de Conventional Comments mais adequada usando `references/conventional-comments.md`.
4. Determinar o melhor ponto de inserção no código:
   - priorize a linha exata do problema;
   - se o comentário for sobre um bloco, indique a primeira linha relevante do bloco;
   - sempre informe `arquivo` e `linha`;
   - se a linha for aproximada, sinalize isso como `linha sugerida`.
5. Redigir um comentário por achado.
6. Não publicar nada. Entregar somente rascunhos.

## Regras de tom
- O padrão é o tom mais amigável possível, sempre propositivo, respeitoso e aberto à conversa.
- Quando houver oportunidade real, comece reconhecendo algo positivo no trecho, na intenção ou na direção da implementação. O elogio deve ser concreto e curto, nunca artificial.
- Frases como `talvez faça sentido...`, `o que você acha?` e `faz sentido para você?` deixam o comentário mais colaborativo porque comunicam que você está propondo uma conversa, não apenas impondo uma correção.
- Use essas frases sempre que ajudarem a convidar a participação do outro, inclusive em bugs, riscos e pontos obrigatórios, mas evite repetir a mesma formulação em comentários diferentes do mesmo review.
- Para dúvidas ou pontos negociáveis, prefira formulações como `Fiquei com uma dúvida sobre...`, `Me pareceu que...`, `Talvez faça sentido considerar...` e `O que você acha?`.
- Quando for bug, segurança, regra de negócio quebrada ou algo que precisa mudar, mantenha a gravidade explícita, mas ainda com linguagem amigável, propositiva e aberta à contrapartida.
- Em pontos obrigatórios, evite tom impositivo ou acusatório. Prefira formulações como `me parece que aqui temos um risco real...`, `acho que vale ajustar esse ponto porque...` e `faz sentido para você?`.
- Evite passivo-agressividade, ironia, excesso de contexto e comentários vagos.
- Convide a resposta do outro sempre que possível, mas sem transformar o comentário em pergunta vazia ou artificial.

## Variação de linguagem
- Não reutilize mecanicamente a mesma abertura, a mesma transição ou o mesmo fechamento em vários comentários do mesmo review.
- Antes de concluir, revise o conjunto inteiro e troque formulações repetidas por alternativas equivalentes.
- Se um comentário já usou `talvez faça sentido...`, prefira em outros itens alternativas como:
  - `pode valer a pena...`
  - `acho que vale considerar...`
  - `me parece uma boa oportunidade para...`
  - `talvez ajude...`
  - `talvez seja interessante...`
  - `uma possibilidade aqui seria...`
  - `dá para considerar...`
  - `pode fazer sentido avaliar...`
- Para abrir dúvidas ou observações, varie entre alternativas como:
  - `Fiquei com uma dúvida sobre...`
  - `Fiquei pensando se...`
  - `Me chamou atenção que...`
  - `Quis confirmar uma coisa aqui...`
  - `Não sei se estou vendo certo, mas...`
  - `Posso estar enganado, mas me parece que...`
  - `Queria entender melhor...`
  - `Me pareceu que...`
- Para convidar a contrapartida do autor, varie entre alternativas como:
  - `O que você acha?`
  - `Faz sentido para você?`
  - `Como você está vendo isso?`
  - `Queria ouvir sua leitura desse ponto.`
  - `Tem algum contexto aqui que eu possa não estar vendo?`
  - `Vê diferente por algum motivo?`
  - `Se eu estiver perdendo algum contexto, me avisa.`
  - `Curioso para entender sua leitura aqui.`
- Para reconhecer algo positivo sem soar artificial, varie entre alternativas como:
  - `Gostei da direção aqui.`
  - `Boa separação deste fluxo.`
  - `Achei boa a intenção desta mudança.`
  - `Está claro o objetivo deste trecho.`
  - `Gostei de como você isolou essa responsabilidade.`
  - `A estrutura aqui ficou fácil de acompanhar.`

## Regras de classificação
- Use `[suggestion]`, `[question]`, `[thought]`, `[minor]`, `[nit]` e `[praise]` para pontos negociáveis ou exploratórios.
- Use `[issue]`, `[bug]`, `[security]` e `[performance]` quando houver problema concreto ou risco técnico.
- Use `[todo]` apenas quando o próprio comentário for um lembrete explícito de trabalho pendente.
- Use `[typo]` apenas para erro textual ou de digitação.
- Em caso de dúvida entre duas tags, prefira a mais específica.

## Como escrever
Cada comentário deve:
- começar pela tag Conventional Comments;
- quando fizer sentido, abrir com um reconhecimento curto e específico antes do ponto principal;
- citar o problema ou oportunidade de forma objetiva;
- incluir contexto técnico mínimo suficiente para o autor entender o motivo;
- sugerir uma direção de ajuste de forma propositiva;
- manter abertura explícita para ouvir a contrapartida do autor;
- variar a linguagem entre comentários do mesmo review para evitar repetição mecânica;
- soar como comentário inline real de review.

## Formato de saída
Para cada achado, responda neste formato:

```md
### Achado <n>
- Arquivo: `caminho/relativo/do/arquivo.ext`
- Linha: `<numero>` ou `<numero aproximado>`
- Severidade: `<baixa|média|alta|crítica>`
- Tag: `[suggestion]`
- Motivo da localização: `<1 frase curta explicando por que essa linha é o melhor ponto>`
- Rascunho:
  `[suggestion] gostei da separação que você fez aqui. Fiquei com uma dúvida sobre manter essa validação duplicada nos dois fluxos; talvez faça sentido extrair isso para um helper compartilhado. O que você acha?`
```

Se o comentário apontar um problema obrigatório:

```md
### Achado <n>
- Arquivo: `caminho/relativo/do/arquivo.ext`
- Linha: `123`
- Severidade: `alta`
- Tag: `[bug]`
- Motivo da localização: `a falha acontece na condição que acessa o valor sem garantir presença`
- Rascunho:
  `[bug] gostei da direção do fluxo aqui. Me parece que neste ponto temos um risco real de acessar um valor ausente e quebrar quando a lista vier vazia; talvez faça sentido proteger esse caso antes de usar o primeiro elemento. Faz sentido para você ou tem algum contexto que eu não esteja vendo?`
```

## Validações obrigatórias
Antes de concluir, confira:
- existe exatamente um rascunho por achado;
- toda sugestão tem tag compatível com a severidade;
- comentários de dúvida ou negociação usam formulações como `Fiquei com uma dúvida...` quando isso soar natural;
- elogios, quando usados, são concretos e não decorativos;
- comentários mandatórios mantêm a gravidade explícita sem perder o tom amigável e participativo;
- comentários negociáveis não ficaram impositivos;
- comentários obrigatórios também convidam à contrapartida do autor quando isso não prejudicar a clareza;
- comentários diferentes não repetem a mesma abertura, o mesmo `talvez faça sentido...` ou o mesmo fechamento em sequência;
- cada item informa arquivo e linha;
- nada foi publicado.
