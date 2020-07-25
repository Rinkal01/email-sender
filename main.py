import smtplib

to = "shivam890k@gmail.com"

content='''Hello Its an automated mail from CEO of CEZ
it is sent to you as you are a member of CREATIVE EXPERTz

Codes:- https://github.com/shivam907

Our new website is Live https://ceziot.tech  
Owned and Managed by CEZ
It could be Down for sometime Due to Server Migration if it is Then Please 
try Later

Shivam(Founder and CEO of CEZ)'''

# content="https://ceziot.tech"

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email@demo.com', 'Password')
    server.sendmail('email@demo.com', to, content)
    server.close()

sendEmail(to, content)
