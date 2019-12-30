from gpiozero import LED
from gpiozero import Button
from gpiozero import PWMOutputDevice
from gpiozero import DistanceSensor
import Adafruit_DHT as dht
import smtplib
import time
import imaplib
import email

FROM_EMAIL  = "raspberrypi0142@gmail.com"
FROM_PWD    = "JyQ75uCWJ94M"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

# pins echo 8 and trigger 25 for sensor

led_heater              = LED(15)
heater                  = False
desiredTemperature      = 75

led_1                   = LED(18)
led_2                   = LED(7)
led_1_status            = False
led_2_status            = False

door_open_motor         = PWMOutputDevice(13)
door_close_motor        = PWMOutputDevice(19)
door_open_request       = False
door_close_request      = False
door_status             = False

stove_button            = Button(24)
stove_led               = LED(23)

distance_sensor         = DistanceSensor(echo=8, trigger=25)
people                  = 4

def checkMail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        type, data = mail.search(None, 'UNSEEN')
        mail_ids = data[0]

        id_list = mail_ids.split()

        if len(id_list) is not 0:
            typ, data = mail.fetch(id_list[0], '(RFC822)')
            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])
                    return msg['subject']

    except Exception, e:
        print str(e)

def parseMessage(msg):
    global heater
    global led_1_status
    global led_2_status
    global door_open_request
    global door_close_request

    print 'Message recieved : ' + msg
    #check for temperature email (set heater to true or false, desired temp)
    if msg == 'heater on':
        print('Heater turning on.')
        heater = True

    if msg == 'heater off':
        print('Heater turning on.')
        heater = True

    if msg.startswith('set temp'):
        temp = int(filter(str.isdigit, msg))
        print('Setting temperature to ' + temp + ' F.')
        desiredTemperature = temp

    #check for led emails
    if msg == 'light 1 on':
        print('Light 1 turning on.')
        led_1_status = True

    if msg == 'light 1 off':
        print('Light 2 turning off.')
        led_1_status = False

    if msg == 'light 2 on':
        print('Light 2 turning on.')
        led_2_status = True
    
    if msg == 'light 2 off':
        print('Light 2 turning off.')
        led_2_status = False

    #check for door emails (open close)

    if msg == 'door open':
        print('Door unlocked.')
        door_open_request = True
    
    if msg == 'door close':
        print('Door locked.')
        door_close_request = True

def temperature():
    h, t = dht.read_retry(dht.AM2302, 14)
    t = t*1.8+32
    print('The temperature is currently {0:0.1f}*F.'.format(t))
    if t < desiredTemperature and heater is True:
        led_heater.on()
    else:
        led_heater.off()

def lights():
    if led_1_status is True:
        led_1.on()
    else:
        led_1.off()

    if led_2_status is True:
        led_2.on()
    else:
        led_2.off()

def doors():
    global door_open_request
    global door_close_request
    global door_status

    if door_open_request is True and door_status is False:
        print('Door open request recieved')
        door_open_motor.value = 0.3
        door_close_motor.value = 0
        time.sleep(0.25)
        door_open_motor.value = 0
        door_close_motor.value = 0
        door_open_request = False
        door_status = True
    
    if door_close_request is True and door_status is True:
        print('Door open request recieved')
        door_close_motor.value = 0.3
        door_open_motor.value = 0
        time.sleep(0.25)
        door_close_motor.value = 0
        door_open_motor.value = 0
        door_close_request = False
        door_status = True

def stove():
    global people
    if stove_button.is_pressed:
        stove_led.on()
        if people is 0:
            print "Warning: stove is still on"
    else:
        stove_led.off()

def distance():
    global people

    sensor_value0 = distance_sensor.distance*100
    time.sleep(1)
    sensor_value1 = distance_sensor.distance*100
    
    v = sensor_value0 - sensor_value1

    print people

    if abs(v) > 3 and abs(v) < 18:
        if v > 0:
            people = people + 1
        if v < 0:
            people = people - 1


while 1:
    msg = checkMail()
    if msg is not None:
        parseMessage(msg)
    temperature()    
    lights()
    doors()
    stove()
    distance()


