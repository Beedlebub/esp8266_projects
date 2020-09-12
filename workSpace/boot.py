# This file is executed on every boot (including wake-boot from deepsleep)
import esp
import gc
import webrepl
import uos
import machine

esp.osdebug(None)
gc.collect()
webrepl.start()
# uos.dupterm(None, 1) # disable REPL on UART(0)
