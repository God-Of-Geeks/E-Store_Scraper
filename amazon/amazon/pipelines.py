# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector

class AmazonPipeline(object):
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
        self.curr.execute("""DROP TABLE IF EXISTS amazon_products_tb""")
        self.curr.execute("""create table amazon_products_tb(amazon_url longtext,product_name VARCHAR(700)null,product_by text null,amazon_product_price text null,Availability longtext null)""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item
    def store_db(self,item):
        self.curr.execute("""insert into amazon_products_tb values (%s,%s,%s,%s,%s)""",(item['amazon_url'],item['product_name'][0],item['product_by'][0],item['amazon_product_price'][0],item['Availability'][0]))
        self.conn.commit()
