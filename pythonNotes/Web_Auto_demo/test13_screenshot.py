"""
webdriver内置了一些在测试中捕获屏幕并保存的方法
save_screenshot(filename)      获取当前屏幕截图并保存为指定文件，filename指指定保存的路径或者图片的文件名
get_screenshot_as_base64()     获取当前屏幕截图base65编码字符串
get_screenshot_as_file(filename)  获取当前的屏幕截图，使用完整的路径
get_screenshot_as_png()         获取当前屏幕截图的二进制文件数据
"""


from selenium import webdriver
from time import sleep

class TestCase(object):
	def __init__(self):
		self.driver = webdriver.Chrome('./chromedriver')
		self.driver.get('http://www.baidu.com')
	def test1(self):
		self.driver.find_element_by_id('kw').send_keys('selenium')
		self.driver.find_element_by_id('su').click()

		sleep(2)

		self.driver.save_screenshot('baidu.png')



if __name__ == '__main__':
	case = TestCase()
	case.test1()