Required libraries

$pip install adafruit-io
$pip install twilio
$pip install Flask

Required software

ngrok: https://ngrok.com/

homeautomation.py

A home automation script that uses raspberry pi gpio pins to communicate with simple
components through email.

Usage:
$python homeautomation.py

webserver.py

It is Flask Web Server which uses the Fask-Mail to send commands entered in the Web fom to
the the mail server(raspberrypi0142@gmail.com) that is listening for new commands in the pi.

Usage:
Run the flask application using 
$python sendmail.py 

smsserver.py

It is Flask web server using TwiML library provided my twilio to receive and send sms between 
the web server and the host using SMS. It requires us to set up a number with twilio and use 
twilio webhook to redirect requests sent to the twilio number to the web server(sendmail.py). 
twiML also enables the server to send sms messages to host .and we use flask-Mail to mail the 
command received through sms to the Mail listening mail server(raspberrypi0142@gmail.com)

Usage:
Used program ngrok to make the web server visible outside local network.
$python sendsms.py
