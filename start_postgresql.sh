export $(cat .env-dev)
docker run -d \
  --name dev-postgres-container \
  -e POSTGRES_DB=$POSTGRES_DB \
  -e POSTGRES_USER=$POSTGRES_USER \
  -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD \
  -p 5432:5432 \
  postgres
