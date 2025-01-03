import http.server
import socketserver
import random

PORT = 80

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        random_number = random.randint(1, 100)
        self.wfile.write(bytes(f"Your random number is: {random_number}", "utf-8"))

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving on http://localhost:{PORT}")
    httpd.serve_forever()