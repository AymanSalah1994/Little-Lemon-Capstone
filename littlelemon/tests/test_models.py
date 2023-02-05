from django.test import TestCase
from restaurant.models import MenuItem


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(
            title="Canjica",
            price=10.33,
            inventory=20
        )
        self.assertEqual(str(item), "Canjica : 10.33")
