
from selenium import webdriver
import time
import threading
import os
from datetime import date
import datetime
import json
import sys
import schedule

data = {}
data['Sushi Swap'] = []

def getVolume():
    url = "https://analytics.sushi.com/"
    PATH = 'C:\\Users\\lipso\\Desktop\\chromedriver_win32\\chromedriver.exe'
    driver = webdriver.Chrome(PATH)
    # Goes to website
    driver.get(url)
    # Pulls the volume
    getVolume.Volume = driver.find_element_by_xpath('//*[@id="__next"]/div/main/div[2]/div[2]/div[2]/div/div/div/div[1]/h5').text
    #### print(getVolume.Volume)
    # Gets rid of '$' from volume
    getVolume.removedDollarSign = getVolume.Volume.lstrip('$')
    # Removes the commas
    getVolume.cleanedVolume = getVolume.removedDollarSign.replace(',', '')
    #### print(getVolume.cleanedVolume)
    # closes webdriver
    driver.quit()


def getFees():
    # Multiplies the total volume by .
    getFees.xSushiPay = (float(getVolume.cleanedVolume) * 0.0005)
    print(f'${getFees.xSushiPay} Paid out to token holders')
 
def append_data():
    today = str(date.today())
    now = datetime.datetime.now()
    hour = now.hour
    minutes = now.minute
    data['Sushi Swap'].append({
    'Date': f'{today} {hour}:{minutes}',
    'Volume': f'{getVolume.cleanedVolume}',
    'Fees': f'{getFees.xSushiPay}'
})

    with open('sushi.json', 'w') as outfile:
     json.dump(data, outfile)


def getData():
    getVolume()
    getFees()
    append_data()

schedule.every().monday.at("19:59").do(getData)
schedule.every().tuesday.at("19:59").do(getData)
schedule.every().wednesday.at("19:59").do(getData)
schedule.every().thursday.at("19:59").do(getData)
schedule.every().friday.at("19:59").do(getData)
schedule.every().saturday.at("19:59").do(getData)
schedule.every().sunday.at("19:59").do(getData)

while True:
    schedule.run_pending()
    time.sleep(1)


