#!/bin/bash
if [[ $(docker ps -q -f name=node_exporter) ]]; then
  echo "node_exporter is already running."
  exit 0
fi

# if network monitoring is not exists, create it
if [[ -z $(docker network ls -q -f name=monitoring) ]]; then
  docker network create monitoring
fi

# exclude rslave
docker run -d \
  --net="host" \
  --pid="host" \
  --name=node_exporter \
  -v "/:/host:ro" \
  quay.io/prometheus/node-exporter:latest \
  --path.rootfs=/host
