import http.server
import time
import random
# metrics 서버를 위한 라이브러리
from prometheus_client import start_http_server, Gauge
 
# Gauge metric 정의
INPROGRESS = Gauge('inprogress_requests', 'Number of in-progress requests')
LAST = Gauge('last_time_seconds', 'The last time a request was processed')
 
class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        INPROGRESS.inc()
        # 요청 처리 시간을 랜덤하게 지연시켜 INPROGRESS 상태 유지
        process_time = random.uniform(2.0, 3.0)
        time.sleep(process_time)
         
        # 응답 바이트 수를 다르게 할 수 있도록 랜덤하게 생성
        response_content = f"Hello, Prometheus Gauge! Processed in {process_time:.2f}s".encode()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(response_content)
        LAST.set(time.time())  # 마지막 요청 시간 갱신
        INPROGRESS.dec()
 
 
if __name__ == "__main__":
    print("Starting metric server on port 8000...")
    start_http_server(8000)
     
    print("Starting app server on port 8001...")
    server = http.server.HTTPServer(("0.0.0.0", 8001), MyHandler)
    server.serve_forever()
