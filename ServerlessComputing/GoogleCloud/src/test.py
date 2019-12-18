from flask import Flask, request
from resize.main import resize
app = Flask(__name__)

@app.route('/resize', methods = ['POST'])
def index():
    return resize(request)

app.run('127.0.0.1', 8888, debug=True)