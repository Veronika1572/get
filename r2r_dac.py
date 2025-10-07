import RPi.GPIO as GPIO
dac_bits = [16, 12, 25, 17, 27, 23, 22, 24]
dynamic_range = 3.3



class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)
    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()
    def set_number(self, number):
        binary = [int(element) for element in bin(number)[2:].zfill(8)]
        GPIO.output(self.gpio_bits, binary)
    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= dynamic_range):
            print(f"напряжение выходит за динамический диапазон ЦАП (0.0 - {dynamic_range:.2f} B")
            print("устанавливаем 0.0 B")
            return 0
        number = int(voltage/dynamic_range * 255)
        self.set_number(number)

if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)
        while True:
            try:
                voltage = float(input("Введите напряжение в вольтах:"))
                dac.set_voltage(voltage)
            except ValueError:
                print("Вы ввели не число. Попробуйте еще раз\n")
    finally:
        dac.deinit()