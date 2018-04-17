from flask import Flask 

app = Flask(__name__)

@app.route('/')

def home():
    return "Miew Miew"


app.run(port=8000)
