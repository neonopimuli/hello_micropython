from machine import Pin
from machine import SoftI2C
from i2c_lcd import I2cLcd
from time  import sleep

i2c = SoftI2C(scl=Pin(21), sda=Pin(19), freq = 400000)
lcd = I2cLcd(i2c, 0x20, 2, 16)
lcd.clear()
count = 0

while True:
    print('Counter:{}'.format(count))
    lcd.clear()
    lcd.putstr('Counter:{}'.format(count))
    count = count + 1
    sleep(1)
