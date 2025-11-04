# Introdução ao DevOps

Estudo em: November 2, 2025

O nome **DevOps** é a junção de **"Desenvolvimento" (Dev)** e **"Operações" (Ops)**.

É uma filosofia que busca **quebrar os silos** (as "paredes") que tradicionalmente existem entre a equipe que *constrói* o software (Devs) e a equipe que *mantém* esse software no ar (Ops).

**O Problema Antigo:**

- **Devs:** Querem lançar novas funcionalidades o mais rápido possível (foco na **mudança**).
- **Ops:** Querem que o sistema fique estável e nunca caia (foco na **estabilidade**).
- **Resultado:** Conflito. Os Devs "jogavam o código por cima do muro" e o time de Ops que se virasse para fazer funcionar.

**A Solução DevOps:**
O DevOps une essas duas equipes (e também times de Qualidade/QA e Segurança/Sec) em um único fluxo, com um objetivo comum: **entregar software de alta qualidade, de forma rápida e confiável.**

Para fazer isso, o DevOps se baseia em **automação**, **colaboração** e **comunicação**.

## Os 5 Princípios Chave (O "CALMS")

Uma forma fácil de lembrar os princípios do DevOps é através do acrônimo **CALMS**:

1. **C - Cultura (Culture):**
É o pilar mais importante. É a mudança de mentalidade para a **colaboração** e **responsabilidade compartilhada**. O desenvolvedor não diz "funcionou na minha máquina"; ele é responsável pelo código até a produção. E o time de Ops ajuda a criar ferramentas para que os Devs façam isso com segurança.
2. **A - Automação (Automation):**
É o "motor" do DevOps. A ideia é: "Se você precisa fazer algo mais de uma vez, automatize". Isso inclui automatizar os testes, a criação da infraestrutura (IaC), a integração do código e a implantação (deploy).
3. **L - Lean (Enxuto):**
Baseado nas ideias de "Lean Manufacturing" (Manufatura Enxuta). A ideia é focar na entrega de valor ao cliente, eliminando desperdício. Na prática, isso significa fazer **entregas pequenas e frequentes** (ex: lançar 10 pequenas melhorias por dia, em vez de 1 pacote gigante por mês).
4. **M - Medição (Measurement):**
Você não pode melhorar o que não pode medir. É fundamental ter **monitoramento** e **feedback** constantes.
    - *Performance do App:* O site está rápido? (Ex: **AWS CloudWatch** Metrics)
    - *Erros:* Quantos erros estão acontecendo? (Ex: **CloudWatch Logs Insights**)
    - *Processo:* Quanto tempo leva do código escrito até a produção?
5. **S - Sharing (Compartilhamento):**
Compartilhar conhecimento, ferramentas e responsabilidades. O time de Ops compartilha como o sistema funciona em produção, e o time de Devs compartilha o que é preciso para o software rodar bem.

## Como Trabalhar com DevOps (Na Prática)

Na prática, "fazer DevOps" significa implementar um conjunto de processos e ferramentas que dão suporte aos princípios CALMS. Os mais importantes são:

### 1. Implementar um Pipeline de CI/CD

Este é o coração da automação. **CI/CD** significa **Integração Contínua (CI)** e **Entrega/Implantação Contínua (CD)**.

- **Integração Contínua (CI):** Toda vez que um desenvolvedor envia (commita) um novo código, um processo automático é disparado para:
    1. Baixar o código.
    2. Compilar (buildar).
    3. Rodar testes automatizados.
    *Se algo falhar, o time é notificado imediatamente.(Ferramentas AWS: CodeCommit, CodeBuild)*
- **Entrega/Implantação Contínua (CD):** Se os testes da CI passarem, o processo continua:
4. O código é "empacotado" (ex: uma imagem Docker).
5. Esse pacote é enviado para um ambiente (ex: Teste ou Produção).
*(Ferramentas AWS: CodeDeploy, CodePipeline)*

### 2. Adotar Infraestrutura como Código (IaC)

Em vez de criar servidores ou bancos de dados clicando no console, você **escreve um código** que descreve sua infraestrutura.

- **Por quê?** Para ter consistência (o ambiente de Teste é *idêntico* ao de Produção), rastreabilidade (você pode ver quem mudou a infra no Git) e velocidade (você sobe um ambiente novo em minutos).
- **(Ferramenta AWS: AWS CloudFormation)**, que você já estudou.

### 3. Praticar "You Build It, You Run It" (Você Constrói, Você Opera)

Esta é a aplicação prática da **Cultura**. A equipe que desenvolveu uma funcionalidade (um "microserviço") é também a equipe que fica de plantão (on-call) para resolver problemas dela em produção.

- Isso força os desenvolvedores a se preocuparem com a estabilidade e a qualidade, pois serão eles mesmos a acordar de madrugada se algo quebrar.

### 4. Focar em Monitoramento e Observabilidade

Você não pode ter DevOps sem feedback. O time *inteiro* (Devs e Ops) deve olhar para os mesmos dashboards.

- Se o deploy de uma nova versão fez a latência do site subir, o time precisa ver isso *imediatamente* (via **CloudWatch Alarms**) e agir, seja revertendo a mudança (rollback) ou corrigindo rápido.