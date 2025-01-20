import requests
import os
import telebot
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    # Headless Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")  # Necessary for some environments
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    options.add_argument("--disable-gpu")  # Applicable to Windows OS only
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--remote-debugging-port=9222")

    # Initialize ChromeDriver using webdriver-manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("https://www.qwertee.com/")

        # Wait for images to load
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, '//img[contains(@src, "product-thumbs") and contains(@src, "zoom")]'))
        )

        # Find images that have "product-thumbs" and "zoom" in the src attribute
        images = driver.find_elements(
            By.XPATH,
            '//img[contains(@src, "product-thumbs") and contains(@src, "zoom")]',
        )

        if len(images) < 3:
            print("Less than 3 images found.")
            return [], []

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
            else:
                print(f"Failed to download image: {image_url}")

    except Exception as e:
        print(f"An error occurred while fetching images: {e}")
        return [], []
    finally:
        driver.quit()

    return image_titles, image_data

def qweerte():
    try:
        titles, images = getImages()
        if not titles or not images:
            print("No images to send.")
            return

        bot = telebot.TeleBot(os.environ["key"])
        for title, image in zip(titles, images):
            bot.send_photo("@DailyQwertee", image, f"{title}, @DailyQwertee")
    except Exception as e:
        print(f"An error occurred in qweerte: {e}")

if __name__ == "__main__":
    qweerte()
