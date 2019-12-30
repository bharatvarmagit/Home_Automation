from gpiozero import PWMOutputDevice
from time import sleep

a = PWMOutputDevice(13)
b = PWMOutputDevice(19)

while True:
    a.value = 0.3
    b.value = 0
    sleep(1)
    a.value = 0
    b.value = 0.3
    sleep(1)
