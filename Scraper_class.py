from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
from datetime import date
today = date.today()
today = today.strftime("%d_%m_%Y")


class Scraper:
    def __init__(self, province, min_price, max_price, year):
        # Sets up the basic stuff
        normal_site = "https://www.autotrader.co.za/cars-for-sale"
        website = f"{normal_site}/{province}/p-1?pagenumber=1&price={min_price}-to-{max_price}&year=more-than-{year}&priceoption=RetailPrice "
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.implicitly_wait(0.5)
        driver.maximize_window()
        driver.get(website)

        # Calculates the total number of matches
        num_results = int(driver.find_element(By.CLASS_NAME, "e-results-total").text.replace(" ", ""))
        print(f"==============================================================================================\n"
              f"There are {num_results} cars\n"
              f"Which are displayed on {(num_results // 20) + 1} pages\n"
              f"==============================================================================================\n")

        listing = []

        # Gets info from each element in page
        for page_number in range(1, ((num_results // 20) + 1)):
            website = f"{normal_site}/{province}/p-1?pagenumber={page_number}&price={min_price}-to-{max_price}&year" \
                      f"=more-than-{year}&priceoption=RetailPrice "
            driver.get(website)

            cars = driver.find_elements(By.CLASS_NAME, "m-has-photos")

            for car in cars:
                listing_desc = car.text.split("\n")

                try:
                    temp_df = pd.DataFrame(listing_desc)
                    if len(temp_df) == 8:
                        listing.append(temp_df.T)
                    else:
                        continue
                except Exception as e:
                    print(e)
                    continue

        # Exports data
        export_df = pd.concat(listing)
        export_df.to_csv(f'data_{today}.csv', index=False)
