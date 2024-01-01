from machine import Pin
import time

# 핀 번호 지정
led_red_pin = 32
switch_pin = 12

# LED 핀 모드 설정
red_led = Pin(led_red_pin, Pin.OUT)

# 스위치 핀 모드 설정
push_switch = Pin(switch_pin, Pin.IN)

# 스위치 상태 감지
while True:
    if push_switch.value() == 1:
        red_led.value(1)
        time.sleep(0.2)
        print("on")
    else:
        red_led.value(0)
        time.sleep(0.2)