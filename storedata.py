import sushiswap
import quickswap
import json
import datetime
from datetime import date
import schedule
import time

data = {}
data['Sushi Swap'] = []
data['Quick Swap'] = []

def append_data():

    today = str(date.today())
    now = datetime.datetime.now()
    hour = now.hour
    minutes = now.minute

    data['Sushi Swap'].append({
    'Date': f'{today} {hour}:{minutes}',
    'Volume': f'{sushiswap.getVolume.cleanedVolume}',
    'Fees': f'{sushiswap.getFees.xSushiPay}'
})

    data['Quick Swap'].append({
    'Date': f'{today} {hour}:{minutes}',
    'Volume': f'{quickswap.getFees.volume}',
    'Fees': f'{quickswap.getFees.quickSwapPay}'
})

    with open('data.json', 'w') as outfile:
     json.dump(data, outfile)


def getData():
    sushiswap.getVolume()
    sushiswap.getFees()
    quickswap.getFees()
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