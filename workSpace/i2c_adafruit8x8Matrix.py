import machine
import ht16k33_matrix
import time

i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
matrix = ht16k33_matrix.Matrix8x8(i2c, 0x70)

# auto write can be turned off
matrix.auto_write = False
# and fill is same as before
matrix.fill(0)
# but now you have to call show()
matrix.show()

time.sleep(1)
matrix.fill(1)
matrix.show()
time.sleep(1)
matrix.fill(0)
matrix.show()
