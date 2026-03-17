#!/bin/bash

# prometheus
function func_deploy_prometheus() { 
    if [[ $(docker ps -q -f name=prometheus)  ]]; then
        echo "Prometheus container already exists. Please remove it before running this script."
        exit 1
    fi
    # if prometheus.yaml is exists, use it as config file
    # in container, the config file is located at /etc/prometheus/prometheus.yml
    if [[ -f "prometheus_with_alerts.yaml" ]]; then
        echo "Using prometheus_with_alerts.yaml as config file."
        docker run --name prometheus -d --net="host" \
            -v $(pwd)/prometheus_with_alerts.yaml:/etc/prometheus/prometheus.yml \
            -v $(pwd)/rules.yaml:/etc/prometheus/rules.yaml prom/prometheus
    else
        echo "prometheus_with_alerts.yaml not found. Using default config."
        docker run --name prometheus -d --net="host" \
            prom/prometheus
    fi
}

func_deploy_prometheus
