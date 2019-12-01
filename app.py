from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import json
import DataAccess as DA

app=Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'hello world '

@app.route('/users', methods=['GET'])
def get_users():
    rows=DA.get_rows()
    return jsonify(rows)
@app.route('/users',methods=['POST'])
def add_user():    
    
    user=(request.json['name'],request.json['age'],request.json['email'])
    lastrowid= DA.add_user(user)
    return jsonify(lastrowid)

if __name__=='__main__':
    app.run()
