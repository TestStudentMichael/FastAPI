import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('TOKEN', 'default_value')

domain = 't.me'

url = 'https://www.virustotal.com/vtapi/v2/domain/report'

params = {'apikey':token,'domain':domain}

response = requests.get(url, params = params)

dict = json.loads(response.text)

for item in dict:
    if(type(dict[item]) == int):
        print(f'{item} - {dict[item]}')
        continue
    if(type(dict[item]) == str):
        print(f'{item} - {dict[item]}')
        continue
    if(type(dict[item]) == object):
        print(f'{item} - {dict[item]}')
        continue
    if(len(dict[item]) > 5):
        print(dict[item][0:3])    
'''
TestConnection
'''