import smtplib
import ssl
import RPi.GPIO as G
import time
inp =  35
G.setwarnings(False)
G.setmode(G.BOARD)
G.setup(inp,G.IN)
#Your SMTP server
host = "smtp.gmail.com"
port = 465

#Your credentials
login = "Sender@mail.com"
password = "** ** ** **" #enter your own code

#Build your email
context = ssl.create_default_context()
dest = "receive@mail.com"
subject = "Test email Python"
body = "Paresh Detected"



email = "Subject: detection\nTo: receive@mail.com\nFrom: Sender@mail.com\nMotion detected"

#Send email
while True:
    time.sleep(1)
    if(G.input(inp)):
        print("Detected")
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(login, password)
            server.sendmail(login, dest, email)
            break
