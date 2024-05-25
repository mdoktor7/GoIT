import os
import json
import socket
import threading
import datetime
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

# Server configuration
HTTP_HOST = '0.0.0.0'
HTTP_PORT = 3000
SOCKET_HOST = '0.0.0.0'
SOCKET_PORT = 5000

storage_dir = 'storage'
os.makedirs(storage_dir, exist_ok=True)

class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/templates/index.html'
        elif self.path == '/message.html':
            self.path = '/templates/message.html'
        elif self.path.startswith('/static/'):
            pass
        else:
            self.path = '/templates/error.html'
        return super().do_GET()

    def do_POST(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path == '/submit_message':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = parse_qs(post_data.decode())
            message = {
                'username': data['username'][0],
                'message': data['message'][0]
            }
            self.send_to_socket_server(message)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Message received")
        else:
            self.send_error(404)
            self.path = '/templates/error.html'
            return super().do_GET()

    def send_to_socket_server(self, message):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        message_bytes = json.dumps(message).encode()
        sock.sendto(message_bytes, (SOCKET_HOST, SOCKET_PORT))
        sock.close()

def handle_socket_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((SOCKET_HOST, SOCKET_PORT))
    while True:
        data, addr = sock.recvfrom(1024)
        if not data:
            continue
        message = json.loads(data.decode())
        timestamp = datetime.datetime.now().isoformat()
        json_file = os.path.join(storage_dir, 'data.json')
        if os.path.exists(json_file):
            with open(json_file, 'r') as f:
                messages = json.load(f)
        else:
            messages = {}
        messages[timestamp] = message
        with open(json_file, 'w') as f:
            json.dump(messages, f, indent=2)

def run_http_server():
    server_address = (HTTP_HOST, HTTP_PORT)
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    print(f"HTTP server running on {HTTP_HOST}:{HTTP_PORT}")
    httpd.serve_forever()

def run_socket_server():
    print(f"Socket server running on {SOCKET_HOST}:{SOCKET_PORT}")
    handle_socket_client()

if __name__ == "__main__":
    threading.Thread(target=run_http_server).start()
    threading.Thread(target=run_socket_server).start()
