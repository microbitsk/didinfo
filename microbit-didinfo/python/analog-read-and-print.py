from microbit import pin0, sleep

while True:
    value = (pin0.read_analog(), )
    print(value)
    sleep(100)