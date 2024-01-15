from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd 

# webdriver setup
def create_driver():
    return webdriver.Chrome()

# URL setup
def build_url(departure, destination, start_date, end_date):
    return f'https://www.ca.kayak.com/flights/{departure}-{destination}/{start_date}/{end_date}?sort=bestflight_a'

# XPath element finder with waiting
def get_flight_elements(driver, xpath, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_all_elements_located((By.XPATH, xpath))
    )

# scraper extraction with waiting
def extract_company_names_and_prices(flight_elements, timeout=10):
    list_company_names = []
    list_prices = []

    for web_element in flight_elements:
        element_html = web_element.get_attribute('outerHTML')
        element_soup = BeautifulSoup(element_html, 'html.parser')

        # Get company names
        company_names_element = WebDriverWait(web_element, timeout).until(
            EC.presence_of_element_located((By.CLASS_NAME, "J0g6-operator-text"))
        )
        company_names = company_names_element.text if company_names_element else "Company name not found"
        list_company_names.append(company_names)

        # Get the price
        price_element = WebDriverWait(web_element, timeout).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Oihj-bottom-booking"))
        )
        price = price_element.find_element(By.CLASS_NAME, "f8F1-price-text").text if price_element else "Price not found"
        list_prices.append(price)

    return list_company_names, list_prices


def create_dataframe(list_company_names, list_prices):
    return pd.DataFrame({'Airline': list_company_names, 'Price': list_prices})

# data cleaning (sorting)
def sort_dataframe(df):
    return df.sort_values(by='Price')
