from machine import Pin
from time import sleep_ms
import onewire
import ds18x20

# create a OneWire bus on GPIO12
ow = onewire.OneWire(Pin(12))

# instantiate driver on pin/driver on ow bus
ds = ds18x20.DS18X20(ow)

# check bus to see what remote sensors are attached
roms = ds.scan()

# converts digital readings from ds18b20 to Celcius
ds.convert_temp()

# don't spam the one-wire bus!
sleep_ms(750)

# for each sensor attached to bus, print out temp value
for rom in roms:
    tempC = ds.read_temp(rom)
    tempF = tempC * (9 / 5) + 32
    print("\nCurrent Temperatures:\n")
    print("C: ", round(tempC, 1))
    print("F: ", round(tempF, 1), '\n')
