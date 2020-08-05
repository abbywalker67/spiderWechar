

import requests,time
from spider_content import get_content


headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36',
    'Cookie': 'pgv_pvid=4172661490; eas_sid=a1X5C9m0o919P004r677N7W234; XWINDEXGREY=0; pgv_pvi=4572514304; ptui_loginuin=1115739951; RK=eijIFo22ZF; ptcz=b17e5caa7d3634bf5535dd92cbf108a5c7b45305db24e0c1d5b1406137888ae3; tvfe_boss_uuid=0e80ef9991522086; uin=o1115739951; pgv_info=ssid=s9673673910; o_cookie=1115739951; pac_uid=1_1115739951; iip=0; ied_qq=o1115739951; skey=@JSNwNGkLb; pgv_si=s9303534592; qqmusic_fromtag=66; rewardsn=; wxtokenkey=777; ua_id=np0m6uJnCIzja5l4AAAAADK6gP8zLBRyLWn0CTcYQhU=; openid2ticket_oYVZw5qFI2Kn3TvDpDsoEvNpAHLE=; mm_lang=zh_CN; uuid=f3dd876adf7469207140217b7c3d0e1c; rand_info=CAESIHu3CeOOnlLm0sSkF0Ev+X2y8r8OEXNi+DX2xiMn/LQu; slave_bizuin=3866121825; data_bizuin=3866121825; bizuin=3866121825; data_ticket=WO0+bRUPxOG5JLfVygyGJFAMvSP0CtKVO4tY/YNpaGoOpanUHDahm54R/4uh86Go; slave_sid=UVFOVzdsQUtsQXI0cThmMlYyeGF0UHBaV0tfaUVIRDBhSFZFXzl4NGZZZWpvV3dqbDhBX21raDdoZ0dob0FNd0JocU9CR25Ib3BfaEFfaXhzbVZXUzVwdnhQaTJDTGNiM3UwUEFIQnNSOXloaTBwdWw0RjM5M2M4S0hJZnlqOWp3aU4xTkRUdjNPVGxvaUtG; slave_user=gh_c7728ed4294d; xid=97369ade5d596cbcf20688b330a809b8'
}

params = {
    'action': 'list_ex',
    'count': '5',
    'fakeid': 'MzI2MTE5OTczMw==',
    'type': '9',
    'query':'',
    'token': '362749779',
    'lang': 'zh_CN',
    'f': 'json',
    'ajax': '1'
}

# 获取文章的标题和超链接
def get_url(url):
    #content = []
    count = 0
    page = 0
    for i in range(297):
        params['begin'] = i * 5
        response = requests.get(url,headers=headers,params=params).json()
        time.sleep(3)
        for item in response['app_msg_list']:
            items = [item['title'],item['link']]
            print(items)
            #content.append(items)
            get_content(item['title'],item['link'])
            time.sleep(2)
            count = count + 1
            print("*"*10+"正在下载，第"+str(count)+"文章"+"*"*10)
        page = page + 1
        print("#"*20)
        print("开始爬取"+str(page)+"页")
        print("#"*20)




if __name__ == '__main__':
    url = 'https://mp.weixin.qq.com/cgi-bin/appmsg'
    get_url(url)
