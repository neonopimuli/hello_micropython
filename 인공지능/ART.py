# 라이브러리 설정
from machine import Pin  # 마이크로컨트롤러의 핀을 다루는 기능을 제공하는 라이브러리
from machine import PWM  # 펄스 폭 변조(PWM) 신호를 생성하는 기능을 제공하는 라이브러리
from time import sleep  # 시간과 관련된 기능을 제공하는 라이브러리
from machine import UART  # 시리얼 통신을 위한 기능을 제공하는 라이브러리
from machine import SoftI2C  # I2C 통신을 위한 기능을 제공하는 라이브러리
from i2c_lcd import I2cLcd  # LCD 화면을 다루는 기능을 제공하는 라이브러리
from mg90s_servo import MG90S_SERVO  # 서보 모터를 다루는 기능을 제공하는 라이브러리
from neopixel import NeoPixel  # Neopixel LED를 다루는 기능을 제공하는 라이브러리

# 핀연결 번호  
# UART 16,17
# LCD 21,22
# 네오픽셀 25,26,27
# 서보모터 27, 32, 33

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000)  # I2C 통신을 위한 초기 설정
lcd = I2cLcd(i2c, 0x20, 2, 16)  # LCD 초기 설정
lcd.clear()
servo = MG90S_SERVO(signal_pin=27)  # 서보모터 초기 설정
servo.rotate(90)
np = NeoPixel(Pin(25), 16)  # Neopixel 초기 설정
uart = UART(2, baudrate=115200, tx=17, rx=16)  # UART 통신을 위한 초기 설정
uart.init(115200, bits=8, parity=None, stop=1)  # UART 설정 초기화

# UART 통신 설명
# tx는 출력을 의미하고 rx는 입력을 의미합니다.
# UART tx 핀은 16번에 연결되어 있지만 esp32 입장에서는 받는 포트이므로 rx는 16번입니다.
# uart=UART(1, baudrate=9600, tx=1, rx=3) # 주석 처리된 코드는 다른 설정 예시입니다.

# 핀설정
# r = Pin(23, Pin.OUT)
# g = Pin(25, Pin.OUT)
# b = Pin(26, Pin.OUT)
# 
# def set_rgb(x, y, z):
#     r.value(x)
#     g.value(y)
#     b.value(z)
#     
# def rst_rgb():
#     r.off()
#     g.off()
#     b.off()
# 위의 코드는 주석 처리되어 있어 사용되지 않습니다.

uart.write("hello world")  # UART를 통해 "hello world"를 전송합니다.

while True:
    if uart.any() > 0:  # UART로부터 데이터가 수신되었는지 확인
        data = uart.read()  # 수신된 데이터를 읽어옴
        data = data[0]  # 수신된 데이터의 첫 번째 바이트를 사용합니다.
        print(data)  # 수신된 데이터를 출력합니다.
        
        lcd.clear()  # LCD 화면을 지웁니다.
        lcd.putstr('Rx:{}'.format(data))  # LCD 화면에 수신된 데이터를 출력합니다.
        
        # 수신된 데이터에 따라 다른 동작 수행
        if data == 115 :  # 만약 데이터가 "배경소음"이면
            servo.rotate(180)  # 서보모터를 90도로 회전시킵니다.
            np.write()  # Neopixel을 활성화합니다.
            sleep(1)  # 잠시 대기합니다.
        if data == 119 :  # 데이터가 "weaker"이면
            servo.rotate(90)  # 서보모터를 180도로 회전시킵니다.
            np[0] = (100, 100, 0)  # Neopixel의 첫 번째 LED를 빨간색으로 설정합니다.
            sleep(1)  # 잠시 대기합니다.
#             np.write()  # Neopixel을 활성화합니다.
            
        if data == "stronger":  # 데이터가 "stronger"이면
            servo.rotate(0)  # 서보모터를 초기 위치로 회전시킵니다.
            np[0] = (0, 100, 0)  # Neopixel의 첫 번째 LED를 초록색으로 설정합니다.
            np.write()  # Neopixel을 활성화합니다.
            sleep(1)  # 잠시 대기합니다.
        if data == "switchon":  # 데이터가 "switchon"이면
            servo.rotate(0)  # 서보모터를 초기 위치로 회전시킵니다.
            np[0] = (100, 100, 0)  # Neopixel의 첫 번째 LED를 노란색으로 설정합니다.
            np.write()  # Neopixel을 활성화합니다.
            sleep(1)  # 잠시 대기합니다.
        if data == "switchooff":  # 데이터가 "switchooff"이면
            servo.rotate(0)  # 서보모터를 초기 위치로 회전시킵니다.
            np[0] = (100, 0, 100)  # Neopixel의 첫 번째 LED를 보라색으로 설정합니다.
            np.write()  # Neopixel을 활성화합니다.
            sleep(1)  # 잠시 대기합니다.