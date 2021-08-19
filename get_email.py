# coding=utf-8
import imaplib, email, os
import email
from email.header import decode_header
import datetime

if __name__ == '__main__':
    a = []
    username = 'jie.lu@garena.cn'
    pw = 'BMvgJX7gbut44Xz4'
    imapadd = "smtp.exmail.qq.com"
    today = datetime.datetime.now().strftime('%d-%b-%Y')
    conn = imaplib.IMAP4(imapadd)
    conn.login(username, pw)
    conn.select('INBOX')
    print(today)
    # resp, item = conn.search(None, 'ON %s' % today)
    resp, item = conn.search(None, "[Arukas][Client]")
    # print(item)
    print('Today`s total mail is [%s],and Subject is here:' % len(item[0].split()))
    #筛选前20封邮件

    count = 0
    for i in range(len(item[0].split())-20, len(item[0].split())):
        resp, mailData = conn.fetch(item[0].split()[i], '(RFC822)')
        mailText = mailData[0][1]
        msg = email.message_from_bytes(mailText)
        subject = msg['Subject']
        subdecode = decode_header(subject)
        if subdecode[0][1] == None:
            if "[Arukas][Client]" in subdecode[0][0]:
                # print(subdecode[0][0])
                str = ''.join(subdecode[0][0])
                print(str)
                a.append(str)
            else:
                pass
            count = count + 1
            print(count)
        else:
            # print(subdecode[0][0].decode('utf8'))
            pass

    # 把列表a中的元素拆分最后三位至b
    b = []
    for i in range(len(a)):
        b.append(int(a[i][-3:]))
    print(b)
    # 找到最大值的索引
    max_index = b.index(max(b))
    #找到对应索引的数值
    max_num = int(a[max_index][-3:])
    #找到最大值重复元素的个数
    max_num_count = b.count(max_num)
    print(max_num_count)
    if max_num_count == 2:
        print("打包成功！！！")
        pass
    elif max_num_count == 1:
        if "[ios]" in a[max_index]:
            print("未发现安卓版本")
        else:
            print("未发现IOS版本")
    else:
        print("两个包均打包失败")




