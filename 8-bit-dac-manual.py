import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac_bits = [16, 12, 25, 17, 27, 23, 22, 24]

GPIO.setup(dac_bits, GPIO.OUT)
GPIO.output(dac_bits, 0)
dynamic_range = 3.3
def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"напряжение выходит за динамический диапазон ЦАП (0.0 - {dynamic_range:.2f} B")
        print("устанавливаем 0.0 B")
        return 0
    return int(voltage/dynamic_range * 255)

sleep_time = 0.2

def number_to_dac(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
try:
     while True:
        try:
            voltage = float(input("Введите напряжение в вольтах:"))
            number = voltage_to_number(voltage)
            number_to_dac(number)
            print(number, number_to_dac(number))
            time.sleep(sleep_time)
        except ValueError:
            print("Вы ввели не число. Попробуйте еще раз\n")
finally:
    GPIO.output(dac_bits, 0)
    GPIO.cleanup()