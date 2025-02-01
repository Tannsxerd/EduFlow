from django.test import TestCase 
from django.http import HttpRequest 
from board.views import login_view

# Create your tests here.
class page_test(TestCase):
    def test_login_page(self):
        request = HttpRequest()  
        response = login_view(request)  
        html = response.content.decode("utf8")  
        self.assertIn("<title>EduFlow</title>", html)
