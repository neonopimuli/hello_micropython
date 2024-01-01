from machine import Pin
from tm1637 import TM1637
from time import sleep_ms

tm = TM1637(dio = Pin(26), clk = Pin(27))
# tm.show('abcd')
# tm.number(1234)
# tm.numbers(12,34)
# tm.numbers(12,34,True)
# tm.scroll('Hello World',1000)
# tm.temperature(-9)
# tm.brightness(7)
# tm.brightness(1)

while True:
    for i in range(20):
        print(i)
        tm.number(i)
        sleep_ms(500)
    for i in range(20, 0, -1):
        tm.number(i)
        sleep_ms(500)    
