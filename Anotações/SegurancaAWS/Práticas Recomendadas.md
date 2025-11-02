# Práticas Recomendadas de Segurança na Nuvem

Estudo em: November 2, 2025

## Modelo de Responsabilidade Compartilhada – AWS

O **modelo de responsabilidade compartilhada** define **quem é responsável por qual parte da segurança** na nuvem da AWS.

Nesse modelo:

- A **AWS** é responsável pela **segurança *DA* nuvem**.
- O **usuário (cliente)** é responsável pela **segurança *NA* nuvem**.

### Responsabilidade da AWS — *Segurança DA Nuvem*

A AWS garante que toda a infraestrutura que executa seus serviços seja segura e confiável.

**Inclui:**

- Hardware físico (servidores, armazenamento, rede)
- Infraestrutura dos data centers
- Software que executa os serviços de nuvem
- Atualizações e segurança da infraestrutura subjacente em **serviços gerenciados**, como:
    - **Amazon S3**
    - **Amazon DynamoDB**

### Responsabilidade do Usuário — *Segurança NA Nuvem*

O cliente deve proteger o que ele **cria, armazena e configura** dentro da nuvem.

**Inclui:**

- Configuração e gerenciamento de **permissões de acesso** aos recursos.
    - Exemplo: em uma **instância EC2**, o usuário tem **controle total** sobre o sistema operacional e deve aplicar suas próprias medidas de segurança.
- Definição de **políticas de controle** para proteger dados e usuários.
- **Monitoramento e boas práticas**, como:
    - Criptografia de dados **em repouso** e **em trânsito**
    - Acompanhamento de logs e atividades

### Práticas Recomendadas de Segurança na AWS

**1. Controle de Acesso**

- Uso de **MFA (autenticação multifator)**
- Criação e gerenciamento de **usuários e grupos** no IAM
- Aplicação do **princípio do menor privilégio**

**2. Proteção de Dados**

- Criptografia de dados em repouso e em trânsito
- Uso do **AWS Key Management Service (KMS)** para gerenciamento de chaves

**3. Monitoramento e Resposta a Incidentes**

- Uso do **AWS CloudTrail** para auditoria e monitoramento de atividades
- Planejamento e resposta a incidentes de segurança

**4. Segurança da Infraestrutura**

- Proteção contra ataques DDoS com **AWS Shield**
- Mitigação de ameaças e filtros de tráfego com **AWS WAF**

### Framework de Boas Práticas

O **AWS Well-Architected Framework** é um guia que ajuda a aplicar **boas práticas de arquitetura e segurança**, reforçando os princípios do modelo de responsabilidade compartilhada.