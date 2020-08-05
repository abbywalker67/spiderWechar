
import requests
from lxml import html

def get_content(name,url):
    # 设置请求头
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}

    html_data = requests.get(url, headers=headers).text
    #使用xpath语法
    selector = html.fromstring(html_data)

    texts = selector.xpath('//*[@class="rich_media_content "]//text()')

    result = ''
    for text in texts:
        result = result + text.replace(' ','').replace('\n','')

    print(result)

    name = name.replace('/','').replace('\\','').replace(':','').replace('*','').replace('?','').replace('"','').replace('<','').replace('>','').replace('|','')

    with open('./Data/'+name+'.txt','a+',encoding='utf-8') as f:
        f.write(result)
