__author__ = 'Administrator'
import xlrd
import pymysql
import re

# 将xlsx文件中的数据导入到MYSQL数据库中

# 打开EXCEL文件的地址
excel = xlrd.open_workbook(r'E:\WCC_SuperMarket\彩虹码超市交易记录2016-09-08.xlsx')
# 连接数据库
connection = pymysql.connect(host='localhost', user='root', password='',
                             db='mall_databases', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
# 设置导入的Sheet
# 获取第一个sheet
# sheet = excel.sheets()[0]
cursor = connection.cursor()
# # try:
# for a in range(1, 1000):
#     issue = sheet.row_values(a)
#     storage_methods = issue[0]
#     barcode = int(issue[2])
#     rainbow_code = int(issue[3])
#
#     #shelf_life = int(re.findall(r"\d+\.?\d*", shelf_life)[0]) * 30
#
#     update_sql = "UPDATE stock_management_rainbow_code_table SET status = '-1' WHERE barcode = '"+str(barcode)+"'and rainbow_code = '"+str(rainbow_code)+"'"
#     print(update_sql)
#     cursor.execute(update_sql)
#     print("数据升级成功")
#     connection.commit()


select_sql = "select * from stock_management_rainbow_code_table WHERE status = '1'"
print(select_sql)
cursor.execute(select_sql)
result = cursor.fetchall()
arr_barcode = []
for list in result:
    product = list['product_name']
    barcode = list['barcode']
    rainbow_code = list['barcode']
    arr_barcode.append(barcode)
dic = {}
for item in arr_barcode:
    if item in dic.keys():
        dic[item] = dic[item] + 1
    else:
        dic[item] = 1
print(dic)
for code in dic:
    stock = dic[code]
    print(stock)
    update_sql = "UPDATE stock_management_m_product SET stock = '"+str(stock)+"'WHERE barcode = '"+str(code)+"'"
    print(update_sql)
    cursor.execute(update_sql)
    print("数据升级成功")

connection.commit()





