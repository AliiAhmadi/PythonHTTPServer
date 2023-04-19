from http.server import HTTPServer, BaseHTTPRequestHandler


# HOST = "<YOUR-IP-ADDRESS>"
# PORT = "<YOUR-PORT-NUMBER>"

HOST = "localhost" # "<YOUR-IP-ADDRESS>"
PORT = 3322 # "<YOUR-PORT-NUMBER>"


class HTTP(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write("hello")
        
    
    def do_POST(self):
        self.wfile.write("Post")
        

server = HTTPServer((HOST, PORT), HTTP)

print("===== Serving Started =====")
server.serve_forever()
server.server_close()
print("===== Serving Stopped =====")
