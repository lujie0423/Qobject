import smtplib
import calendar
import datetime
import os,time,re
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email import encoders
from email.mime.base import MIMEBase




today = datetime.datetime.now()
#strftime 当数字为
now_month = today.strftime('%m')
now_day = today.strftime('%d')
now = now_month + "月" + now_day + "号"


# 日报 #
mailserver = "smtp.exmail.qq.com"  #邮箱服务器地址
username_send = 'jie.lu@garena.cn'  #邮箱用户名
password = 'BMvgJX7gbut44Xz4'   #邮箱密码：需要使用授权码
username_recv = ['aru_all@garena.cn']  #收件人，多个收件人用逗号隔开
username_cc = ['guol@garena.cn']  #抄送人，多个收件人用逗号隔开
reciver = username_recv + username_cc

# 创建一个带附件的邮件实例（内容）
msg = MIMEMultipart('alternative')
#找到report目录下最新生成的报告文件供后续使用
result_dir = 'C:\\Users\\jie.lu\\Desktop'
lists=os.listdir(result_dir)
lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn) if not
               os.path.isdir(result_dir+"\\"+fn) else 0)
print (u'The Latest Test Report is: '+lists[-1])
file_new = os.path.join(result_dir,lists[-1])

msgtext = MIMEText("<font style=font-size:19px;>Hi，<br>QA已经完成 %s Dev（iOS&Android）版本的Smoke Test。<br>以下为总表，详细测试用例请看附件。</font><br>" %(now), "html", "utf-8")
msg.attach(msgtext)


# html = """
# <html>
#     <body>
#         <p>
#         <br><img src ="cid:image1"></br>
#         <br><img src ="cid:image2"></br>
#         </p>
#     </body>
# </html>
# """


# 指定图片为当前目录
msg.attach(MIMEText('<html><body>'+'<p><img src="cid:1"></p>'+'<p><img src="cid:2"></p>'+'</body></html>', 'html', 'utf-8'))
with open('C:\\Users\\jie.lu\\Desktop\\每日报告\\1.png', 'rb') as fp:
    # msgImage = MIMEImage(fp.read())
    # fp.close()
    # msgImage.add_header('Content-ID', '<image1>')
    # msg.attach(msgImage)
    mine = MIMEBase('image', 'png')
    mine.add_header('Content-ID', '1')
    mine.set_payload(fp.read())
    encoders.encode_base64(mine)
    msg.attach(mine)

with open('C:\\Users\\jie.lu\\Desktop\\每日报告\\2.png', 'rb') as fp:
    mine = MIMEBase('image', 'png')
    mine.add_header('Content-ID', '2')
    mine.set_payload(fp.read())
    encoders.encode_base64(mine)
    msg.attach(mine)


# fp = open('C:\\Users\\jie.lu\\Desktop\\每日报告\\2.png', 'rb')
# msgImage1 = MIMEImage(fp.read())
# fp.close()
# msgImage1.add_header('Content-ID', '<image2>')
# msg.attach(msgImage1)
#
# The_end = MIMEText(html, _subtype='html', _charset="utf")
# # encoders.encode_base64(The_end)
# msg.attach(The_end)

#定义邮件的附件
with  open(file_new, 'rb') as fp:
    att1 = MIMEText(fp.read(), 'base64', 'utf-8')
    #[errno 13]权限被拒绝  关闭文件后，重新运行
    att1["Content-Type"] = 'application/octet-stream'
    att1.add_header('Content-Disposition', 'attachment', filename='SMOKE_版本.xlsx')#这里的filename指的是附件的名称及类型
    # 把附件的内容读进来:
    # att1.set_payload(fp.read())
    # 用Base64编码:
    # encoders.encode_base64(att1)
    msg.attach(att1)

# # 构造图片链接
# sendimagefile_1=open(r'C:\Users\jie.lu\Desktop\每日报告\1.png','rb').read()
# sendimagefile_2=open(r'C:\Users\jie.lu\Desktop\每日报告\2.png','rb').read()
# image_1 = MIMEImage(sendimagefile_1)
# image_2 = MIMEImage(sendimagefile_2)
# image_1.add_header('Content-ID','<image1>')
# image_2.add_header('Content-ID','<image2>')
# image_1["Content-Disposition"] = 'attachment; filename="1.png"'
# image_2["Content-Disposition"] = 'attachment; filename="2.png"'
# msg.attach(image_1)
# msg.attach(image_2)


# mail = MIMEText(mail_msg,'html','utf-8')
msg['Subject'] = '[QA][iOS&Android]Daily Smoke Test Report-2021_'+ now_month +'_'+ now_day
msg['From'] = username_send  #发件人
msg['To'] = ";".join(username_recv)  #收件人；[]里的三个是固定写法，别问为什么，我只是代码的搬运工
msg['Cc'] = ";".join(username_cc)
# smtp = smtplib.SMTP(mailserver,port=25) # 连接邮箱服务器，smtp的端口号是25
smtp=smtplib.SMTP_SSL(mailserver,port=465) #QQ邮箱的服务器和端口号
smtp.ehlo()
smtp.login(username_send,password)  #登录邮箱

smtp.sendmail(username_send,reciver,msg.as_string())# 参数分别是发送者，接收者，第三个是把上面的发送邮件的内容变成字符串
smtp.quit() # 发送完毕后退出smtp
print ('success')

# BMvgJX7gbut44Xz4