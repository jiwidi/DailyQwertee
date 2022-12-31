import requests
import os
import telebot
from selenium import webdriver
from selenium.webdriver.common.by import By

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
    # Headless chrome driver options
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.qwertee.com/")

    # Wait for the page to load
    time.sleep(5)

    # Find images that have "product-thumbs" and "zoom" in the src attribute
    images = driver.find_elements(
        By.XPATH,
        '//img[contains(@src, "product-thumbs") and contains(@src, "zoom")]',
    )

    # Extract the src attribute from the first 3 images
    image_urls = [image.get_attribute("src") for image in images[:3]]

    # Extract the alt attribute from the first 3 images
    image_titles = [image.get_attribute("alt") for image in images[:3]]

    # Download the images
    image_data = []
    for image_url in image_urls:
        r = requests.get(image_url, stream=True)
        if r.status_code == 200:
            img = r.content
            image_data.append(img)

    return image_titles, image_data


def qweerte():
    url, images = getImages()
    bot = telebot.TeleBot(open("token.txt").read().strip())
    for u in range(3):
        file = images[u]
        bot.send_photo("@DailyQwertee", file, url[u] + ", @DailyQwertee")



if __name__ == "__main__":
    qweerte()
