# Amazon DynamoDB

Estudo em: October 21, 2025

Amazon DynamoDB é um banco de dados NoSQL totalmente gerenciado oferencendo escalabilidade, desempenho e flexibilidade para aplicativos de qualquer tamanho. O DynamoDB é rápido e flexível e foi projetado para fornecer armazenamento e recuperação de dados de baixa latência em qualquer escala. 

Ele permite trabalhar com dados não estruturados ou semi-estruturado, com isto ele permite o desenvolvimento mais rápido e interativo.

> 👉🏾 Diferente dos bancos relacionais (como RDS), ele **não usa tabelas com colunas fixas, nem JOINs**, e **não precisa de servidor nem manutenção** — a AWS cuida de tudo.


### Principais características:

- **Sem servidor (managed)**: você não gerencia instâncias, só configura tabelas e capacidade.
- **Escalabilidade automática** (dependendo do modo de capacidade).
- **Replicação rápida** dentro da região e opção de **Global Tables** para multi-região.
- **Consistência configurável**: eventual ou forte (para leituras).
- **Índices secundários** (GSI/LSI), **streams**, **TTL**, **transações** e **DAX** (cache) disponíveis.

### Como ele funciona na prática?

Em vez de tabelas com colunas fixas, você armazena dados como **itens com formato flexível**, parecidos com **JSON**.

**Exemplo de item no DynamoDB:**

```json
{
  "UserId": "123",
  "Nome": "Heloisa",
  "GeneroMusical": "R&B",
  "Favoritos": ["Beyoncé", "SZA", "Daniel Caesar"]
}
```

- `UserId` é a **chave primária** → usada para **buscar o item rapidamente**.
- Os outros campos podem variar — **cada item pode ter atributos diferentes**, sem precisar alterar estrutura.

**Exemplo de item no DynamoDB com Sort Key (SK):**

Vamos dizer que você quer guardar **várias playlists de um mesmo usuário**.

```json
{
  "UserId": "123",     ← PK (o usuário)
  "PlaylistId": "001", ← SK (item específico desse usuário)
  "NomePlaylist": "R&B vibes"
}

{
  "UserId": "123",     ← PK igual (mesmo usuário)
  "PlaylistId": "002", ← SK diferente
  "NomePlaylist": "Chill Night"
}
```

## Conceitos fundamentais

- **Tabela**: coleção de itens.
- **Item**: equivalente a uma linha; formato JSON com atributos.
- **Atributos**: campos (string, number, binary, Boolean, list, map, null).
- **Primary Key** — obrigatória: dois tipos:
    - **Partition Key (PK) simples** — apenas uma chave (ex.: `userId`). DynamoDB usa hash dessa chave para distribuir dados.
    - **Composite Key** — `Partition Key` + `Sort Key` (ex.: `userId` + `createdAt`). Permite armazenar múltiplos itens com mesma PK e ordená-los por SK.
- **Sort Key** — opcional: Só usamos **quando queremos guardar VÁRIOS itens para a MESMA PK**.
- **Índices secundários**:
    - **GSI (Global Secondary Index)** — indexa atributos com uma PK/SK própria; permite consultar por outras chaves; é global (pode ter outra partition key).
    - **LSI (Local Secondary Index)** — só pode ser criado junto com a tabela e usa a mesma partition key da tabela original, mas uma sort key diferente; só ao criar a tabela.
- **Capacidade**:
    - **Provisioned**: você escolhe RCUs (Read Capacity Units) e WCUs (Write Capacity Units). Pode configurar Auto Scaling.
    - **On-Demand**: paga por leitura/gravação consumida — bom para tráfego imprevisível.
- **R/W units**: leitura/escrita é cobrada em unidades; leitura forte consome mais que leitura eventual dependendo do tamanho.
- **DynamoDB Streams**: fluxo de alterações (insert/update/delete) — usado com Lambda para triggers/replicação/event sourcing.
- **DAX**: cache in-memory para reduzir latência em leituras.
- **Transações**: `TransactWriteItems` / `TransactGetItems` para ACID entre múltiplos itens.
- **TTL**: expiração automática de itens.
- **Limite de item**: 400 KB por item (atenção a esse limite).