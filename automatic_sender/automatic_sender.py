import requests , schedule
from phone_number import number

def send_msg():
  resp = requests.post('https://textbelt.com/text', {
    'phone': number,
    'message': 'Be a warrior, Be a queen , Be you !',
    'key': 'textbelt',
  })
  print(resp.json())


schedule.every().day.at('10:00').do(send_msg())


