from flask import Flask
from config import Config

app = Flask(__name__)

@app.route("/home")
def home():
    return (index.html)

def top5():
    return (top5.html)

if __name__ == "__name__":
    app.run()