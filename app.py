from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    port = os.environ.get('PORT', 8080)
    app.run(port=port, host="0.0.0.0")