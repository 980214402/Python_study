"""
url ：https://www.baidu.com/s
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75
"""

import requests

def get_baidu():
    url_baidu = 'https://www.baidu.com/s'
    headers_baidu = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75'}
    params_baidu = {'wd': '呵呵'}

    response_baidu = requests.get(url=url_baidu, params=params_baidu, headers=headers_baidu)
    print(response_baidu.text)


