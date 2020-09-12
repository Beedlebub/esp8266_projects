# tmp36_basicTemp

from machine import ADC

adc = ADC(0)

voltage = adc.read() * (1000 / 1023.0)
tempC = ((voltage - 100.0) / 10) - 40
tempF = (tempC * 1.8) + 32

print("C: ", round(tempC, 1))
print("F: ", round(tempF, 1))
