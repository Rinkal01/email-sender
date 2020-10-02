import smtplib

to=input("Whom You Want to Send the Mail")

content=input("Enter Content You Want To Mail")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('cezlogin@gmail.com', 'creativeexpertz')
    server.sendmail('email@demo.com', to, content)
    server.close()

sendEmail(to, content)
