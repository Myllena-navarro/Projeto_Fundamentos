SERVER_HOST=${SERVER_HOST:-server}
SERVER_PORT=${SERVER_PORT:-8080}
SLEEP_SEC=${SLEEP_SEC:-2}

echo "Iniciando cliente que consulta http://$SERVER_HOST:$SERVER_PORT a cada $SLEEP_SEC s"

while true; do
  TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
  echo "[$TIMESTAMP] Fazendo GET /"
  curl --silent --show-error --fail "http://$SERVER_HOST:$SERVER_PORT/" || echo "Erro na requisição"
  echo ""
  sleep $SLEEP_SEC
done
