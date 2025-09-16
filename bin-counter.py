import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds = [16, 12, 25, 17, 27, 23, 22, 24]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)
up = 9
low = 10
GPIO.setup(9, GPIO.IN)
GPIO.setup(10, GPIO.IN)
num = 0
sleep_time = 0.2
def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
while True:
    if GPIO.input(up):
        num += 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    if GPIO.input(low):
        num -= 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    if num > 100:
        num = 100
    if num < 0:
        num = 0