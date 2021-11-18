"""
title_is    判断title，是否出现       布尔类型
title_contains 判断title，是否包含某些字符。    布尔类型
presence_of_element_located       判断某个元素是否加到了dom树里，并不代表该元素一定可见     WebElement
visibility_of_element_located     判断某个元素是否被加到了dom树里并且可见，宽和高都大于0    WebElement
visibility_of                     判断元素是否可见，如果可见就返回这个元素                 WebElement
presence_of_all_elements_located  判断是否至少有一个元素存在dom树中                       列表
vicibility_of_any_elements_located  判断是否至少有一个元素在页面中可见。                   列表
text_to_be_present_in_element       判断指定的元素中是否包含了预期的字符串。           布尔
text_to_be_present_in_element_value 判断指定元素的属性值中是否包含了预期的字符串             布尔
frame_to_be_available_and_switch_to_it   判断该frame是否可以switch进去。                  布尔
invisibility_of_element_located          判断某个元素是否存在于dom或不可见。                布尔
elemen_to_be_clickable                   判断某个元素中是否可见并且是enable的，代表可点击。  布尔
staleness_of                             判断某个元素从dom树中移除。                      布尔
element_to_be_selected                   判断某个元素是否被选中了，一般用在下拉列表。
element_selection_state_to_be            判断某个元素的选中状态是否符合预期。               布尔
element_located_selection_state_to_be    判断某个元素的选中状态是否符合预期。               布尔
"""
from selenium import webdriver 
from time import sleep
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


class TestCase(object):
	def __init__(self):
		self.driver = webdriver.Chrome('/')
		path = 'file:///'+os.path.abspath('test_wait.html')
		self.driver.get(path)
		self.driver.maximize_window()


	def test(self):
		self.driver.find_element_by_id('bth').click()
		#显示等待
		wait = WebDriverWait(self.driver,1)
		wait.util(Ec.text_to_be_present_in_element((By.ID,'id2'),'id 2'))
		print(self.driver.find_element_by_id('id2').text)
		print('ok')


if __name__ == '__main__':
	case = TestCase()
	case.test()



