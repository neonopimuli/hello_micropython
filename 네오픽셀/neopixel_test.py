from machine import Pin
from neopixel import NeoPixel
from time import sleep

np = NeoPixel(Pin(25), 16)

while True:
    for i in range(16):
        np[i] = (100, 0, 0)
        np.write()
        sleep(1)


