from bs4 import BeautifulSoup
from robobrowser import RoboBrowser
import pandas as pd

browser=RoboBrowser()
base_url='https://www.worldometers.info/coronavirus/'
browser.open(base_url)
tabledata=browser.find("tbody")
rowdata=tabledata.select("tr")

lst=[]
temp=[]
temp1=[]
temp2=[]
temp3=[]
temp4=[]
for i in range(0,9):
    temp.append(rowdata[0].select("td")[i].get_text())
for i in range(0,9):
    temp1.append(rowdata[1].select("td")[i].get_text())
for i in range(0,9):
    temp2.append(rowdata[2].select("td")[i].get_text())
for i in range(0,9):
    temp3.append(rowdata[3].select("td")[i].get_text())
for i in range(0,9):
    temp4.append(rowdata[32].select("td")[i].get_text())
lst.append(temp)
lst.append(temp1)
lst.append(temp2)
lst.append(temp3)
lst.append(temp4)
    
df = pd.DataFrame(lst, columns =['Country', 'Total Cases', 'New Cases','Total Deaths','New Deaths','Total Recoveries','Active Cases','Serious/Critical','Total Cases/1M population']) 

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "tyagipratyaksh@gmail.com"
recipients = ['bhattacharya.2@iitj.ac.in']
password = input("Enter Your Password")

message = MIMEMultipart("alternative")
message["Subject"] = "Corona Virus Tracker Updates"
message["From"] = sender_email
message['To'] = ", ".join(recipients)

html = """\
<html>
  <head></head>
  <body>
    <p>
    Hi  <br>
    This is Corona Virus Tracker Live Updates from different Countries.<br>
    </p>
    {0}
    <br>

    Stay Safe , Stay Alert ! <br>
    Made By Pratyaksh 
  </body>
</html>
""".format(df.to_html())

part1 = MIMEText(html, 'html')
message.attach(part1)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, recipients, message.as_string()
    )
