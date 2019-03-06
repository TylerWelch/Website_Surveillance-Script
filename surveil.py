import os
import requests
import smtplib
import logging
from linode_api4 import LinodeClient, Instance

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
LINODE_TOKEN = os.environ.get('LINODE_TOKEN')

#logging.basicConfig(filename='site_surveillance/surveil.log',
#				   level=logging.INFO,
#				   format='%(asctime)s:%(levelname)s:%(message)s')

def alert_message():
	with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.ehlo()

		smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

		subject = 'Tyler_live SITE IS DOWN!'
		body = 'Check for Server Restart and is backed up'
		msg = f'Subject: {subject}\n\n{body}'

#		logging.info('Sending Email...')
		smtp.sendmail(EMAIL_ADDRESS, 'tylerwelchlive@gmail.com', msg)

def server_reboot():
	client = LinodeClient(LINODE_TOKEN)
	my_server = client.load(Instance, 13070453)
	my_server.reboot()
#	logging.info('Attempting to reboot Server!')

try:
	r = requests.get('https://tylerwelch.live', timeout=10)

	if r.status_code is not 200:
#		logging.info('Website is Not responding!')
		alert_message()
		server_reboot()
#	else:
#		logging.info('Website is Gucci')
except Exception as e:
#	logging.info('Website has Not Responded!')
	alert_message()
	server_reboot()

