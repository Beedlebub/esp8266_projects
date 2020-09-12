from machine import Pin, I2C
import ssd1306
import time

button = Pin(14, Pin.IN, Pin.PULL_UP)

i2c = I2C(-1, scl=Pin(5), sda=Pin(4))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

while True:
    first = button.value()
    time.sleep(0.01)
    second = button.value()
    if first and not second:
        print('Button pressed!')
        oled.poweron()
        oled.text('Button pressed!', 0, 0)
        oled.show()
    elif not first and second:
        print('Button released!')
        oled.init_display()
        oled.poweroff()
