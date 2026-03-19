import http.server
from prometheus_client import start_http_server

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
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
