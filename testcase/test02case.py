import unittest
from common import configHttp
import paramunittest
import geturlParams
import readExcel

login_xls = readExcel.readExcel().get_xls('testcase.xlsx', 'login')


@paramunittest.parametrized(*login_xls)
class testUserLogin(unittest.TestCase):
    def setParameters(self, case_name, path, data, method):

        self.case_name = str(case_name)
        self.path = str(path)
        self.data = str(data)
        self.method = str(method)

    def description(self):

        self.case_name

    def setUp(self):

        print("测试项目：" + self.case_name)
        print("测试路径：" + self.path)

    def test01case(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self):

        url = geturlParams.geturlParams.get_Url(self)
        info = configHttp.RunMain().run_main(self.method, url=url, data=self.data)
        print(info)

        if self.case_name == 'login':  # 如果case_name是login
            self.assertEqual(info['status'], 0)
        if self.case_name == 'login_error':  # 如果case_name是login_error
            self.assertEqual(info['msg'], '密码有误')
        if self.case_name == 'login_null':  # 如果case_name是login_null
            self.assertEqual(info['msg'], 'Pwd不能为空,Name不能为空')
