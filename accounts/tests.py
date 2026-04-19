from django.test import TestCase

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()

class RegisterViewTests(TestCase):
    def test_get_register_page_returns_200(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')


    def test_register_creates_user(self):
        response = self.client.post(reverse('register'), data={
            'username': 'testuser',
            'email': 'test@example.com',
            'display_name': 'Test User',
            'country': 'Bulgaria',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!',
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(UserModel.objects.filter(username='testuser').exists())


    class LoginViewTests(TestCase):
        def setUp(self):
            self.user = UserModel.objects.create_user(
                username='galin',
                email='galin@example.com',
                password='StrongPass123!',
            )


        def test_get_login_page_returns_200(self):
            response = self.client.get(reverse('login'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'accounts/login.html')

        def test_login_with_valid_credentials(self):
            response = self.client.post(reverse('login'), data={
                'username': 'galin',
                'password': 'StrongPass123!',
            })

            self.assertEqual(response.status_code, 302)

        def test_dashboard_requires_login(self):
            response = self.client.get(reverse('dashboard'))
            self.assertEqual(response.status_code, 302)

        def test_logged_user_can_open_dashboard(self):
            self.client.login(username='galin', password='StrongPass123!')
            response = self.client.get(reverse('dashboard'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'accounts/dashboard.html')





