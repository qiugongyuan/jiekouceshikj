
import json
from pip._vendor import requests

headers={
    "token": "b2ec075bfbda4dbca9bf3c7c348f0fe9",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x1800122c) NetType/WIFI Language/zh_CN",
    "Accept-Encoding": "gzip",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Content-Type": "application/json",
    "Content-Length": "129",
}

def login():
    url = "https://platform-test-api.momtime.com/app/user/login"
    data={
        "pwd": "888888",
        "name": "15330235989"
    }

    luckyUrl = requests.post(url=url,verify=False, data=json.dumps(data), headers=headers)
    result=luckyUrl.json()
    print(luckyUrl.text)
    # print(luckyUrl.status_code)
    # print(result['status'])
    if result['status']==0:
        print ("登录成功")
    else:
        print("登录失败")

if __name__ == '__main__':
    login()


