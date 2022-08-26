import json
from pip._vendor import requests
import hashlib
import time
a = 'LinkDuoo.Sign'
t=int(time.time())
t1=time.time()
sign=a+str(t)
m = hashlib.md5()
m.update(sign.encode("utf8"))
a_md5 = m.hexdigest()


headers = {
 "token" :"9636593800444c6baaadb89ebddbe4b5",
 "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x1800122c) NetType/WIFI Language/zh_CN",
 "Accept-Encoding":"gzip, deflate, br   ",
 "Accept-Language":"zh-CN,zh;q=0.9",
 "Content-Type":"application/json",
 "Content-Length":"129",
 "signature":a_md5,
 "timestamp":str(t1)
}
data={
  "activityCode":"AL133058847498686469",
  "companyCode":"PDT00001"
}
n = 0
while n < 1000:
    # 抽奖接口
    url = "https://manage-test-api.3cpartner.com/platform-eshop/activityLottery/activityRandomAward"
    luckyUrl = requests.post(url=url, data=json.dumps(data),headers=headers)
    print(luckyUrl)
    with open('C:/Users/Lenovo/Desktop/choujiang/choujiang.txt', 'a+', encoding='utf-8') as f:
        print(luckyUrl.text, file=f)
        print('--------------------\n', file=f)
    print("这是第"+str(n+1) +"次")
    n+=1