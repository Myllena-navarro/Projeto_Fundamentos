VOLUME=db_volume
IMAGE=db_image
CONTAINER=db_container

echo "==> Criando volume (se não existir)"
docker volume create $VOLUME

echo "==> Buildando imagem"
docker build -t $IMAGE .

echo "==> Executando container para criar o banco e inserir dados"
docker run --name $CONTAINER -v $VOLUME:/data $IMAGE python init_db.py

echo ""
echo "==> Removendo container..."
docker rm $CONTAINER

echo ""
echo "==> Subindo um novo container para LER o banco e provar que os dados persistiram"
docker run --name $CONTAINER -v $VOLUME:/data $IMAGE python read_db.py

echo ""
echo "==> Pronto! Os dados persistiram mesmo após remover o container."
