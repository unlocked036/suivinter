#!/usr/bin/env python3
"""Petit serveur pour la Feuille de route (suivi intermittent).

Sert le fichier index.html présent dans ce même dossier, et expose une API
JSON minimaliste (/api/data) qui écrit les données dans data.json, à côté de
ce script. Toutes les vues de l'appli (Mac mini, téléphone, autre ordinateur
via Tailscale) lisent et écrivent au même endroit : les données sont donc
partagées et synchronisées entre tous vos appareils.

Utilisation :
    python3 server.py
Puis, dans un autre onglet de Terminal :
    tailscale serve --bg 8088

Aucune dépendance à installer : uniquement la bibliothèque standard de Python.
"""
import http.server
import json
import os
import socketserver

PORT = 8088
DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(DIR, "data.json")


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

    def _send_json(self, obj, status=200):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/api/data":
            if os.path.exists(DATA_FILE):
                try:
                    with open(DATA_FILE, "r", encoding="utf-8") as f:
                        obj = json.load(f)
                except (json.JSONDecodeError, OSError):
                    obj = {"entries": [], "anchor": None}
            else:
                obj = {"entries": [], "anchor": None}
            self._send_json(obj)
        else:
            super().do_GET()

    def do_POST(self):
        if self.path != "/api/data":
            self.send_response(404)
            self.end_headers()
            return
        try:
            length = int(self.headers.get("Content-Length", 0))
            raw = self.rfile.read(length)
            obj = json.loads(raw)
        except (ValueError, json.JSONDecodeError):
            self._send_json({"error": "JSON invalide"}, 400)
            return
        if not isinstance(obj, dict) or "entries" not in obj:
            self._send_json({"error": "Format invalide"}, 400)
            return
        tmp = DATA_FILE + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(obj, f, ensure_ascii=False, indent=2)
        os.replace(tmp, DATA_FILE)
        self._send_json({"ok": True})

    def log_message(self, format, *args):
        pass  # terminal silencieux


if __name__ == "__main__":
    with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
        print(f"Feuille de route servie sur http://127.0.0.1:{PORT}")
        print(f"Données stockées dans : {DATA_FILE}")
        print("Ctrl+C pour arrêter.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
