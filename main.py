import autogitmand
import requests
import datetime

today = datetime.datetime.now()
today = today.strftime("%Y-%m-%d")

response = requests.get('https://www.bbc.com/')

webpage = response.text

with open(f'{today}.html', 'w') as f:
    f.write(webpage)

autogitmand.start(f'{today}.html')