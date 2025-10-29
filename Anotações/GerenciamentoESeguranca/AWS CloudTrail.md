# AWS CloudTrail

Estudo em: October 29, 2025

AWS CloudTrail é um serviço da AWS que ajuda você na auditoria operacional e de risco, a governança e a conformidade da sua conta da AWS.

Toda ação realizada por um usuário, função ou serviço serão registradas como eventos em CloudTrail. Os eventos incluem ações realizadas no Console AWS, Command Line Interface e chamada de API.

### O que é uma "Chamada de API"?

Pense em uma "chamada de API" como **qualquer ação** que você ou um serviço realiza na sua conta.

- Clicar em "Ligar" uma instância EC2 no console? Isso é uma chamada de API (`ec2:RunInstances`).
- Salvar um arquivo no S3? Isso é uma chamada de API (`s3:PutObject`).
- Criar um novo usuário no IAM? Isso é uma chamada de API (`iam:CreateUser`).
- Até mesmo falhar ao tentar fazer login? Isso é um evento que o CloudTrail registra.

### As Perguntas que o CloudTrail Responde

O CloudTrail foi feito para responder a perguntas cruciais de segurança e auditoria, como:

- **QUEM?** (Qual usuário, qual role, qual serviço)
- **FEZ O QUÊ?** (Qual ação/chamada de API? Ex: `ec2:StopInstances`)
- **QUANDO?** (O timestamp exato)
- **EM QUAL RECURSO?** (Ex: na instância `i-12345abcdef`)
- **DE ONDE?** (De qual endereço de IP)

### Por que isso é TÃO Importante?

1.  🕵️ Segurança e Investigação (O Detetive)

Este é o uso mais famoso.

- **Cenário:** Um servidor de produção crítico (Instância EC2) foi desligado misteriosamente. Ninguém sabe quem foi.
- **Solução:** Você vai ao CloudTrail, filtra pela ação `ec2:StopInstances` e pelo ID da instância. Em segundos, você descobre: "Foi o usuário `joao.silva` que executou essa ação às 14:52, do IP `xxx.xxx.xxx.xxx`."
1. 🧾 Auditoria e Compliance (O Auditor)

Muitas indústrias (financeira, saúde) exigem que você *prove* que tem controle sobre seu ambiente.

- **Cenário:** Um auditor externo pergunta: "Me prove que ninguém alterou a política de segurança do seu bucket S3 que contém dados sensíveis nos últimos 6 meses."
- **Solução:** Você usa os logs do CloudTrail para gerar um relatório mostrando todas as ações `s3:PutBucketPolicy` naquele bucket (e, com sorte, mostrar que não houve nenhuma).
1. ⚙️ Solução de Problemas Operacionais

Às vezes, as coisas param de funcionar não por um bug, mas porque alguém *mudou* uma configuração.

- **Cenário:** Sua aplicação web parou de se conectar ao banco de dados.
- **Solução:** Você olha no CloudWatch e vê que as conexões estão falhando (o *sintoma*). Você olha no CloudTrail e vê que 1 minuto antes, "alguém" (uma pessoa ou um script) alterou a regra do Security Group (o *firewall*), bloqueando a porta do banco de dados (a *causa*).

### CloudWatch VS CloudTrail

- CloudWatch: gera análises, métricas e gráficos visuais.
- CloudTrail: ajuda na auditoria, pois ele registra o caminho, com ele conseguimos saber quem acessou determinado recurso, quais alterações foram feitas, dias e horários.