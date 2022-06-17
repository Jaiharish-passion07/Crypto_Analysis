#Import libraires
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from datetime import datetime
from sql_db import create_table,insert_table


def bitcoin_historical_data(coin_name,date_1):

    #path for chromw webdriver
    path=Service("C:\selenium drivers\chromedriver.exe")
    op = webdriver.ChromeOptions()

    #date_1 = '28/4/2013'
    date_2 = '16/6/2022'
    start = datetime.strptime(date_1, "%d/%m/%Y")
    end =   datetime.strptime(date_2, "%d/%m/%Y")
    diff = (end.year - start.year) * 12 + (end.month  - start.month )
    no_of_month=diff
    delta = end.date() - start.date()
    no_of_days=int(delta.days)

    try:
        history_data_list = []
        # URL path
        driver = webdriver.Chrome(service=path, options=op)
        # For maximizing window
        driver.maximize_window()
        # Implicit wait apply for all elements to wait for 5 seconds to load
        driver.implicitly_wait(5)
        #url link
        url="https://coinmarketcap.com/currencies/"+coin_name+"/historical-data/"
        driver.get(url)
        time.sleep(3)
        driver.find_element(by=By.XPATH, value="//*[@id='cmc-cookie-policy-banner']/div[2]").click()
        for j in range(1, no_of_month):
            # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(3)
            # driver.find_element(by=By.XPATH,value="//*[@id='__next']/div[1]/div[1]/div[2]/div/div[3]/div/div/div[1]/p[1]/button").click()
            driver.find_element(by=By.XPATH, value='//button[normalize-space()="Load More"]').click()

        for i in range(1, no_of_days + 2):
            date = driver.find_element(by=By.XPATH,
                                       value="//*[@id='__next']/div[1]/div[1]/div[2]/div/div[3]/div/div/div[1]/div[2]/table/tbody/tr[" + str(
                                           i) + "]/td[1]")
            open_price = driver.find_element(by=By.XPATH,
                                             value="//*[@id='__next']/div[1]/div[1]/div[2]/div/div[3]/div/div/div[1]/div[2]/table/tbody/tr[" + str(
                                                 i) + "]/td[2]")
            high_price = driver.find_element(by=By.XPATH,
                                             value="//*[@id='__next']/div[1]/div[1]/div[2]/div/div[3]/div/div/div[1]/div[2]/table/tbody/tr[" + str(
                                                 i) + "]/td[3]")
            low_price = driver.find_element(by=By.XPATH,
                                            value="//*[@id='__next']/div[1]/div[1]/div[2]/div/div[3]/div/div/div[1]/div[2]/table/tbody/tr[" + str(
                                                i) + "]/td[4]")
            close_price = driver.find_element(by=By.XPATH,
                                              value="//*[@id='__next']/div[1]/div[1]/div[2]/div/div[3]/div/div/div[1]/div[2]/table/tbody/tr[" + str(
                                                  i) + "]/td[5]")
            volume = driver.find_element(by=By.XPATH,
                                         value="//*[@id='__next']/div[1]/div[1]/div[2]/div/div[3]/div/div/div[1]/div[2]/table/tbody/tr[" + str(
                                             i) + "]/td[6]")
            mak_cap = driver.find_element(by=By.XPATH,
                                          value="//*[@id='__next']/div[1]/div[1]/div[2]/div/div[3]/div/div/div[1]/div[2]/table/tbody/tr[" + str(
                                              i) + "]/td[7]")
            # print(date.text.strip(),open_price.text.strip())
            history_data_list.append((date.text.strip(),
            open_price.text.strip(),
            high_price.text.strip(),
            low_price.text.strip(),
            close_price.text.strip(),
            volume.text.strip(),
            mak_cap.text.strip()))

    except:
        time.sleep(3)
        driver.close()
    finally:
        # passing the data to postgres sql db
        table_name="historical_"+coin_name+"_data_"+date_1.replace("/","_")+"_to_"+""+date_2.replace("/","_")
        create_table(table_name)
        insert_table(table_name,history_data_list)
        # setting time to close after 3 sec
        time.sleep(3)
        driver.close()

if __name__ =="__main__":
    select_coins=['bitcoin','ethereum','bnb','solana','polkadot-new','cardano']
    bitcoin_historical_data(coin_name=select_coins[2],date_1='1/1/2022')
