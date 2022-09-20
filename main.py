import autogitmand
import requests
import datetime

today = datetime.datetime.now()
today = today.strftime("%Y-%m-%d")

response = requests.get('https://www.bbc.com/')

webpage = response.text

with open(f'{today}.html', 'w', newline='' , encoding="utf-8") as file:
    file.writelines(webpage)

autogitmand.start(f'{today}.html')
