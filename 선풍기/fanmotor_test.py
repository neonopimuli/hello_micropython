from machine import Pin
from machine import PWM
from time import sleep



# fan motor 설정 
inA = PWM(Pin(23))
inB= PWM(Pin(25))

#초기화 명령
inA.init(freq=10, duty=0)
inB.init(freq=10, duty=0)