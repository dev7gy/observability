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
#### Counter 증가 크기 변경
Counter.inc(숫자)
```PromQL
hello_world_response_size_bytes_total
```
### Gauge
게이지가 관심을 두는 것은 실제 값

현재 상태에 대한 스냅샷, 따라서 값은 증가할 수도 감소할 수도 있음

게이지의 예
- 대기열 내의 항목 개수
- 캐시의 메모리 사용량
- 활성 스레드 개수
- 레코드가 처리된 마지막 시간
- 마지막 1분 동안의 초당 평균 요청 개수

### Summary
관측된 값들의 분표와 평균
내부적으로 _count와 _sum이라는 두 개의 시계열을 생성하여 누적 합산
- _count: 관측된 이벤트의 총 개수 (Counter 방식)
- _sum: 관측된 모든 값의 합계 (Counter 방식)
#### 특징
집계(Aggregation) 가능: 여러 인스턴스의 _sum과 _count를 각각 더해 전체 시스템의 평균을 정확히 구할 수 있음
분위수(Quantile) 설정: 클라이언트 측에서 p95, p99 같은 분위수를 직접 계산하도록 설정할 수 있으나, CPU 비용이 높고 여러 인스턴스의 값을 합산할 수 없는 단점이 있음

#### 사용 예
요청 지연 시간(Latency)이나 응답 크기처럼 합계와 개수를 통해 평균을 계산해야 할 때 사용

#### 주의 사항
클라이언트 측 분위수를 사용할 경우, 개별 서버 단위의 지표는 확인 가능하지만 전체 서비스의 분위수를 계산하는 것은 수학적으로 불가능함 (이럴 땐 Histogram 권장)
_sum과 _count는 Counter 성격이므로 애플리케이션 재시작 시 0으로 초기화되지만, Prometheus의 rate 함수가 이를 자동으로 감지하여 처리함

### Histogram

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
