# 🚀 Desafio 1 — Containers em Rede (Docker)
 
O objetivo deste desafio é demonstrar a comunicação entre dois containers Docker conectados a uma **rede customizada**, utilizando um servidor web simples e um cliente que realiza requisições periódicas.

---

##  Objetivo do Desafio

- Criar uma rede Docker personalizada  
- Executar dois containers conectados à mesma rede  
- Container 1 → Servidor Flask (porta 8080)  
- Container 2 → Cliente realizando requisições HTTP periódicas via `curl`  
- Demonstrar comunicação entre containers através de logs  
- Organizar o projeto com scripts e documentação  

---

## Arquitetura do Projeto

A arquitetura consiste em:

┌───────────────────────────────────┐

│ Container Servidor (Flask) │ │ Container Cliente (Curl) │

│ - Porta 8080 │ <────> │ - Executa loop de req. │

│ - Responde JSON │ │ - Envia GET a cada 2s │

└───────────────────────────────────┘ 

│ │
└────────── Rede Docker ─────────────┘

Ambos os containers estão conectados à rede `rede_desafio1`, criada pelo script `network.sh`.

---

## Estrutura do Projeto

desafio1_rede/

├── server/

│ ├── app.py

│ └── Dockerfile

├── client/

│ ├── loop.sh

│ └── Dockerfile

├── network.sh

└── README.md


Cada componente foi separado para facilitar manutenção e entendimento.

---

## Como Executar (Linux)

### 1. Dar permissão aos scripts

```bash
chmod +x network.sh
chmod +x client/loop.sh
```

`./network.sh up`

O script irá:

✔ Criar a rede rede_desafio1

✔ Buildar a imagem do servidor

✔ Buildar a imagem do cliente

✔ Executar ambos os containers conectados à rede


## Testando a Comunicação
### 1. Logs do Cliente (mostra as requisições acontecendo)

```bash
docker logs -f desafio1_client_ctr
```

Exemplo real:

```bash
[2025-12-02 03:35:17] Fazendo GET /
{"host":"256d6a3e95a7","message":"Olá do servidor Flask!","time":"2025-12-02 03:35:17"}
```

### 2. Testando o servidor via navegador ou curl

```bash
curl localhost:8080
```

Resposta esperada:
```bash
{
  "message": "Olá do servidor Flask!",
  "time": "2025-12-02 03:35:23",
  "host": "desafio1_server_ctr"
}
```

## Inspeção da Rede Docker

Para validar que ambos estão na mesma rede:
```bash
docker network inspect rede_desafio1
```

Trecho esperado:
```bash
"Containers": {
    "desafio1_server_ctr": {
        "Name": "desafio1_server_ctr",
        "IPv4Address": "172.20.0.2/16"
    },
    "desafio1_client_ctr": {
        "Name": "desafio1_client_ctr",
        "IPv4Address": "172.20.0.3/16"
    }
}
```

Isso prova que os containers compartilham a mesma rede.

## Como remover tudo
```bash
./network.sh down
```

Limpa:

- containers
- imagens
- rede

## Explicação Técnica

### ✔ Uso de rede customizada

Utilizamos:

```bash
docker network create rede_desafio1
```

Isso permite:

- Comunicação interna por hostname
- Isolamento da aplicação
- Resolução automática de nomes entre containers

✔ Comunicação entre containers

O cliente acessa o servidor usando o nome do container, por exemplo:

```bash
SERVER_HOST=desafio1_server_ctr
```

O Docker resolve automaticamente para o IP interno.

### ✔ Servidor Flask

Escolhido por:

- código simples
- resposta em JSON
- facilidade de log e testes

### ✔ Cliente curl em loop

Simula tráfego contínuo de um serviço real.

## Conclusão

Este projeto demonstra de forma clara como:

- Criar e utilizar redes Docker personalizadas
- Estabelecer comunicação entre containers isolados
- Utilizar scripts para automação
- Organizar a estrutura de um microprojeto real