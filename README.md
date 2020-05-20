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

After running the crawler
Run:
python db.py //to generate the database files

To see scrapy documentation visit:
https://docs.scrapy.org/en/latest/#

# Contribution

Pull requests are welcome.
<br>For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.
