import requests

url = "https://v2.alapi.cn/api/zaobao"

payload = "token= xxxxx &format=json" #tohen需注册alapi账号获得
headers = {'Content-Type': "application/x-www-form-urlencoded"}

response = requests.request("POST", url, data=payload, headers=headers)
print(type(response.json()))
text = response.json()

print(text)
text_1 = text['data']['news']
print(type(text_1))
print(text_1)
str= text['data']['date'] + '\n'
print(type(text_1[0]))
for i in text_1:
    str += i
    str += '\n'
print(str)
