from django.test import TestCase
from django.core.urlresolvers import resolve
from solos.views import index


class SolosURLsTestCase(TestCase):
	def test_root_url_uses_index_view(self):
		root = resolve('/')
		self.assertEqual(root.func,index)
