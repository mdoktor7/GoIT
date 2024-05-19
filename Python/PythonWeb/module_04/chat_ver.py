import http.server
import socketserver
import socket
import threading
import json
import os
from datetime import datetime
from urllib.parse import urlparse, parse_qs

# Constants
WEB_PORT = 3000
SOCKET_PORT = 5000
HOST = 'localhost'

# Paths
STATIC_DIR = 'static'
TEMPLATES_DIR = 'templates'
STORAGE_DIR = 'storage'
DATA_FILE = os.path.join(STORAGE_DIR, 'data.json')

# Initialize data storage file
if not os.path.exists(STORAGE_DIR):
    os.makedirs(STORAGE_DIR)

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump({}, f)

# HTTP Request Handler
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path == '/':
            self.path = 'templates/index.html'
        elif parsed_path.path == '/message.html':
            self.path = 'templates/message.html'
        elif parsed_path.path.startswith('/static/'):
            self.path = self.path[1:]  # Strip leading '/'
        else:
            self.path = 'templates/error.html'
        
        return super().do_GET()

    def do_POST(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path == '/submit_message':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = parse_qs(post_data.decode('utf-8'))
            username = data.get('username', [''])[0]
            message = data.get('message', [''])[0]
            self.send_to_socket_server(username, message)
            self.send_response(302)
            self.send_header('Location', '/')
            self.end_headers()
        else:
            self.send_error(404, "File not found")

    def send_to_socket_server(self, username, message):
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.sendto(f'{username}::{message}'.encode('utf-8'), (HOST, SOCKET_PORT))

# UDP Socket Server
def udp_socket_server():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((HOST, SOCKET_PORT))
    
    while True:
        data, _ = udp_socket.recvfrom(1024)
        username, message = data.decode('utf-8').split('::')
        timestamp = datetime.now().isoformat()
        with open(DATA_FILE, 'r+') as f:
            messages = json.load(f)
            messages[timestamp] = {'username': username, 'message': message}
            f.seek(0)
            json.dump(messages, f, indent=2)

# Run HTTP Server
def run_http_server():
    handler = MyHandler
    httpd = socketserver.TCPServer((HOST, WEB_PORT), handler)
    print(f"Serving HTTP on port {WEB_PORT}")
    httpd.serve_forever()

# Run UDP Server in a thread
def run_udp_server():
    udp_thread = threading.Thread(target=udp_socket_server)
    udp_thread.daemon = True
    udp_thread.start()

if __name__ == '__main__':
    run_udp_server()
    run_http_server()
