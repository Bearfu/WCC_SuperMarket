# 逐行读取文件并将其作为数组返回
# Input 文件路径以及文件名称
# Output 包含文件内容的数组，可能出现空

import pymysql
import re

def _Read_Line_by_Line(path):
    all_line = []
    for line in open(path, encoding="utf-8"):
        line = line.strip("\n")
        all_line.append(line)
    return all_line
connection = pymysql.connect(host='localhost', user='root', password='',
                                 db='mall_databases', charset='utf8', cursorclass = pymysql.cursors.DictCursor)

cursor =  connection.cursor()


if __name__ == '__main__':
    path = r"E:\WCC_SuperMarket\test.txt"
    all_line = []
    line = _Read_Line_by_Line(path)
    for list in line:
        line = list.split("\t@\t")
        all_line.append(line)
    for line in all_line:
        storage_methods = line[0]
        big_class = line[1]
        small_class = line[2]
        source = line[3]
        barcode = line[6]
        product_name = line[7]
        spec = line[8]
        shelf_life = line[10]
        string = "A1.45，b5，6.45，8.82"
        shelf_life = int(re.findall(r"\d+\.?\d*", shelf_life)[0]) * 30
        stock = line[11]
        in_price = line[12]
        print(line)
        print(shelf_life)
        sql = 'INSERT INTO stock_management_m_product (storage_methods, big_class, small_class, source, barcode, product_name,spec,shelf_life,stock,in_price) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)'
        cursor.execute(sql, (storage_methods, big_class, small_class, source, barcode, product_name,spec,shelf_life,stock,in_price))
        connection.commit()


    connection.close();