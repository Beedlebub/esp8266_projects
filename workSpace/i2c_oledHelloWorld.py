from machine import Pin, I2C
import ssd1306

# ESP8266 Pin assignment
i2c = I2C(-1, scl=Pin(5), sda=Pin(4))
# Set size of screen, typically height is 64 or 32
oled_width = 128
oled_height = 64
# Create I2C OLED device from parameters above
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

while True:
  oled.text('Hello, World 1!', 0, 0)
  oled.text('Hello, World 2!', 0, 8)
  oled.text('Hello, World 3!', 0, 16)
  oled.text('Hello, World 4!', 0, 24)
  if oled_height == 64:
    oled.text('Hello, World 5!', 0, 32)
    oled.text('Hello, World 6!', 0, 40)
    oled.text('Hello, World 7!', 0, 48)
    oled.text('Hello, World 8!', 0, 56)
    # Unused on any screen 64 or smaller
    if oled_height > 64:
      oled.text('Hello, World 9!', 0, 64)
  # Actually print everything to OLED
  oled.show()

