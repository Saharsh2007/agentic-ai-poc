from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, World!"

@app.route('/health')
def health():
    return "OK", 200