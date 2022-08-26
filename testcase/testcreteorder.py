import unittest
from common import configHttp
import paramunittest
import geturlParams
import readExcel
import jsonpath

createoder_xls = readExcel.readExcel().get_xls('testcase.xlsx', 'order')


@paramunittest.parametrized(*createoder_xls)
class testCreateOrder(unittest.TestCase):
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

        if self.case_name == 'yichang':  # 如果case_name是search
            self.assertEqual(info['msg'], '获取供应商编码异常,请稍后再试')
        if self.case_name == 'success':  # 如果case_name是search_null
            self.assertEqual(info['status'], 0)


