import unittest
from tools.HTMLTestRunner import HTMLTestRunner
from srcipts.test01_login import login_test
from srcipts.test02_wokers import wokers_test
import time
if __name__ == "__main__":
    path='./report/report{}.html'.format(time.strftime("%Y%m%d-%H%M%S"))
    suit=unittest.TestSuite()
    suit.addTest(unittest.TestLoader.loadTestsFromTestCase(login_test))
    #多场景依赖问题
    suit.addTest(login_test("test01_login"))
    suit.addTest(unittest.TestLoader.loadTestsFromTestCase(wokers_test))
    with open(path,'wb',encoding='utf-8') as fd:
         runner=HTMLTestRunner(fd)
         runner.run(suit)