import requests
import json
import requests
import json
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/fh', methods=['GET', 'POST'])
def fh():
    if request.method == "POST":
        base_url2 = 'http://router-order.test.yuoucn.cn:50000/feign/order/supplier_logistic_callback'
        dingdanhao = request.form.get("订单号")
        yonghubianma = request.form.get("用户编码")
        shangpinbianma=request.form.get("商品编码")
        shangjiahuohao=request.form.get("商家货号")

        data = {
            "orderSn": dingdanhao,
            "packs": [
                {
                    "goodsList": [
                        {
                            "goodsBaseCode": shangpinbianma,  # 0300349
                            "merchantGoodsCode": shangjiahuohao,  # lhq123123
                            "number": 1
                        }
                    ],
                    "logisticsCompanyCode": "3",
                    "trackingCode": "YT2163659769780"
                }
            ],
            "roleType": "02",
            "userCode": yonghubianma
        }

        headers = {
            "Content-Length": "100",
            "Content-Type": "application/json",
            "Date": "Wed, 17 Aug 2022 06:46:10 GMT"
        }

        luckyUrl = requests.post(url=base_url2, verify=False, data=json.dumps(data), headers=headers)
        result = luckyUrl.json()
        print(luckyUrl.text)
        # print(luckyUrl.status_code)
        # print(result['status'])
        if result['code'] == 200:
            print("拉取成功")
            return result
        else:
            print(result['message'])


if __name__ == "__main__":
    app.run(port=5555)
