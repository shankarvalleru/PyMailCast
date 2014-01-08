#!/usr/bin/python
__author__ = 'svalleru'

import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#email config
user_name = 'I@me.com'
password = 'jackp0t'
smtp_server = 'smtpout.secureserver.net'
smtp_port = 3535
subject = 'Thanks for using PyMailCast'
email_template = 'mailme.html'

with open(email_template) as temp:
 html = temp.read()

with open('emails.csv') as mfile:
 emails = mfile.read().split(',')

msg = MIMEMultipart('alternative')
msg['Subject'] = subject
msg['From'] = user_name
body = MIMEText(html, 'html')

msg.attach(body)

server = smtplib.SMTP(smtp_server, smtp_port)
server.login(user_name, password)
for rec in emails:
 msg['To'] = rec
 try:
  server.sendmail(user_name, rec, msg.as_string())
  print 'mail sent to:' + rec
 except smtplib.SMTPException, e:
  print 'unable to email:' + rec
  print e
server.quit()
