# -*- coding: utf-8 -*-
import scrapy
import MySQLdb
import mysql.connector
from scrapy.http import Request
from ..items import FlipkartItem

class FlipSpider(scrapy.Spider):
    name = 'flip'
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

         cursor.execute("SELECT flipkart FROM `links`")
         rows = cursor.fetchall()

         for row in rows:
             url=row[0]
             yield Request(url=url)

         cursor.close()

    def parse(self, response):
        items = FlipkartItem()
        flipkart_product_name = response.css('._35KyD6::text').extract() or ['product unavailable']
        flipkart_product_price = response.css('._3qQ9m1').css('::text').extract() or ['price unavailable']
        flipkart_url = response.url or ['link unavailable']
        items['flipkart_product_name']=flipkart_product_name
        items['flipkart_product_price']=flipkart_product_price
        items['flipkart_url']=flipkart_url
        yield items
