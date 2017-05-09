import requests
import shutil
import telebot
import time

def getDATAfromString(text):
    indT=text.find('data-name="')
    title=text[indT:indT+250].rsplit(' data-id="')[0].rsplit('data-name="')[1].replace('"',"")
    return [text.rsplit(".jpg")[0].rsplit('source srcset="')[1].replace("mens","zoom"),title]
   
def getImages():
    r = requests.get('https://www.qwertee.com/')
    result = []
    ind=0
    for i in range(3):
        ind=r.text.find('<picture>',ind+1)
        url=getDATAfromString(r.text[ind:ind+1000])
        z = requests.get("https:"+url[0]+".jpg", stream=True)
        if z.status_code == 200:
            with open(url[1]+".jpg", 'wb') as f:
                z.raw.decode_content = True
                shutil.copyfileobj(z.raw, f)
        result.append(url[1])
        
    return result

names=getImages()
bot=telebot.TeleBot(open('token.txt').read().strip())
for u in range(3):
    file = open(names[u]+".jpg", 'rb')
    bot.send_photo("@DailyQwertee", file,names[u])
    #bot.send_photo(5901753, file,names[u]) #just for testing

