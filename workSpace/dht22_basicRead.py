from machine import Pin
from time import sleep
import dht

sensor = dht.DHT22(Pin(14))

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        temp_f = temp * (9/5) + 32.0
        print('Temperature: %3.1f C' % temp)
        print('Temperature: %3.1f F' % temp_f)
        print('Humidity: %3.1f %%' % hum)
        sleep(10)
    except OSError as e:
        print('Failed to read sensor.')
