---
name: pr-description
description: Analisa mudanças de uma branch em relação à base e gera um documento técnico objetivo com descrição do problema, solução proposta, como testar e resultados. Use quando o usuário pedir material de contexto para PR, validação técnica rápida, ou handoff de implementação.
---

# PR Description

## Objetivo
Gerar um documento técnico curto e direto, focado em explicar o problema resolvido pela branch, a solução implementada, o plano de testes e os resultados observados.

## Entradas
- `branch_base` (obrigatório; se ausente, assumir `main`)
- `branch_alvo` (opcional, padrão: HEAD atual)
- `contexto` (opcional)
- `arquivo_saida` (opcional)

## Precedência de contexto
- Priorizar sempre: `diff` > `contexto`.
- Se o `contexto` divergir do `diff`, registrar a divergência e seguir o `diff`.

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
2. Obter branch atual com `git branch --show-current` quando `branch_alvo` não for informado.
3. Se `branch_alvo` continuar ausente (ex.: `HEAD` destacado), usar `HEAD` explicitamente.
4. Sanitizar nome da branch para path substituindo `/` por `-`.
5. Definir `ref_base` (`origin/<branch_base>` ou fallback local `<branch_base>`).
6. Definir arquivo de saída padrão quando não informado: `docs/pr/<branch-sanitizada>/pr-description.md`.
7. Coletar resumo do diff com `git diff --stat <ref_base>...<branch_alvo_ou_HEAD>`.
    - 7.1 Avaliar tamanho da mudança usando o diff summary:
        - Contar arquivos modificados.
        - Somar linhas adicionadas e removidas.
    - 7.2 Se qualquer uma das condições abaixo for verdadeira:
        - mais de 20 arquivos modificados
        - mais de 500 linhas adicionadas
        - mais de 300 linhas removidas

        - Então registrar no documento (na seção "Resultados observados") que o PR possui grande volume de mudanças e **recomendar avaliação para divisão em múltiplos PRs menores**, caso seja tecnicamente viável.
            - A recomendação deve:
                - ser objetiva
                - não bloquear o PR
                - não assumir que a divisão é obrigatória
                - indicar possíveis critérios de separação (ex.: refactor vs feature, backend vs testes, infra vs código).
8. Coletar diff completo com `git diff <ref_base>...<branch_alvo_ou_HEAD>`.
9. Inferir e descrever o problema com base em mudanças de código, testes, configuração e documentação.
10. Descrever solução proposta com foco em decisões técnicas e trade-offs visíveis no diff.
11. Montar seção de testes usando apenas evidências reais (testes adicionados/alterados, comandos e cobertura observável).
12. Consolidar resultados esperados/obtidos e riscos residuais.
13. Montar o conteúdo final usando `assets/pr-description-template.md`.
14. Salvar documento final em PT-BR no arquivo de saída.

## Formato do Documento
O documento deve seguir obrigatoriamente `assets/pr-description-template.md`.

## Regras
- Basear o conteúdo no diff e no contexto fornecido.
- Se o volume de mudanças ultrapassar os thresholds definidos, incluir recomendação de divisão do PR para facilitar revisão.
- A recomendação deve ser baseada exclusivamente no tamanho do diff.
- Reportar uso de APIs/métodos depreciados apenas quando houver evidência no diff ou em logs fornecidos.
- Declarar ausência de deprecações somente com evidência observável; quando não houver evidência suficiente, usar linguagem de melhor esforço.
- Em caso de conflito, priorizar o diff e explicitar a divergência.
- Evitar generalizações sem evidência técnica.
- Se houver lacunas, declarar explicitamente as incertezas.
- Manter texto objetivo, sem jargão desnecessário.
- Usar caminhos relativos ao citar arquivos.
- Manter a frase final com o link do Guia de revisão de código.

## Ambiguidade e Suposições
- Sem `contexto`, inferir problema e solução exclusivamente a partir do diff.
- Com diff parcial/truncado, explicitar limitação e produzir análise de melhor esforço.
- Se não houver evidência de execução de testes, declarar que os resultados são esperados e não observados.
- Se não houver evidência suficiente para avaliar deprecações, declarar explicitamente a limitação.
- Se não for possível confirmar impacto em compatibilidade, declarar incerteza explicitamente.

## Restrições
- Preservar o código sem alterações.
- Reportar apenas resultados de testes com evidência no diff.
- Inferir métricas somente quando houver evidência no diff.
- Limitar o documento às quatro seções exigidas pelo template.
- Usar exclusivamente caminhos relativos no documento final.

## Tratamento de Erro
Quando a geração do documento falhar, retornar:

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
