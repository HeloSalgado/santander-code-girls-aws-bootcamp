# AWS CLI e SDKs

Estudo em: November 2, 2025

## AWS SDK

O **AWS SDK** permite interagir com os serviços da AWS **diretamente em sua linguagem de programação preferida**.

**Linguagens suportadas:**

- Java
- .NET
- Node.js
- Python
- Ruby
- PHP
- iOS
- Android
- Go

### Instalação do AWS SDK

| Linguagem | Comando de instalação |
| --- | --- |
| Node.js | `npm install @aws-sdk/client-s3` |
| Python | `pip install boto3` |
| Java | Maven: Adicione `<dependency>` ao `pom.xml`Gradle: `implementation 'software.amazon.awssdk:s3:2.20.0'` |
| .NET | `dotnet add package AWSSDK.S3` |
| Ruby | `gem install aws-sdk-s3` |
| PHP | `composer require aws/aws-sdk-php` |
| Go | `go get github.com/aws/aws-sdk-go-v2` |

## AWS CLI

O **AWS CLI (Command Line Interface)** é uma ferramenta baseada em **linha de comando** para gerenciar recursos da AWS.

- Ideal para **administradores** que precisam automatizar ou gerenciar infraestrutura rapidamente.
- Permite executar comandos diretamente no terminal ou em scripts.

## Comparação: AWS SDK vs AWS CLI

| Aspecto | AWS SDK | AWS CLI |
| --- | --- | --- |
| **Interface** | Linguagem de programação (código) | Linha de comando (terminal ou script) |
| **Usuário alvo** | Desenvolvedores que constroem aplicações | Administradores e usuários de automação |
| **Linguagens suportadas** | Python, Java, C#, Node.js, etc. | Nenhuma (baseado em comandos CLI) |
| **Complexidade** | Exige conhecimento em programação | Mais simples; comandos diretos |
| **Automação** | Adequado para fluxos complexos e integrações | Ótimo para tarefas repetitivas e rápidas |