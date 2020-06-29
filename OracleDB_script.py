#!/usr/bin/env python
import cx_Oracle
import xlsxwriter
import numpy as np
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# 1) We need to connect to database and then execute sql-query
# First variant:
conn_info = { 'host': 'IP-ADDRESS',
              'port': 'PORT',
              'user': 'USERNAME',
              'psw': 'PASSWORD',
              'service': 'SERVICE_NAME'     # Service_Name - это функция, в которой база данных может зарегистрироваться для прослушивателя.
                                            # https://stackoverflow.com/questions/22399766/how-to-find-oracle-service-name
            }
conn_str = '{user}/{psw}@{host}:{port}/{service}'.format(**CONN_INFO)
QUERY = ''' select * from table where ... '''  # You need to put you SQL-query here

class DB:
    def __init__(self):
        self.conn = cx_Oracle.connection(conn_str)

    def query(self, query):
        cursor = self.conn.cursor()
        sql_result = cursor.execute(query).fetchall()
        cursor.close()
        return sql_result

db = DB()
sql_result = db.query(QUERY)

#Second variant
# dsn_tns = cx_Oracle.makedsn('server', 'port', service_name='service_name')
# conn = cx_Oracle.connect(user='username', password='password', dsn=dsn_tns)
# c = conn.cursor()
# rows = c.execute('select count(*) from TABLE_NAME')


# 2) Transfering data from list to array
# FIRST OPTION:
array = np.array(sql_result)
# SECOND OPTION:
#array = np.array(rows)


# 3) From array to Excel file
workbook = xlsxwriter.Workbook('PATH_TO_FILE.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold':True})
worksheet.write('A1', 'COLUMN1', bold) # Количество колонок и подписей колонки нужно добавлять в зависимости от полученных данных
worksheet.write('B1', 'COLUMN2', bold) # Тоесть мы подстраиваемся под итоговые колонки из Select
row = 1
col = 0
for COLUMN1, COLUMN2 in (array):
    worksheet.write(row, col, COLUMN1)
    worksheet.write(row, col + 1, COLUMN2)
    row += 1
workbook.close()

# 4) Sending Excel file using GMAIL SMTP server
fromaddr = "EMAIL_FROM@gmail.com"
toaddr = "EMAIL TO"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Excel doc"
body = "Body"
msg.attach(MIMEText(body, 'plain'))
filename = "File.xlsx"
attachment = open("PATH TO FILE", "rb")
p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(p)
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(fromaddr, "PASSWORD")
text = msg.as_string()
s.sendmail(fromaddr, toaddr, text)
print('Message Sent')
s.quit()
