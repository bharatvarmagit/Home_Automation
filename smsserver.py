from flask import Flask, request, redirect
import os
from twilio.twiml.messaging_response import MessagingResponse 
from flask_mail import Mail, Message
app = Flask(__name__)
mail=Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'itsbharatvarma@gmail.com'
app.config['MAIL_PASSWORD'] = '**********'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail=Mail(app)

@app.route('/sms',methods=['GET','POST'])
def sms_reply():
    command = request.form['Body']
    resp= MessagingResponse()
    resp.message("command {} recieved".format(command))
    msg = Message(str(command),sender = 'itsbharatvarma@gmail.com', recipients = ['raspberrypi0142@gmail.com'])
    msg.body = "Hello Flask message sent from Flask-SMS"
    mail.send(msg)
    return str(resp)
if __name__=="__main__":
    app.run(debug=True)
