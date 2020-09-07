from flask import Flask,jsonify,request
from flask_mail import Mail, Message
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
mail = Mail(app) # instantiate the mail class

# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'dranerai@gmail.com'
app.config['MAIL_PASSWORD'] = 'Giveitachance.4'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/api/send_mail",methods=['POST'])
def send_mail():
    print(request.json)
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")
    subject = request.json.get("subject")
    mail_footer = "\n\nRegards,\n"+email+"\n"+"Sent via draner.ai\n"
    componsed_msg = "Hi Rony,\nYou have a new message from "+first_name+" "+last_name+"\n\n"
    msg = Message(subject, sender ='dranerai@gmail.com', recipients = ['ronythankachan324@gmail.com'] )
    msg.body = componsed_msg+request.json.get("message")+mail_footer
    status = "Message sending failed"
    error_code = 400
    try:
        mail.send(msg)
        status = "Message sent"
        error_code =200
    except:
        print(status);
    response = jsonify({'status':status})
    return response,error_code

if __name__ == "__main__":
    app.run(debug = True)
