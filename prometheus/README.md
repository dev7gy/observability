# prometheus
## node_exporter
process_resident_memory_bytes: 노드 익스포터 프로세스가 사용하고 있는 메모리 크기
```PromQL
process_resident_memory_bytes{job="node"}
```

node_network_receive_bytes_total: 네트워크 인터페이스에 수신된 데이터를 바이트 단위로 표시하는 카운트 값
```PromQL
rate(node_network_receive_bytes_total[1m])
```

## alertmanager
https://github.com/prometheus/alertmanager
