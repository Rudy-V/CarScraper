import Scraper_class
import clean_data


if __name__ == "__main__":
    province = "gauteng"
    min_price = "50001"  # Works only on R xxx1 format
    max_price = '150000'
    year = '1'  # Gets all cars greater than this year

    Scraper_class.Scraper(province, min_price, max_price, year)
    clean_data.CleanData()

