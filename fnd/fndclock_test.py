from machine import Pin
from tm1637 import TM1637
from machine import RTC
from time import sleep_ms

tm = TM1637(dio = Pin(26), clk = Pin(27))
rtc = RTC()
rtc.datetime((2023,9,18,1, 21,24,00,00))
isPoint = True
# tm.show('abcd')
# tm.number(1234)
# tm.numbers(12,34)
# tm.numbers(12,34,True)
# tm.scroll('Hello World',1000)
# tm.temperature(-9)
# tm.brightness(7)
# tm.brightness(1)

while True:
    t = rtc.datetime()
    tm.numbers(t[4],t[5],isPoint)
    sleep_ms(200)
    isPoint = not isPoint
