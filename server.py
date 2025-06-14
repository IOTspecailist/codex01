from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

MESSAGE_FILE = "message.txt"
WEB_DIR = "webpage"

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ('/', '/index.html'):
            try:
                with open(f'{WEB_DIR}/index.html', 'rb') as f:
                    content = f.read()
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                self.wfile.write(content)
            except FileNotFoundError:
                self.send_error(404)
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path == '/save':
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length).decode('utf-8')
            data = parse_qs(body)
            message = data.get('message', [''])[0]
            with open(MESSAGE_FILE, 'w', encoding='utf-8') as f:
                f.write(message)
            self.send_response(303)
            self.send_header('Location', '/')
            self.end_headers()
        else:
            self.send_error(404)

def run(server_class=HTTPServer, handler_class=SimpleHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print('Serving on http://localhost:8000')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
