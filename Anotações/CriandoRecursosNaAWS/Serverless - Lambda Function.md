# Serverless - Lambda Function

Estudo em: October 15, 2025

Apesar do nome "Serverless" (sem servidor), os servidores ainda existem. A grande diferença é que **você não é o responsável por eles**. O provedor de nuvem (como a AWS) cuida de toda a infraestrutura, e você se preocupa apenas em escrever e enviar seu código.

**AWS Lambda** é o serviço da Amazon que permite que você faça exatamente isso.

### Analogia: Cozinhar em Casa vs. Pedir Comida

- **Modelo Tradicional (com servidores):** É como ter sua própria cozinha. Você precisa comprar os ingredientes (servidores), o fogão (sistema operacional), manter o gás (rede, energia) e limpar tudo depois (manutenção, patches de segurança). Se você for receber 50 pessoas, precisa garantir que sua cozinha aguenta o tranco.
- **Modelo Serverless (com Lambda):** É como pedir comida por um aplicativo. Você só escolhe o prato que quer (seu código/função) e diz quando quer comer (o evento/trigger). O restaurante (AWS) cuida de tudo: prepara, cozinha, entrega e limpa. Se você fizer 1 pedido ou 50 pedidos ao mesmo tempo, o restaurante simplesmente escala a produção para te atender. Você paga apenas pelos pratos que pediu.

## Como o AWS Lambda Funciona

O processo é bem simples:

1. **Você escreve o código:** Você cria uma pequena porção de código que realiza uma tarefa específica. Isso é a sua **"Função Lambda"**. Pode ser em Python, Node.js, Java, etc.
2. **Você faz o upload:** Você envia sua função para o serviço AWS Lambda.
3. **Você configura um "gatilho" (Trigger):** Você define *o que* fará sua função ser executada. Isso é um **evento**.
4. **A mágica acontece:** Quando o evento ocorre, a AWS automaticamente encontra um servidor, executa seu código, e depois descarta o ambiente.

**Exemplo clássico:**

- **Evento:** Um usuário faz upload de uma imagem para um bucket S3.
- **Função Lambda:** Seu código é acionado, pega essa imagem, redimensiona para um tamanho de thumbnail e a salva em outro bucket.
- **Resultado:** Tudo acontece automaticamente, sem que você precise de um servidor ligado 24/7 esperando por novos uploads.

## Vantagens do Serverless (Lambda)

- **Zero Gerenciamento de Servidores:** Você nunca precisa se preocupar com sistema operacional, atualizações de segurança, patches ou qualquer outra coisa relacionada à infraestrutura.
- **Custo-Benefício (Pay-per-use):** Este é um dos maiores atrativos. Você paga **apenas** pelo tempo em que seu código está realmente executando, medido em milissegundos. Se sua função não for chamada, você não paga nada. Adeus, servidores ociosos!
- **Escalabilidade Automática:** Se 10 pessoas fazem upload de uma foto ao mesmo tempo, a AWS executa sua função 10 vezes em paralelo. Se 10.000 pessoas fazem o upload, ela executa 10.000 vezes. Você não precisa configurar nada para isso acontecer.
- **Foco no Código:** Sua equipe de desenvolvimento pode se concentrar em criar funcionalidades que agregam valor ao negócio, em vez de gastar tempo gerenciando a infraestrutura.

## Desvantagens e Pontos de Atenção

- **Cold Start:** Se sua função não é chamada há algum tempo, ela pode estar "fria". A primeira vez que ela for acionada, a AWS precisa preparar o ambiente, o que pode adicionar uma pequena latência (atraso) na primeira execução.
- **Limites de Tempo:** As funções Lambda têm um tempo máximo de execução (atualmente 15 minutos). Elas não são ideais para processos extremamente longos e ininterruptos.
- **Stateless (Sem estado):** Cada execução de uma função é independente. Ela não "lembra" de nada da execução anterior. Se você precisa guardar informações (estado), deve usar um serviço externo, como um banco de dados.

| Serviços AWS que são Serveless |  |
| --- | --- |
| Lambda Functions |  |
| Dynamo DB | Banco de dados NoSQL |
| AWS Cognito | Autenticação |
| AWS API Gateway | Proteger chamadas de API |
| Amazon S3 |  |
| Amazon SNS e SQS | Gerenciamento de notificações e filas, respectivamente |
| AWS Kinesis | Logs |
| AWS Aurora Serveless | Banco de dados |

# Diferença entre EC2 X Lambda Function

| EC2 | Lambda Function |
| --- | --- |
| Servidor virtualizado | Sem servidor para gerenciar |
| Limitado por RAM e CPU | Limite de tempo -  máximo de 15 min por requisição |
| Servidor ligado 24 horas | Executa somente quando requisitado |
| Escalonamento manual / gerenciado | Escalonamento automático  |

### Benefícios AWS Lambda

- Cobrado por requisição
- Free Tier 1.000.000 requisições
- Integração com vários serviços AWS
- Integração com várias linguagens
- $0.20 por 1 milhão de requisições
- Depois $0.02 por requisição