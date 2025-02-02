from django.test import TestCase 
from django.http import HttpRequest 
from board.views import login_view
from board.models import KanbanUser

# Create your tests here.
class Login_test(TestCase):
    def test_user(self):
        #create test user
        user = KanbanUser.objects.create(username = "testuser" , password = "testpass1234")
        self.assertEqual(user.username,"testuser" )
        self.assertEqual(user.password , "testpass1234")
        self.assertEqual(str(user), "testuser") 

    def test_login_page(self):
        request = HttpRequest()  
        response = login_view(request)  
        html = response.content.decode("utf8")  
        self.assertIn("<title>EduFlow</title>", html)
