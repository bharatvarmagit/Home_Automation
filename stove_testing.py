from gpiozero import Button
from gpiozero import LED
from time import sleep

button = Button(14)
led = LED(15)

while True:
    button.wait_for_press()
    led.on()
    button.wait_for_release()
    led.off()
