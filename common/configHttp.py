import requests
import json

headers={
    "token": "b2ec075bfbda4dbca9bf3c7c348f0fe9",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x1800122c) NetType/WIFI Language/zh_CN",
    "Accept-Encoding": "gzip",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Content-Type": "application/json",
    "Content-Length": "129",
}
class RunMain():

    def send_post(self, url, data):  # 定义一个方法，传入需要的参数url和data
        # 参数必须按照url、data顺序传入
        result = requests.post(url=url, data=json.dumps(data), headers=headers)  # 因为这里要封装post方法，所以这里的url和data值不能写死
        res = result.json()
        return res

    def send_get(self, url, data):
        result = requests.get(url=url, data=json.dumps(data), headers=headers)
        res = result.json()
        return res

    def run_main(self, method, url=None, data=None):  # 定义一个run_main函数，通过传过来的method来进行不同的get或post请求
        result = None
        if method == 'post':
            result = self.send_post(url, data)
        elif method == 'get':
            result = self.send_get(url, data)
        else:
            print("method值错误！！！,method:%s" % (str(method)))
        return result



if __name__ == '__main__':  # 通过写死参数，来验证我们写的请求是否正确
    result1 = RunMain().run_main('post', 'https://platform-test-api.momtime.com/app/user/login', {"pwd":"888888", "name":"15330235989"})

    print(result1)
