"""
url: http://test.lemonban.com/futureloan/mvc/api/member/register
url: http://120.25.246.42:8080/futureloan/mvc/api/member/register
data: {'mobilephone': 18482247433, 'pwd': 'lemon123'}

    http://test.lemonban.com/futureloan/mvc/api/member/register?mobilephone=18281186785&pwd=lemon123
    http://120.25.246.42:8080/futureloan/mvc/api/member/register?mobilephone=18281186785&pwd=lemon123

"""

import requests

post_url = 'http://120.25.246.42:8080/futureloan/mvc/api/member/register'
post_data = {'mobilephone': 18281186785, 'pwd': 'lemon123'}
response = requests.post(url=post_url, data=post_data)
print(response.json())
