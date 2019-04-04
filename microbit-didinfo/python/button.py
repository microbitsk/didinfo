from microbit import pin0, pin1, sleep

while True:
    if pin1.read_digital():
        pin0.write_digital(1)
    else:
        pin0.write_digital(0)