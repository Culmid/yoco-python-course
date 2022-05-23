from flask import Flask, request
from dotenv import load_dotenv
from cryptography import rot13

load_dotenv()

app = Flask(__name__)


@app.route("/api/rot13", methods=["GET"])
def rot13_translation():
    return {"text": rot13(request.json["text"])}
