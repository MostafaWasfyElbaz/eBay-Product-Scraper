# eBay Product Scraper
This is a web scraper built with Scrapy that extracts product information from eBay based on a user-provided product name. The scraper retrieves details such as the product name, price, link, seller location, and shipping information, and saves the data in a CSV file.

## Prerequisites
Make sure you have the following installed before running the scraper:

<span style="font-size: 2em; line-height: 0; vertical-align: middle;">&bull;</span> Python (3.6 or higher)

<span style="font-size: 2em; line-height: 0; vertical-align: middle;">&bull;</span> Scrapy library

<span style="font-size: 2em; line-height: 0; vertical-align: middle;">&bull;</span> CSV module

## Installation
1.Clone the repository to your local machine:

    git clone https://github.com/MostafaWasfyElbaz/eBay-Product-Scraper.git
  
2.Navigate to the project directory:

    cd ebay-product-scraper
  
3.Install the required dependencies:

    pip install scrapy
  
## Usage
1.Open a terminal or command prompt and navigate to the project directory.

2.Run the scraper by executing the following command:

    scrapy crawl ebaySpider
    
3.Provide the requested input when prompted:

  <span style="font-size: 2em; line-height: 0; vertical-align: middle;">&bull;</span> Product Name: Enter the name of the product you want to search for on eBay.
  
  <span style="font-size: 2em; line-height: 0; vertical-align: middle;">&bull;</span>File Name: Specify the name for the CSV file where the scraped data will be stored.

4.The scraper will start extracting data from eBay based on the provided product name. Progress and status information will be displayed in the terminal.

5.Once the scraping process is complete, a CSV file will be generated with the specified file name, containing the extracted product information.

## Customization
If you wish to modify or customize the scraper, you can make changes to the EbayspiderSpider class in the ebay_spider.py file. Here are a few possible modifications:

<span style="font-size: 2em; line-height: 0; vertical-align: middle;">&bull;</span>Adjust the CSS selectors in the parse method to extract different data fields or additional information.

<span style="font-size: 2em; line-height: 0; vertical-align: middle;">&bull;</span>Implement data validation or further data processing logic.

<span style="font-size: 2em; line-height: 0; vertical-align: middle;">&bull;</span>Customize the output format or change the storage method from CSV to a different format.

## License
This project is licensed under the MIT License.

## Disclaimer
This web scraper is meant for educational purposes only. Use it responsibly and in accordance with eBay's terms of service. The developers of this project are not responsible for any misuse or violations.
