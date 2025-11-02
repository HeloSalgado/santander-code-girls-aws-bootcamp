# Policies e Roles na AWS

Estudo em: October 29, 2025

A forma mais simples de pensar é:

- **Política (Policy):** É um **documento**. É o "o quê".
- **Role (Função):** É uma **identidade**. É o "quem" (temporário).

Uma **Role** (identidade) usa **Policies** (documentos) para saber o que pode fazer.

### 1. 📜 Policies (Políticas) - O Documento de Permissão

Uma política é um **documento JSON** que define permissões. É um pedaço de papel digital que diz "Sim, você pode fazer X" ou "Não, você não pode fazer Y".

**Analogia:** Pense na política como um **crachá detalhado**.

O crachá não é *você*. É apenas um cartão que lista:

- `Efeito`: Permitido (Allow)
- `Ação`: Entrar no Prédio B, Usar o Elevador de Carga
- `Recurso`: Apenas no Prédio B, Apenas o Elevador de Carga da Ala Leste

### A Anatomia de uma Política (JSON)

Este é o ponto-chave. Toda política segue esta estrutura básica:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:StartInstances",
        "ec2:StopInstances"
      ],
      "Resource": "arn:aws:ec2:us-east-1:123456789012:instance/i-0abcdef1234567890"
    },
    {
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::meu-bucket-de-logs/*"
    },
    {
      "Effect": "Deny",
      "Action": "ec2:TerminateInstances",
      "Resource": "*"
    }
  ]
}
```

Vamos dissecar o que importa:

- `Effect`: O efeito da declaração.
    - `Allow` (Permitir): Concede a permissão.
    - `Deny` (Negar): Proíbe explicitamente. **Um `Deny` sempre vence um `Allow`!** Se uma política permite `ec2:*` e outra nega `ec2:TerminateInstances`, você *não pode* terminar instâncias.
- `Action`: A(s) ação(ções) de API que estão sendo permitidas ou negadas.
    - `ec2:StartInstances` (Ligar um servidor)
    - `s3:GetObject` (Ler um arquivo do S3)
    - (Um curinga que significa "todas as ações". Use com cuidado!)
- `Resource`: O(s) recurso(s) específico(s) aos quais a ação se aplica.
    - É aqui que você aplica o **Princípio do Menor Privilégio**.
    - (Um curinga que significa "todos os recursos". Muito perigoso!)
    - `arn:aws:s3:::meu-bucket-de-logs/*` (Ação se aplica apenas a objetos dentro do bucket `meu-bucket-de-logs`).

**Tipos de Políticas:**

1. **Políticas Baseadas em Identidade (Identity-based):** São as que você **anexa** a um Usuário, Grupo ou Role. Elas dizem: "O que *esta identidade* (Heloisa, Grupo Devs, Role do EC2) pode fazer?"
2. **Políticas Baseadas em Recurso (Resource-based):** São as que você **anexa** ao *próprio recurso*. (Ex: uma "Política de Bucket" do S3). Elas dizem: "Quem de fora pode tocar *neste recurso*?"

### 2. 🎭 Roles (Funções) - A Identidade Temporária

Uma Role é uma **identidade** que *não* tem credenciais permanentes (senha ou chaves de acesso). Ela foi criada para ser **assumida** temporariamente por outra entidade (um usuário, uma aplicação, um serviço da AWS).

**Analogia:** Pense na Role como um **uniforme de especialista** (ex: "Uniforme de Eletricista").

- O uniforme não pertence a uma pessoa. Ele fica guardado em uma sala.
- Qualquer pessoa autorizada (você, um colega) pode ir lá e "vestir" o uniforme.
- Enquanto está com o uniforme, você ganha os poderes dele (ex: o uniforme vem com as chaves-mestras das salas elétricas).
- Seu crachá normal (`heloisa`) não tem acesso. O *uniforme* (`Role-Eletricista`) tem.
- Quando você termina o trabalho, você "tira" o uniforme e volta a ser `heloisa`.

### A Anatomia de uma Role (A Mágica de Duas Partes)

Isto é o que confunde a maioria. Uma Role é definida por **DOIS** documentos de política separados:

**Parte 1: A Política de Confiança (Trust Policy)**
Esta é a parte mais importante. Ela define **QUEM PODE ASSUMIR** a Role (quem pode "vestir o uniforme").

- **Analogia:** É a **lista na porta da sala de uniformes**. Ela diz quem tem permissão para entrar e pegar o uniforme `Role-Eletricista`.

**Exemplo de Trust Policy (JSON):**
Esta política diz: "Apenas o serviço EC2 da AWS pode assumir esta Role".

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

- `Principal`: É o "quem". Aqui, é o serviço `ec2.amazonaws.com`. Poderia ser um usuário (`"AWS": "arn:aws:iam::123456789012:user/Heloisa"`) ou até outra conta AWS.
- `Action`: É sempre `sts:AssumeRole`. Esta é a ação de "vestir o uniforme".

**Parte 2: A(s) Política(s) de Permissão (Permission Policy)**
Esta é uma (ou mais) política **padrão** (como a que vimos na seção 1) que define **O QUE A ROLE PODE FAZER** *depois* que ela é assumida.

- **Analogia:** São as **ferramentas e chaves** que vêm *dentro* do uniforme.

**Exemplo de Permission Policy (JSON) para esta Role:**
Esta política diz: "Quem estiver usando esta Role pode escrever no S3 e no CloudWatch Logs".

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetObject"
      ],
      "Resource": "arn:aws:s3:::meu-bucket-de-logs/*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "*"
    }
  ]
}
```

### Resumo

**Cenário:** Você tem um servidor **EC2** que precisa salvar logs em um bucket **S3**.

1. **Criação:**
    - Você cria uma **Role** chamada `Role-EC2-Logs`.
    - Na **Política de Confiança** (Parte 1) dela, você coloca `"Principal": {"Service": "ec2.amazonaws.com"}`. (Você diz: "Servidores EC2 podem vestir este uniforme").
    - Você cria uma **Política de Permissão** (Parte 2) chamada `Politica-Acesso-S3` que permite `s3:PutObject` no bucket `meu-bucket-de-logs`.
    - Você **anexa** a `Politica-Acesso-S3` à `Role-EC2-Logs`.
2. **Execução:**
    - Você liga sua instância **EC2** e a "associa" com a `Role-EC2-Logs`.
    - O EC2 (graças à Política de Confiança) "veste o uniforme" (chama `sts:AssumeRole`) e recebe **credenciais temporárias**.
    - Sua aplicação no EC2 tenta salvar um log no S3.
    - A AWS vê que a chamada está sendo feita com as credenciais temporárias da `Role-EC2-Logs`.
    - A AWS checa a **Política de Permissão** da Role e vê: `Allow: s3:PutObject`.
    - **Sucesso!** O log é salvo.

> 💡**A grande vantagem:** A sua instância EC2 **nunca** teve uma chave de acesso (senha) permanente salva nela. É muito mais seguro!
