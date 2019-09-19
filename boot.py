try:
  import usocket as socket
except:
  import socket

from time import sleep

from machine import Pin, I2C
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

import hardware

from sensors import BME280
from wifi import wifi

# ESP32 - Pin assignment
#i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)
# ESP8266 - Pin assignment
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)

wifi.connect()
