from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def getLocation():
    options = Options()
    options.add_argument("--use--fake-ui-for-media-stream")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) #Edit path of chromedriver accordingly
    timeout = 20
    driver.get("https://mycurrentlocation.net/")
    wait = WebDriverWait(driver, timeout)
    time.sleep(3)
    longitude = driver.find_elements(By.XPATH, '//*[@id="longitude"]')  # Replace with any XPath
    longitude = [x.text for x in longitude]
    longitude = longitude[0]
    latitude = driver.find_elements(By.XPATH, '//*[@id="latitude"]')
    latitude = [x.text for x in latitude]
    latitude = latitude[0]
    driver.quit()
    return (latitude, longitude)


print(getLocation())
