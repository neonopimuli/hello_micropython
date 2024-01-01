from machine import Pin
#from machine import PWM
from time import sleep

#적외선 측정
pir = Pin(13, Pin.IN)

led = Pin(27, Pin.OUT)


while True:
    if pir.value() == 1:
        print(pir.value())
        print('Human detected')
        led.on()
        sleep(0.1)
    else:
        print(pir.value())
        led.off()
        sleep(0.1)


