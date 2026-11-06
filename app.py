from flask import Flask, send_from_directory
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")

@app.route("/style.css")
def css():
    return send_from_directory(BASE_DIR, "style.css")

@app.route("/script.js")
def js():
    return send_from_directory(BASE_DIR, "script.js")

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
