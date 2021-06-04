from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def getFees():
    url = "https://info.quickswap.exchange/home"
    PATH = 'C:\\Users\\lipso\\Desktop\\chromedriver_win32\\chromedriver.exe'
    driver = webdriver.Chrome(PATH)
    # Goes to website
    driver.get(url)
    # Pulls the volume

    delay = 10
    
    try: 
        getFees.totalFees = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="center"]/div/div[2]/div/div[1]/div[3]/div/div/div[4]/span'))).text
    except TimeoutException:
        print('Took to long to load!')

    
    # closes webdriver
    driver.quit()
    # Gets rid of '$' from volume
    getFees.removedDollarSign = getFees.totalFees.lstrip('$')
    # Removes the commas
    getFees.cleanedFees = getFees.removedDollarSign.replace(',', '')
    # .04% of volume is paid out to QuickSwap holders, .26% to LPs divided 4 by 30 to get the percnent given to QuickSwap holders
    getFees.quickSwapPay = (float(getFees.cleanedFees) * (4 / 30))
    print(f'${getFees.quickSwapPay} Paid out to token holders')

    getFees.volume = (float(getFees.cleanedFees) * 333.333)






# def getFees():
#     # Multiplies the total volume by .
#     getFees.xSushiPay = (float(getVolume.cleanedVolume) * 0.0005)
#     print(f'${getFees.xSushiPay} Paid out to token holders')
 
