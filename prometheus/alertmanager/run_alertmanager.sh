#!/bin/bash
if [[ $(docker ps -q -f name=alertmanager) ]]; then
  echo "Alertmanager is already running."
  exit 0
fi

docker run --name alertmanager -d \
   --net="host" \
   --name=alertmanager \
   -v $(pwd)/alertmanager.yml:/etc/alertmanager/alertmanager.yml \
   quay.io/prometheus/alertmanager
