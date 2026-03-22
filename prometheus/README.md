# Metric
## Metric 유형
### Counter
이벤트 개수나 크기를 추적하며, 주로 특정 경로의 코드가 얼마나 자주 실행되는지 추적하는데 사용
```PromQL
rate(hello_world_total[1m])
```
#### 카운팅 예외 처리
```PromQL
rate(hello_world_exceptions_total[1m])
```
얼마나 많은 요청이 처리되었는지 알지 못하면, 예외 개수는 유횽하지 않음
수직 브라우저에서 다음 식을 사용해서 더 유용한 예외 비율을 계산 할 수 있음
```PromQL
rate(hello_world_exceptions_total[1m]) / rate(hello_world_total[1m])
```
# prometheus
https://prometheus.io/download/
https://hub.docker.com/r/prom/prometheus

## With Node Exporter
process_resident_memory_bytes: 노드 익스포터 프로세스가 사용하고 있는 메모리 크기
```PromQL
process_resident_memory_byts{job="node"}

node_network_receive_bytes_total: 네트워크 인터페이스에 수신된 데이터를 바이트 단위로 표시하는 카운트 값
```PromQL
rate(node_network_receive_bytes_total[1m])
```
