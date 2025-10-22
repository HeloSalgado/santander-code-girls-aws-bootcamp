# Amazon Glacier

Estudo em: October 21, 2025

O **Amazon S3 Glacier** é uma **classe de armazenamento do Amazon S3** focada em **arquivamento de dados de longo prazo** com **custo extremamente baixo**.

Ele é ideal para dados que **não precisam ser acessados imediatamente** e podem esperar algumas horas para serem recuperados.

Além disso, **pode ser configurado junto com regras de ciclo de vida (Lifecycle Management)** para **mover automaticamente dados raramente acessados** para esse armazenamento frio — gerando economia.

### Quando usar o Glacier?

- Quando os dados **não precisam de acesso imediato** (recuperação padrão leva de 3 a 5 horas).
- **Backup anual** ou dados arquivados.
- **Obrigação legal de retenção de dados** (ex: notas fiscais, auditorias).
- **Fotos, relatórios ou logs históricos**.
- **Armazenamento por pelo menos 90 dias (Glacier)** ou **180 dias (Glacier Deep Archive)**.

### Custos e prazos

| Classe | Mínimo de armazenamento | Tempo médio de recuperação | Exemplo de uso |
| --- | --- | --- | --- |
| **S3 Glacier** | 90 dias | 3 a 5 horas | Backup, logs antigos |
| **S3 Glacier Deep Archive** | 180 dias | 5 a 12 horas | Dados legais de longo prazo |
- **Recuperação padrão custa cerca de US$ 0,01/GB**
- **1.000 solicitações ≈ US$ 0,05**

## Snow Family (Transferência de grandes volumes de dados)

Quando precisamos **mover enormes quantidades de dados (TBs ou PBs)** para a AWS — de forma **offline** — utilizamos a **Snow Family**:

### AWS Snowball

- Dispositivo físico enviado pela AWS.
- Usado para **migração de dados em larga escala** ou **armazenamento local temporário**.

### AWS Snowball Edge

- Versão mais avançada do Snowball.
- **Transfere dados mais rápido que a internet** usando envio físico.
- Dispositivo **resistente e preparado para transporte**.

### AWS Snowmobile

- **Caminhão da AWS** para migração massiva.
- **Transporta até 100 petabytes**.
- Usado por **grandes empresas e governos**.