#Import libraires
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from sql_db import create_table,insert_table

def crypto_scraping_data():

    #path for chrome webdriver
    path=Service("C:\selenium drivers\chromedriver.exe")
    op = webdriver.ChromeOptions()

    # Initializing list to store the data
    top_100_coin_list = []

    try:
        # URL path
        driver = webdriver.Chrome(service=path, options=op)
        # For maximizing window
        driver.maximize_window()
        # Implicit wait apply for all elements to wait for 5 seconds to load
        driver.implicitly_wait(5)
        driver.get("https:/coinmarketcap.com/")
        # col = driver.find_elements(by=By.XPATH,
        #                            value="//*[@id='__next']/div/div[1]/div[2]/div/div/div[5]/table/thead/tr/th")
        # # print(len(col),len(rows))
        for i in range(1,101):
            flag = driver.find_element(by=By.XPATH,
                                       value="//*[@id='__next']/div/div[1]/div[2]/div/div/div[5]/table/tbody/tr[" + str(
                                           i) + "]/td[3]/div/a/div/div/p")

            # Accessing coin name, price,24 hr change, Mkt Cap directly

            coin_name = driver.find_element(by=By.XPATH,
                                            value="//*[@id='__next']/div/div[1]/div[2]/div/div/div[5]/table/tbody/tr[" + str(
                                                i) + "]/td[3]/div/a/div/div/p")

            coin_symbol = driver.find_element(by=By.XPATH,
                                              value="//*[@id='__next']/div/div[1]/div[2]/div/div/div[5]/table/tbody/tr[" + str(
                                                  i) + "]/td[3]/div/a/div/div/div/p")

            coin_price = driver.find_element(by=By.XPATH,
                                             value="//*[@id='__next']/div/div[1]/div[2]/div/div/div[5]/table/tbody/tr[" + str(
                                                 i) + "]/td[4]/div/a/span")

            hr_24 = driver.find_element(by=By.XPATH,
                                        value="//*[@id='__next']/div/div[1]/div[2]/div/div/div[5]/table/tbody/tr[" + str(
                                            i) + "]/td[5]/span")

            market_cap = driver.find_element(by=By.XPATH,
                                             value="//*[@id='__next']/div/div[1]/div[2]/div/div/div[5]/table/tbody/tr[" + str(
                                                 i) + "]/td[7]/p/span[2]")

            volume_24hr = driver.find_element(by=By.XPATH,
                                              value="//*[@id='__next']/div/div[1]/div[2]/div/div/div[5]/table/tbody/tr[" + str(
                                                  i) + "]/td[8]/div/a/p")

            driver.execute_script("arguments[0].scrollIntoView();", flag)

            # Appending all Data into respective records

            #list of tuples
            top_100_coin_list.append((coin_name.text.replace("\n", "").strip(),
                                      coin_symbol.text.replace("\n", "").strip(),
                                      coin_price.text.replace("\n", "").strip(),
                                      hr_24.text.replace("\n", "").strip(),
                                      market_cap.text.replace("\n", "").strip(),
                                      volume_24hr.text.replace("\n", "").strip()))


    except:
        # setting time to close after 3 sec
        time.sleep(3)
        driver.close()

    finally:
        #passing the data to postgres sql db
        create_table('top_100_coins')
        insert_table('top_100_coins',top_100_coin_list)
        # setting time to close after 3 sec
        time.sleep(3)
        driver.close()

    #crypto_df.to_excel('Cryto_top_100_coins.xlsx',sheet_name='top_100_coins')

if __name__ =="__main__":
    count=1
    crypto_scraping_data()
    # while True:
    #     crypto_scraping_data()
    #     time_wait_min = 15
    #     print()
    #     print("Finished scraping data for count: "+ str(count)+"\n")
    #     print("Waiting for : " + str(time_wait_min) + " mins"+"\n")
    #     time.sleep(time_wait_min*60)
    #     count+=1


