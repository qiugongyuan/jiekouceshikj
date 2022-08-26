import requests
import json
from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/lq/', methods=['GET','POST'])
def lq():
    if request.method == "POST":
        base_url = 'http://router-order.test.yuoucn.cn:50000/feign/order/supplier_confirm_get'
        dingdanhao = request.form.get("订单号")
        yonghubianma = request.form.get("用户编码")
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
        luckyUrl = requests.post(url=base_url, verify=False, data=json.dumps(data), headers=headers)
        if luckyUrl.status_code == 400:
            print(luckyUrl.reason)
            return luckyUrl.reason
        result = luckyUrl.json()
        print(luckyUrl.text)
        # print(luckyUrl.status_code)
        # print(result['status'])
        if result['code'] == 200:
            print("拉取成功")
            return result
        else:
            print(result['message'])
            return luckyUrl.text





if __name__ == "__main__":
    app.run(port = 8881)
