import socket
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hell, my container is named: " + socket.gethostname()

