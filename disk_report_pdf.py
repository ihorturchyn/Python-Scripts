#!/usr/bin/env python
import subprocess
import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def disk_report():
	p = subprocess.Popen("df -h", shell=True, stdout=subprocess.PIPE)
	return p.stdout.readlines()

def create_pdf(input, output = "/home/disk_report.pdf"):
	now = datetime.datetime.today()
	date = now.strftime("%h %d %Y %H:%M:%S")
	c = canvas.Canvas(output)
	textobject = c.beginText()
	textobject.setTextOrigin(inch, 11*inch)
	textobject.textLines(''' Disk Capacity Report: %s ''' % date)
	
	for line in input:
		textobject.textLine(line.strip())
	c.drawText(textobject)
	c.showPage()
	c.save()

report = disk_report()
create_pdf(report)

fromaddr = "lahermandad94@gmail.com"
toaddr = "BlackStile@ukr.net"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Disk Space doc"
body = "Hello"
msg.attach(MIMEText(body, 'plain'))
filename = "disk_report.pdf"
attachment = open("/home/disk_report.pdf", "rb")
p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(p)
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(fromaddr, "VerizonR523")
text = msg.as_string()
s.sendmail(fromaddr, toaddr, text)
print('Message Sent')
s.quit()
