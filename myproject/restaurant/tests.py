from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from .models import Menu , Product
from .views import home_resto, menus_product, 



# Create your tests here.


class HomeTests(TestCase):
    def setUp(self):
        self.menu = Menu.objects.create(nom='Kamer', description='Chez moi')
        url = reverse('home_resto')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home_resto)

    def test_home_view_contains_link_to_topics_page(self):
        menu_topics_url = reverse('menus_product', kwargs={'pk': self.menu.pk})
        self.assertContains(self.response, 'href="{0}"'.format(menu_topics_url))



class MenuTests(TestCase):
    def setUp(self):
        Menu.objects.create(nom='Kamer', description='Chez moi')

    def test_menu_product_view_success_status_code(self):
        url = reverse('menus_product', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_menus_product_view_not_found_status_code(self):
        url = reverse('menus_product', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_menus_product_url_resolves_menus_product_view(self):
        view = resolve('/menus/1/')
        self.assertEquals(view.func, menus_product)
        
    def test_menus_product_view_contains_link_back_to_homepage(self):
        menus_product_url = reverse('menus_product', kwargs={'pk': 1})
        response = self.client.get(menus_product_url)
        homepage_url = reverse('home_resto')
        homepage_url = reverse('home_resto')
        self.assertContains(response, 'href="{0}"'.format(homepage_url))
