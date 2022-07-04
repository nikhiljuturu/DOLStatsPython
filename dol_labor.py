import webbrowser
import urllib2
from twilio.rest import TwilioRestClient

#twilio client messages
account_sid = "xxxxxxxxxxx" #enter account SID here
auth_token  = "xxxxxxxxxxx" #enter auth token here
client = TwilioRestClient(account_sid, auth_token)

#initializing the counter for finding my A-number
finder = 0

#trying to search for the value of the A-number in the webpage
page = "http://dolstats.com/company/profile/"
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
        to="+1XXXXXXXXXX",    # Replace with your phone number
        from_="+1XXXXXXXXXX") # Replace with your Twilio number
    print message.sid
    webbrowser.open("https://www.youtube.com/watch?v=bUP5H3c02Wk")

