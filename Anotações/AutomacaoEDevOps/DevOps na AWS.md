# DevOps na AWS

Estudo em: November 2, 2025

### 1. Infraestrutura como Código (IaC)

Em vez de criar servidores manualmente, você escreve código para defini-los.

- **AWS CloudFormation:** O serviço principal para isso. Você escreve um "blueprint" (template YAML/JSON) e o CloudFormation constrói sua infraestrutura.
- **AWS CDK (Cloud Development Kit):** Uma forma mais avançada onde você usa linguagens como Python ou TypeScript para definir sua infraestrutura.

### 2. CI/CD (Integração e Entrega Contínua)

O "motor" da automação. É o pipeline que leva o código do desenvolvedor até a produção de forma segura.

- **AWS CodePipeline:** O orquestrador. Ele desenha o fluxo: "Pegue o código -> Compile -> Teste -> Implante".
- **AWS CodeCommit:** Um repositório Git (como o GitHub, mas dentro da AWS).
- **AWS CodeBuild:** O serviço que compila seu código e executa os testes automatizados.
- **AWS CodeDeploy:** O serviço que implanta sua aplicação nos servidores (EC2), contêineres (ECS) ou Lambdas.

### 3. Monitoramento e Observabilidade (Feedback)

Você não pode melhorar o que não pode medir. DevOps depende de feedback rápido.

- **Amazon CloudWatch:** O "sistema nervoso". Coleta **Métricas** (CPU, Rede), **Logs** (para investigar erros) e permite criar **Alarmes** (para avisar se algo quebrar).
- **AWS CloudTrail:** O "sistema de segurança". Grava **quem** fez **o quê** na sua conta (auditoria).

### 4. Segurança e Governança

Automatizar a segurança é um pilar do DevOps (às vezes chamado de "DevSecOps").

- **AWS IAM (Identity and Access Management):** O "porteiro". Define quem (ou o quê) pode fazer o quê. O uso de **Roles (Funções)** é a prática DevOps fundamental para dar permissões seguras e temporárias para seus serviços (ex: para o CodeDeploy poder falar com o EC2).

### 5. Automação e Operações

Ferramentas para automatizar tarefas repetitivas.

- **AWS Lambda:** O "canivete suíço". Funções que rodam sob demanda para "colar" serviços. (Ex: "Quando o deploy terminar, avise no Slack").
- **AWS Systems Manager:** Para gerenciar e aplicar patches em centenas de servidores de uma só vez.

**Em resumo:** "DevOps na AWS" é usar esse ecossistema de serviços integrados (CloudFormation + CodePipeline + CloudWatch + IAM) para construir, testar e implantar software de forma rápida, automatizada e segura.