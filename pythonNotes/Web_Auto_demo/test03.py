from selenium import webdriver
from time import sleep 

class TestCase(object):
	def __init__(self):
		self.driver = webdriver.Chrome(executable_path='./chromedriver')
		self.driver.get('http://www.baidu.com')
		self.driver.maximize_window()
		sleep(1)

	def test_prop(self):
		print(self.driver.name)#查看浏览器的名称
		print(self.driver.current_url)#当前的url
		print(self.driver.title)#首页，比如可以用来判断用户当前是不是在首页
		print(self.driver.windows_handles)#查看当前的句柄数，就是浏览器的窗口数
		self.driver.quit()#关闭浏览器，包括所有的tab
		
	def test_method(self):
		self.driver.find_element_by_id('kw').send_keys('selenium')
		self.driver.find_element_by_id('su').click()
		sleep(1)
		self.driver.back()#返回上一页
		sleep(1)
		self.driver.refresh()#刷新
		sleep(1)
		self.driver.forward()#前进一页
		sleep(2)
		self.driver.close()#关闭当前tab

	def test_windows(self):#测试窗口
		self.driver.find_element_by_link_text('新闻').click()
		windows = self.driver.window_handles

		while 1:
			for  w in windows:
				self.driver.switch_to.window(w)#窗口切换
				sleep(1)



if __name__ == '__main__':
	case = TestCase()
	#case.test_prop()
	# case.test_method()
	case.test_windows()