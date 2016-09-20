__author__ = 'Administrator'
import xlrd
import pymysql
import re

# 将xlsx文件中的数据导入到MYSQL数据库中

# 打开EXCEL文件的地址
excel = xlrd.open_workbook(r'E:\WCC_SuperMarket\工作簿1.xlsx')
sheet = excel.sheets()[0]
for a in range(1, 1000):
    issue = sheet.row_values(a)
    barcode = int(issue[0])
    name = issue[1]
    shelf_life = int(issue[2])
    print("UPDATE TABLE_NAME SET shelf_life ='"+str(shelf_life) +"'WHERE barcode = '" + str(barcode)+"'")