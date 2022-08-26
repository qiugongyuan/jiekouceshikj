import requests
import json
from flask import Flask
from flask import render_template
from flask import url_for
from flask import request

base_url = 'http://router-order.test.yuoucn.cn:50000/feign/order/supplier_confirm_get'
dingdanhao = input("请输入订单号：")
yonghubianma = input("请输入用户编码：")
data = {
    "isComeFromLinkduoo": 'true',  #
    "orderSn": dingdanhao,  # YUOU202208166337658627
    "userCode": yonghubianma
}

headers = {
    "Content-Length": "100",
    "Content-Type": "application/json",
    "Date": "Wed, 17 Aug 2022 06:46:10 GMT"
}


def wuliuhuichuan():
    luckyUrl = requests.post(url=base_url, verify=False, data=json.dumps(data), headers=headers)
    result = luckyUrl.json()
    print(luckyUrl.text)
    # print(luckyUrl.status_code)
    # print(result['status'])
    if result['code'] == 200:
        print("拉取成功")
    else:
        print(result['message'])


if __name__ == '__main__':
    wuliuhuichuan()
