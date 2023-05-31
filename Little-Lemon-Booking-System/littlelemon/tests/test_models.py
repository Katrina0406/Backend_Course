from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_instance(self):
        menu = Menu.objects.create(
            title='Pizza',
            inventory=10,
            price=14.00
        )
        self.assertEqual(str(menu), "Pizza : 14.0")