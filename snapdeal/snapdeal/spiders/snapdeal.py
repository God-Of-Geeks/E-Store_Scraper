# -*- coding: utf-8 -*-
import scrapy
import MySQLdb
import mysql.connector
from scrapy.http import Request
from ..items import SnapdealItem

class SnapdealSpider(scrapy.Spider):
    name = 'snapdeal'
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

         cursor.execute("SELECT snapdeal FROM `links`")
         rows = cursor.fetchall()

         for row in rows:
             url=row[0]
             yield Request(url=url)

         cursor.close()

    def parse(self, response):
        items = SnapdealItem()
        product_name = response.css('.pdp-e-i-head').css('::text').extract() or ['product unavailable']
        snapdeal_product_price = response.css('.payBlkBig').css('::text').extract() or ['price unavailable']
        snapdeal_url=response.url or ['link unavailable']
        items['product_name']=product_name
        items['snapdeal_product_price']=snapdeal_product_price
        items['snapdeal_url']=snapdeal_url
        yield items
