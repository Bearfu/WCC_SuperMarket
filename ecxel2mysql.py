__author__ = 'Administrator'
import xlrd
import pymysql
import re

# 将xlsx文件中的数据导入到MYSQL数据库中

# 打开EXCEL文件的地址
excel = xlrd.open_workbook(r'E:\WCC_SuperMarket\彩虹超市商品明细.xlsx')
# 连接数据库
connection = pymysql.connect(host='localhost', user='root', password='',
                             db='mall_databases', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
# 设置导入的Sheet
# 获取第一个sheet
sheet = excel.sheets()[0]
cursor = connection.cursor()
# try:
for a in range(1, 1000):
    issue = sheet.row_values(a)
    storage_methods = issue[0]
    big_class = issue[1]
    small_class = issue[2]
    source = issue[3]
    barcode = int(issue[6])
    product_name = issue[7]
    spec = issue[9]
    level = issue[10]
    unit = issue[11]
    shelf_life = issue[13]
    shelf_life_format = str(re.sub(r'([\d]+)','',shelf_life))
    if shelf_life_format == "个月":
        shelf_life = int(re.findall(r"\d+\.?\d*", shelf_life)[0]) * 30
    if shelf_life_format == "天":
        shelf_life = int(re.findall(r"\d+\.?\d*", shelf_life)[0])
    if shelf_life_format == "年":
        shelf_life = int(re.findall(r"\d+\.?\d*", shelf_life)[0]) * 365
    in_price = issue[15]
    out_price = issue[17]
    size = issue[19]
    # print(storage_methods)
    # print(small_class)
    # print(source)
    # print(barcode)
    # print(product_name)
    # print(spec)
    # print(level)
    # print(unit)
    # print(shelf_life)
    print(product_name)
    # 检索是否存在相同条码的数据在数据库中
    select_sql = "select * from stock_management_m_product WHERE barcode = '" + str(barcode) + "'"
    result = cursor.execute(select_sql)
    if result == 0:
        insert_sql = "INSERT INTO stock_management_m_product" \
                     "(`storage_methods`,`big_class`,`small_class`,`source`,`barcode`,`product_name`,`spec`,`level`,`unit`,`shelf_life`,`in_price`,`size`)" \
                     " VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(insert_sql,(storage_methods, big_class, small_class, source, barcode, product_name, spec, level, unit, shelf_life, in_price, size))
        print("数据升级成功")
        connection.commit()

    try:
        update_sql = "UPDATE stock_management_rainbow_code_table SET out_price =' "+str(out_price)+"'WHERE barcode = "+str(barcode)
        print(update_sql)
        cursor.execute(update_sql)
        print("数据升级成功")
        connection.commit()
        update_sql = "UPDATE stock_management_rainbow_code_table SET product_name =' " + str(product_name) + "'WHERE barcode = " + str(barcode)
        print(update_sql)
        cursor.execute(update_sql)
        print("数据升级成功")
        connection.commit()
        update_sql = "UPDATE stock_management_m_product SET shelf_life =" + str(shelf_life) + " WHERE barcode = " + str(barcode)
        print(update_sql)
        cursor.execute(update_sql)
        print("数据升级成功")
        connection.commit()
    except:
        pass

