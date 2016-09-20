import requests
import datetime
import json
import urllib.request
def print_rainbowcode():
    today = str(datetime.date.today())
    # print(today)
    url = 'http://192.168.3.147:8000/Stock/api/purchase/print_rainbowcode'
    payload = {"Device_ID":"001","Income":[{"Barcode":"6920152429686","Batch":"1609015001001","Channel":"SH Channel","GuaranteePeriod":180,"ProductionDate":"2016-09-01","PurchasePrice":5.5,"RainbowCode":"417022801010010"},{"Barcode":"6920152429686","Batch":"1609015001001","Channel":"SH Channel","GuaranteePeriod":180,"ProductionDate":"2016-09-01","PurchasePrice":5.5,"RainbowCode":"417022801011585"}],"Operator":"admin","SumNum":2,"UploadIndex":"1"}
    r = requests.post(url, data=json.dumps(payload))

    print(r.text)
    print(r)

def upload_index():
    today = str(datetime.date.today())
    # 请求：
    # POST http://xxx.xxx.xxx.xxx/api/Supermarket/print_rainbowcode/
    # Operator: 本次上传的操作人员, string
    # device_id ：上传的操作设备
    # Income: 本次上传的数据（数组List）
    #     Barcode: 商品条码,string
    #     RainbowCode: 彩虹码,string
    #     Batch: 该品的批次号,string
    # 响应：
    #      statue 写入状态 string
    url = 'http://192.168.3.147:8000/Stock/api/purchase/upload_index'

    payload = {"Device_ID":"001","Operator_Num":"admin","Batch":"1609055001001","CodeGen":["6901234000184*424110801011201","6901234000184*424110801010750","6901234000184*424110801011206","6901234000184*424110801012536","6901234000184*424110801011656","6901234000184*424110801012055","6901234000184*424110801013106","6901234000184*424110801011027","6901234000184*424110801012661","6901234000184*424110801012734"]}

    r = requests.post(url, data=json.dumps(payload))

    print(r.text)
    print(r)

def get_product_info():
    url = 'http://192.168.3.147:8000/Stock/api/purchase/get_product_info'
    payload = {"Barcode":"6902890234166","RainbowCode":"416111901013866"}
    r = requests.post(url, data=json.dumps(payload))
    print(r.text)
    print(r)

def order_list():
    url = r'http://192.168.3.147:8000/Stock/api/purchase/order_list'
    # orderID:订单编号, string
    # PC_num:pos机编号, string
    # operator:操作员工号,string
    # product_info[array]
    #     Barcode: 商品条码,int
    #     RainbowCode: 彩虹码,int
    product_info = [
        {'Barcode': 6924513905086,
         'RainbowCode': 2016062301048550,
         },
        {'Barcode': 6924513905086,
         'RainbowCode': 2016062301048551,
         },
        {'Barcode': 6924513905086,
         'RainbowCode': 2016062301048552,
         },
        {'Barcode': 6924513905086,
         'RainbowCode': 2016062301048553,
         },
        {'Barcode': 6924513905086,
         'RainbowCode': 2016062301048554,
         },
        {'Barcode': 6924513905086,
         'RainbowCode': 2016062301048555,
         }

    ]
    payload = {
            "orderID": "SH10011609051234500100000001",
            "PC_num": "1234",
            "operator": "5001",
            "product_info": [
        {
            "Barcode": "6926858908005",
            "RainbowCode": "417082801013775"
        }
    ]
}
    r = requests.post(url, data=json.dumps(payload))
    print(r.text)
    print(r)

def Other():
    from datetime import datetime, timedelta
    import datetime
    ProductionDate = '2016-08-26'
    date_formate = "%Y-%m-%d" # year-month-day
    ProductionDate = datetime.datetime.strptime(ProductionDate, date_formate)
    date = 30
    d = datetime.timedelta(date)
    end_Date = ProductionDate + d
    if ProductionDate < end_Date:
        print('a')

def Write_off():
    url = r'http://192.168.3.147:8000/Stock/api/purchase/Write_off'
    #     orderID:订单编号, string
    #     in_come:收到金额,Float
    #     out_come:找零金额,Float
    payload = {
  "orderID": "SH10011609121234500100000022",
  "PC_num": "1234",
  "operator": "5001",
  "all_price": 2.2,
  "off_price": 0.0,
  "out_price": 2.2,
  "in_come": 2.2,
  "out_come": 0.0,
  "product_info": [
    {
      "Barcode": "6907992100272",
      "RainbowCode": "417012801012356"
    }
  ]
}
    r = requests.post(url, data=json.dumps(payload))
    print(r.text)
    print(r)

def UP():
    url = 'http://businessrm.alpha.wochacha.cn/rainbowmarket/uploadcominfo'
    a = {"data":[
        {
            "ComCatID": "1",
            "Spec": "瓶",
            "Unit": "100ml",
            "ComName": "正官庄高丽参元饮品",
            "ShelfLifeUnit": "1",
            "ShelfLife": 720,
            "MEID": 1,
            "Barcode": 8809023009135,
            "Image": "http://imagealpha.wochacha.com/picture1.jpg"
        },
        {
            "ComCatID": "1",
            "Spec": "瓶",
            "Unit": "100ml",
            "ComName": "正官庄高丽参元饮品",
            "ShelfLifeUnit": "1",
            "ShelfLife": 720,
            "MEID": 1,
            "Barcode": 8809023009135,
            "Image": "http://imagealpha.wochacha.com/picture1.jpg"
        }
    ]
    }
    r = requests.post(url, data=a)
    print(r.text)

def UP_RainBow():
    URL = "http://businessrm.alpha.wochacha.cn/rainbowmarket/updaterainbowstatus"
    load = {
        'MEID': 64,
        'Barcode': 6941994000918,
        'RainbowCode': 419041301010124,
        'RainbowStatus': 30
    }
    r = requests.post(URL, data=load)
    print(r.text)

def up_load_Produce_WCC():
    arr = []
    URL = r"http://businessrm.alpha.wochacha.cn/rainbowmarket/uploadcominfo"
    data = {
            "ComCatID": 1,
            "Spec": "包",
            "Unit": "68g",
            "ComName": "卫龙大面筋",
            "ShelfLifeUnit": "1",
            "ShelfLife": 720,
            "MEID": 1,
            "Barcode": 6935284412239,
            #"Image": "http://imagealpha.wochacha.com/picture1.jpg"
        }
    arr.append(data)
    data = {"data": json.dumps(arr, ensure_ascii=False, indent=2)}
    r = requests.post(URL, data=data)
    print(r.text)
    print(data)

def check_order_list(Orderid):
    URL = r"http://businessrm.alpha.wochacha.cn/rainbowmarket/getorderdetailmarket"
    load = {
        'Orderid': Orderid,
    }
    r = requests.post(URL, data=load)
    json_data = r.json()
    isok = json_data['data']
    print(isok)
    print(r.json())
    print(r)

if __name__ == '__main__':
    UP_RainBow()


