# -*- coding: utf-8 -*-
import requests
import os
#报错：check_hostname requires server_hostname，关闭代理

headers = {
    'User-Agent': 'lujie'
}
dir_name = '爬虫'
path = r'C:\Users\jie.lu\Desktop\fiddler'
create_url = path + '\\'+ dir_name

if not os.path.exists(dir_name):
    os.mkdir(create_url)


for i in range(1,10):
    url = 'https://api.bilibili.com/x/tag/ranking/archives?tag_id=1240&rid=20&type=0&pn='+ str(i) + '&ps=20&jsonp=jsonp'

    #请求网址
    html = requests.get(url,headers=headers)
    # print(html.text)
    #查看headers
    print(html.request.headers)

    for j in range(len(html.json()['data']['archives'])):
        pic = html.json()['data']['archives'][j]['pic']
        name =  html.json()['data']['archives'][j]['owner']['name'] + '.jpg'
        print(pic)
        print(name)



        response = requests.get(pic,headers=headers)
        with open(create_url + '/' + name,'wb') as f:
            # 如果想取文本数据可以通过response.text 如果想取图片，文件，则可以通过 response.content
            f.write(response.content)


