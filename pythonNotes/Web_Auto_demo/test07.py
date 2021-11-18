"""
14.下拉列表 forms3.html
SE提供了一个工具类select
select_by_value() 根据值选择
select_by_index() 根据索引选择
select_by_visible_text 根据文本选择
deselect_by_value 根据值反选
deselect_by_index 根据索引反选
deselect_by_visible_text 根据文本反选
deselect_all 反选所有
options 所有选项
all_selected_options 所有选中选项
first_selected_option 第一个选择选项
"""
from selenium import webdriver
from time import sleep
import os
from selenium.webdriver.support.select import Select

class TestCase(object):
	def __init__(self):
		self.driver = webdriver.Chrome("./chromedriver")
		path =os.path.dirname(os.path.abspath(__file__))
		file_path = 'file:///'+path+'/forms3.html'
		self.driver.get(file_path)
		self.driver.maximize_window()

	def test_select(self):
		se = self.driver.find_element_by_id('provide')
		select=Select(se)

		select.select_by_index(2)

		sleep(2)

		select.select_by_value('bj')

		sleep(2)

		select.select_by_visible_text('TianJin')

		sleep(2)

		self.driver.quit()

	def test_select1(self):
		"""
		对应下拉框多选的情况，multiple在html中表示下拉框可以多选
		全选与取消全选
		"""

		se = self.driver.find_element_by_id('provide')
		select = Select(se)
		for x in range(3):
			select.select_by_index(x)
			sleep(1)
		sleep(2)



		select.deselect_all()#取消全选

		sleep(2)

		self.driver.quit()

	

	def test_select2(self):
		"""

		"""
		se = self.driver.find_element_by_id('provide')

		select = Select(se)

		for option in select.options:
			print(option.text)

		self.driver.quit()




if __name__ == '__main__':
	case = TestCase()
	# case.test_select()
	# case.test_select1()
	case.test_select2()

















