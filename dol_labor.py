import webbrowser
import urllib2
from twilio.rest import TwilioRestClient

#twilio client messages
account_sid = "AC619397348359d64b87add3c99e73c510"
auth_token  = "35047d0c66b01a949f48ac95275c30a6"
client = TwilioRestClient(account_sid, auth_token)

#initializing the counter for finding my A-number
finder = 0

#trying to search for the value of the A-number in the webpage
page = "http://dolstats.com/company/profile/CW%2BPROFESSIONAL%2BSERVICES%2BDBA%2BLOCHBRIDGE"
linked = urllib2.urlopen(page)
data = linked.read()

#Assigning counter to a number in case of successful search for A-number
if data.find('A-15020-43673') == -1:
    global finder
    finder = 0
else:
    global finder
    finder = 1

if (finder==1):
    message = client.messages.create(body="Your Labor is approved!! Congrats!",
        to="+18322943791",    # Replace with your phone number
        from_="+18635883725") # Replace with your Twilio number
    print message.sid
    webbrowser.open("https://www.youtube.com/watch?v=bUP5H3c02Wk")

