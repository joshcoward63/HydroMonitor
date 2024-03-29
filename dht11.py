import time
import board
import adafruit_dht
 
# Initial the dht device, with data pin connected to:
# dhtDevice = adafruit_dht.DHT22(board.D4)
 
# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
dhtDevice = adafruit_dht.DHT11(board.D17, use_pulseio=False)

def get_temp_humidity():
    # Print the values to the serial port
    temperature_c = dhtDevice.temperature
    temperature_f = temperature_c * (9 / 5) + 32
    humidity = dhtDevice.humidity
    # print(
    #     "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
    #         temperature_f, temperature_c, humidity
    #     )
    # )
    return temperature_f, humidity


