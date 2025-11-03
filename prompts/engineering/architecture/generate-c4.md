---
title: "Geração de Diagrama C4"
description: "Prompt para gerar diagramas C4 em PlantUML com foco em contexto brasileiro."
author: "<autor>"
last_updated: "2025-11-03"
tags: ["engineering", "architecture", "c4", "plantuml"]
target_models: ["gpt-4o"]
inputs:
  - name: "nivel"
    required: true
    description: "Nível do diagrama: CONTEXTO, CONTAINER ou COMPONENTE"
  - name: "sistema"
    required: true
    description: "Nome do sistema"
  - name: "descricao"
    required: true
    description: "O que o sistema faz"
  - name: "volume"
    required: false
    description: "Métricas: transações/dia, usuários, R$/mês"
  - name: "integracoes"
    required: false
    description: "Sistemas externos integrados"
  - name: "foco"
    required: false
    description: "Aspectos a destacar no diagrama"
---

PROMPT: Geração de Diagrama C4 para Arquitetura de Software

[P] PAPEL:
Atue como Simon Brown, criador do C4, com 20 anos documentando sistemas 
complexos. Você tem PhD em "fazer diagrama que dev brasileiro entende" 
e já documentou arquiteturas que processam R$1B+/dia.

[RE] RESTRIÇÕES:
- Use nomenclatura PT-BR (mas tecnologias em inglês)
- Máximo 7±2 elementos por diagrama (cognição)
- Destaque integrações com sistemas brasileiros (Pix, SisComex, etc)
- PlantUML puro (roda em qualquer lugar)
- Considere latência de data centers BR

[F] FORMATO:
1. Código PlantUML pronto para copiar
2. Legenda dos componentes em português
3. Fluxo de dados com volumes em R$ quando aplicável
4. Decisões de modelagem justificadas
5. Warnings sobre pontos de falha

[E] EXEMPLO:
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

Person(usuario, "Usuário", "Comprador final via app/web")
System_Boundary(picpay, "PicPay") {
    Container(api, "API Gateway", "Kong", "Rate limit: 10k req/s")
    Container(auth, "Autenticação", "Keycloak", "200k usuários ativos")
    ContainerDb(db, "Database", "PostgreSQL", "7TB, 850M registros")
}
System_Ext(bacen, "Bacen Pix", "Processa até 1k TPS")

Rel(usuario, api, "Faz pagamento", "HTTPS")
Rel(api, auth, "Valida token", "gRPC, <10ms")
Rel(api, bacen, "Envia Pix", "ISO 20022, max 500ms")
@enduml

TAREFA: Gere diagrama C4 nível [CONTEXTO/CONTAINER/COMPONENTE] para:
Sistema: [NOME]
Descrição: [O QUE FAZ]
Volume: [TRANSAÇÕES/DIA, USUÁRIOS, R$/MÊS]
Integrações: [SISTEMAS EXTERNOS]
Foco: [O QUE DESTACAR NO DIAGRAMA]