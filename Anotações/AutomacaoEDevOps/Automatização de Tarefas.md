# Automatização de Tarefas

Estudo em: November 2, 2025

A **automação** nos ajuda a **simplificar e acelerar tarefas repetitivas** dentro da nuvem, otimizando processos e **reduzindo erros humanos**.

Na AWS, é possível automatizar desde a **criação da infraestrutura** até o **gerenciamento e implantação de aplicações**.

### **Ferramentas para Automação na AWS**

| Ferramenta | Descrição |
| --- | --- |
| **AWS CloudFormation** | Cria e gerencia infraestrutura como código (IaC) usando templates em JSON ou YAML. Permite reproduzir ambientes de forma rápida e consistente. |
| **AWS Lambda** | Executa código sob demanda **sem gerenciar servidores**, ideal para reagir automaticamente a eventos. |
| **AWS CodePipeline** | Automatiza o ciclo de vida de desenvolvimento (CI/CD), integrando etapas de build, teste e deploy. |
| **AWS Systems Manager** | Facilita o gerenciamento de instâncias EC2 e automação de tarefas operacionais, como manutenção de patches e execução de comandos. |
| **AWS Step Functions** | Cria fluxos de trabalho automatizados que orquestram diferentes serviços da AWS em uma única sequência lógica. |

### **Formas de Automação**

| Tipo | Descrição |
| --- | --- |
| **Infraestrutura como Código (IaC)** | Usa ferramentas como **AWS CloudFormation** ou **Terraform** para criar e gerenciar recursos de forma padronizada e versionada. |
| **Scripts e Linha de Comando** | Utiliza o **AWS CLI** para automatizar tarefas com comandos e scripts shell, como iniciar instâncias ou criar buckets S3. |
| **SDKs (Kits de Desenvolvimento)** | Usa linguagens como **Python (Boto3)**, **JavaScript**, ou **Java** para criar automações personalizadas e integrar sistemas à AWS. |

### **Benefícios da Automação**

- **Redução de Erros:** elimina falhas humanas em tarefas repetitivas.
- **Eficiência:** economiza tempo e aumenta a produtividade.
- **Escalabilidade:** permite automatizar desde pequenas tarefas até arquiteturas complexas.
- **Reprodutibilidade:** facilita a recriação de ambientes idênticos.
- **Integração com DevOps:** melhora o fluxo de CI/CD e a colaboração entre times.

## **Ansible para AWS**

O **Ansible** é uma ferramenta de **automação e gerenciamento de configuração** de código aberto, muito usada para gerenciar servidores e implantações.

### 🔹 Como ele funciona:

- Usa **playbooks** escritos em **YAML**, descrevendo o que deve ser feito (instalar pacotes, copiar arquivos, configurar serviços).
- Baseia-se em **SSH** (sem agentes) — não é necessário instalar software nas máquinas gerenciadas.
- Pode ser integrado com a AWS para **criar, configurar e manter recursos** (como EC2, RDS, S3, etc.).

### 🔹 Exemplos de uso na AWS:

- Provisionar automaticamente instâncias EC2.
- Configurar ambientes após a criação (como instalar dependências).
- Automatizar deploys em múltiplos servidores.

> 👉🏾 É ideal para **gerenciamento de configuração** e **automação pós-provisionamento** (ou seja, depois que a infraestrutura já foi criada).


## **Terraform**

O **Terraform**, criado pela HashiCorp, é uma ferramenta de **Infraestrutura como Código (IaC)** usada para **provisionar e gerenciar recursos** em múltiplos provedores, incluindo a AWS.

### 🔹 Como ele funciona:

- Usa arquivos de configuração escritos em **HCL (HashiCorp Configuration Language)**.
- Você define os recursos que deseja (como EC2, S3, VPC, etc.).
- O Terraform **compara o estado atual da infraestrutura** com o desejado e aplica apenas as mudanças necessárias.

### 🔹 Benefícios:

- Multi-cloud (funciona com AWS, Azure, Google Cloud e mais).
- Versionamento e rastreabilidade das mudanças.
- Garante consistência entre ambientes (dev, teste, produção).
- Permite **planejar antes de aplicar** (`terraform plan`) para prever mudanças.


>👉🏾 É ideal para **criação e manutenção de infraestrutura** de forma segura, escalável e reproduzível.


### **Resumo Comparativo**

| Ferramenta | Foco Principal | Nível de Automação | Tipo de Código |
| --- | --- | --- | --- |
| **Ansible** | Configuração e Deploy | Pós-provisionamento | YAML |
| **Terraform** | Criação e Gerenciamento de Infraestrutura | Infraestrutura como Código | HCL |
| **AWS CloudFormation** | Infraestrutura na AWS | IaC nativo da AWS | JSON / YAML |