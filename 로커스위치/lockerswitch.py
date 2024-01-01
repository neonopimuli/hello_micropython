from machine import Pin

# GPIO 핀 번호를 설정
switch = Pin(3, Pin.IN)
led = Pin(27, Pin.OUT)


# 스위치의 상태를 확인
if switch.value() == 1:
    led.on()
elif switch.value() == 0:
    led.off()