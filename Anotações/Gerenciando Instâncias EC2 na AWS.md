# Gerenciando Instâncias EC2 na AWS

Data: September 22, 2025

## Criação e uso de imagens AMI (Amazon Machine Image)

Uma **Amazon Machine Image (AMI)** é um modelo de máquina virtual que contém a configuração necessária para iniciar uma **instância EC2** na Amazon Web Services (AWS). Pense nela como um "molde" ou "blueprint" que define o estado inicial de um servidor virtual.

### Tipos de AMI

Existem diferentes tipos de AMIs, cada um com uma finalidade:

- **AMIs fornecidas pela AWS:** São imagens prontas e seguras, criadas e mantidas pela própria Amazon. Elas são ideais para começar rapidamente, pois já vêm com os sistemas operacionais mais comuns.
- **AMIs da comunidade e do Marketplace:** Essas imagens são criadas e compartilhadas por terceiros. Algumas são gratuitas, outras são pagas e podem incluir softwares comerciais ou licenças já configuradas.
- **Suas próprias AMIs personalizadas:** Você pode criar uma AMI a partir de uma instância EC2 que você já configurou. Isso é extremamente útil para criar backups, padronizar ambientes (desenvolvimento, produção) ou escalar seu aplicativo, pois você pode lançar novas instâncias com a mesma configuração exata.

>💡Entender as AMIs é crucial para gerenciar e implantar instâncias no EC2 de forma eficiente. Elas fornecem uma base para a criação de ambientes consistentes e reproduzíveis na nuvem.

## Snapshots EBS

- Guarda dentro do S3
- Modelo IAAS

O snapshot do EBS é um serviço de backup nativo do AWS que faz backup dos volumes do EBS em um determinado momento.

E é possível configurar a frequência com que os snapshots são tirados

---

Os snapshots do EBS armazenam os volumes do EBS no AWS S3, em um matriz de armazenamento diferente de onde estão os volumes do EBS.

Para fins de recuperação de desastres (DR), os snapshots do EBS podem ser armazenados em uma região remota.

Podemos também otimizar o armazenamento em SSD para operações de leitura/gravação com uso intensivo de I/O.

### Como o custo é calculado
- **Principal**: O custo é baseado no armazenamento dos volumes (GB-mês) e em um custo adicional pelos snapshots.
- **Snapshots**: São incrementais. Você é cobrado apenas pela quantidade de dados novos ou alterados em cada novo snapshot, e não pelo volume total novamente. Isso torna os backups muito mais baratos.
- **Tamanho**: O custo dos snapshots é medido em GB-mês, e eles são armazenados no S3.

### Qual a diferença entre imagem e o snapshot?

No Amazon EC2, uma imagem de máquina da Amazon (AMI) faz o backup de um servidor inteiro, incluindo volumes EBS anexados.

Um snapshot é uma cópia pontual de um determinado volume. Você pode tirar snapshot de seus volumes EBS e salvá-los no armazenamento S3.