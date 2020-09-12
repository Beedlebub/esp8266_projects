import machine
import time

servo = machine.PWM(machine.Pin(12), freq=50)

servo.duty(77)
time.sleep(1)
servo.duty(45)
time.sleep(1)
servo.duty(77)
time.sleep(1)
servo.duty(115)
time.sleep(1)
servo.duty(77)
