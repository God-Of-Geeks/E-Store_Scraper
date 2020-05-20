# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector
class ShopcluesPipeline(object):

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
        self.curr.execute("""DROP TABLE IF EXISTS shopclue_tb""")
        self.curr.execute("""create table shopclue_tb(shopclues_url longtext,product_name VARCHAR(700),shopclues_product_price VARCHAR(700))""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item
    def store_db(self,item):
        self.curr.execute("""insert into shopclue_tb values (%s,%s,%s)""",(item['shopclues_url'],item['product_name'][0],item['shopclues_product_price'][0]))
        self.conn.commit()
