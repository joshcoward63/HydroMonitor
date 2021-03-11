

DHT11 requirements:

sudo apt-get update
sudo apt-get install build-essential python-dev python-openssl git
sudo pip3 install adafruit-circuitpython-dht
sudo apt-get install libgpiod2


DS18B20 requiremnts:
1. At the command prompt, enter sudo nano /boot/config.txt, then add this to the bottom of the file:

dtoverlay=w1-gpio

2. Exit Nano, and reboot the Pi with sudo reboot

3. Log in to the Pi again, and at the command prompt enter sudo modprobe w1-gpio

4. Then enter sudo modprobe w1-therm

5. Change directories to the /sys/bus/w1/devices directory by entering cd /sys/bus/w1/devices

6. Now enter ls to list the devices:
 Should display an address that looks like 28-XXXXXXXXXXX next to w1_bus_master1