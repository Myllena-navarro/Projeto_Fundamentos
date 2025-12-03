set -e

NETWORK_NAME="rede_desafio1"
SERVER_IMG="desafio1_server"
CLIENT_IMG="desafio1_client"
SERVER_CONTAINER="desafio1_server_ctr"
CLIENT_CONTAINER="desafio1_client_ctr"

case "$1" in
  up)
    echo "==> Criando rede Docker '$NETWORK_NAME' (se não existir)"
    docker network inspect $NETWORK_NAME >/dev/null 2>&1 || docker network create $NETWORK_NAME

    echo "==> Buildando imagem do servidor"
    docker build -t $SERVER_IMG ./server

    echo "==> Buildando imagem do cliente"
    docker build -t $CLIENT_IMG ./client

    echo "==> Rodando servidor (nome: $SERVER_CONTAINER) na rede $NETWORK_NAME"
    docker run -d --name $SERVER_CONTAINER --network $NETWORK_NAME -p 8080:8080 $SERVER_IMG

    echo "==> Rodando cliente (nome: $CLIENT_CONTAINER) na rede $NETWORK_NAME"
    docker run -d --name $CLIENT_CONTAINER --network $NETWORK_NAME -e SERVER_HOST=$SERVER_CONTAINER $CLIENT_IMG

    echo "==> Tudo rodando. Use: docker logs -f $CLIENT_CONTAINER  para ver as requisições do cliente"
    echo "==> Use: docker logs -f $SERVER_CONTAINER  para ver os logs do servidor (se você logasse no servidor)"
    ;;

  down)
    echo "==> Parando e removendo containers e rede"
    docker rm -f $CLIENT_CONTAINER $SERVER_CONTAINER >/dev/null 2>&1 || true
    docker rmi -f $CLIENT_IMG $SERVER_IMG >/dev/null 2>&1 || true
    docker network rm $NETWORK_NAME >/dev/null 2>&1 || true
    echo "==> Limpou tudo."
    ;;

  *)
    echo "Uso: $0 {up|down}"
    exit 1
    ;;
esac
