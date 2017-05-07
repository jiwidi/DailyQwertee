import requests
import shutil
import telebot
import time

def getURLfromString(text):
    return text.rsplit(".jpg")[0].rsplit('source srcset="')[1]
def getImages():
    r = requests.get('https://www.qwertee.com/')
    result = []
    ind=0
    for i in range(3):
        ind=r.text.find('<picture>',ind+1)
        url=getURLfromString(r.text[ind:ind+300])
        z = requests.get("https:"+url+".jpg", stream=True)
        if z.status_code == 200:
            with open("daily"+str(i)+".jpg", 'wb') as f:
                z.raw.decode_content = True
                shutil.copyfileobj(z.raw, f)
        #result.append(url)
        #print(url)

getImages()
bot=telebot.TeleBot('open('token.txt').read())
for u in range(3):
    file = open("daily"+str(u)+".jpg", 'rb')
    bot.send_photo("@DailyQwertee", file)
    #bot.send_message(5901753, "hi") just for testing

