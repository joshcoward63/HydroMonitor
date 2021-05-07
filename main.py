from flask import Flask, render_template,request, redirect, request
import webbrowser
from time import time
from threading import Timer
import json
import tempRecorder
import dht11

app = Flask(__name__)


"""The Following variables are  placeholders for the temperature readings"""
hourlyLow = 10000
hourlyHigh = -10000
dailyLow = 10000
dailyHigh = -10000
weeklyLow = 10000
weeklyHigh = -10000
monthlyLow = 10000
monthlyHigh = -10000
currentTemp = 0

@app.route('/')
def home():
    return render_template("index.html")

def open_browser():
      webbrowser.open_new('http://0.0.0.0:5000/')

@app.route('/getTemp', methods=['GET'])
def getTemp():
    global currentTemp
    try:
        c, f = tempRecorder.get_temp()
        temp = f
    except:
        temp = 0
        print("Error temperature not read")
    currentTemp = temp
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

@app.route('/getHourly', methods=['GET'])
def getHourly():
    global hourlyHigh
    global hourlyLow
    while True:
        hourlyLow = 10000
        hourlyHigh = -10000
        end = time() + 3600
        while time() < end:
            if currentTemp > hourlyHigh:
                hourlyHigh = currentTemp
            if currentTemp < hourlyLow:
                hourlyLow = currentTemp
            return hourlyLow, hourlyHigh

@app.route('/getDaily', methods=['GET'])
def getDaily():
    global dailyHigh
    global dailyLow
    while True:
        dailyLow = 10000
        dailyHigh = -10000
        end = time() + 86400
        while time() < end:
            print("hello")
            if currentTemp > dailyHigh:
                dailyHigh = currentTemp
            if currentTemp < dailyLow:
                dailyLow = currentTemp

@app.route('/getWeekly', methods=['GET'])
def getWeekly():
    global weeklyHigh
    global weeklyLow
    while True:
        weeklyHigh = 10000
        weeklyLow = -10000
        end = time() + 604800
        while time() < end:
            if currentTemp > weeklyHigh:
                weeklyHigh = currentTemp
            if currentTemp < weeklyLow:
                weeklyLow = currentTemp

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(host='0.0.0.0')
