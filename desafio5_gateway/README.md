# Desafio 5 — Microsserviços com API Gateway
## Descrição Geral

O objetivo deste desafio é implementar uma arquitetura baseada em microsserviços, utilizando um API Gateway como ponto único de entrada para o cliente.

A solução foi desenvolvida com três serviços:

- Serviço de Usuários — fornece informações básicas de usuários
- Serviço de Pedidos — expõe uma lista de pedidos associados a usuários
- API Gateway — centraliza as requisições e redireciona para os serviços apropriados

Cada serviço roda em um container Docker independente, com seu próprio Dockerfile.

A comunicação entre eles ocorre dentro da rede interna criada pelo Docker Compose.

## Arquitetura da Solução

A estrutura geral da arquitetura é:

CLIENTE → API Gateway → Users Service

                         ↑

                         └─ Orders Service


- O cliente faz requisições somente ao gateway
- O gateway consulta os demais serviços
- Cada microsserviço tem sua função isolada, seguindo os princípios de arquitetura distribuída

Essa abordagem facilita escalabilidade, manutenção e substituição de serviços de forma independente.

## Execução do Projeto
### 1. Subir toda a aplicação

Dentro da pasta do desafio:

```bash
docker compose up -d
```

O Compose irá:

✔ construir as imagens

✔ criar a rede interna

✔ iniciar os três containers

✔ disponibilizar o gateway na porta 8000

## Testes

Após subir os containers, os testes devem ser feitos sempre pelo gateway, que é o ponto central da arquitetura.

### ✔ Teste 1 — Verificar se o Gateway está ativo

```bash
curl localhost:8000
```

### ✔ Teste 2 — Consultar lista de usuários (redirecionado pelo gateway)

```bash
curl localhost:8000/users
```

O gateway chama internamente o serviço users_service, processa a resposta e retorna para o cliente.

### ✔ Teste 3 — Consultar lista de pedidos (via gateway)

```bash
curl localhost:8000/orders
```

O gateway acessa internamente o `orders_service.`

Esses testes confirmam:

- funcionamento do API Gateway
- comunicação entre os serviços
- rede interna funcionando
- containers isolados e acessíveis

## Componentes Entregues
- Microsserviço de Usuários
- Microsserviço de Pedidos
- API Gateway
- Dockerfiles individuais
- Orquestração completa com Compose
- Testes executados com sucesso

## Conclusão

A solução demonstra uma arquitetura simples, bem definida e alinhada com práticas modernas utilizadas em aplicações reais distribuídas.