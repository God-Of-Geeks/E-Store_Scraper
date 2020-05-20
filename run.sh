#!/bin/bash
while true
do
echo "Deleting previous data table"
sudo rm /tmp/price_details_tab.csv
echo "_______________________________________________________________________________________________________________________________"
echo "Loading links table"
mysql -u root product_data <<QUERY_INPUT
LOAD DATA infile '/tmp/links.csv' replace into table links FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'LINES TERMINATED BY '\n'
QUERY_INPUT
echo "_______________________________________________________________________________________________________________________________"
echo "Altering table character-set"
mysql -u root product_data -e 'ALTER TABLE links CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci'
echo "_______________________________________________________________________________________________________________________________"
cd /home/pi/scraper/amazon && scrapy crawl amazon
echo "_______________________________________________________________________________________________________________________________"
cd /home/pi/scraper/flipkart && scrapy crawl flip
echo "_______________________________________________________________________________________________________________________________"
cd /home/pi/scraper/snapdeal && scrapy crawl snapdeal
echo "_______________________________________________________________________________________________________________________________"
cd /home/pi/scraper/shopclues && scrapy crawl shopclues
echo "_______________________________________________________________________________________________________________________________"
echo "crawled the links....Configuring database"
mysql -u root product_data <<QUERY_INPUT
DROP TABLE IF EXISTS final_flip;
QUERY_INPUT

mysql -u root product_data <<QUERY_INPUT
CREATE TABLE final_flip AS
SELECT DISTINCT shop_id,flipkart_product_name,flipkart_product_price,flipkart_url
FROM links,flipkart_tb
WHERE flipkart=flipkart_url;
QUERY_INPUT

mysql -u root product_data <<QUERY_INPUT
    DROP TABLE IF EXISTS final_amazon;
QUERY_INPUT

mysql -u root product_data <<QUERY_INPUT
CREATE TABLE final_amazon AS
SELECT DISTINCT shop_id,product_name,amazon_product_price,amazon_url
FROM amazon_products_tb,links
WHERE amazon_url=amazon;
QUERY_INPUT

mysql -u root product_data <<QUERY_INPUT
    DROP TABLE IF EXISTS final_shopclues;
QUERY_INPUT

mysql -u root product_data <<QUERY_INPUT
CREATE TABLE final_shopclues AS
SELECT DISTINCT shop_id,product_name,shopclues_product_price,shopclues_url
FROM links,shopclue_tb
WHERE shopclues=shopclues_url;
QUERY_INPUT

mysql -u root product_data <<QUERY_INPUT
DROP TABLE IF EXISTS final_snapdeal;
QUERY_INPUT

mysql -u root product_data <<QUERY_INPUT
CREATE TABLE final_snapdeal AS
SELECT DISTINCT shop_id,product_name,snapdeal_product_price,snapdeal_url
FROM snapdeal_tb,links
WHERE snapdeal_url=snapdeal;
QUERY_INPUT

mysql -u root product_data <<QUERY_INPUT
DROP TABLE IF EXISTS final_tab;
QUERY_INPUT

mysql -u root product_data <<QUERY_INPUT
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
QUERY_INPUT

mysql -u root product_data <<QUERY_INPUT
DROP TABLE IF EXISTS price_details;
QUERY_INPUT

mysql -u root product_data <<QUERY_INPUT
CREATE TABLE price_details AS
SELECT links.shop_id,links.shop_product_name,final_amazon.amazon_product_price,final_snapdeal.snapdeal_product_price,final_shopclues.shopclues_product_price,final_flip.flipkart_product_price
FROM links,final_amazon,final_snapdeal,final_shopclues,final_flip
WHERE links.shop_id=final_amazon.shop_id
AND links.shop_id=final_snapdeal.shop_id
AND links.shop_id=final_shopclues.shop_id
AND links.shop_id=final_flip.shop_id
QUERY_INPUT

echo "_______________________________________________________________________________________________________________________________"
echo "_______________________________________________________________________________________________________________________________"
echo "Database configured"
echo "_______________________________________________________________________________________________________________________________"
echo "Generating output....."
mysql -u root product_data <<QUERY_INPUT
     SELECT * INTO OUTFILE '/tmp/price_details_tab.csv' FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n' FROM price_details
QUERY_INPUT
echo "Output Generated....:)"
sleep 24h
echo "_______________________________________________________________________________________________________________________________"
done
