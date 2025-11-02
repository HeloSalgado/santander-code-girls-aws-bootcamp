# AWS CloudFormation

Estudo em: November 2, 2025

O **AWS CloudFormation** é um serviço que facilita a **modelagem e configuração de recursos na AWS**.

Com ele, podemos **criar modelos (templates)** que descrevem os recursos necessários — como **instâncias EC2**, **bancos de dados RDS**, **VPCs**, entre outros — automatizando todo o **provisionamento e configuração da infraestrutura**.

>💡 Assim, **eliminamos a necessidade de configurar recursos manualmente**, permitindo foco no **desenvolvimento e na gestão das aplicações**.

## Benefícios do AWS CloudFormation

1. **Automação**
    
    Automatiza a criação, configuração e gerenciamento de recursos da AWS, tornando o processo **rápido, confiável e repetível**.
    
2. **Consistência e Padronização**
    
    Permite criar **modelos padrão de infraestrutura**, garantindo que cada ambiente (desenvolvimento, teste, produção) seja **idêntico e estável**.
    
3. **Economia de Custos**
    
    Os **modelos podem ser reutilizados**, reduzindo o tempo e o custo de projetar e implementar novas infraestruturas.
    
4. **Segurança**
    
    Garante que todos os recursos sejam criados com **políticas de segurança consistentes**, reduzindo riscos e falhas de configuração.
    

## Formatos de Templates

Os modelos (templates) do CloudFormation podem ser escritos em **JSON** ou **YAML**.

### 📄 JSON

Formato tradicional, baseado em pares *chave-valor*.

```json
{
  "Resources": {
    "MyInstance": {
      "Type": "AWS::EC2::Instance",
      "Properties": {
        "InstanceType": "t2.micro",
        "ImageId": "ami-12345678"
      }
    }
  }
}
```

### 📄 YAML

Formato mais legível e amplamente preferido.

```yaml
Resources:
  MyInstance:
    Type: "AWS::EC2::Instance"
    Properties:
      InstanceType: "t2.micro"
      ImageId: "ami-12345678"
```

## Diferença entre CloudFormation e Terraform

| Aspecto | **AWS CloudFormation** | **Terraform** |
| --- | --- | --- |
| **Provedor** | Específico da AWS | Multi-cloud (suporta AWS, Azure, GCP etc.) |
| **Linguagem** | JSON / YAML | HCL (HashiCorp Configuration Language) |
| **Integração** | Nativa na AWS | Independente |
| **Controle de estado** | Gerenciado automaticamente pela AWS | Armazenado e gerenciado pelo usuário |
| **Curva de aprendizado** | Mais simples para quem já usa AWS | Mais flexível, mas requer mais configuração |

## Exemplo Prático

Criar uma **instância EC2** com um **Security Group** e um **bucket S3** automaticamente.

### Exemplo em YAML:

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: Template para criar uma instância EC2 e um bucket S3

Resources:
  MyBucket:
    Type: "AWS::S3::Bucket"
    Properties:
      BucketName: "meu-bucket-exemplo-cloudformation"

  MySecurityGroup:
    Type: "AWS::EC2::SecurityGroup"
    Properties:
      GroupDescription: "Permitir acesso SSH"
      SecurityGroupIngress:
        - IpProtocol: "tcp"
          FromPort: 22
          ToPort: 22
          CidrIp: "0.0.0.0/0"

  MyInstance:
    Type: "AWS::EC2::Instance"
    Properties:
      InstanceType: "t2.micro"
      ImageId: "ami-0ed9277fb7eb570c9"
      SecurityGroups:
        - !Ref MySecurityGroup

```

➡️ **O que esse template faz:**

- Cria um **bucket S3**.
- Cria um **Security Group** com acesso SSH.
- Cria uma **instância EC2** usando esse Security Group.

Tudo isso de forma **automática e padronizada**, com apenas um arquivo.