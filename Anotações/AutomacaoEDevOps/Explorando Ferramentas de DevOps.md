# Explorando Ferramentas de DevOps

Estudo em: November 2, 2025

## Migração de empresas para Cloud

### **Dores (problemas que levam à migração)**

Antes da migração, as empresas costumam enfrentar desafios como:

1. **Custos altos com infraestrutura física**
    - Servidores locais (on-premises) exigem compra, manutenção e atualização constantes.
    - Pagam por capacidade ociosa (mesmo quando não estão usando).
2. **Dificuldade em escalar**
    - Quando o tráfego aumenta, os servidores não aguentam.
    - É caro e demorado aumentar recursos físicos.
3. **Implantações lentas e manuais**
    - As equipes de TI precisam instalar tudo manualmente, o que gera erros e lentidão.
4. **Falta de agilidade**
    - Lançar novas versões ou correções demora muito tempo.
5. **Problemas de segurança e backup**
    - Sem automação e monitoramento constante, falhas e perdas de dados são mais comuns.

### **Motivações (por que migrar para a cloud)**

A migração para a nuvem traz benefícios que resolvem essas dores:

1. **Escalabilidade**
    - Você pode aumentar ou reduzir recursos em segundos, conforme a demanda.
    - Ex: aumentar capacidade durante a Black Friday.
2. **Redução de custos**
    - Paga apenas pelo que usa (“pay as you go”).
    - Sem necessidade de comprar servidores caros.
3. **Maior agilidade**
    - DevOps e Cloud juntos permitem automação de deploys, testes e monitoramento.
    - Menos falhas e mais entregas rápidas.
4. **Disponibilidade e segurança**
    - A AWS, Azure e GCP oferecem alta disponibilidade, backup automático e ferramentas de segurança integradas.
5. **Inovação**
    - Facilita o uso de inteligência artificial, análise de dados, e outras tecnologias modernas.

## **Conexão com DevOps**

O **DevOps** é um conjunto de práticas e ferramentas que unem **desenvolvimento (Dev)** e **operações (Ops)**, automatizando todo o ciclo de entrega de software.

Durante a **migração para a cloud**, o DevOps é essencial porque:

- Automatiza a criação da infraestrutura (com ferramentas como **Terraform**, **AWS CloudFormation**).
- Garante entregas contínuas com **CI/CD** (usando **GitHub Actions**, **Jenkins**, **AWS CodePipeline**, etc).
- Monitora e mantém os sistemas com **CloudWatch**, **Prometheus**, etc.

➡️ **Exemplo prático:**
Uma empresa que antes demorava semanas para subir um novo servidor agora pode criar tudo automaticamente com um arquivo Terraform e implantar em minutos.

## **Resumo final**

| Antes da Cloud | Com Cloud + DevOps |
| --- | --- |
| Servidores físicos caros | Infraestrutura sob demanda |
| Deploys manuais e lentos | Deploys automáticos e rápidos |
| Falta de escalabilidade | Escalabilidade elástica |
| Alto custo e manutenção | Custo sob uso e automação |
| Risco de falhas e downtime | Alta disponibilidade e monitoramento contínuo |