# -*- coding: utf-8 -*-
import scrapy
import MySQLdb
import mysql.connector
from scrapy.http import Request
from ..items import ShopcluesItem

class ShopcluesSpider(scrapy.Spider):
    name = 'shopclues'
    download_delay = 5.0
    def start_requests(self):
         connection = MySQLdb.connect(

        host = 'localhost',
        user = 'root',
        passwd = '',
        database = 'product_data',
        charset="utf8",
        use_unicode=True
         )
         cursor = connection.cursor()

         cursor.execute("SELECT shopclues FROM `links`")
         rows = cursor.fetchall()

         for row in rows:
             url=row[0]
             yield Request(url=url)

         cursor.close()

    def parse(self, response):
        items = ShopcluesItem()
        product_name = response.css('h1').css('::text').extract() or ['product unavailable']
        shopclues_product_price = response.css('.f_price').css('::text').extract() or ['price unavailable']
        shopclues_url=response.url or ['link unavailable']
        items['product_name']=product_name
        items['shopclues_product_price']=shopclues_product_price
        items['shopclues_url']=shopclues_url
        yield items
