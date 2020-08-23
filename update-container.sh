#!/bin/sh
CONTAINER_NAME=docker_content_prospector
IMAGE_NAME=content-prospector

# remove existing resources
echo "Stopping old container..."
docker stop ${CONTAINER_NAME}
echo "Removing old container..."
docker container rm ${CONTAINER_NAME}
echo "Removing old image..."
docker image rm ${IMAGE_NAME}

# start up container with updated code
echo "Building new image..."
docker build -t ${IMAGE_NAME} .
echo "Starting new container..."
docker run --name ${CONTAINER_NAME} -dp 1544:1544 ${IMAGE_NAME}