#NOTES


from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import json

HOST = "localhost"
PORT = 8000

notes = []

class NotesHandler(BaseHTTPRequestHandler):

    def send_json(self, status, data):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def get_path(self):
        return urlparse(self.path).path

    def read_json(self):
        length = int(self.headers.get("Content-Length", 0))
        if length == 0:
            raise ValueError("Empty body")
        return json.loads(self.rfile.read(length))

    def do_GET(self):
        if self.get_path() == "/notes":
            self.send_json(200, notes)
        else:
            self.send_json(404, {"error": "Route not found"})

    def do_POST(self):
        if self.get_path() != "/notes":
            self.send_json(404, {"error": "Route not found"})
            return

        try:
            data = self.read_json()
            if "text" not in data:
                self.send_json(400, {"error": "text is required"})
                return

            note = {"id": len(notes) + 1, "text": data["text"]}
            notes.append(note)
            self.send_json(201, note)

        except json.JSONDecodeError:
            self.send_json(400, {"error": "Invalid JSON"})
        except ValueError as e:
            self.send_json(400, {"error": str(e)})

def run():
    server = HTTPServer((HOST, PORT), NotesHandler)
    print(f"Server running at http://{HOST}:{PORT}")
    server.serve_forever()

if __name__ == "__main__":
    run()
