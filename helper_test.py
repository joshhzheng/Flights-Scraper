import unittest
import pandas as pd
from unittest.mock import MagicMock
from helper import *

class TestHelperFunctions(unittest.TestCase):

    def test_create_driver(self):
        driver = create_driver()
        self.assertIsNotNone(driver) 

    def test_build_url(self):
        departure = 'YVR'
        destination = 'HKG'
        start_date = '2024-06-01'
        end_date = '2024-09-05'
        url = build_url(departure, destination, start_date, end_date)
        expected_url = f'https://www.ca.kayak.com/flights/{departure}-{destination}/{start_date}/{end_date}?sort=bestflight_a'
        self.assertEqual(url, expected_url) 

    def test_get_flight_elements(self):
        driver = MagicMock() 
        xpath = '//div[@class="nrc6-inner"]'
        elements = get_flight_elements(driver, xpath)
        driver.find_elements.assert_called_once_with("xpath", xpath)  

    def test_extract_company_names_and_prices(self):
        mock_element1 = MagicMock()
        mock_element1.get_attribute.return_value = '<div class="J0g6-operator-text">Airline1</div><div class="Oihj-bottom-booking"><div class="f8F1-price-text">100</div></div>'
        mock_element2 = MagicMock()
        mock_element2.get_attribute.return_value = '<div class="J0g6-operator-text">Airline2</div><div class="Oihj-bottom-booking"><div class="f8F1-price-text">150</div></div>'
        
        flight_elements = [mock_element1, mock_element2]
        company_names, prices = extract_company_names_and_prices(flight_elements)

        self.assertEqual(company_names, ['Airline1', 'Airline2'])
        self.assertEqual(prices, ['100', '150'])

    def test_create_dataframe(self):
        company_names = ['Airline1', 'Airline2']
        prices = ['100', '150']

        df = create_dataframe(company_names, prices)

        expected_df = pd.DataFrame({'Airline': ['Airline1', 'Airline2'], 'Price': ['100', '150']})
        pd.testing.assert_frame_equal(df, expected_df)

    def test_sort_dataframe(self):
        mock_df = MagicMock()
        sort_dataframe(mock_df)

        mock_df.sort_values.assert_called_once_with(by='Price')

if __name__ == '__main__':
    unittest.main()
