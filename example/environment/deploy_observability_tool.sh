#!/bin/bash
# first parameter: deploy_target
deploy_target=$1
if [ -z "$deploy_target" ]; then
  echo "Usage: $0 <deploy_target>"
  exit 1
fi
# Enable deploy_target list
# docker-otel-lgtm
function func_deploy_docker_otel_lgtm() {
    if [[ -d "docker-otel-lgtm" ]]; then
        echo "Directory 'docker-otel-lgtm' already exists. Please remove it before running this script."
    else
        echo "Cloning the docker-otel-lgtm repository..."
        git clone https://github.com/grafana/docker-otel-lgtm.git
    fi
    cd docker-otel-lgtm

    # check docker run 
    docker ps -a |grep "lgtm"
    if [[ $? -eq 0 ]]; then
        echo "LGTM container already exists. Please remove it before running this script."
        exit 1
    fi
    ./run-lgtm.sh &
}

# prometheus
function func_deploy_prometheus() {
    docker ps -a |grep "prometheus"
    if [[ $? -eq 0 ]]; then
        echo "Prometheus container already exists. Please remove it before running this script."
        exit 1
    fi
    docker run --name prometheus -d -p 127.0.0.1:9090:9090 prom/prometheus
}

if [[ "$deploy_target" == "docker-otel-lgtm" ]]; then
  echo "Deploying docker-otel-lgtm..."
  func_deploy_docker_otel_lgtm
elif [[ "$deploy_target" == "prometheus" ]]; then
  echo "Deploying prometheus..."
  func_deploy_prometheus
else
  echo "Unknown deploy target: $deploy_target"
  exit 1
fi
