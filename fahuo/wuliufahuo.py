import requests
import json

base_url = 'http://router-order.test.yuoucn.cn:50000/feign/order/supplier_logistic_callback'
dingdanhao = input("请输入订单号：")  # YUOU202208166337658627
yonghubianma = input("请输入用户编码：")
shangpinbianma = input("请输入商品编码：")  # 0300349
shangjiahuohao = input("请输入商家货号：")  # lhq123123
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
    "Content-Type": "application/json",
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
