#This is a program taht uses Twilio to send text messages to a phone

from twilio.rest import TwilioRestClient

account_sid = "{{ theOneYouGet }}" # Your Account SID from www.twilio.com/console
auth_token  = "{{ theOneYouGet}}"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="You just got a text from Christina's Robotic Assitant, BaciBot!  Hooray!",
    to="+1888123456789",    # Replace with your phone number
    from_="+1888123456789") # Replace with your Twilio number

print(message.sid)