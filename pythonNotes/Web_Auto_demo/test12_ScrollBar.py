# """
# WebDriver 有两个方法来执行JavaScript，分别是：
# ·execute_script同步执行
# ·execute_async_script异步执行
# 通过JavaScript通常可以实现页面滚动
# """
# from selenium import webdriver 
# from time import sleep

# class TestCase(object):

# 	def __init__(self):
# 		self.driver = webdriver.Chrome('./chromedriver')
# 		self.driver.maximize_window()
# 		self.driver.get('http://www.baidu.com')

# 	def test1(self):
# 		self.driver.execute_script("alert('test')")
# 		sleep(2)
# 		self.driver.switch_to_alert.accept()
# 		print('测试完成')

# if __name__ == '__main__':
# 	case = TestCase()
# 	case.test1()
from selenium import webdriver
from time import sleep

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get('http://www.baidu.com')

    def test1(self):
        js = "alert('test')"
        self.driver.execute_script(js)
        sleep(2)
        self.driver.switch_to.alert.accept()

    def test2(self):
        js = 'return document.title'
        title = self.driver.execute_script(js)
        print(title)
        self.driver.quit()
    def test3(self):
        js = 'var q = document.getElementById("kw"); q.style.border="2px solid red"'
        self.driver.execute_script(js)

    def test4(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(2)
        js = 'window.scrollTo(0, document.body.scrollHeight)'#滚动到的地方
        self.driver.execute_script(js)
        sleep(2)


if __name__ == '__main__':
    case = TestCase()
    case.test2()







