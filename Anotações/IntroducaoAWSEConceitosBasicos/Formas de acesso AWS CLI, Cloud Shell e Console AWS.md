# Formas de acesso: AWS CLI, Cloud Shell e Console AWS

Data: September 5, 2025

---

Console AWS → Aonde acessamos, de forma visual a AWS.

Cloud Shell → Linha de comando que pode ser acessada pelo Console, onde nos permite fazer comandos para criar recursos.

- Pré-configurado em Python

CLI → Usa comandos no terminal para acessar a AWS e seus recursos - precisando configurar as credenciais de acesso.

### **AWS Management Console** (interface gráfica)

- **Como funciona:**
    
    Você acessa pelo navegador o **AWS Console** e vai até o painel de **Billing and Cost Management**.
    
- **Vantagens:**
    - Interface visual intuitiva.
    - Fácil de explorar relatórios no **Cost Explorer** com gráficos.
    - Ideal para iniciantes e para monitorar rapidamente custos e faturas.
- **Uso comum:**
    
    Empresas e usuários individuais que querem **ver os custos de forma clara e rápida**.
    

### **AWS CLI (Command Line Interface)**

- **Como funciona:**
    
    Você usa comandos no terminal para acessar e extrair informações de billing.
    
    Exemplo:
    
    ```bash
    aws ce get-cost-and-usage --time-period Start=2025-09-01,End=2025-09-05 --granularity=DAILY --metrics "UnblendedCost"
    ```
    
- **Vantagens:**
    - Automação de consultas de custo.
    - Integração com scripts para relatórios customizados.
    - Mais rápido quando você já sabe os comandos.
- **Uso comum:**
    
    Times de **DevOps e FinOps** que automatizam monitoramento e geração de relatórios.
    

### **AWS CloudShell**

- **Como funciona:**
    
    É um terminal baseado no navegador, dentro do Console AWS, já configurado com credenciais e a AWS CLI.
    
- **Vantagens:**
    - Não precisa instalar a CLI localmente.
    - Já vem autenticado, sem necessidade de configurar `aws configure`.
    - Prático para consultas rápidas sem sair do Console.
- **Uso comum:**
    
    Usuários que querem a **facilidade de um terminal pronto** sem precisar configurar ambiente local.
    

## Acessar AWS CLI

1. Gerar a Access Key do usuário
2. No GitBash:
    
    ```bash
    aws configure
    ```
    
3. Preencher as informações:
    
    ```bash
    AWS Access Key ID [****************6JZM]: 
    AWS Secret Access Key [****************HbeP]:
    Default region name [us-east-1]: us-east-1 # mesma sugerida
    Default output format [json]: json # mesmo sugerido
    ```
    

Pegar a região:

```bash
aws configure get region
```

Listar as configurações:

```bash
aws configure list
```

### Automação de criação de usuários

```bash
bash scriptIAM.sh usuarios.csv
```

```bash
#!/bin/bash

# Verifica se o argumento de entrada foi fornecido
if [ -z "$1" ]; then
    echo "Por favor, forneça o arquivo CSV como argumento."
    exit 1
fi

# Armazena o nome do arquivo de entrada
INPUT="$1"

# Verifica se o arquivo de entrada existe
if [ ! -f "$INPUT" ]; then
    echo "$INPUT arquivo não encontrado"
    exit 1
fi

# Verifica se o utilitário dos2unix está instalado
command -v dos2unix >/dev/null || { echo "utilitário dos2unix não encontrado. Por favor, instale dos2unix antes de executar o script."; exit 1; }

# Converte o arquivo CSV para o formato Unix para garantir compatibilidade
dos2unix "$INPUT"

# Loop para ler cada linha do arquivo CSV e processar as informações
while IFS= read -r line || [ -n "$line" ]; do
    
	# Separa as informações usando o delimitador ';' e atribui a variáveis
    usuario=$(echo "$line" | cut -d';' -f1)
    grupo=$(echo "$line" | cut -d';' -f2)
    senha=$(echo "$line" | cut -d';' -f3)

    # Cria um usuário no IAM
    aws iam create-user --user-name "$usuario"
    # Define uma senha e solicita a redefinição da senha no próximo login
    aws iam create-login-profile --password-reset-required --user-name "$usuario" --password "$senha"
    # Adiciona o usuário ao grupo especificado
    aws iam add-user-to-group --group-name "$grupo" --user-name "$usuario"
done < "$INPUT"

echo "Usuários importados com sucesso."
```