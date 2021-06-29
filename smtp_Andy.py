import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
sys.path.append("/Users/shijunliao/Desktop/Python/side_project/weather")
import config as cfg


content = MIMEMultipart() # 建立MIMEMultipart物件

"""
Creat email content
"""
content["from"] = cfg.config["Gmail"]["Andy"]["account"]
content["to"] = cfg.config["Gmail"]["Andy_trial"]["account"]
content["subject"] = "Python SMTP Email"
content.attach(MIMEText(open("/Users/shijunliao/Desktop/Python/side_project/weather/mail.txt",'r').read()))  #郵件內容

# attach 附件
att_1 = MIMEText(open('/Users/shijunliao/Desktop/Python/side_project/weather/weather.zip','rb').read(),'base64','utf-8')
att_1.add_header('Content-Disposition','attachment',filename = ("utf-8","","weather.zip"))
content.attach(att_1)

"""
Try connect SMTP Server
"""
account = cfg.config["Gmail"]["Andy"]["account"]
password = cfg.config["Gmail"]["Andy"]["password"]

with smtplib.SMTP(host='smtp.gmail.com',port="587") as smtp:
    try:
        #驗證smtp伺服器
        smtp.ehlo()
        print("驗證成功")

        #建立加密傳輸
        smtp.starttls()

        #login sender email
        smtp.login(account, password)
        print("Login successed")

        #Send the mail
        smtp.send_message(content)
        print("Complete")

        smtp.quit()
        print("SMTP quit")

    except Exception as e:
        print("Error message: " , e)
