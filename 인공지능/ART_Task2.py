from machine import Pin
from time import sleep
from machine import PWM
from machine import UART
from machine import SoftI2C
from i2c_lcd import I2cLcd

uart = UART(2, baudrate=115200, tx=17, rx=16)
uart.init(115200, bits=8, parity=None, stop=1)

inA = PWM(Pin(23))
inB = PWM(Pin(25))
inA.init(freq=10, duty=0)
inB.init(freq=10, duty=0)
inA.duty(0)
inB.duty(0)

g = Pin(27, Pin.OUT)
y = Pin(32, Pin.OUT)
r = Pin(33, Pin.OUT)
y.off()
g.off()
r.off()

i2c = SoftI2C(scl=Pin(21), sda=Pin(19), freq=400000)
lcd = I2cLcd(i2c, 0x20, 2, 16)
lcd.clear()

while True:
    if uart.any() > 0:
        data = uart.read()
        data = data[0]
        print(data)
        

        if data == 49:
            lcd.clear()
            lcd.putstr('step1')
            inB.duty(200)
            g.on()
            y.off()
            r.off()
        elif data == 50:
            lcd.clear()
            lcd.putstr('step2')
            y.on()
            g.off()
            r.off()
            inB.duty(400)
        elif data == 51:
            lcd.clear()
            lcd.putstr('stop')
            y.off()
            g.off()
            r.on()
            inB.duty(0)
      