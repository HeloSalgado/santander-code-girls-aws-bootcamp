# O que é Amazon Elastic Load Balancer?

Criado por: Helo Salgado
Criado em: October 15, 2025 4:18 PM
Categoria: Redes na AWS
Última atualização em: October 15, 2025 5:35 PM
Estudo em: October 15, 2025

O Elastic Load Balancer é um serviço que trabalha com a distribuição de carga de forma eficiente e automática para um grupo de servidores de uma maneira que aumenta a velocidade e o desempenho.

![image.png](image.png)

## Tipos de balanceadores

- Application Load Balancer
    - Gerencia o tráfego de aplicação HTTP/HTTPS, distribuindo solicitações com base em regras, como caminhos de URL e cabeçalhos.
    - Uso ideal: balancear o tráfego de aplicativos web que precisam de roteamento avançado e suporte a WebSockets
- Network Load Balancer
    - Gerencia o tráfego TCP/UDP a nível de rede, fornecendo baixa latência e alta taxa de transferência.
    - Use ideal: perfeito para balancear o tráfego de aplicativos que exigem alta performance e baixa latência, como serviços financeiros e jogos.
- Gateway Load Balancer
    - Combina funções de load balancing com serviços de segurança de rede, como firewalls e detecção de intrusões, em uma única solução.
    - Uso ideal: ideal para distribuir tráfego e adicionar funcionalidades e segurança a aplicativos, simplificando a arquitetura de segurança da aplicação.
- Classic Load Balancer
    - Um load balancer legado que distribui tráfego HTTP/HTTPS e TCP entre instâncias EC2.
    - Uso ideal: adequado para aplicativos que foram desenvolvidos antes dos ALBs e NLBs atuais. (aplicações monolíticas)