# Desafio 3 — Docker Compose Orquestrando Serviços

O objetivo do desafio é utilizar **Docker Compose** para orquestrar uma aplicação composta por **três serviços**:  
- um serviço web (Flask),  
- um banco de dados (PostgreSQL),  
- e um serviço de cache (Redis).

---

## Objetivo do Desafio

Demonstrar:

- Configuração de múltiplos serviços com Docker Compose  
- Comunicação interna via rede criada automaticamente  
- Uso de `depends_on`  
- Conexão do serviço web com Redis e PostgreSQL  
- Exposição de porta para acesso externo  

---

## Estrutura do Projeto

desafio3_compose/

├── web/

│ ├── app.py

│ └── Dockerfile

├── docker-compose.yml

└── README.md


### ✔ `web/app.py`
Aplicação Flask que acessa Redis e PostgreSQL.

### ✔ `web/Dockerfile`
Imagem do serviço web.

### ✔ `docker-compose.yml`
Arquivo principal que define os três serviços: web, db, cache.

---

## Arquitetura dos Serviços

                       ┌────────────────────────────┐

                       │        web_service         │

                       │ Flask (porta 5000)         │

                       │ - /cache → Redis           │

                       │ - /db → PostgreSQL         │

                       └───────────┬────────────────┘

                                   │

             ┌─────────────────────┼─────────────────────┐

             │                     │                     │

  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐

  │   cache_service   │  │    db_service    │  │  compose network │

  │ Redis (6379)      │  │ PostgreSQL (5432)│  │  rede interna    │

  └──────────────────┘  └──────────────────┘  └──────────────────┘


A rede interna é criada automaticamente como:  
`desafio3_compose_default`

---

## Como Executar

Dentro da pasta desafio3_compose, rode:

```bash
docker compose up -d
```

Ver containers:
```bash
docker ps
```

Você verá:
- web_service
- db_service
- cache_service

Todos ativos e conectados.

## Testes
### ✔ 1 — Testar o serviço web

```bash
curl localhost:5000
```

Saída:

```bash
{"message":"Aplicação Web no ar (serviço web)!"}
```
### ✔ 2 — Testar o cache (Redis)

```bash
curl localhost:5000/cache
```

Saída:

```bash
{"visitas": 1}
```

Ao repetir:

```bash
{"visitas": 2}
```

Redis funcionando ✔

### ✔ 3 — Testar o PostgreSQL
```bash
curl localhost:5000/db
```
Exemplo de saída:

```bash
{"postgres_version":["PostgreSQL 15.x on Linux ..."]}
```
Conexão com o banco funcionando ✔

## Como parar tudo
```bash
docker compose down
```
Para remover volumes também:

```bash
docker compose down -v
```
## Componentes Entregues
### ✔ Docker Compose cria rede automaticamente

Os serviços se comunicam por hostname (ex: cache, db).

### ✔ Uso de depends_on

Garante ordem de inicialização.

### ✔ Redis como cache

Mantém estado entre requisições.

### ✔ Postgres com volume

Persistência do banco de dados.

### ✔ Web acessa serviços apenas pela rede interna

Boa prática de isolamento.

## Conclusão
O desafio demonstra, na prática, como usar o Docker Compose para orquestrar múltiplos serviços que trabalham juntos em uma arquitetura distribuída.