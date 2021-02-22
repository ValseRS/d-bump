import requests
import json
import time
import os


os.system("cls")
print("La Planque V19\n \n")
token = input("Rentre ton token : ")





i = 0




while i < 200000:
    header = {"authorization": f'{token}', "Content-Type": 'application/json' }
    url = 'https://discord.com/api/v8/channels/***********/messages'
    payload = {"content": "!d bump"}
    r = requests.post(url, headers=header, data=json.dumps(payload))
    r.json()
    print("\n \nRéponse de la requête : \n")
    print(r.json())
    print("\n \n")
    print("Message envoyé")
    time.sleep(7200)
    i = i + 1
    
    