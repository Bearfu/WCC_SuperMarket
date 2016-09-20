from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEBase
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import pymysql
import datetime



# 生成需要发送的文件
def Create_csv(result):
    name = str(today) + '.csv'
    print(name)
    csvfile = open(name, 'w', newline='')
    title = "orderID,barcode,rainbow_code,out_datetime,all_price \n"
    csvfile.write(title)
    for line in result:
        print(line)
        barcode = line['barcode']
        rainbow_code = line['rainbow_code']
        orderID = line['orderID']
        out_datetime = line['out_datetime']
        all_price = line['out_price']
        data = str(orderID)+','+ str(barcode)+','+ str(rainbow_code)+','+ str(out_datetime)+','+ str(all_price)
        csvfile.write(data + '\n')

    csvfile.close()
    return name

def sql():
    # 从数据库获取需要发送的数据
    # 连接数据库
    connection = pymysql.connect(host='localhost', user='root', password='',
                                 db='mall_databases', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    select_sql = "select * from stock_management_mall_out_product WHERE DATE_ADD(now(),INTERVAL -1 DAY)< out_datetime and out_datetime < now()"
    cursor.execute(select_sql)
    result = cursor.fetchall()
    connection.commit()
    name = Create_csv(result)
    send_email(name)

# Email地址自动格式化
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
# 发送E_mail
def send_email(name):
    # 输入Email地址和口令:
    from_addr = '15071051125@163.com'
    password = '134679852'
    # 输入收件人地址:
    to_addr = 'rex_chen@wochacha.com'
    #to_addr = '15071051125@163.com'
    # 输入SMTP服务器地址:
    smtp_server = 'smtp.163.com'
    # 创建Message对象
    msg = MIMEMultipart()
    msg.attach(MIMEText('这是今天的线下销售数据，请查收。', 'plain', 'utf-8'))
    # 添加附件就是加上一个MIMEBase，从本地xlsx文件:
    with open(name, 'rb') as f:
        # 设置附件的MIME和文件名，这里是png类型:
        mime = MIMEBase('csv', 'csv', filename=name)
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename=name)
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)
    msg['From'] = _format_addr('Bear_fu<%s>' % from_addr)
    msg['To'] = _format_addr('leader <%s>' % to_addr)
    msg['Subject'] = Header('定时邮件', 'utf-8').encode()
    server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()

    # 输入Email地址和口令:
    from_addr = '15071051125@163.com'
    password = '134679852'
    # 输入收件人地址:
    to_addr = 'Nancy_meng@wochacha.com'
    # 输入SMTP服务器地址:
    smtp_server = 'smtp.163.com'
    # 创建Message对象
    msg = MIMEMultipart()
    msg.attach(MIMEText('这是今天的线下销售数据，请查收。', 'plain', 'utf-8'))
    # 添加附件就是加上一个MIMEBase，从本地csv文件:
    with open(name, 'rb') as f:
        # 设置附件的MIME和文件名，这里是csv类型:
        mime = MIMEBase('csv', 'csv', filename=name)
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename=name)
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)
    msg['From'] = _format_addr('Bear_fu<%s>' % from_addr)
    msg['To'] = _format_addr('leader <%s>' % to_addr)
    msg['Subject'] = Header('定时邮件', 'utf-8').encode()
    server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


#
# if __name__ == '__main__':
#     send_email()

if __name__ == '__main__':
    # 定时部分
    today = datetime.date.today()
    sql()
