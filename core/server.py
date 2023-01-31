from concurrent.futures import as_completed
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

class Server:
    wordlist = []
    server_thread = None

    def __init__(self,serverPort,wordlist):
        self.serverPort = serverPort
        self.wordlist = wordlist 

        with open(wordlist, 'r') as f:
            self.wordlist = f.read().split('\n')
    
    def start_server(self):
        handler = _WordHandler
        handler.wordlist = self.wordlist
        self.server = HTTPServer(('', self.serverPort), handler)
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.start()

    def stop_server(self):
        self.server.shutdown()

class _WordHandler(BaseHTTPRequestHandler):
    wordlist = None
    def log_message(self, format, *args):
        return

    def do_GET(self):
        if self.path == '/words':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin','*')
            self.end_headers()
            self.wfile.write("\n".join(self.wordlist).encode())
