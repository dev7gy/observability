import http.server
import time
 
from prometheus_client import start_http_server, Histogram
# Histogram metric 정의
LATENCY = Histogram('request_latency_seconds', 'Time spent processing request')
 
class MyHandler(http.server.BaseHTTPRequestHandler):
    @LATENCY.time() # time함수 데코레이터를 사용하여 요청 처리 시간을 자동으로 관측
    def do_GET(self):
        # 응답 바이트 수를 다르게 할 수 있도록 랜덤하게 생성
        response_content = f"Hello, Prometheus Histogram!".encode()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(response_content)
 
 
if __name__ == "__main__":
    print("Starting metric server on port 8000...")
    start_http_server(8000)
     
    print("Starting app server on port 8001...")
    server = http.server.HTTPServer(("0.0.0.0", 8001), MyHandler)
    server.serve_forever()
