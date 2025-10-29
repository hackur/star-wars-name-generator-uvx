#!/bin/bash
# Docker Integration Examples for Star Wars Name Generator

echo "========================================================"
echo "Star Wars Name Generator - Docker Integration Examples"
echo "========================================================"
echo ""

echo "=== Example 1: Launch Container with Generated Name ==="
CONTAINER_NAME=$(starwars-namegen --random digits)
echo "Generated container name: $CONTAINER_NAME"
echo "Command: docker run -d --name $CONTAINER_NAME nginx:latest"
echo "(Not executing - demo only)"
echo ""

echo "=== Example 2: Launch Multiple Containers ==="
echo "Launching 5 containers with unique Star Wars names..."
for i in {1..5}; do
    NAME=$(starwars-namegen -c 2 --random hex)
    echo "Container $i: $NAME"
    echo "  → docker run -d --name $NAME nginx:latest"
done
echo "(Not executing - demo only)"
echo ""

echo "=== Example 3: Create Docker Network with Generated Name ==="
NETWORK_NAME=$(starwars-namegen -c 3)
echo "Generated network name: $NETWORK_NAME"
echo "Command: docker network create $NETWORK_NAME"
echo "(Not executing - demo only)"
echo ""

echo "=== Example 4: Reproducible Container Names (CI/CD) ==="
echo "Using seed for consistent naming in CI/CD pipelines..."
SEED=12345
APP_NAME=$(starwars-namegen --seed $SEED -c 2)
DB_NAME=$(starwars-namegen --seed $((SEED + 1)) -c 2)
CACHE_NAME=$(starwars-namegen --seed $((SEED + 2)) -c 2)

echo "Application container: $APP_NAME"
echo "Database container: $DB_NAME"
echo "Cache container: $CACHE_NAME"
echo ""

echo "=== Example 5: Generate docker-compose Service Names ==="
echo "Generating names for docker-compose.yml..."
cat <<EOF
services:
  $(starwars-namegen -c 2 -f snake):
    image: nginx:latest
    ports:
      - "8080:80"

  $(starwars-namegen -c 2 -f snake):
    image: postgres:14
    environment:
      POSTGRES_PASSWORD: secret

  $(starwars-namegen -c 2 -f snake):
    image: redis:7
EOF
echo ""

echo "========================================================"
echo "Docker integration examples completed!"
echo "========================================================"
