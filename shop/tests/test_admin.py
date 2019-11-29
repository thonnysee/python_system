from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='test@test.com',
            password='test123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='another@test.com',
            password='password123',
            firstname='Testing first name'
        )

    def test_users_listed(self):
        """Test that users are listed on user page of admin"""
        url = reverse('admin:shop_user_changelist')
        response = self.client.get(url)

        self.assertContains(response, self.user.firstname)
        self.assertContains(response, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:shop_user_change', args=[self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:shop_user_add')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
