import http.server
import socketserver

# Define the port you want to use
PORT = 8000

# Change to the directory where your HTML file is located
import os
web_dir = os.path.join(os.path.dirname(__file__), '')
os.chdir(web_dir)

# Set up the server
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
    