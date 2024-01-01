from machine import Pin  # 마이크로컨트롤러의 핀을 다루는 기능을 제공하는 라이브러리
from time import sleep  # 시간과 관련된 기능을 제공하는 라이브러리
from machine import PWM  # 펄스 폭 변조(PWM) 신호를 생성하는 기능을 제공하는 라이브러리
from machine import UART  # 시리얼 통신을 위한 기능을 제공하는 라이브러리
from machine import SoftI2C  # I2C 통신을 위한 기능을 제공하는 라이브러리
from i2c_lcd import I2cLcd  # LCD 화면을 다루는 기능을 제공하는 라이브러리

uart = UART(2, baudrate=115200, tx=17, rx=16)  # UART 초기화
uart.init(115200, bits=8, parity=None, stop=1)  # UART 설정 초기화

inA = PWM(Pin(23))  # inA 핀에 PWM 설정
inB = PWM(Pin(25))  # inB 핀에 PWM 설정
inA.init(freq=10, duty=0)  # inA PWM 주파수 및 듀티 사이클 초기화
inB.init(freq=10, duty=0)  # inB PWM 주파수 및 듀티 사이클 초기화
inA.duty(0)  # inA PWM 듀티 사이클 0으로 설정
inB.duty(0)  # inB PWM 듀티 사이클 0으로 설정

g = Pin(27, Pin.OUT)  # 초록 LED 설정
y = Pin(32, Pin.OUT)  # 노란 LED 설정
r = Pin(33, Pin.OUT)  # 빨간 LED 설정
y.off()  # 노란 LED 초기화 시 꺼진 상태로 설정
g.off()  # 초록 LED 초기화 시 꺼진 상태로 설정
r.off()  # 빨간 LED 초기화 시 꺼진 상태로 설정

i2c = SoftI2C(scl=Pin(21), sda=Pin(19), freq=400000)  # I2C 통신 설정
lcd = I2cLcd(i2c, 0x20, 2, 16)  # LCD 초기화
lcd.clear()  # LCD 화면 초기화

while True:  # 계속 반복 실행하는 무한 루프
    if uart.any() > 0:  # UART로부터 데이터가 수신되었는지 확인
        data = uart.read()  # 수신된 데이터를 읽어옴
        data = data[0]  # 수신된 데이터의 첫 번째 바이트를 사용

        print(data)  # 수신된 데이터를 출력

        if data == 49:  # 데이터가 1일 때
            lcd.clear()
            lcd.putstr('step1')  # LCD에 "1단 바람" 표시
            inB.duty(200)  # 선풍기 바람세기를 설정
            g.on()  # 초록 LED 켜기
            y.off()  # 노란 LED 끄기
            r.off()  # 빨간 LED 끄기
        elif data == 50:  # 데이터가 2일 때
            lcd.clear()
            lcd.putstr('step2')  # LCD에 "2단 바람" 표시
            y.on()  # 노란 LED 켜기
            g.off()  # 초록 LED 끄기
            r.off()  # 빨간 LED 끄기
            inB.duty(400)  # 선풍기 바람세기를 설정
        elif data == 51:  # 데이터가 3일 때
            lcd.clear()
            lcd.putstr('stop')  # LCD에 "정지" 표시
            y.off()  # 노란 LED 끄기
            g.off()  # 초록 LED 끄기
            r.on()  # 빨간 LED 켜기
            inB.duty(0)  # 선풍기 끄기

