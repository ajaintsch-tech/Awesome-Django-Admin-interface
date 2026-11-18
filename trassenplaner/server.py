#!/usr/bin/env python3
"""Startet den DB InfraGO Trassenplaner lokal (nur Python-Standardbibliothek).

Aufruf:  python3 trassenplaner/server.py [--port 8000] [--host 127.0.0.1]
"""
import argparse
import functools
import http.server
import os
import socketserver

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    parser = argparse.ArgumentParser(description="Trassenplaner Preview-Server")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=int(os.environ.get("PORT", "8000")))
    args = parser.parse_args()

    handler = functools.partial(
        http.server.SimpleHTTPRequestHandler, directory=HERE
    )
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer((args.host, args.port), handler) as httpd:
        print(f"Trassenplaner läuft auf http://{args.host}:{args.port}/ (Strg+C beendet)")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nBeendet.")


if __name__ == "__main__":
    main()
