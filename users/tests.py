from django.test import TestCase
from .models import User

# Create your tests here.


class UserDemoTests(TestCase):
    def test_demo(self):
        new = User(username="new")
        self.assertIs(new.gender, 0)
