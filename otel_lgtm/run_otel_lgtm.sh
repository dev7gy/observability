#!/bin/bash
# Enable deploy_target list
# docker-otel-lgtm
function func_deploy_docker_otel_lgtm() {
    if [[ -d "docker-otel-lgtm" ]]; then
        echo "Directory 'docker-otel-lgtm' already exists."
    else
        echo "Cloning the docker-otel-lgtm repository..."
        git clone https://github.com/grafana/docker-otel-lgtm.git
    fi

    cd docker-otel-lgtm

    # check docker run 
    if [[ $(docker ps -q -f name=lgtm) ]]; then
      echo "lgtm is already running."
      exit 0
    fi
    ./run-lgtm.sh &
}

func_deploy_docker_otel_lgtm
