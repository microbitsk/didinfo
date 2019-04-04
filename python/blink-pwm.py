from microbit import pin0, sleep

while True:
    # svieti slabo
    pin0.write_analog(600)
    sleep(500)
    # svieti naplno
    pin0.write_analog(0)
    sleep(500)