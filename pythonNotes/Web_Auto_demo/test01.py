# # 导入selenium 包
# from time import sleep
# from selenium import webdriver
# # 创建浏览器实例
# driver = webdriver.Chrome(executable_path='./chromedriver')
# # 打开百度
# driver.get("https://www.baidu.com")
# sleep(1)
# driver.find_element_by_id('kw').send_keys('selenium')
# driver.find_element_by_id('su')

# sleep(2)
# driver.quit()


# #元素定位find_element_by_id 通过ID定位元素
# from selenium import webdriver
# from time import sleep
# # 等价于from .chrome.webdriver import WebDriver as Chrome
# driver = webdriver.Chrome(executable_path='./chromedriver')
# driver.get('https://www.baidu.com')
# driver.maximize_window()
# sleep(2)

# element = driver.find_element_by_id('kw')
# element.send_keys('selenium')
# print(type(element))
# #<class 'selenium.webdriver.remote.webelement.WebElement'>


# driver.find_element_by_id('su').click()
# sleep(3)

# driver.quit()

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestCase(object):
	def __init__(self):
		self.driver = webdriver.Chrome(executable_path='./chromedriver')
		self.driver.get('https://www.baidu.com')
		self.driver.maximize_window()
		sleep(2)

	def test_id(self):
		element = self.driver.find_element_by_id('kw')
		element.send_keys('selenium')
		print(type(element))

		self.driver.find_element_by_id('su').click()
		sleep(3)

		#self.driver.quit()

	def test_name(self):
		self.driver.find_element_by_name('wd').send_keys('selenium')

		self.driver.find_element_by_id('su').click()
		sleep(3)

		self.driver.quit()

	def test_linktext(self):
		self.test.id()
		self.driver.find_element_by_link_text('百度首页').click()
		sleep(3)

		self.driver.quit()

		self.driver.quit()
	def test_partial_link_text(self):
		self.test_id()
		self.driver.find_element_by_partial_link_text('首页').click()
		sleep(3)

		self.driver.quit()

	def test_xpath(self):
		self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys('selenium')
		self.driver.find_element_by_id('su').click()
		sleep(2)

		self.driver.quit()

	def test_tag(self):
		# input = self.driver.find_element_by_tag_name('input')
		# print(input)#<selenium.webdriver.remote.webelement.WebElement (session="81eaf78f529ade9ae8c9f31b2f626e42", element="02ae77a8-4c41-4cab-afa5-4ac44bc3f94a")>
		# 会返回很多的input，这时就取你需要的那一个
		self.driver.find_element_by_tag_name('input')[0].send_keys('selenium')
		self.driver.find_element_by_id('su').click()
		sleep(2)

		self.driver.quit()


	def test_css_selector(self):
		self.driver.find_element_by_css_selector('#kw').send_keys('selenium')
		self.driver.find_element_by_id('su').click()
		sleep(2)

		self.driver.quit()

	def test_class_name(self):
		self.driver.find_element_by_class_name('s_ipt').send_keys('selenium')
		self.driver.find_element_by_id('su').click()

		sleep(2)
		self.driver.quit()

	def test_all(self):
		self.driver.find_element(value='kw').send_keys('selenium')#默认by_id
		self.driver.find_element(value='su').click()
		sleep(2)
		self.driver.quit()






if __name__ == '__main__':
	test=TestCase()
	# test.test_name()
	# test.test_partial_link_text()
	# test.test_xpath()
	# test.test_tag()
	# test.test_css_selector()
	# test.test_class_name()
	test.test_all()

























