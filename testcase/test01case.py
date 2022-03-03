import json
import unittest
from common import configHttp
import paramunittest
import geturlParams
import readExcel


login_xls = readExcel.readExcel().get_xls('testcase.xlsx', 'login')


@paramunittest.parametrized(*login_xls)
class testUserLogin(unittest.TestCase):
    def setParameters(self, case_name, path, data, method):
        """
        set params
        :param case_name:
        :param path
        :param query
        :param method
        :return:
        """
        self.case_name = str(case_name)
        self.path = str(path)
        self.data = str(data)
        self.method = str(method)

    def description(self):
        """
        test report description
        :return:
        """
        self.case_name

    def setUp(self):
        """
        :return:
        """
        print(self.case_name + ",测试开始前准备")
        print(self.path + ",测试开始前准备")

    def test01case(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self):  # 断言
        """
        check test result
        :return:
        """

        url = geturlParams.geturlParams.get_Url(self)
        info=configHttp.RunMain().run_main(self.method,url=url,data=self.data)
        print(info)



        # ss = info.json()
        if self.case_name == 'login':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(info['status'], 0)
        if self.case_name == 'login_error':  # 同上
            self.assertEqual(info['status'], 2)
        if self.case_name == 'login_null':  # 同上
            self.assertEqual(info['code'], 10001)