# Kayak.com Flights Web Scraper

This Python script allows you to scrape flight information from the Kayak website for a specific route and date range.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.x
- Required Python libraries: Selenium, BeautifulSoup, Pandas

```bash
pip install selenium beautifulsoup4 pandas
# or
pip3 install selenium beautifulsoup4 pandas
```

## Usage 

Clone the repository or download the files

```bash
git clone https://github.com/your-username/flight-web-scraper.git
cd flight-web-scraper
```

Update variables names

```
departure = ''
destination = ''
start_date = ''
end_date = ''
```

Run the script

```bash
python main.py
# or
python3 main.py
```

## Optional: Deploy to AWS Lambda

Zip the deployment packages and upload to AWS Lambda

```bash
zip -r deployment_package.zip lambda_function.py main.py helper.py requirements.txt
```

Note: add the `AWSSDKPandas-Python312` layer to import Pandas
