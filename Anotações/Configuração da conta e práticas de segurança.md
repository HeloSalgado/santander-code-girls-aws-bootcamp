# Configuração da conta e práticas de segurança

Data: September 2, 2025

Website: https://docs.aws.amazon.com/pt_br/IAM/latest/UserGuide/best-practices.html

# Criação da conta

É importante saber que a criação de toda conta CLOUD você terá uma conta principal (root) com super permissões ao seu workspace

> 📌 Quando criar a conta root é interessante criar uma outra conta (IAM) com alguns privilégios


# Práticas de Segurança

1. Criar conta root e depois guardar
2. Não compartilhar dados da conta
3. Ficar atento ao email com as cobranças
4. Autenticação multifator (MFA)
5. Estabelecer barreiras de proteção para permissões

# IAM

**IAM** significa **Identity and Access Management** (Gerenciamento de Identidade e Acesso). 💡

Basicamente, é o serviço que permite você **controlar quem pode acessar os recursos da sua conta AWS e o que cada um pode fazer**. Ele é super importante para segurança.

Principais conceitos do IAM:

1. **Usuários (Users)** – contas individuais com permissões específicas.
2. **Grupos (Groups)** – conjuntos de usuários que compartilham as mesmas permissões.
3. **Funções (Roles)** – permissões atribuídas para serviços ou usuários temporariamente, útil para aplicações ou EC2, por exemplo.
4. **Políticas (Policies)** – regras que definem exatamente **o que pode ou não ser feito** nos recursos AWS.

💡 **Exemplo prático:**

- Você pode criar um usuário “Desenvolvedor” e dar permissão apenas para acessar S3 e Lambda, sem poder mexer em EC2 ou RDS.
- Isso evita que alguém acabe mexendo em recursos que não deveria.

>❗IAMUserChangePassword → o novo usuário poderá mudar sua senha após o primeiro acesso


# Gerenciamento de faturamento e custos (**Billing and Cost Management)**

É o painel dentro do **AWS Management Console** que centraliza tudo relacionado a:

- **Faturamento (Billing):** onde você visualiza suas faturas, histórico de pagamentos e métodos de cobrança.
- **Custos (Cost Management):** onde você acompanha detalhadamente o consumo de cada serviço da AWS (EC2, S3, RDS, Lambda etc.), consegue criar relatórios e definir orçamentos.

>Primeira coisa a se configurar!


## Principais recursos

1. **Bills** – mostra o valor detalhado de cada serviço e recurso utilizado.
2. **Cost Explorer** – ferramenta visual para analisar custos e uso ao longo do tempo, identificar tendências e prever gastos futuros.
3. **Budgets** – permite criar **orçamentos personalizados** e configurar alertas (ex.: "me avise quando os custos passarem de $50").
4. **Cost and Usage Reports (CUR)** – relatórios completos e personalizáveis, exportáveis para análise mais profunda.
5. **Free Tier Dashboard** – acompanha se você ainda está dentro da camada gratuita da AWS.

## Por que é importante?

1. **Controle Financeiro:** evita surpresas na fatura, especialmente em ambientes de teste ou aprendizado.
2. **Previsibilidade:** ajuda a entender padrões de consumo e prever custos futuros.
3. **Otimização:** permite identificar serviços subutilizados ou instâncias superdimensionadas (e reduzir custos).
4. **Governança:** essencial para empresas que precisam controlar o orçamento de diferentes equipes ou projetos.
5. **Alertas Preventivos:** reduz o risco de ultrapassar o orçamento planejado.

> 📌 Em resumo: o **Billing and Cost Management** é como o "extrato bancário + planejador financeiro" da AWS. Ele é fundamental para **evitar desperdício**, **manter controle** e **otimizar recursos** na nuvem.