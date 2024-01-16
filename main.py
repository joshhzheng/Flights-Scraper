from components.helper import *

def main():
    # input information here
    departure = 'YVR'
    destination = 'JFK'
    start_date = '2024-08-03'
    end_date = '2024-10-20'

    driver = create_driver()
    url = build_url(departure, destination, start_date, end_date)
    driver.get(url)

    xpath = '//div[@class="nrc6-inner"]'
    flights = get_flight_elements(driver, xpath)

    list_company_names, list_prices = extract_company_names_and_prices(flights)

    df = create_dataframe(list_company_names, list_prices)
    df_sorted = sort_dataframe(df)

    # Display the sorted DataFrame
    print(df_sorted)
    print(url)

if __name__ == "__main__":
    main()
