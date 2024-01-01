from machine import Pin, PWM, ADC
from tm1637 import TM1637
import time

# Initialize pins and modules
red_led = Pin(32, Pin.OUT)
push_switch = Pin(12, Pin.IN)
tm = TM1637(dio=Pin(26), clk=Pin(27))
inA = PWM(Pin(23))
inB = PWM(Pin(25))
inA.init(freq=10, duty=0)
inB.init(freq=10, duty=0)
pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)

while True:
    if push_switch.value() == 1:
        red_led.value(1)
        
        analog_value = pot.read()
        duty_cycle = int(analog_value * 1023 / 4095)
        inA.duty(0)
        inB.duty(duty_cycle)
        
        if analog_value == 0:
            tm.number(0)
        elif 1000 >= analog_value > 0:
            tm.number(1)
        elif 2000 >= analog_value > 1000:
            tm.number(2)
        elif 3000 >= analog_value > 2000:
            tm.number(3)
        elif 4096 >= analog_value > 3000:
            tm.number(4)
            
        print("Analog Value:", analog_value, "Duty Cycle:", duty_cycle)
        
    else:
        red_led.value(0)
        inA.duty(0)
        inB.duty(0)
        tm.number(0)
        
    time.sleep(0.1)