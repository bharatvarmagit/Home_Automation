from gpiozero import LED
import Adafruit_DHT as dht
from time import sleep

led = LED(15)
    
while True:
    h, t = dht.read_retry(dht.AM2302, 14)
    t = t*1.8+32

    if t < 77: 
        led.on()
    else:
        led.off()
    print(t)
    sleep(5)
