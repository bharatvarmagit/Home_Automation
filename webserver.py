from flask import Flask, request,render_template 
from flask_mail import Mail, Message



app = Flask(__name__)
mail=Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'itsbharatvarma@gmail.com'
app.config['MAIL_PASSWORD'] = '*********'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail=Mail(app)



@app.route('/')
def index():
    return render_template("mainscreen.html")

@app.route('/form', methods=["POST","GET"])
def form():
    command =request.form.get('command')
    msg = Message(str(command),sender = 'itsbharatvarma@gmail.com',recipients = ['raspberrypi0142@gmail.com'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return render_template("index.html",command=command)
    
if __name__ == "__main__":
    app.run(debug=True)