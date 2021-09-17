import requests
import shutil
import telebot
import time


def getDATAfromString(text):
    indT = text.find('data-name="')
    title = (
        text[indT : indT + 250]
        .rsplit(' data-id="')[0]
        .rsplit('data-name="')[1]
        .replace('"', "")
    )
    return [
        text.rsplit(".jpg")[0].rsplit('source srcset="')[1].replace("mens", "zoom"),
        title,
    ]


def getImages():
    r = requests.get("https://www.qwertee.com/")
    result = []
    filenames = ["pic1", "pic2", "pic3"]
    ind = 0
    for i in range(3):
        ind = r.text.find("<picture>", ind + 1)
        url = getDATAfromString(r.text[ind : ind + 1000])
        z = requests.get(url[0] + ".jpg", stream=True)
        if z.status_code == 200:
            with open(filenames[i] + ".jpg", "wb") as f:
                z.raw.decode_content = True
                shutil.copyfileobj(z.raw, f)
        result.append(url[1])

    return result, filenames


url, filenames = getImages()
bot = telebot.TeleBot(open("token.txt").read().strip())
for u in range(3):
    file = open(filenames[u] + ".jpg", "rb")
    bot.send_photo("@DailyQwertee", file, url[u] + ", @DailyQwertee")
    # bot.send_photo(5901753, file,names[u]) #just for testing
