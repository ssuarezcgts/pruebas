from django.test import TestCase

# Create your tests here.
class HelloViewTestCase(TestCase):

	def test_index_view(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'hello/index.html')
