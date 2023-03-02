import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import os


def scraper():
    # Setting up driver and pointing to website
    website = f"https://www.autotrader.co.za/cars-for-sale/gauteng/p-1?pagenumber=1&price=50001-to-100000&year=more" \
              f"-than-2012&priceoption=RetailPrice "
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(0.5)
    driver.maximize_window()
    driver.get(website)

    # Calculate number of cars
    num_results = int(driver.find_element(By.CLASS_NAME, "e-results-total").text)
    print(f"==============================================================================================\n"
          f"There are {num_results} cars\n"
          f"Which are displayed on {(num_results // 20) + 1} pages\n"
          f"==============================================================================================\n")

    listing = []

    for page_number in range(1, ((num_results // 20) + 1)):
        website = f"https://www.autotrader.co.za/cars-for-sale/gauteng/p-1?pagenumber={page_number}&price=50001-to" \
                  f"-100000&year=more-than-2012&priceoption=RetailPrice "
        driver.get(website)

        cars = driver.find_elements(By.CLASS_NAME, "m-has-photos")
        cars = driver.find_element(By.CLASS_NAME, "m-has-photos")

        for car in cars:
            listing_desc = car.text.split("\n")

            # try:
            #     temp_df = pd.DataFrame(listing_desc)
            #     if len(temp_df) == 8:
            #         listing.append(temp_df.T)
            #     else:
            #         continue
            # except Exception as e:
            #     print(e)
            #     continue

        print(len(listing))

    export_df = pd.concat(listing)
    export_df.to_csv('cars.csv', index=False)


if __name__ == "__main__":
    scraper()
