PyMailCast
==========

Python script that multicasts HTML emails


Usage
==========
1. Add all the recipient emails in CSV(comma separated) format in emails.csv file
2. Update the following variables(user_name, password, smtp_server, smtp_port, subject, email_template) in mailcast.py

	user_name = 'your_user_name_string'
	password = 'your_password_string'
	smtp_server = 'your_smtp_server_address_string'
	smtp_port = your_smtp_server_port_int 
	subject = 'email_subject_string'
	email_template = 'your_html_email_template_file'
	
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
