
from selenium import webdriver


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
 



