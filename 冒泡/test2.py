
#!/usr/bin/python
# -*- coding: utf-8 -*-
import smtplib, time, os
from email.mime.text import MIMEText
from email.header import Header

def send_mail_html(file):
    sender = 'jie.lu@garena.cn' #发件人
    receiver = 'jie.lu@garena.cn' #收件人
    t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  #获取当前时间
    subject = '博客磁盘使用报警_' + t  #邮件主题
    smtpserver = 'smtp.exmail.qq.com' #发送服务器地址
    username = 'jie.lu@garena.cn' #用户名
    password = 'BMvgJX7gbut44Xz4' #密码

    f = open(file, 'rb')
    mail_body = f.read()
    f.close()


    msg = MIMEText(mail_body, _subtype='html', _charset='gbk')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = receiver

    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
    except:
        print("邮件发送失败！")
    else:
        print("邮件发送成功！")
    finally:
        smtp.quit()

file = 'C:\\Users\\jie.lu\\Desktop\\test_111.files\\sheet001.htm' #html文件
send_mail_html(file)