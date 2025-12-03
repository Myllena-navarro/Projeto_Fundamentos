# Projeto — Arquiteturas Distribuídas com Docker e Microsserviços

Este repositório reúne cinco desafios desenvolvidos para a disciplina Fundamentos de Computação Concorrente, Paralela e Distribuída.

O objetivo do projeto foi praticar conceitos de:

- Containers Docker

- Redes internas

- Persistência com volumes

- Orquestração com Docker Compose

- Microsserviços

- API Gateway

- Comunicação HTTP entre serviços

Cada desafio possui sua própria pasta e um README específico com detalhes da implementação.

## Estrutura do Repositório
Projeto_Docker/

│

├── desafio1_rede/          → Comunicação entre containers em rede customizada

├── desafio2_volumes/       → Persistência de dados com volumes Docker

├── desafio3_compose/       → Orquestração de 3 serviços com Docker Compose

├── desafio4_microservicos/ → Microsserviços independentes com HTTP

├── desafio5_gateway/       → Microsserviços + API Gateway centralizando requisições

│

└── README.md               → Este arquivo (visão geral)

## Resumo dos Desafios
### Desafio 1 — Containers em Rede

Criar dois containers (servidor e cliente) comunicando-se por uma rede Docker customizada.

- Rede criada manualmente

- Servidor Flask respondendo em /

- Cliente fazendo requisições periódicas via curl

- Comunicação comprovada via logs

### Desafio 2 — Volumes e Persistência

Demonstrar persistência de dados usando volumes.

- Banco SQLite ou PostgreSQL

- Volume local mantendo os dados mesmo após deletar o container

- Testes mostrando a persistência real

### Desafio 3 — Docker Compose

- Orquestrar três serviços interconectados:

- Web (Flask)

- Redis (cache)

- PostgreSQL (db)

- Comunicação testada entre web → cache e web → db

- Compose simulando um ambiente real com múltiplos serviços

### Desafio 4 — Microsserviços Independentes

Dois microsserviços separados se comunicando via HTTP:

- Serviço A → lista de usuários

- Serviço B → consome o serviço A e retorna dados enriquecidos

- Cada um com Dockerfile próprio

- Compose para rodar tudo junto

### Desafio 5 — Microsserviços com API Gateway

API Gateway centralizando o acesso aos microsserviços.

- Serviço de usuários

- Serviço de pedidos

- Gateway redirecionando /users e /orders

- Único ponto de entrada para o cliente

- Arquitetura moderna e escalável

## Como Rodar Qualquer Desafio

Entre na pasta do desafio desejado e execute:

```bash
docker compose up -d
```

Para parar:

```bash
docker compose down
```

## Tecnologias Utilizadas

- Docker

- Docker Compose

- Flask

- Redis

- PostgreSQL

- Python 3.11

- Requests (para comunicação HTTP)

- Containers isolados + rede interna

## Aprendizados Principais

Durante o desenvolvimento, coloquei em prática:

- Criação de imagens personalizadas com Dockerfile

- Comunicação entre containers por hostname

- Persistência de dados com volumes

- Orquestração de múltiplos containers com Compose

- Construção de microsserviços independentes

- Implementação de API Gateway

- Comunicação HTTP dentro de uma arquitetura distribuída
