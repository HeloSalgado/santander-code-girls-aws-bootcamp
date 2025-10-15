# O que é Amazon CloudFront?

Estudo em: October 15, 2025 

O Amazon CloudFront é o serviço de CDN (Content Delivery Network) da AWS.
Ele serve para distribuir conteúdo (como sites, vídeos, imagens e APIs) de forma mais rápida, segura e eficiente para usuários em qualquer lugar do mundo.

### Como ele funciona

O CloudFront usa uma **rede global de servidores** (chamados **Edge Locations**) espalhados por dezenas de países.

Quando alguém acessa seu site ou sistema:

1. O CloudFront **entrega o conteúdo a partir do servidor mais próximo geograficamente** do usuário.
2. Isso **reduz a latência** (tempo de resposta) e **melhora o desempenho**.
3. Se o conteúdo for estático (como imagens, CSS ou vídeos), ele é **armazenado temporariamente em cache** nessas Edge Locations para entregas ainda mais rápidas nas próximas requisições.

### Integração com outros serviços da AWS

O CloudFront se conecta facilmente com:

- **S3:** para distribuir arquivos estáticos armazenados em buckets;
- **EC2 ou Load Balancer:** para distribuir conteúdo dinâmico de aplicações;
- **Route 53:** para gerenciar o domínio e o roteamento do tráfego.

## Edge Location

É basicamente um servidor de cache, esse tipo de servidor está espalhado em cidades do mundo e são usados pelo CloudFront para distribuir conteúdo ao usuário final e reduzir a latência de acesso.