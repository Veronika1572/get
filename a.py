import smbus
import time
import numpy as np
import matplotlib.pyplot as plt

vol = []
t = []

class MCP3021:
    def __init__(self, dynamic_range, verbose = True):
        self.bus = smbus.SMBus(1)

        self.address = 0x4D

        self.dynamic_range = dynamic_range
        self.verbose = verbose

    def deinit(self):
        self.bus.close()

        
    def get_number(self):
        data = self.bus.read_word_data(self.address, 0)
        lower_data_byte = data >> 8
        upper_data_byte = data & 0xFF
        number = (upper_data_byte << 6) | (lower_data_byte >> 2)
#        if self.verbose:
#            print(data, upper_data_byte, lower_data_byte, number)
        return number
        
    def get_voltage(self):
        number = self.get_number()
        return (number/1023.0)*self.dynamic_range

if __name__ == "__main__":
    adc = MCP3021(5.18, verbose = True)
    try:
        start_time = time.time()
        now_time = time.time()
        while now_time - start_time < 40:
            now_time = time.time()
            voltage = adc.get_voltage()
            vol.append(voltage)
            t.append(now_time - start_time)
            time.sleep(0.0001)
        plt.plot(t, vol)
        plt.show()
        data = np.column_stack((t, vol))
        np.savetxt('dataILIAfiz.csv', data, delimiter = ',', fmt = '%.4f', header = 'Time, Voltage', comments='', encoding = 'utf-8')
    finally:
        adc.deinit()
