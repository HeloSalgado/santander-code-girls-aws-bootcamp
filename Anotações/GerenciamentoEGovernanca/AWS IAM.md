# Gerenciando Usuários e Permissões na AWS com Identity and Access Management (IAM)

Estudo em: October 29, 2025

Seu trabalho é controlar de forma granular **QUEM** (identidade) pode fazer **O QUÊ** (acesso) na sua conta.

O IAM faz duas coisas principais:

1. **Autenticação (Quem é você?):** Confirma que você é quem diz ser (login e senha, chaves de acesso, MFA).
2. **Autorização (O que você pode fazer?):** Concede as permissões que você tem, depois que você se autentica.

### Os 4 "Pilares" (Componentes) do IAM

Para entender o IAM, você precisa conhecer estes quatro componentes principais:

### 1. 👤 Usuário (User)

É uma **pessoa** ou **aplicação** (um "usuário de serviço") que interage com a AWS.

- **Exemplo:** Um usuário para você (`heloisa`), um usuário para um colega (`joao.programador`), ou um usuário para um sistema de build (`jenkins`).
- Cada usuário tem credenciais (senha para o console, ou chaves de acesso para a API).

### 2. 👥 Grupo (Group)

É simplesmente uma **coleção de usuários**. Você não anexa permissões diretamente a um grupo. Em vez disso, você anexa *políticas* a ele.

- **Por que usar?** É para facilitar o gerenciamento. Em vez de dar a 10 programadores as mesmas 50 permissões, uma por uma, você:
    1. Cria um grupo `Developers`.
    2. Anexa as 50 permissões (em uma política) a esse grupo.
    3. Adiciona os 10 programadores ao grupo.
- Se um novo programador (`maria`) entrar, você só a adiciona ao grupo `Developers` e ela *herda* todas as permissões instantaneamente.

### 3. 📜 Política (Policy)

Este é o **cérebro** do IAM. A política é um **documento JSON** que define as permissões. É ela que diz "sim" ou "não".

Uma política define:

- **Effect:** `Allow` (Permitir) ou `Deny` (Negar).
- **Action:** O que você pode fazer (ex: `ec2:StartInstances`, `s3:GetObject`).
- **Resource:** Em quais recursos você pode agir (ex: "em *todas* as instâncias EC2" ou "apenas no bucket S3 chamado `fotos-secretas`").

> Analogia: Uma Política é como o seu crachá. O crachá diz quais portas (Recursos) você pode abrir (Ações) e se você está permitido (Effect: Allow) ou banido (Effect: Deny) daquele andar.
> 

### 4. 🎭 Role (Função)

Este é o conceito mais poderoso (e às vezes confuso). Uma **Role (Função)** não está ligada a uma pessoa específica. É um conjunto de permissões que *qualquer um* (ou *qualquer serviço*) pode **assumir temporariamente**.

Pense em uma Role como **"vestir um chapéu"** para fazer um trabalho específico.

- **Exemplo 1 (Humano):** Você (`heloisa`) é uma programadora normal, mas precisa fazer algo como admin por 5 minutos. Em vez de ter a senha de admin, você "assume a Role" de `Administrador` e ganha esses poderes temporariamente.
- **Exemplo 2 (Serviço) - O MAIS IMPORTANTE:**
    - Sua instância **EC2** (um servidor) precisa salvar um arquivo no **S3** (armazenamento).
    - **Modo Inseguro:** Você salva uma chave de acesso (usuário e senha) dentro do servidor. Se o servidor for hackeado, o hacker rouba suas credenciais. PÉSSIMO.
    - **Modo Seguro (com Roles):** Você cria uma Role chamada `EC2-pode-escrever-no-S3`. Você anexa essa Role à sua instância EC2. A EC2 agora pode "vestir o chapéu" dessa role e ganhar permissões *temporárias* para falar com o S3, sem precisar de senhas ou chaves.

---

### Os Princípios de Ouro do IAM

1. **Princípio do Menor Privilégio (Least Privilege):**
Sempre dê o **mínimo** de permissão que um usuário (ou serviço) precisa para fazer *exclusivamente* o seu trabalho. Não dê `Admin` para todo mundo. Se um usuário só precisa ler o S3, dê a ele `s3:GetObject` e nada mais.
2. **NÃO use o Usuário Root:**
O usuário Root (o e-mail que você usou para criar a conta AWS) é o "Deus" da conta. Ele não pode ser restrito. **Nunca** o use para tarefas do dia-a-dia. Crie um usuário IAM (ex: `heloisa-admin`) para você e guarde o Root em um cofre, protegido com **MFA**.
3. **Use MFA (Multi-Factor Authentication):**
Sempre. Em todos os usuários, mas *principalmente* no usuário Root. É a sua melhor camada de defesa contra roubo de senhas.