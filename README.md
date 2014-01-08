PyMailCast
==========

Python script that multicasts HTML emails


Usage
==========
1. Add all the recipient emails in CSV(comma separated) format in emails.csv file
2. Update the following variables(user_name, password, smtp_server, smtp_port, subject, email_template) in mailcast.py

    example config:

	user_name = 'I@me.com'
	password = 'jackp0t'
	smtp_server = 'smtpout.secureserver.net'
	smtp_port = 3535
	subject = 'Thanks for using PyMailCast'
	email_template = 'mailme.html'
	
3. Run mailcast.py
	sudo python mailcast.py
	or
	./mailcast.py
