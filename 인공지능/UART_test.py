# 라이브러리 설정
from machine import Pin
from machine import PWM
from time import sleep
from machine import UART
from machine import SoftI2C # I2C 인터페이스 라이브러리
from i2c_lcd import I2cLcd # LCD 라이브러리
from mg90s_servo import MG90S_SERVO # 서보모터 라이브러리
from neopixel import NeoPixel # 내장된 라이브러리

i2c = SoftI2C(scl = Pin(22), sda = Pin(21), freq = 400000)
lcd = I2cLcd(i2c, 0x20, 2, 16) # lcd 초기세팅
lcd.clear()
servo = MG90S_SERVO(signal_pin = 27) # servo 초기세팅
servo.rotate(90)
np = NeoPixel(Pin(25), 16) # neopixel 초기세팅
uart=UART(2, baudrate=115200, tx=17, rx=16) # uart tx 에 연결된 esp32 핀은 16번이나, esp32 입장에서는 받는 포트이므로 16번이 rx이다
#uart=UART(1, baudrate=9600, tx=1, rx=3)
uart.init(115200, bits=8, parity=None, stop=1)

# #핀설정
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
#      r.off()
#      g.off()
#      b.off()
     
uart.write("hello world")     
    

while True:
   if uart.any() > 0:
        data = uart.read()
        #data = ord(r_data) # ord는 문자의 ASCII 코드를 반환
        data = data[0]
        print(data)
                   
    
        if data ==1:
            set_rgb(1, 1, 1)
        if data ==2:
            set_rgb(1, 0, 0)
        if data ==3:
            set_rgb(0, 1, 0)
        if data ==4:
            set_rgb(0, 0, 1)