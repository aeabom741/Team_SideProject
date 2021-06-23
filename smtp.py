from email.mime import multipart
import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText


content = MIMEMultipart() # Build MIMEMultipart object

"""
Creat email content
"""
# sender
content["from"] = "g1072111012@gm.lhu.edu.tw" 

# receiver
content["to"] = "aeabom741@gmail.com" 

# Title
subject = "Python SMTP Email"
content["Subject"] = Header(subject,'utf-8')


att_1 = MIMEText(open('美國大盤.csv','rb').read(),'base64','utf-8')
att_1.add_header('Content-Disposition','attachment',filename = ('gbk','','美國大盤.csv'))
content.attach(att_1)

"""
Try connect SMTP Server
"""

with smtplib.SMTP(host='smtp.gmail.com',port="587") as smtp:
    
    try:
        #驗證smtp伺服器
        smtp.ehlo()
        print("驗證成功")

        #建立加密傳輸
        smtp.starttls()

        #login sender email
        smtp.login("g1072111012@gm.lhu.edu.tw",'vuratkokbufhuapb')
        print("Login successed")

        #Send the mail
        smtp.send_message(content)
        print("Complete")

        smtp.quit()
        print("SMTP quit")

    except Exception as e:
        print("Error message: " , e)
