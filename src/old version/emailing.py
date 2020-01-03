from dotenv import load_dotenv
import smtplib
import os
load_dotenv()

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

from email import encoders
import os.path

def hand_solo_mail():
    email = os.getenv("email")
    password = os.getenv("pass") 
    send_to_email ="a.vargas.pina@gmail.com"
    subject = 'Your statistics playing Hand Solo'
    message = 'Hand Solo Team wants to thank your time playing Hand Solo. Wish you luck next time! ;)'
    file_location = "../output/music_report.pdf"

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587) # Connect to the server
    server.starttls() # Use TLS
    server.login(email, password) # Login to the email server
    server.sendmail(email, send_to_email , message) # Send the email
    server.quit() # Logout of the email server





