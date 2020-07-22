from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import json as jn
import pandas as pd
import numpy as np
import pymongo
from datetime import datetime
import time
app = Flask(__name__)
socketio = SocketIO(app)

final_vals =[]
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydata_vision"]
mycol = mydb["my_data"]
@app.route('/')
def home():
    print("SERVER STARTED")
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    print("SOCKET CONNECTED")

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: '+ str(json))
    if(str(json) !="{'data': []}"):
      ts = time.time()
      dt_object = datetime.fromtimestamp(ts)
      print("############################")
      valid_json_string = "[" + jn.dumps(json) + "]" 
      data = jn.loads(valid_json_string)[0]
      print("\n EXPRESSOIONS \n")
      print(data["data"][0]["expressions"]) # now we can choose any type of expresiosn we want
      final_vals.append(data["data"][0]["expressions"])
      sd =data["data"][0]["expressions"]
      sd["time"]=dt_object
     # mycol.insert_one(data["data"][0]["expressions"])
      mycol.insert_one(sd)
    
if __name__ == '__main__':
    socketio.run(app)