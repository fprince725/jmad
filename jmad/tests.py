from django.test import LiveServerTestCase
from selenium import webdriver

class StudentTestCase(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Chrome()
		self.browser.implicitly_wait(10)
	
	def tearDown(self):
		self.browser.quit()

	def test_student_find_solos(self):
		home_page = self.browser.get(self.live_server_url + '/')
		# home_page = self.browser.get('http://www.facebook.com')
'''
		brand_element = self.browser.find_element_by_css_selector('.navbar-brand')
		self.assertEqual('JMAD', brand_element.text)
		self.fail('Incomplete Test')

	
		test finding solos
		'''

	#a user action

	# another user action

	# yet another user action