# Amazon CloudFront

Estudo em: October 21, 2025

O **Amazon CloudFront** é um **CDN (Content Delivery Network)** da AWS. Ele serve para entregar conteúdo (imagens, vídeos, arquivos, APIs, sites) **rapidamente** aos usuários, usando servidores distribuídos pelo mundo chamados **edge locations**.

Basicamente, ele **leva o conteúdo mais próximo do usuário**, diminuindo a latência e melhorando a experiência.

## Como funciona

1. Você tem seu conteúdo em um **origin** (pode ser S3, EC2, ALB, ou até outro servidor na internet).
2. Você cria uma **distribuição CloudFront** apontando para esse origin.
3. Quando alguém acessa o conteúdo:
    - O CloudFront verifica se já tem uma **cópia em cache** próxima ao usuário.
    - Se tiver, entrega imediatamente (super rápido!).
    - Se não tiver, busca no origin, entrega ao usuário e **armazena em cache** para os próximos.

> Pense no CloudFront como uma rede de correios super rápida, que já deixa as cartas perto das casas das pessoas.
> 

## Tipos de conteúdo que podemos entregar

- Arquivos estáticos: imagens, CSS, JS, PDFs
- Arquivos dinâmicos ou APIs: com **cache configurável**
- Streaming de vídeos
- Sites inteiros (com HTTPS, custom domain, WAF)

## Exemplo prático: Site estático no S3

1. Você tem um **bucket S3** chamado `meusite-statico` com seu site.
2. Cria uma **distribuição CloudFront** apontando para esse bucket.
3. Usuário acessa `www.meusite.com`:
    - CloudFront entrega o conteúdo do edge mais próximo dele.
    - Se o arquivo ainda não estiver em cache, CloudFront pega do S3 e guarda para a próxima pessoa.

**Vantagem:** Mesmo que o S3 esteja nos EUA, usuários no Brasil recebem o site rápido porque o CloudFront tem servidores em São Paulo.

## Outras funcionalidades importantes

- **HTTPS e custom domain:** entrega segura com certificado SSL/TLS.
- **Lambda@Edge:** roda funções em edge locations antes ou depois da entrega, útil para personalizar conteúdo.
- **WAF (Web Application Firewall):** protege contra ataques.
- **Geo-restriction:** bloqueia ou libera acesso por região.