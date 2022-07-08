import os # Importing the OS module
from twilio.rest import Client # Importing the Twilio module

# Your Account SID from twilio.com/console
account_sid = os.environ['TWILIO_ACCOUNT_SID']
# Your Auth Token from twilio.com/console
auth_token = os.environ['TWILIO_AUTH_TOKEN']
