from machine import Pin
from time import sleep

g = Pin(27, Pin.OUT)
y = Pin(32, Pin.OUT)
r = Pin(33, Pin.OUT)

t_s = ['SOLID_GRN', 'BLINK_GRN','SOLID_RED', 'SOLID_ORN']

while True:
    for x in t_s:
        if x == 'SOLID_GRN':
            g.on()
            sleep(5)
            g.off()
        if x == 'BLINK_GRN':
            for i in range(4):
                g.on()
                sleep(0.2)
                g.off()
                sleep(0.2)
        
        if x == 'SOLID_RED':
            r.on()
            sleep(6)
            r.off()
        if x == 'SOLID_ORN':
            y.on()
            sleep(1)
            y.off()


