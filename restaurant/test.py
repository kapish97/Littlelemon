from django.test import TestCase
from restaurant.models import Menu


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title='test',Price=90,Inventory=123)
        self.assertEqual(item.Title,"test")
        self.assertEqual(item.Price,90)
        self.assertEqual(item.Inventory,123)


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(Title="menu1",Price=1,Inventory=23)
        Menu.objects.create(Title='menu2',Price=2,Inventory=342)

    def test_getall(self):
        menu1 = Menu.objects.get(Title ="menu1")
        menu2  = Menu.objects.get(Title="menu2")
        self.assertEqual(menu1.Title,"menu1")
        self.assertEqual(menu2.Title,"menu2")
