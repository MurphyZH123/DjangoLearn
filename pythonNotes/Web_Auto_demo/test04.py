from selenium import webdriver
from time import sleep
#测试webelement的网站http://sahitest.com/demo/，可以供学习
class TestCase(object):
	def __init__(self):
		self.driver = webdriver.Chrome(executable_path='./chromedriver')
		self.driver.get('http://sahitest.com/demo/linkTest.htm')

	def test_webelement_prop(self):#测试webelement相关的属性
		e = self.driver.find_element_by_id('t1')
		print(type(e))
		
		# e1 = WebElement#alt+点击WebElement
		print(type(e))
		print(e.id)
		print(e.tag_name)
		print(e.size)
		print(e.rect)#宽度和高度
		print(e.text)

		sleep(2)
		self.driver.quit()

	def test_webelement_method(self):#测试webelement相关的方法
		e = self.driver.find_element_by_id('t1')
		e.send_keys('hello world')

		sleep(1)
		print(e.get_attribute('type'))
		print(e.get_attribute('name'))
		print(e.get_attribute('value'))
		print(e.get_attribute('font'))#字体
		print(e.get_attribute('color'))#颜色

		sleep(1)
		e.clear()#清空内容
		self.driver.quit()


	def test_method2(self):
		form_element = self.driver.find_element_by_xpath('/html/body/form[1]')
		form_element.find_element_by_id('t1').send_keys('hello world')


if __name__ == '__main__':
	case = TestCase()
	# case.test_webelement_prop()
	case.test_webelement_method()
