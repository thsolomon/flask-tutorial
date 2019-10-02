# flask_app.py
from flask import Flask
from flask import jsonify
import pandas as pd

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api')
def details_dict():
    return ({ 'username':'thsolomon',
               'email':'tiegsti.solomon@bbc.co.uk',
               'id':'WH04M1'})


@app.route('/api_v2')
def details_dict_json():
    return pd.DataFrame([{ 'username':'thsolomon',
               'email':'tiegsti.solomon@bbc.co.uk',
               'id':'WH04M1'}]).to_json(orient='records')