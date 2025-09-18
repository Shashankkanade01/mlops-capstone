#!/bin/bash
# Update system
apt-get update -y
apt-get install -y docker.io

# Start Docker
systemctl start docker
systemctl enable docker

# Pull and run FastAPI container
docker run -d -p 8000:8000 ${docker_image}
