"""
页面上的弹窗有三种：forms4.html
（1）alert：用来提示
（2）confirm：用来确认
（3）prompt:输入内容
accept() 接受
dismiss() 取消
text 显示的文本
send_keys 输入内容
"""
from selenium import webdriver
from time import sleep
import os

class TestCase(object):

	def __init__(self):
		self.driver = webdriver.Chrome('./chromedriver')
		path = os.path.dirname(os.path.abspath(__file__))
		file_path = 'file:///'+path+'/forms4.html'
		self.driver.get(file_path)
		self.driver.maximize_window()


	def test_alert(self):
		self.driver.find_element_by_id('alert').click()
		#切换到alert
		alert = self.driver.switch_to.alert#获取到alert元素
		print(alert.text)

		sleep(3)
		alert.accept()#点击确定

		self.driver.quit()


	def test_confirm(self):
		self.driver.find_element_by_id('confirm').click()
		confirm = self.driver.switch_to.alert
		print(confirm.text)

		sleep(3)
		# confirm.accept()#点击确定

		confirm.dismiss()



		self.driver.quit()

	def test_prompt(self):
		self.driver.find_element_by_id('prompt').click()
		sleep(2)

		prompt = self.driver.switch_to.alert
		print(prompt.text)
		sleep(2)


		prompt.accept()
		sleep(5)


		self.driver.quit()






if __name__ == '__main__':
	case = TestCase()
	# case.test_alert()
	# case.test_prompt()
	case.test_prompt()



