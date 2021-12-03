from requests import *
from json import dumps, loads#
import time
import urllib3

TOKEN = "<YOUR TOKEN>"

ATRIBUT = "limit=3&offset=-3&allowed_updates=message"

HTTP = f"https://api.telegram.org/bot{TOKEN}/"


global UpIDs

UpIDs = 0

global ID
ID = 172631146


while True:
    global response 
    response = get(HTTP + "getUpdates?"+ ATRIBUT)
    print('We have logged in as ')
    #a_list = list(json.loads(response).values())
    #a = json.dumps(response)
    #print(json.dumps(response.json(), sort_keys=True, indent=4))
    #print("\n")
    a = dumps(response.json(), sort_keys=True, indent=4)
    decoded_hand = loads(a)
    #print(decoded_hand)
    #print(response.json())

    #print(decoded_hand.keys())
    b = decoded_hand.get('result')
    #print(b)
    #print(b[2].keys())
    UpID = b[-1].get('update_id')
    if UpIDs == 0 : 
        UpIDs = UpID

    if UpID != UpIDs :
        UpIDs = UpID
        print(UpID)
        c = b[-1].get('message')
    #print(c)
    #print(c.keys())
        d = c.get('text')


        if d == "!huid" :
            for i in range(3):
                S = ['mr.ДЕгенерал - это Рома','mr.Да - НЯ!! - это Даня Даниил наивысший','mr.Андрей (( - это Андрей','mr.SaSKEE - это Саня вот и всё']
                resp = get(HTTP + f"sendMessage?chat_id=<chat_id>&text={S[i]}")
            #resp = get(HTTP + "sendMessage?chat_id=848986553&text=Без%20python%20не%20кошерно")
        print(d)
    time.sleep(0.2)

#with open(response, 'r') as f:
#   json_data = json.load(f)
    
#print(json_data)
print(response.json())