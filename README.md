# E-Store_Scraper
This is a simple E-commerce website scraper  which scrapes the price details from various websites and stores in a database.
The urls of the websites to scrape has to be stored in the database for scraping.
# Softwares Required
<ul>
  <li>Mysql (Database)</li> 
  <li>Myphp (Server)</li>
  <li>Scrapy</li>
  <li>Httpd: Local host</li>
  </ul>
  
# Usage
To Run the crawler:
'''scrapy crawl _name_(amazon,flip,snapdeal,shopclues){example: scrapy crawl amazon}'''
  # Steps to interact with the application
     - Install the required packages
    - Install the required modules
    - Setup  the backend applications such as mysql mariadb 
    - Start the server [Apache2/lighttpd]
    - After doing these prerequisites go to the scraper file 
    - Run the crawler with the command scrapy crawl CRAWLER_NAME 
    - The crawler name can be found in the spider file in the scraper
    - After running the crawler if you find any module errors [I.e: Module not found error]:
    - Install the specific module with the command [pip install MODULE_NAME]
    - After installing the modules run the crawler 
    - The links of the website is extracted from the table [LINKS]
    - The links table can be updated via command line or the phpmyadmin which can be accessed by any web browser.
    - Each crawler has a seperate table to store the crawled data
    - amazon_products_tb for amazon
    - flipkart_tb for flipkart
    - shopclue_tb for shopclues
    - snapdeal_tb for snapdeal
    - Shop_id:This shop_id is the unique ID for the CK_fortunes products. This ID should also be typed in the [LINKS] table. This shop_ID is added to the final tables of the shops
    - The final tables of the shops is given below
    - final_amazon
    - final_flip
    - final_snapdeal
    - final_shopclues
    - All the final tables are Used to create a new table which is embedded into a new table contains all the data of the final tables that table name is [FINAL_TAB]
    - This final table is used to get the price details of every product which in  return stored in another table [PRICE_DETAILS]
    - The user has to do two operations
        - Running every spider in the folder
        - Running a database file which will process the  tables and generate the final price_details table
        - The file is located in scrapy/db.py
    - The tables could be used however the user needs.  He can either use a php/ java application to retreive the data from the database to the webpage.

To see scrapy documentation visit:<br>
https://docs.scrapy.org/en/latest/#

# Contribution

Pull requests are welcome.
<br>For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.
