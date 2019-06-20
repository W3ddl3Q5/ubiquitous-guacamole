# Allow Python to Send HTTP request
import requests
import Receiver

# Pretty Printer
from pprint import pprint

# Setting up some variables...
BOT_TOKEN = '791716181:AAFRAedCeXDAK0QwF8lHuC3J_7tsBO2J2es'
BOT_URL = 'https://api.telegram.org/bot' + BOT_TOKEN + '/'

# Send Message (/sendMessage)

if Receiver.message == "Hello":
    reply = "Hello"

elif Receiver.message == "Bye":
    reply = "Bye"
    
else:
    reply = "I don't understand wtf you're talking! Speak EnGliSh"
    
data = {
    'chat_id': Receiver.chat_id,
    'text': reply
}
response = requests.post(BOT_URL+'sendMessage',data)

# Print Response
pprint(response.json())