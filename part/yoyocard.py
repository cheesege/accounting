import requests as req
from bs4 import BeautifulSoup
from tesseract import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from PIL import Image


driver  = webdriver.Chrome()
driver.get("https://ezweb.easycard.com.tw/search/CardSearch.php")
driver.save_screenshot("part\captcha.jpg")
time.sleep(1)
pic = driver.find_element(By.ID, "imgcode")
#print(pic.location)
#print(pic.size)
up = pic.location['y']
down = pic.location['y'] + pic.size['height']
left = pic.location['x']
right = pic.location['x'] + pic.size['width']

capt =  Image.open('part\captcha.jpg')
croped = capt.crop((left,up,right,down))
croped.save("part\captcha.png")
#croped.show()
print(solve_captcha())

time.sleep(1000)
r = req.Session()
payload = {
    'Cont':'Cont',
    'card_id': '8692420073',
    'birthday': '',
    'date': 'date1w',
    'START_DATE': '2024-05-29',
    'END_DATE': '2024-06-05',
    'checkword': '784396'
}
print()