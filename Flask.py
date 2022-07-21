from flask import *
import os
import math
import smtplib
import random


#Getting an OTP
digits = [i for i in range(0, 10)]

random_str = ""

for i in range(6):
    index = math.floor(random.random() * 10)
    random_str += str(digits[index])
otp = random_str+" is your OTP"
print(otp)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template ('login.html')

@app.route("/getOTP", methods=['POST'])
def getOTP():
    emailid = request.form['EmailID']
    val = getOTPnow(emailid)
    return render_template('OTP.html')

@app.route("/validateOTP", methods=['POST'])
def validateOTP():
    otp_web=request.form['OTP']
    
    print(otp_web)
    if random_str==otp_web:
        return 'You are Authorized to access Website'
    else:
        return 'You are not Authorized'    
    
#Function for sending otp to email
def getOTPnow(emailid):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    emailid = emailid
    s.login(emailid, "krufftuknbcqdcgx")
    s.sendmail('&&&&&&',emailid,otp)    
if __name__=='__main__':
    app.run(debug='True')
