import socketio
import requests
import json
import threading
import time
import tempRecorder
import dht11


#Creates the client
sio = socketio.Client()

#Connects to server
sio.connect("http://192.168.0.15:5005")

#The Following variables are  placeholders for the temperature readings
hourlyLow = 10000
hourlyHigh = -10000
dailyLow = 10000
dailyHigh = -10000
weeklyLow = 10000
weeklyHigh = -10000
monthlyLow = 10000
monthlyHigh = -10000
currentTemp = 0


def getTemp():
    global currentTemp
    while True:
        time.sleep(30)
        try:
            c, f = tempRecorder.get_temp()
            temp = f
        except:
            temp = 0
            print("Error temperature not read")
        currentTemp = temp
        sio.emit("temp", str(temp))

def getHumidity():
    while True:
        time.sleep(30)
        try:
            temp, humidity = dht11.get_temp_humidity()
        except:
            temp = 0
            humidity = 0
            print("Error Humidity not read")
        sio.emit("humidity", str(humidity))

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
        sio.emit("hourly", hourlyLow, hourlyHigh)

def getDaily():
    global dailyHigh
    global dailyLow
    while True:
        dailyLow = 10000
        dailyHigh = -10000
        end = time() + 86400
        while time() < end:
            if currentTemp > dailyHigh:
                dailyHigh = currentTemp
            if currentTemp < dailyLow:
                dailyLow = currentTemp
        sio.emit("daily", hourlyLow, hourlyHigh)


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
        sio.emit("weekly", hourlyLow, hourlyHigh)




# When the socket connects    
@sio.event
def connect():
    print("I'm connected!")

# When the socket has an error
@sio.event
def connect_error():
    print("The connection failed!")

# When the socket disconnects
@sio.event
def disconnect():
    print("I'm disconnected!")    


if __name__=='__main__':
    thread1 