
#POST NOTES: 1.Go to Headers tab
# Key: Content-Type
# Value: application/json

# 2.Go to Body tab: Select raw, Select JSON
# {
#   "text": "first note"
# }

#SEARCH NOTES: http://localhost:8000/notes/search?text=hello
#GET VALUES BY ID: http://localhost:8000/notes/1

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
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

    def get_query(self):
        return parse_qs(urlparse(self.path).query)

    def read_json(self):
        length = int(self.headers.get("Content-Length", 0))
        if length == 0:
            raise ValueError("Empty body")
        return json.loads(self.rfile.read(length))

  
    def do_GET(self):
        path = self.get_path()
        parts = path.split("/")


        if path == "/notes/search":
            query = self.get_query()
            search_text = query.get("text", [None])[0]

            if not search_text:
                self.send_json(400, {"error": "search text is required"})
                return

            result = [
                note for note in notes
                if search_text.lower() in note["text"].lower()
            ]

            self.send_json(200, result)
            return

    
        if path == "/notes":
            self.send_json(200, notes)
            return

   
        if len(parts) == 3 and parts[1] == "notes":
            note_id = parts[2]

            if not note_id.isdigit():
                self.send_json(400, {"error": "Invalid note ID"})
                return

            note_id = int(note_id)

            for note in notes:
                if note["id"] == note_id:
                    self.send_json(200, note)
                    return

            self.send_json(404, {"error": "Note not found"})
            return

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

   
    def do_PUT(self):
        parts = self.get_path().split("/")

        if len(parts) != 3 or parts[1] != "notes":
            self.send_json(404, {"error": "Route not found"})
            return

        note_id = parts[2]

        if not note_id.isdigit():
            self.send_json(400, {"error": "Invalid note ID"})
            return

        note_id = int(note_id)

        try:
            data = self.read_json()
            if "text" not in data:
                self.send_json(400, {"error": "text is required"})
                return

            for note in notes:
                if note["id"] == note_id:
                    note["text"] = data["text"]
                    self.send_json(200, note)
                    return

            self.send_json(404, {"error": "Note not found"})

        except json.JSONDecodeError:
            self.send_json(400, {"error": "Invalid JSON"})


    def do_DELETE(self):
        parts = self.get_path().split("/")

        if len(parts) != 3 or parts[1] != "notes":
            self.send_json(404, {"error": "Route not found"})
            return

        note_id = parts[2]

        if not note_id.isdigit():
            self.send_json(400, {"error": "Invalid note ID"})
            return

        note_id = int(note_id)

        for note in notes:
            if note["id"] == note_id:
                notes.remove(note)
                self.send_json(200, {"message": "Note deleted"})
                return

        self.send_json(404, {"error": "Note not found"})


def run():
    server = HTTPServer((HOST, PORT), NotesHandler)
    print(f"Server running at http://{HOST}:{PORT}")
    server.serve_forever()


if __name__ == "__main__":
    run()