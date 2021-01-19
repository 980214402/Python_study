"""

User-Agent:
    Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36
"""

import requests

def get_baidu():
    url_baidu = 'https://www.baidu.com/s'
    baidu_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
    baidu_param = {'wd': '柠檬班'}

    response = requests.get(url=url_baidu, headers=baidu_headers, params=baidu_param)

    html1 = response.text
    print(html1)


post_url = 'http://test.lemonban.com/futureloan/mvc/api/member/register'
post_data = {'mobilephone': 18482247433, 'pwd': 'lemon123'}
response = requests.post(url=post_url, data=post_data)
# html = response.json()
# print(html)

# if html.get('msg') == '手机号码已被注册':
#     print('pass')
# if html['msg'] == '手机号码已被注册':
#     print('pass')