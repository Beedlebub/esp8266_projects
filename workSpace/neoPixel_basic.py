from machine import Pin
from neopixel import NeoPixel

pin = Pin(13, Pin.OUT)   # set GPIO0 to output to drive NeoPixels
np = NeoPixel(pin, 3)   # create NeoPixel driver on GPIO0 for 8 pixels

np[0] = (255, 0, 0)  # set the first pixel
np[1] = (0, 255, 0)  # set the first pixel
np[2] = (0, 0, 255)  # set the first pixel

np.write()              # write data to all pixels
