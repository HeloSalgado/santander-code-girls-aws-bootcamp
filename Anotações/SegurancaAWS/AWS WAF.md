# AWS WAF

Estudo em: November 2, 2025

O **AWS WAF** é um serviço **gerenciado** que ajuda a proteger suas **aplicações web** (como sites, APIs e apps hospedados no AWS CloudFront, ALB, API Gateway ou AppSync) contra:

- **Injeções de SQL (SQL Injection)**
- **Cross-Site Scripting (XSS)**
- **Bots maliciosos**
- **Ataques DDoS de camada de aplicação (L7)**
- **Tráfego suspeito ou não autorizado**

### Como ele funciona?

Ele age como um **filtro inteligente** que fica entre o usuário e sua aplicação:

1. O usuário faz uma requisição (HTTP ou HTTPS).
2. O **WAF** analisa essa requisição com base em **regras** configuradas.
3. Se a requisição for segura, ela é **permitida**; se for maliciosa, é **bloqueada ou registrada (log)**.

### Componentes principais

| Componente | Descrição |
| --- | --- |
| **Web ACL (Access Control List)** | Conjunto de regras aplicadas a um recurso (CloudFront, ALB, API Gateway, etc.) |
| **Rules (Regras)** | Definem as condições de bloqueio, permissão ou contagem (ex: bloquear IPs específicos, padrões de SQL Injection, etc.) |
| **Rule Groups** | Conjuntos de regras reutilizáveis (você pode criar suas próprias ou usar gerenciadas pela AWS) |
| **Managed Rules** | Pacotes prontos feitos pela AWS ou parceiros que protegem contra ameaças conhecidas automaticamente |

### Exemplo prático

Imagine que você tenha um site em produção com um formulário de login.

Você pode usar o AWS WAF para:

- Bloquear requisições que contenham **comandos SQL suspeitos**.
- Impedir **múltiplas tentativas de login** (limite por IP).
- Permitir acesso **somente de determinados países**.
- Monitorar e **gerar logs de tráfego** via Amazon CloudWatch ou Kinesis Firehose.

### Benefícios

- **Totalmente gerenciado:** sem necessidade de instalar ou manter servidores.
- **Escalável automaticamente** conforme o tráfego cresce.
- **Integração nativa** com CloudFront, ALB, API Gateway e AppSync.
- **Custo sob demanda:** você paga pelo número de regras e requisições inspecionadas.
- **Proteção contínua**, com regras gerenciadas atualizadas automaticamente pela AWS.