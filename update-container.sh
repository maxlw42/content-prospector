#!/bin/sh
CONTAINER_NAME=$1
IMAGE_NAME=content-prospector

if [ -z "$CONTAINER_NAME" ]
then
      echo "Error: no container name specified to update"
      exit 1
fi

# remove existing resources
docker stop ${CONTAINER_NAME}
docker container rm ${CONTAINER_NAME}
docker image rm ${IMAGE_NAME}

# start up container with updated code
docker build -t ${IMAGE_NAME} .
docker run -dp 1544:1544 ${IMAGE_NAME}