#!/bin/bash
# Docker Integration Examples
# CONTAINER FLEET NAMING PROTOCOLS

echo "================================================"
echo "Docker Integration - Container Naming Examples"
echo "================================================"
echo ""

echo "=== Scenario 1: Launch Container Fleet with Unique Names ==="
echo "Generating 5 container names..."
for i in {1..5}; do
    CONTAINER_NAME=$(starwars-namegen -c 2 -f kebab --random digits)
    echo "Container $i: $CONTAINER_NAME"
    # Example command (commented out to avoid actually creating containers):
    # docker run -d --name $CONTAINER_NAME nginx:alpine
done
echo ""

echo "=== Scenario 2: Database Containers with Descriptive Names ==="
echo "Generating 3 database instance names..."
for i in {1..3}; do
    DB_NAME=$(starwars-namegen -c 2 -f snake --random hex)
    echo "Database $i: db_${DB_NAME}"
    # Example command:
    # docker run -d --name db_${DB_NAME} postgres:latest
done
echo ""

echo "=== Scenario 3: Microservices Architecture ==="
echo "Generating service names for different components..."
API_NAME=$(starwars-namegen -c 2 -f kebab --random digits)
WORKER_NAME=$(starwars-namegen -c 2 -f kebab --random digits)
CACHE_NAME=$(starwars-namegen -c 2 -f kebab --random digits)
QUEUE_NAME=$(starwars-namegen -c 2 -f kebab --random digits)

echo "API Service: $API_NAME"
echo "Worker Service: $WORKER_NAME"
echo "Cache Service: $CACHE_NAME"
echo "Queue Service: $QUEUE_NAME"
echo ""

echo "=== Scenario 4: Reproducible Deployment Names ==="
echo "Using seed for consistent naming across environments..."
SEED_VALUE=12345
PROD_NAME=$(starwars-namegen --seed $SEED_VALUE -c 3 -f kebab)
echo "Production deployment (seed $SEED_VALUE): $PROD_NAME"
echo "Running again with same seed:"
PROD_NAME_2=$(starwars-namegen --seed $SEED_VALUE -c 3 -f kebab)
echo "Production deployment (seed $SEED_VALUE): $PROD_NAME_2"
echo "Names match: $([ "$PROD_NAME" = "$PROD_NAME_2" ] && echo 'YES' || echo 'NO')"
echo ""

echo "================================================"
echo "Docker integration examples completed!"
echo "================================================"
