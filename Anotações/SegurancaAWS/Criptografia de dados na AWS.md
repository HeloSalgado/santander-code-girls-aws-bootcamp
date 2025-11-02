# Criptografia de dados na AWS

Estudo em: November 2, 2025

Os dados podem estar em **repouso** (armazenados) ou em **trânsito** (sendo transmitidos).

Cada estado requer medidas específicas de segurança e criptografia.

## **Dados em Repouso**

> Exemplo: dados armazenados em bancos de dados ou em buckets do Amazon S3
> 

### Criptografia em Repouso

Concentra-se na proteção dos dados **armazenados em discos ou bancos de dados**, garantindo sua segurança mesmo quando **não estão em movimento**.

**Serviços com criptografia em repouso integrada:**

- **Amazon S3**
- **Amazon RDS**
- **Amazon EBS**

> 👉🏾 Os dados são **criptografados automaticamente** antes de serem gravados e **descriptografados** no momento do acesso.

### AWS Key Management Service (KMS)

- Permite **criar, gerenciar e controlar chaves de criptografia**.
- Oferece **controle granular** sobre o uso das chaves.
- É amplamente integrado a serviços como S3, RDS, EBS e Redshift.

## **Dados em Trânsito**

> Exemplo: dados sendo transmitidos entre a AWS e um ambiente on-premises
> 

### Criptografia em Trânsito

Conjunto de medidas que protege os dados **durante a transmissão** de um ponto a outro (como na comunicação via internet ou VPN).

Garante que as informações **não sejam interceptadas ou manipuladas** durante o envio.

---

### Tipos de Criptografia

**Criptografia de Volumes**

- **Amazon EBS (Elastic Block Store)** – Criptografia de disco
- **Arquivos** – Soluções de parceiros disponíveis no **AWS Marketplace**

**Criptografia de Objetos**

- **S3 Server-Side Encryption (SSE)**
- **S3 SSE com chaves do cliente**
- **Criptografia do lado do cliente**

**Criptografia de Bancos de Dados**

- **Microsoft SQL Server (MSSQL)**
- **Oracle**
- **MySQL**
- **PostgreSQL**
- **Amazon Redshift**

---

### **AWS Secrets Manager**

Gerencia **segredos e credenciais sensíveis**, como senhas, tokens de API e strings de conexão de banco de dados.

**Principais usos:**

- Armazenar e recuperar segredos de forma **segura**
- **Automatizar a rotação** de credenciais (ex: senhas de banco ou tokens)
- **Evitar** o armazenamento de credenciais diretamente no código