from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
def get_element(driver,*loc):
	e = driver.find_element(*loc)
	return e

if __name__ == '__main__':
	driver = webdriver.Chrome(executable_path='./chromedriver')
	driver.get('https://www.baidu.com')
	driver.maximize_window()
	sleep(2)
	# get_element(driver,By.ID,'kw').send_keys('selenium')
	# get_element(driver,By.ID,'su').click()

	loc = (By.ID,'kw')
	loc2 = (By.ID,'su')
	get_element(driver,*loc).send_keys('selenium')#此处的*代表这个参数要解包
	get_element(driver,*loc2).click()

	sleep(2)
	driver.quit()