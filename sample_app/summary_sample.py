import http.server
import time
 
from prometheus_client import start_http_server, Summary
# Summary metric 정의
LATENCY = Summary('request_latency_seconds', 'Time spent processing request')
 
class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        start = time.time()
        # 응답 바이트 수를 다르게 할 수 있도록 랜덤하게 생성
        response_content = f"Hello, Prometheus Summary!".encode()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(response_content)
        LATENCY.observe(time.time() - start)  # 요청 처리 시간 관측
 
 
if __name__ == "__main__":
    print("Starting metric server on port 8000...")
    start_http_server(8000)
     
    print("Starting app server on port 8001...")
    server = http.server.HTTPServer(("0.0.0.0", 8001), MyHandler)
    server.serve_forever()
    