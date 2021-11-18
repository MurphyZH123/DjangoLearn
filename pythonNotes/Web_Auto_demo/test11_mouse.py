"""
Selenium中的鼠标和键盘事件被封装在ActionChains类
正确的使用方法是：
ActionChains(driver).click(btn).perform()
下面列出ActionChains中常用方法：

click(on_element=None)  单击鼠标左键
click_and_hold(on_element=None) 点击鼠标左键，不松手
context_click(on_element=None)  点击鼠标右键
double_click(on_element=None)   双击鼠标左键
drag_and_drop(source,target)    拖拽到某个元素然后松开
drag_and_drop_by_offset(source,xoffset,yoffset)   拖拽到某个坐标然后松开
key_dome(value,element=None)  按下某个键盘上的键
key_up(value,element=None)   松开某个键
move_by_offset(xoffset,yoffset)   鼠标从当前位置移动到某个坐标
move_to_element(to_element)    鼠标移动到某个元素
move_to_element_with_offset(to_element.xoffset,yoffset)   动到距某个元素(左上角坐标)多少距离的位置
perform()    执行链中的所有动作
release(on_element=None)    在某个元素位置松开鼠标左键
send_keys(*keys_to_send)    发送某个键到当前焦点的元素
send_keys_to_element(element,*keys_to_send)  发送某个键到指定元素
测试的网址：http://sahitest.com/demo/clicks.htm

"""

from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys #虚拟键


class TestCase(object):
	def __init__(self):
		self.driver = webdriver.Chrome('./chromedriver')
		self.driver.maximize_window()
		#self.driver.get('http://sahitest.com/demo/clicks.htm')

	
	def test_mouse(self):
		#测试双击
		btn = self.driver.find_elenment_by_xpath()
		ActionChains(self.driver).double_click(btn).perform()
		sleep(2)

		#测试单击(一般使用click())
		btn = self.driver.find_elenment_by_xpath('/html/body/form/input[3]')
		ActionChains(self.driver).click(btn).profrom()
		sleep(2)

		#测试右键
		btn = self.driver.find_elenment_by_xpath('/html/body/form/input[4]')
		ActionChains(self.driver).context_click(btn).perform()

		sleep(2)


	#有关键盘的操作:如全选、复制、剪切、粘贴
	def test_key(self):
		self.driver.get('http://www.baidu.com')
		kw = self.driver.find_element_by_id('kw')
		kw.send_keys('selenium')
		kw.send_keys(Keys.CONTROL,'a')
		sleep(3)
		kw.send_keys(Keys.CONTROL,'x')
		sleep(3)
		kw.send_keys(Keys.CONTROL,'v')
		sleep(3)
		self.driver.quit()
		# e = self.driver.find_element_by_link_text('新闻')
		# print(e)
		# ActionChains(self.driver).move_to_element(e).click(e).perform()
		# sleep(2)
	





if __name__ =='__main__':
	case = TestCase()
	case.test_key()
















