from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import math
import time
import uuid


def score_transaction(tx):
    reasons = []
    rule_score = 0
    amount = float(tx.get("amount", 0) or 0)
    if amount >= 100_000:
        rule_score += 350
        reasons.append("large_amount")
    if tx.get("country") and tx["country"] not in {"IN", "SG", "AE"}:
        rule_score += 250
        reasons.append("unusual_country")
    if int(tx.get("transactions_last_10m", 0) or 0) >= 5:
        rule_score += 250
        reasons.append("high_velocity")

    # Placeholder anomaly score, not a trained model.
    anomaly_score = min(250, max(0, int((amount - 10_000) / 1_000)))
    if anomaly_score >= 100:
        reasons.append("amount_anomaly_heuristic")

    # Tiny in-memory stand-in for graph signals.
    graph_score = 100 if tx.get("shared_device_fraud_reports", 0) else 0
    if graph_score:
        reasons.append("device_linked_to_report")

    score = min(1000, rule_score + anomaly_score + graph_score)
    action = ("approve" if score < 200 else "step_up" if score < 600
              else "review" if score < 800 else "decline")
    return {
        "transaction_id": tx.get("transaction_id", str(uuid.uuid4())),
        "trace_id": str(uuid.uuid4()),
        "risk_score": score,
        "action": action,
        "signals": {"rules": rule_score, "anomaly_heuristic": anomaly_score,
                    "graph_stub": graph_score},
        "reasons": reasons,
        "prototype_only": True,
    }


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/healthz":
            self._send(200, {"status": "ok", "prototype": True})
        else:
            self._send(404, {"error": "not_found"})

    def do_POST(self):
        if self.path != "/api/v1/transactions":
            return self._send(404, {"error": "not_found"})
        try:
            size = int(self.headers.get("Content-Length", "0"))
            if size <= 0 or size > 64_000:
                return self._send(400, {"error": "invalid_body_size"})
            tx = json.loads(self.rfile.read(size))
            if not isinstance(tx, dict):
                return self._send(400, {"error": "json_object_required"})
            result = score_transaction(tx)
            result["elapsed_ms"] = round((time.perf_counter() - self.server.started) * 1000, 2)
            return self._send(200, result)
        except (ValueError, TypeError, json.JSONDecodeError):
            return self._send(400, {"error": "invalid_json_or_fields"})

    def _send(self, status, payload):
        body = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        print("%s - %s" % (self.address_string(), fmt % args))


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8080), Handler)
    server.started = time.perf_counter()
    print("Rough Aegis demo listening on http://127.0.0.1:8080")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Stopping demo")
        server.server_close()
