import socketio
import requests
import json
import threading
import time



#Creates the client
sio = socketio.Client()

#Connects to server
sio.connect("http://192.168.0.15:5005")
sio.emit("tits","yeahhhhh")

@sio.on('test')
def message3(data):
   print(data)


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
