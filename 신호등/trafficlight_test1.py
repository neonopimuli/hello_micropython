from machine import Pin
from time import sleep

g = Pin(27, Pin.OUT)
y = Pin(32, Pin.OUT)
r = Pin(33, Pin.OUT)

led = [g,y,r]

while True:
    for x in range(3):
        print(x)
        led[x].on()
        sleep(1)
        led[x].off()
        sleep(1)
