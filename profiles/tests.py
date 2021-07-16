from django.test import TestCase
from django.contrib.auth import get_user_model
from django.conf import settings


User = get_user_model()


class ProfileException(Exception):
    pass


class ProfileTest(TestCase):

    def setUp(self):
        self.admin_user_test = User(username='test', email='test@test.com')
        self.admin_user_test.is_staff = True
        self.admin_user_test.is_superuser = True
        self.admin_user_test.set_password('test')
        self.admin_user_test.save()

    def test_user_name(self):
        self.assertNotEqual(self.admin_user_test.username, 'test0')

    def test_admin_user_exists(self):
        user_exists = User.objects.filter(pk=1).exists()
        if user_exists:
            admin_user = User.objects.get(pk=1)
            self.assertEqual(admin_user.is_staff, True)
        else:
            raise ProfileException('Ne OK')

    def test_login_url(self):
        login_url = '/login/'
        self.assertEqual(settings.LOGIN_URL, login_url)