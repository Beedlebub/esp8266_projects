
from machine import Pin, I2C
import onewire
import time
import ds18x20
import ssd1306


# default ESP8266 Pin assignment for I2C
i2c = I2C(-1, scl=Pin(5), sda=Pin(4))


# set up oled device on I2C bus
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# create a OneWire bus on GPIO12
ow = onewire.OneWire(Pin(12)) 

# create driver on pin/driver on ow bus
ds = ds18x20.DS18X20(ow)

# check bus to see what remote sensors are attached
roms = ds.scan()

# converts digital readings from ds18b20 to Celcius
ds.convert_temp()

# don't spam the one-wire bus!
time.sleep_ms(750)

# set variables for Celsius and Fahrenheit temp values
# tempC = ds.read_temp(rom)
# tempF = tempC * (9 /5) + 32

# for each sensor attached to bus, print out temp value
for rom in roms:
  tempC = ds.read_temp(rom)
  tempF = tempC * (9 /5) + 32
  oledHeading_1 = 'Current '
  oledHeading_2 = 'Temperature: '
  
  print("")
  print(oledHeading_1)
  print(oledHeading_2)
  print("")
  print("C: ", round(tempC, 1))
  print("F: ", round(tempF, 1))
  print("")
    
  # set what will displayed on oled, per line, this display update
  oled.text(oledHeading_1, 0, 0)
  oled.text(oledHeading_2, 0, 8)
  oled.text(str(tempC), 0, 24)
  oled.text(str(tempF), 0, 40)
  # update oled screen with above info
  oled.show()




