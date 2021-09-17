import requests
import shutil
import os
import telebot
import time


def getDATAfromString(text):
    indT=text.find('data-name="')
    title=text[indT:indT+250].rsplit(' data-id="')[0].rsplit('data-name="')[1].replace('"',"")
    return [text.rsplit(".jpg")[0].rsplit('source srcset="')[1].replace("mens","zoom"),title]

def getImages():
    r = requests.get('https://www.qwertee.com/')
    result = []
    images=[]
    ind=0
    for i in range(3):
        ind=r.text.find('<picture>',ind+1)
        url=getDATAfromString(r.text[ind:ind+1000])
        z = requests.get(url[0]+".jpg", stream=True)
        if z.status_code == 200:
            img = z.content
            images.append(img)
        result.append(url[1])

    return result, images
def qweerte():
    url, images =getImages()
    bot=telebot.TeleBot('383215304:AAEY_OZrVgbIA9eNcITbTlfMePU5gqmbYlM')
    for u in range(3):
        file = images[u]
        # bot.send_photo("@DailyQwertee", file,url[u]+", @DailyQwertee")
        bot.send_photo(5901753, file,url[u]+", @DailyQwertee") #just for testing

qweerte()

