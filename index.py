from flask import Flask, request, jsonify

app = Flask(__name__)

API_KEY = "MY_SECRET_KEY_123"

@app.before_request
def check_api_key():
    provided = request.headers.get("X-API-Key") or request.args.get("api_key")
    if provided != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401

@app.route("/", methods=["GET"])
def hello():
    return jsonify({"message": "Hello, World!", "source": "Flask on Vercel"})

@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"ok": True, "path": "ping"})

# Expose WSGI app for Vercel via serverless-wsgi
# Vercel will call this handler
def handler(environ, start_response):
    from werkzeug.middleware.dispatcher import DispatcherMiddleware
    return app.wsgi_app(environ, start_response)
