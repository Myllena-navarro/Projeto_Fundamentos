# Desafio 2 — Volumes e Persistência com Docker
 
O objetivo é demonstrar como o Docker utiliza **volumes** para manter dados persistentes, mesmo após a remoção de containers.

---

## Objetivo do Desafio

- Criar um container que utiliza um banco de dados SQLite.  
- Mapear um volume Docker para armazenar os dados fora do container.  
- Inserir registros no banco em um container, remover esse container e subir outro container usando o mesmo volume.  
- Demonstrar que os dados continuam disponíveis — prova prática da persistência.

---

## Estrutura do Projeto

desafio2_volumes/

├── Dockerfile

├── init_db.py

├── read_db.py

├── run.sh

└── README.md


- **init_db.py** → cria a tabela e insere os dados  
- **read_db.py** → lê os dados do banco  
- **run.sh** → automatiza todo o processo  
- **Dockerfile** → define a imagem principal  

---

## Arquitetura e Funcionamento

O fluxo da atividade é o seguinte:

┌─────────────────────────┐

│ 1. Container A │

│ - Usa volume /data │

│ - Executa init_db.py │

│ - Cria banco e insere dados │

└───────────────┬─────────┘

│ Volume: db_volume

┌───────────────┴──────────┐

│ 2. Container B │

│ - Usa o mesmo volume /data │

│ - Executa read_db.py │

│ - Lê os mesmos dados │

└───────────────────────────┘


O volume `db_volume` fica separado dos containers.  
Quando um container é removido, **os dados não somem**, porque estão no volume.

---

## Como Executar o Projeto
✔️ Torne o script principal executável:

```bash
chmod +x run.sh
```

✔️ Execute o projeto:
```bash
./run.sh
```

- O script faz automaticamente:
- Cria o volume db_volume
- Builda a imagem db_image
- Sobe o Container 1 e executa init_db.py (cria e insere dados)
- Remove o container
- Sobe o Container 2 para executar read_db.py
- Mostra os dados persistidos

## Exemplo de saída esperada

==> Criando volume (se não existir)

db_volume

==> Buildando imagem

Successfully built 123abc...

==> Executando container para criar o banco e inserir dados

Banco criado e dados inseridos com sucesso!

==> Removendo container...

db_container

==> Subindo um novo container para ler o banco e provar que os dados persistiram

Dados encontrados:

(1, 'Myllena', 'Computação')

(2, 'João', 'Engenharia')

(3, 'Maria', 'ADS')

==> Pronto! Os dados persistiram mesmo após remover o container.

Essa saída comprova que:

✔ os dados foram criados

✔ o container foi removido

✔ outro container acessou o mesmo volume

✔ os dados continuam existindo

## Comandos úteis para o relatório

Ver volumes existentes:

```bash
docker volume ls
```
Inspecionar detalhes do volume:

```bash
docker volume inspect db_volume
```
Ver containers utilizados:

```bash
docker ps -a
```

## Conclusão

Este projeto demonstra de forma simples e prática como funcionam os volumes Docker, garantindo que dados sobrevivam à remoção de containers.