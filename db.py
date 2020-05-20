import mysql.connector
import MySQLdb
#change the password and the user
cnx = mysql.connector.connect(user='root', database='product_data',password='aventador',charset="utf8",use_unicode=True)
cursor = cnx.cursor()
#sql commands for the final tables with shop_id...
SQL = '''
    DROP TABLE IF EXISTS final_flip;
    CREATE TABLE final_flip AS
    SELECT DISTINCT shop_id,flipkart_product_name,flipkart_product_price,flipkart_url
    FROM links,flipkart_tb
    WHERE flipkart=flipkart_url;

    DROP TABLE IF EXISTS final_amazon;
    CREATE TABLE final_amazon AS
    SELECT DISTINCT shop_id,product_name,amazon_product_price,amazon_url
    FROM amazon_products_tb,links
    WHERE amazon_url=amazon;

    DROP TABLE IF EXISTS final_shopclues;
    CREATE TABLE final_shopclues AS
    SELECT DISTINCT shop_id,product_name,shopclues_product_price,shopclues_url
    FROM links,shopclue_tb
    WHERE shopclues=shopclues_url;

    DROP TABLE IF EXISTS final_snapdeal;
    CREATE TABLE final_snapdeal AS
    SELECT DISTINCT shop_id,product_name,snapdeal_product_price,snapdeal_url
    FROM snapdeal_tb,links
    WHERE snapdeal_url=snapdeal;

    DROP TABLE IF EXISTS final_tab;
    CREATE TABLE final_tab AS
    SELECT final_amazon.shop_id,final_amazon.amazon_url,final_amazon.amazon_product_price
    FROM final_amazon
    UNION
    SELECT final_flip.shop_id,final_flip.flipkart_url,final_flip.flipkart_product_price
    FROM final_flip
    UNION
    SELECT final_snapdeal.shop_id,final_snapdeal.snapdeal_url,final_snapdeal.snapdeal_product_price
    FROM final_snapdeal
    UNION
    SELECT final_shopclues.shop_id,final_shopclues.shopclues_url,final_shopclues.shopclues_product_price
    FROM  final_shopclues
    ORDER BY `shop_id` ASC;

    DROP TABLE IF EXISTS price_details;
    CREATE TABLE price_details AS
    SELECT links.shop_id,links.shop_product_name,final_amazon.amazon_product_price,final_snapdeal.snapdeal_product_price,final_shopclues.shopclues_product_price,final_flip.flipkart_product_price
    FROM links,final_amazon,final_snapdeal,final_shopclues,final_flip
    WHERE links.shop_id=final_amazon.shop_id
    AND links.shop_id=final_snapdeal.shop_id
    AND links.shop_id=final_shopclues.shop_id
    AND links.shop_id=final_flip.shop_id
    ORDER BY `links`.`shop_id` ASC;

'''


cnx.commit()
cnx.close()
cnx.disconnect()
