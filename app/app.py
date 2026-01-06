from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest

app = Flask(__name__)
REQUEST_COUNT = Counter("request_count", "Total HTTP Requests")

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return jsonify(message="Updated Flask DevOps App Running AND ACTIVE")

@app.route("/predict")
def predict():
    REQUEST_COUNT.inc()
    return jsonify(prediction=5)

@app.route("/metrics")
def metrics():
    return generate_latest()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
