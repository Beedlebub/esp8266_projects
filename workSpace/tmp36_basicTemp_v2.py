# tmp36_basicTemp

from machine import ADC

adc = ADC(0)

voltage = adc.read() * (1000 / 1024.0)
tempC = (voltage - 500.0) / 10
tempF = (tempC * (9/5)) + 32

print("C: ", round(tempC, 1))
print("F: ", round(tempF, 1))
