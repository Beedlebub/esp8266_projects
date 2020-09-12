import machine

button = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)

print(button.value())
