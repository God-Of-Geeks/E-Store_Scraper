# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector
class FlipkartPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def  create_connection(self):
        self.conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        database = 'product_data'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS flipkart_tb""")
        self.curr.execute("""create table flipkart_tb(flipkart_url longtext,flipkart_product_name VARCHAR(100),flipkart_product_price text)""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item
    def store_db(self,item):
        self.curr.execute("""insert into flipkart_tb values (%s,%s,%s)""",(item['flipkart_url'],item['flipkart_product_name'][0],item['flipkart_product_price'][0]))
        self.conn.commit()
