from time import sleep_ms
import ds18x20

from machine import Pin
import onewire

ow = onewire.OneWire(Pin(12))  # create a OneWire bus on GPIO12
# ow.scan()               # return a list of devices on the bus
# ow.reset()              # reset the bus
# ow.readbyte()           # read a byte
# ow.writebyte(0x12)      # write a byte on the bus
# ow.write('123')         # write bytes on the bus
# ow.select_rom(b'12345678') # select a specific device by its ROM code

ds = ds18x20.DS18X20(ow)
roms = ds.scan()
ds.convert_temp()
sleep_ms(750)
tempC = ds.read_temp(rom)
tempF = tempC * (9 / 5) + 32
for rom in roms:
    print("C: ", round(tempC, 1))
    print("F: ", round(tempF, 1))
