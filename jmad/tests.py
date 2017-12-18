from django.test import LiveServerTestCase
from selenium import webdriver

class StudentTestCase(LiveServerTestCase):
	def setup(self):
		self.browser = webdriver.Chrome()
		self.browser - implicitly_wait(2)

	def test_student_find_solos(self):

		'''
		test finding solos
		'''

	#a user action

	# another user action

	# yet another user action