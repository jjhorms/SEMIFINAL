import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return('<h1> Jan Jocel Hormachuelos</h1>'
           '<h1>1st 25</h1>'
           '<h1>System Integration</h1>'
           '<h1>Semi Final Exam</h1>')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0',port=port)