from django.test import TestCase
from .models import Product
from django.contrib.auth import get_user_model
from django.urls import reverse


class ProductModelTest(TestCase):

    def setUp(self):

        self.user = get_user_model().objects.create_user(
                username='testuser',
                email='test@email.com',
                password='secret',
                sex = 'M',
                area_code = 90,
                phone_number = 5313964693,
                )

        self.product = Product.objects.create(product_name='test',
                               product_price=10,
                               currency='TL',
                               product_description='just a test',
                               user=self.user)

    def test_get_absolute_url(self):

        self.assertEqual(self.product.get_absolute_url(), '/Catalog/1/')

    def test_product_content(self):
        simple_product = Product.objects.get(id=1)
        expected_object_name = f'{simple_product.product_name}'
        expected_price = simple_product.product_price
        expected_currency = f'{simple_product.currency}'
        expected_description = f'{simple_product.product_description}'

        self.assertEqual(expected_object_name, 'test')
        self.assertEqual(expected_price, 10)
        self.assertEqual(expected_currency, 'TL')
        self.assertEqual(expected_description, 'just a test')

    def test_product_list(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test')
        self.assertTemplateUsed(response, 'home.html')

    def test_detail_list(self):

        response = self.client.get('/Catalog/1/')
        no_response = self.client.get('/Catalog/10000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'test')
        self.assertTemplateUsed(response, 'product_detail.html')

    def test_create_view(self):

        response = self.client.post(reverse('product_new'), {
            'product_name': 'test2',
            'product_price': 12,
            'currency': 'TL',
            'product_description': '-',
            'user': self.user.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Product.objects.last().product_name, 'test2')
        self.assertEqual(Product.objects.last().product_price, 12)
        self.assertEqual(Product.objects.last().currency, 'TL')
        self.assertEqual(Product.objects.last().product_description, '-')

    def test_update_view(self):

        response = self.client.post(reverse('product_edit', args='1'), {
            'product_name': 'test3',
            'product_price': 15,
            'currency': 'TL',
            'product_description': '-'
        } )

        self.assertEqual(response.status_code, 302)

    def test_delete_view(self):

        response = self.client.post(reverse('product_delete', args='1'))
        self.assertEqual(response.status_code, 302)

class SignupPageTests(TestCase):

    def test_status_code(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_temp(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')
