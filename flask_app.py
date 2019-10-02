# flask_app.py
from flask import Flask
from flask import jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api')
def hello():
    return jsonify({'username':'thsolomon',
                   'email':'tiegsti.solomon@bbc.co.uk',
                   'id':'WH04M1'})
