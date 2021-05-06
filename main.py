from flask import Flask, render_template,request, redirect, request
import webbrowser
from threading import Timer
import json
import tempRecorder
import dht11

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/startRandomBehavior', methods=['POST'])
def startRandomBehavior(): 
    cozmo_random_behaviors.start()
    return "success"

def open_browser():
      webbrowser.open_new('http://0.0.0.0:5000/')

@app.route('/getTemp', methods=['GET'])
def getTemp():
    try:
        c, f = tempRecorder.get_temp()
        temp = f
    except:
        temp = 0
        print("Error temperature not read")
    return str(temp)

@app.route('/getHumidity', methods=['GET'])
def getHumidity():
    try:
        temp, humidity = dht11.get_temp_humidity()
    except:
        temp = 0
        humidity = 0
        print("Error Humidity not read")
    return str(humidity)

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(host='0.0.0.0')
