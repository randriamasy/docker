#!/bin/bash

# Construire les images Docker
docker-compose build

# Lancer les conteneurs Docker Compose
docker-compose up
# Combine logs from all test containers
mkdir -p logs
docker-compose logs test_authentification > logs/test_authentification.log
docker-compose logs test_authorization > logs/test_authorization.log
docker-compose logs test_content > logs/test_content.log

# Combine all logs into a single log file
cat logs/test_authentification.log logs/test_authorization.log logs/test_content.log > logs/api_test.log

echo "Logs combined into logs/api_test.log"