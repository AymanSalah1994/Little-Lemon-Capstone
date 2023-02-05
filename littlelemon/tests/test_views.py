from django.test import TestCase, RequestFactory
from restaurant.models import MenuItem
from restaurant.views import MenuItemsView
from restaurant.serializers import MenuItemSerializer

test_items = [
    {
        'title' : 'Canjica',
        'price' : 10.33,
        'inventory' : 20,
    },
]

class MenuViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        for item in test_items:
            MenuItem.objects.create(
                title=item.title,
                price=item.price,
                inventory=item.inventory
            )

    def test_getall(self):
        menuitems = MenuItem.objects.all()
        serialized_menuitems = MenuItemSerializer(menuitems, many=True)
        request = self.factory.get('restaurant/menu/')
        response = MenuItemsView.as_view()(request)

        self.assertEqual(response.data, serialized_menuitems.data)
