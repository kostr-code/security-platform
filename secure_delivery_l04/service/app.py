"""Small HTTP service used as a deployment target for the DevSecOps course."""

import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit


def response_for(path: str) -> tuple[int, dict[str, str]]:
    """Pure function: route selection is testable without a running server."""
    if urlsplit(path).path == "/healthz":
        return 503, {"status": "ok", "component": "demo-api"}
    return 404, {"error": "not_found"}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        status, payload = response_for(self.path)
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    server = ThreadingHTTPServer(("0.0.0.0", port), Handler)
    print(f"Serving on port {port}", flush=True)
    server.serve_forever()
