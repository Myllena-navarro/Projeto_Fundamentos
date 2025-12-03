# Desafio 4 — Microsserviços Independentes (Sem API Gateway)
## Descrição Geral

Este desafio tem como objetivo implementar dois microsserviços independentes, cada um executando em seu próprio container Docker, e que se comunicam entre si utilizando requisições HTTP.

A ideia é simular uma arquitetura simples de microsserviços, onde cada serviço tem sua responsabilidade bem definida e roda isoladamente.

No nosso caso:

- Microsserviço A: fornece uma lista de usuários em formato JSON.
- Microsserviço B: consome o Microsserviço A e retorna informações enriquecidas para o cliente.

Essa comunicação acontece através da rede interna criada automaticamente pelo Docker Compose.

## Arquitetura da Solução

A arquitetura é composta por:

- Serviço A (serviço de usuários)

Responsável por expor um endpoint que retorna uma lista de usuários com informações básicas.

- Serviço B (serviço consumidor) 

Faz requisições ao Serviço A, processa os dados recebidos e devolve uma versão detalhada das informações.

Os dois microsserviços são empacotados em containers individuais, cada um com seu Dockerfile próprio.

O `docker-compose.yml` orquestra a execução simultânea dos dois serviços, gerenciando rede, dependências e portas.

## Comunicação Entre os Serviços

A comunicação ocorre da seguinte forma:

```bash
serviço B  --->  serviço A  ---> retorna JSON
```

O Serviço B utiliza o hostname interno do Docker (servico_a) para alcançar o Serviço A, garantindo isolamento e padronização da comunicação entre containers.

## Execução do Projeto
### 1. Subir os microsserviços

Na pasta do desafio:
```bash
docker compose up -d
```

O Compose irá:
- construir as duas imagens
- criar a rede interna
- iniciar ambos os containers

## Testes
### ✔ Testar o Microsserviço A

Endpoint que lista os usuários cadastrados:
```bash
curl localhost:5001/users
```

Você deve visualizar um JSON contendo a lista de usuários.

### ✔ Testar o Microsserviço B

Endpoint que combina informações e exibe detalhes:
```bash
curl localhost:5002/usuarios-detalhados
```

Você receberá um JSON com frases explicando o status de cada usuário.

Esse teste confirma:

- comunicação via HTTP entre containers
- microsserviços funcionando de forma isolada
- orquestração correta via Docker Compose

## Componentes Entregues

- Dois microsserviços independentes
- Dockerfiles separados
- Comunicação interna por HTTP
- Execução orquestrada com Docker Compose
- Testes executados com sucesso

## Conclusão
A solução implementada demonstra na prática como dois serviços distintos podem interoperar de forma leve, modular e escalável — fundamentos essenciais em arquiteturas distribuídas modernas.