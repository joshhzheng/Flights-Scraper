from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd 

# webdriver setup
def create_driver():
    return webdriver.Chrome()

# url setup
def build_url(departure, destination, start_date, end_date):
    return f'https://www.ca.kayak.com/flights/{departure}-{destination}/{start_date}/{end_date}?sort=bestflight_a'

# xpath element finder
def get_flight_elements(driver, xpath):
    return driver.find_elements("xpath", xpath)

# scraper extraction
def extract_company_names_and_prices(flight_elements):
    list_company_names = []
    list_prices = []

    for WebElement in flight_elements:
        elementHTML = WebElement.get_attribute('outerHTML')
        elementSoup = BeautifulSoup(elementHTML, 'html.parser')

        # get company names
        company_names_element = elementSoup.find("div", {"class": "J0g6-operator-text"})
        company_names = company_names_element.text if company_names_element else "Company name not found"
        list_company_names.append(company_names)

        # get the price
        price_element = elementSoup.find("div", {"class" : "Oihj-bottom-booking"})
        price = price_element.find("div", {"class" : "f8F1-price-text"}).text if price_element else "Price not found"
        list_prices.append(price)

    return list_company_names, list_prices

# data frame creation
def create_dataframe(list_company_names, list_prices):
    return pd.DataFrame({'Airline': list_company_names, 'Price': list_prices})

# data cleaning (sorting)
def sort_dataframe(df):
    return df.sort_values(by='Price')