from microbit import pin0, sleep
from time import ticks_ms

while True:
    value = (ticks_ms(), pin0.read_analog(), )
    print(value)
    sleep(100)