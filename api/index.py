from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'cyberhack882@gmail.com'
app.config['MAIL_PASSWORD'] = 'ukbq wock sitt vmmm'
app.config['MAIL_DEFAULT_SENDER'] = 'cyberhack882@gmail.com'

mail = Mail(app)

@app.route('/sendmail/<string:to>/<string:subject>/<string:msg>')
def send_email(to,subject,msg):
  msg = Message(
    subject,
    recipients=[to],
    body=msg,
  )
  mail.send(msg)
  return 'Email sent succesfully!'

if __name__ == "__main__":
    app.run()
