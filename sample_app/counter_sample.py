import http.server
from prometheus_client import start_http_server
from prometheus_client import Counter

# 메트릭 정의 부분
# Counter는 특정 이벤트가 발생한 횟수를 세는 메트릭입니다.
# 카운터 지정 및 도움말 문구 설정 (메트릭 이름은 'hello_world_total'로 설정)
# 도움말 문구는 /metrics 페이지에 표시
# 메트릭은 기본 레지스트리 내의 클라이언트 라이브러리와 함께 자동으로 등록되므로, (java, golang은 별도 작업 필요할 수 있음)
# 메트릭을 start_http_server 호출로 다시 끌어올 필요가 없음
# 실제로 코드의 계측 방법은 결과를 게시하는 부분과 완전히 분리됨.
# 프로메테우스의 계측을 포함하는 일시적인 의존성이 있다면, /metrics에 의존성이 자동으로 표시됨
# 메트릭은 고유한 이름을 가져야 하며, 같은 메트릭을 두 번 정의하면 오류가 발생
# 이를 방지하려면 메트릭을 클래스나 함수 혹은 메소드 수준이 아닌 파일 수준에서 정의하는 것이 좋음
REQUESTS = Counter('hello_world_total', 'Hello World requested')
# PromQL으로 쿼리시 rate(hello_world_total[1m])라고 하면, 지난 1분 동안의 요청 수의 증가율을 계산할 수 있음
class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # 계측 부분
        # 프로메테우스 클라이언트 라이브러리는 Bookeeping과 thread-safety 같은 세부사항을 모두 처리하므로, 
        # 단순히 카운터를 증가시키는 것만으로 계측이 가능
        REQUESTS.inc()  # 요청이 들어올 때마다 카운터 증가
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, World!')

if __name__ == '__main__':
    # Start the Prometheus metrics server on port 8000
    start_http_server(8000)
    print("Prometheus metrics server started on port 8000")
    
    # Start the HTTP server to serve requests
    server_address = ('', 8001)
    httpd = http.server.HTTPServer(server_address, MyHandler)
    print("HTTP server started on port 8001")
    httpd.serve_forever()
