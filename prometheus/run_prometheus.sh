#!/bin/bash

# prometheus
function func_deploy_prometheus() { 
    if [[ $(docker ps -q -f name=prometheus)  ]]; then
        echo "Prometheus container already exists. Please remove it before running this script."
        exit 1
    fi
    # if prometheus.yaml is exists, use it as config file
    # in container, the config file is located at /etc/prometheus/prometheus.yml
    if [[ -f "prometheus.yaml" ]]; then
        echo "Using prometheus.yaml as config file."
        docker run --name prometheus -d --net="host" \
            -v $(pwd)/prometheus.yaml:/etc/prometheus/prometheus.yml prom/prometheus
    else
        echo "prometheus.yaml not found. Using default config."
        docker run --name prometheus -d --net="host" \
            prom/prometheus
    fi
}

func_deploy_prometheus
