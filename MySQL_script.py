#!/usr/bin/env python
import MySQLdb
import xlsxwriter
import numpy as np
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# 1) We need to connect to database and then execute sql-query
db = MySQLdb.connect(host="IP ADDRESS",user="USER",passwd="password",db="DATABASE_NAME")
cursor = db.cursor()
cursor.execute("SQL QUERY")
rows = cursor.fetchall ()

cursor.close()
db.close()

# 2) Transfering data from list to array
array = np.array(rows)

# 3) From array to Excel file
workbook = xlsxwriter.Workbook('PATH_TO_FILE.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold':True})
worksheet.write('A1', 'COLUMN1', bold)
worksheet.write('B1', 'COLUMN2', bold)
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
