from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
class CustomUserTest(TestCase):
    def test_create_user(self):
        User=get_user_model()
        user=User.objects.create_user(
            username='will',
            email='will@will.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@will.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User=get_user_model()
        admin_user=User.objects.create_superuser(
            username='super',
            email='super@super.com',
            password='testpass123'
        )
        self.assertEqual(admin_user.username, 'super')
        self.assertEqual(admin_user.email, 'super@super.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
