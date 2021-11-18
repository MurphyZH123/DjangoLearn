"""
checkbox和radio
"""




from selenium import webdriver
from time import sleep
import os

class TestCase(object):
	def __init__(self):
		self.driver = webdriver.Chrome('./chromedriver')
		path = os.path.dirname(os.path.abspath(__file__))
		file_path = 'file:///'+path+'/forms2.html'
		self.driver.get(file_path)
		# print(file_path)
		self.driver.maximize_window()

	def test_checkbox(self):
		swimming = self.driver.find_element_by_name('swimming')
		if not swimming.is_seleted():#判断是否选中 is_seleted()
			swimming.click()

		reading = self.driver.find_element_by_name('reading')
		if not reading.is_seleted():
			reading.click()

		sleep(5)
		swimming.click()#反选

		self.driver.quit()

	def test_radio(self):
		lst = self.driver.find_elements_by_name('gender')#拿到多个元素
		lst[1].click()
		# lst[1].click.quit()

		sleep(2)
		self.driver.quit()


if __name__ == '__main__':
	case = TestCase()
	# case.test_checkbox()
	case.test_radio()


