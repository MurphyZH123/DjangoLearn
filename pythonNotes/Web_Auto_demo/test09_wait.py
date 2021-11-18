"""
time.sleep(固定等待)
在开发自动化框架的过程中，最忌讳使用python自带模块的time的sleep方式进行等待，虽然可以自定义等待时间
但当网路条件良好的时候，依旧按照预设定的时间继续等待梦到值整个项目的自动化时间无限延长，不建议使用。
(注意：脚本调试过程时，还是可以使用的，方便快捷)



implicitly_wait(隐式等待)
隐式等待实际是设置了一个最长等待时间，如果在规定时间内网页加载完成，则执行下一步，否则一致等到时间结束，然后执行下一步
这样的隐式等待会有个坑，我们都知道javascript一般都是放在我们的body的最后进行加载，实际这是页面上的元素都已经加载完毕，
我们却还在等待全部页面加载结束
隐式等待对整个driver周期都起作用，在最开始设置一次就可以了，不要当做固定等待使用，到哪都来一个隐式等待



WebDriverWait(显示等待)
WebDriverWait是selenium提供得到显示等待模块引入路径：
from selenium.webdriver.support.wait import WebDriverWait

WebDriverWait参数：
(1) driver    传入WebDriver实例(必传参数)
(2) timeout   超时时间，等待的最长时间（必传参数）
(3) poll_frequency  调用until_not中的方法的间隔时间，默认是0.5秒
(4) ignored——exceptions  忽略的异常

	这个模块中，一共有两种方法until与until_not
	(1)method 在等待期间，每隔一段时间调用这个传入的方法，直到返回值不是Flase
	(2)message 如果超时，抛出TimeoutException，将message传入异常

"""




from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCase(object):
	def __init__(self):
		self.driver = webdriver.Chrome('./')
		self.driver.get('http://www.baidu.com')


	#固定等待
	def test_sleep(self):
		self.driver.find_element_by_id('kw').send_keys('selenium')
		sleep(2)#线程阻塞，blocking wait
		self.driver.find_element_by_id('su').click()
		sleep(3)
		self.driver.quit()


	#隐式等待
	def test_implictly(self):
		self.driver.implicitly_wait(10)
		self.driver.find_element_by_id('kw').send_keys('selenium')
		self.driver.find_element_by_id('su').click()
		self.driver.quit()



	#显示等待
	def test_wait(self):
		wait = WebDriverWait(self.driver,2)#其中的2为超时时间timeout，默认参数poll_frequency为0.5
		wait.util(EC.title_is('百度一下，你就知道'))#util方法,2秒钟还是未显示，就会抛出异常。若是两秒钟出现需要的元素，就会进行下面的代码
		self.driver.find_element_by_id('kw').send_keys('selenium')
		#sleep(2)
		self.driver.find_element_by_id('su').click()
		sleep(3)
		self.driver.quit()



if __name__=='__main__':
	case = TestCase()
	# case.test_sleep()
	case.test_sleep()
























