#basic setting
from machine import Pin, PWM, ADC
from time import sleep

#segment setting
from machine import Pin
from tm1637 import TM1637
from time import sleep_ms

tm = TM1637(dio = Pin(26), clk = Pin(27))



# fan motor setting

inA = PWM(Pin(23))
inB = PWM(Pin(25))

# 초기화
inA.init(freq=10, duty=0)
inB.init(freq=10, duty=0)

# 아날로그 입력 설정
pin_34 = Pin(34, Pin.IN)
pot = ADC(pin_34)
pot.atten(ADC.ATTN_11DB)

while True:
    analog_value = pot.read()
    
    # 아날로그 값을 PWM의 duty cycle로 변환
    duty_cycle = int(analog_value * 1023 / 4095)
    
    # 팬 모터의 속도를 제어
    inA.duty(0)
    inB.duty(duty_cycle)
    
    print("Analog Value:", analog_value, "Duty Cycle:", duty_cycle)
    sleep(0.1)
    
    
    
#segment output
      
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
    






