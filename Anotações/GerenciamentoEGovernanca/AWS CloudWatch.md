# AWS CloudWatch

Estudo em: October 29, 2025

## O que é?

É um serviço de **monitoramento e observabilidade** que coleta dados de praticamente todos os recursos da sua infraestrutura AWS (e até de aplicações fora dela) em forma de logs, métricas e eventos.

O objetivo principal dele é dar a você visibilidade total do que está acontecendo, para que você possa:

1. **Entender** o desempenho das suas aplicações.
2. **Reagir** automaticamente a mudanças.
3. **Resolver** problemas rapidamente.

## Os 4 Pilares Principais do CloudWatch

Para entender o CloudWatch, basta entender estas quatro funções principais:

### 1. 📊 CloudWatch Metrics (Métricas)

Esta é a base de tudo. O CloudWatch coleta automaticamente **métricas** (pontos de dados ao longo do tempo) de seus serviços da AWS.

- **Exemplos:**
    - **EC2 (Servidor):** Qual é o uso da CPU? Quanta rede está sendo usada?
    - **RDS (Banco de Dados):** Quantas conexões estão ativas? Qual é o tempo de resposta de uma consulta?
    - **S3 (Armazenamento):** Quantos arquivos foram baixados?

> **Analogia**: Pense nisso como o painel do seu carro. Ele mostra métricas vitais em tempo real: sua velocidade (CPU), a temperatura do motor (uso de disco) e o nível de gasolina (rede). Você olha para ele para saber se está tudo bem.
> 

### 2. 🔔 CloudWatch Alarms (Alarmes)

Aqui é onde o CloudWatch se torna *proativo*. Você pode definir **alarmes** que monitoram uma métrica específica.

Você diz ao CloudWatch: "Ei, se a utilização da CPU daquele servidor EC2 ficar **acima de 80%** por **mais de 5 minutos**, dispare um alarme!"

Quando um alarme dispara, ele pode:

- Enviar uma notificação para você (via E-mail, SMS, etc.).
- **Tomar uma ação automática**, como reiniciar o servidor ou adicionar mais servidores (auto-scaling).

> Analogia: É a luz de "verificar o motor" no painel do seu carro. Ela não apenas mostra a métrica (temperatura alta), mas avisa ativamente que há um problema que exige sua atenção.
> 

### 3. 📜 CloudWatch Logs (Logs)

Suas aplicações e servidores geram arquivos de log (registros de texto de tudo o que acontece). O CloudWatch Logs permite que você **centralize, armazene e monitore** todos esses logs em um único lugar.

- **Por que isso é útil?** Em vez de acessar 10 servidores diferentes para encontrar um erro, você vai a um só lugar.
- **Recurso Poderoso:** Você pode pesquisar os logs (ex: "me mostre todas as linhas que contêm a palavra 'ERRO'") e até criar métricas e alarmes baseados no que aparece nos logs (ex: "dispare um alarme se a palavra 'ERRO' aparecer mais de 100 vezes em 1 minuto").

> Analogia: É a "caixa-preta" do avião. Se algo der errado (a aplicação cair), você vai aos logs para ver o registro exato do que aconteceu e diagnosticar a causa raiz do problema.
> 

### 4. 🗓️ CloudWatch Events (EventBridge)

*(Nota: Isso evoluiu para um serviço próprio chamado **Amazon EventBridge**, mas a ideia nasceu no CloudWatch).*

Isso permite que você reaja a **eventos** (mudanças de estado) que acontecem na sua conta AWS.

- **Exemplos de eventos:**
    - "Um novo arquivo foi carregado no S3."
    - "Um novo servidor EC2 acabou de ligar."
    - "Um usuário específico fez login no console."

Você pode criar regras que dizem: "**QUANDO** *[um novo arquivo .jpg for carregado no S3]*, **ENTÃO** *[execute esta função Lambda para criar uma miniatura dessa imagem]*."

> Analogia: É um sensor de movimento na sua casa. QUANDO [movimento é detectado (o evento)], ENTÃO [acenda a luz (a ação)].
> 

## CloudWatch Logs Insights

É a **ferramenta de consulta interativa e super-rápida** que permite *analisar* o que está dentro daquela caixa-preta.

Pense no Logs Insights como um **"SQL para seus logs"** ou um "Google super-avançado" para investigar problemas.

### O que o Logs Insights Permite Fazer

1. **Consultas Rápidas e Poderosas:**
Você pode fazer perguntas complexas aos seus logs e ter respostas em segundos, mesmo que tenha terabytes de dados. Ele tem uma linguagem de consulta própria, que é bem simples.SQL
    
    **Exemplo de consulta:**
    
    ```sql
    # "Me mostre as 10 páginas do meu site que mais estão dando 'ERRO 500' e conte quantas vezes cada uma"
    
    filter @message like 'ERRO 500' 
    | stats count() as 'Total_Erros' by endpoint
    | sort 'Total_Erros' desc
    | limit 10
    ```
    
2. **Análise e Agregação (Stats):**
Não é só *encontrar* o erro, é *entender* o padrão. Você pode calcular médias, contagens, percentis, etc.
    - "Qual é o tempo médio de resposta das minhas funções Lambda?"
    - "Quantos usuários únicos acessaram o sistema nos últimos 30 minutos?"
    - "Me mostre os 5% de requisições mais lentas (percentil p95)."
3. **Visualização:**
Depois de rodar a consulta, o Logs Insights pode gerar automaticamente **gráficos de barra ou de linha** com os resultados. Isso é excelente para ver tendências, como um pico de erros logo após uma nova versão (deploy) do código.
4. **Investigação de Causa Raiz:**
Ele é a ferramenta número 1 para *debugar* problemas em produção.
    - **Antes:** "O site caiu."
    - **Depois (com Logs Insights):** "O site caiu porque, às 14:32, o servidor de banco de dados 'db-prod-a' parou de responder, causando um pico de 'timeout' em todas as 50 instâncias EC2, como vejo neste gráfico de contagem de erros."