# Terraform na AWS

Estudo em: November 2, 2025

O **Terraform** é uma ferramenta de **Infraestrutura como Código (IaC)** que permite criar, alterar e versionar infraestrutura de forma segura e previsível.

- **Provider:** O provedor define com qual serviço vamos trabalhar. Ex: `aws` para AWS.
- **Resource:** Um recurso é qualquer serviço que você quer criar, como EC2, S3, VPC etc.
- **State:** O Terraform mantém o estado da infraestrutura em um arquivo (`terraform.tfstate`) para controlar o que já foi criado.
- **Plan:** O comando `terraform plan` mostra o que será criado, alterado ou destruído antes de aplicar.
- **Apply:** O comando `terraform apply` cria ou atualiza os recursos na AWS.

## Arquitetura de exemplo na AWS

Vamos imaginar que você quer criar:

- Uma **VPC**
- Uma **subnet**
- Uma **instância EC2**
- Um **bucket S3**

A estrutura do Terraform ficaria assim:

```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_vpc" "minha_vpc" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "minha_subnet" {
  vpc_id            = aws_vpc.minha_vpc.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "us-east-1a"
}

resource "aws_instance" "minha_ec2" {
  ami           = "ami-0ed9277fb7eb570c9"
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.minha_subnet.id

  tags = {
    Name = "MinhaInstancia"
  }
}

resource "aws_s3_bucket" "meu_bucket" {
  bucket = "meu-bucket-exemplo-12345"
  acl    = "private"
}
```

## Passo a passo prático

1. **Instale o Terraform**
    
    ```bash
    terraform -v
    ```
    
2. **Crie o arquivo main.tf**
    
    (Coloque o código do exemplo acima)
    
3. **Inicialize o Terraform**
    
    ```bash
    terraform init
    ```
    
    - Baixa o provider da AWS.
4. **Veja o que será criado**
    
    ```bash
    terraform plan
    ```
    
5. **Crie os recursos na AWS**
    
    ```bash
    terraform apply
    ```
    
    - Confirme digitando `yes`.
6. **Verifique na AWS**
    - Você verá a VPC, subnet, EC2 e bucket criados.
7. **Destrua os recursos (quando não precisar mais)**
    
    ```bash
    terraform destroy
    ```
    
    - Confirme com `yes`.

## Dicas importantes

- Use **variáveis** para não repetir valores (ex.: região, tipo de instância).
- Use **outputs** para ver IDs ou IPs de recursos.
- Para ambientes complexos, divida em **módulos** (VPC, EC2, S3 separados).
- Armazene o **state remotamente** (ex.: S3 + DynamoDB) se trabalhar em equipe.

Exemplo de **output** para a EC2:

```hcl
output "ip_publica_ec2" {
  value = aws_instance.minha_ec2.public_ip
}
```