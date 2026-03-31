from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time

news = {}

def set_driver():
    driver = webdriver.Chrome()
    return driver

def get_page(driver):
    driver.get("https://rbc.ru/")
    time.sleep(1.3)
    html = bs(driver.page_source, "html.parser")
    return html


def parses(html):
    for el in html.select(".MainNewsComponent_wrapper__Kybz5"):
        title = el.select("div > a > div")
        for i in title:
            new = i.text.strip()
            link = el.find('a').get('href').strip()
            news.update({new: link})
    return news


def set_text(news):
    file = open("news.txt", "w")
    for key in news:
        print(news[key])
        file.write(f" {key:<80}    |||||||||||||||||||||||||||||||||||||||||         https://rbc.ru/{news[key]} \n")
    file.close()
    return