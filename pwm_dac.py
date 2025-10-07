import RPi.GPIO as GPIO
dac_pins = [16, 12, 25, 17, 27, 23, 22, 24]
dynamic_range = 3.3

class PWM_DAC:
    def __init__(self, gpio_pins, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pins = gpio_pins
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pins, GPIO.OUT, initial = 0)
    def deinit(self):
        GPIO.output(self.gpio_pins, 0)
        GPIO.cleanup()
    def set_number(self, number):
        binary = [int(element) for element in bin(number)[2:].zfill(8)]
        GPIO.output(self.gpio_pins, binary)
    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= dynamic_range):
            print(f"напряжение выходит за динамический диапазон ЦАП (0.0 - {dynamic_range:.2f} B")
            print("устанавливаем 0.0 B")
            return 0
        number = int(voltage/dynamic_range * 255)
        self.set_number(number)

if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.290, True)
        while True:
            try:
                voltage = float(input("Введите напряжение в вольтах:"))
                dac.set_voltage(voltage)
            except ValueError:
                print("Вы ввели не число. Попробуйте еще раз\n")
    finally:
        dac.deinit()