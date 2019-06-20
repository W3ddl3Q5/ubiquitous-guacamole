# Allow Python to Send HTTP request
import requests

# Pretty Printer
from pprint import pprint

# Setting up some variables...
BOT_TOKEN = '791716181:AAFRAedCeXDAK0QwF8lHuC3J_7tsBO2J2es'
BOT_URL = 'https://api.telegram.org/bot' + BOT_TOKEN + '/'


# Receive Message (/getUpdates)
response = requests.get(BOT_URL+'getUpdates')


# Print Response (json format)
pprint(response.json())


# Get the first text message that you have send
message = response.json()["result"][-1]["message"]["text"]

pprint(message)
# Get the chat ID of the first message
chat_id = response.json()["result"][-1]["message"]["chat"]["id"]


print('First Message: ', message)
print('Chat ID', chat_id)