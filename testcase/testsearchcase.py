import unittest
from common import configHttp
import paramunittest
import geturlParams
import readExcel
import jsonpath

search_xls = readExcel.readExcel().get_xls('testcase.xlsx', 'search')


@paramunittest.parametrized(*search_xls)
class testUserSearch(unittest.TestCase):
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

    def testsearch(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self):

        url = geturlParams.geturlParams.get_Url(self) + self.path
        info = configHttp.RunMain().run_main(self.method, url=url, data=self.data.encode('utf-8'))
        print(info)

        response = jsonpath.jsonpath(info, '$.data.total[0]')
        test = jsonpath.jsonpath(info, '$..goodsName')

        if self.case_name == 'search':  # 如果case_name是search
            self.assertEqual(test[0], '德国蓝罐爱他美经典款（金华关区）')
        if self.case_name == 'search_null':  # 如果case_name是search_null
            self.assertEqual(response, 0)


