from flask import Flask, jsonify, request

app = Flask(__name__)

API_KEY = "MY_SECRET_KEY_123"  # hardcoded key

@app.before_request
def check_api_key():
    provided = request.headers.get("X-API-Key") or request.args.get("api_key")
    if provided != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401

@app.route("/", methods=["GET"])
def hello():
    return jsonify({"message": "Hello, World!", "source": "Flask on PythonAnywhere"})

@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"ok": True, "path": "ping"})
