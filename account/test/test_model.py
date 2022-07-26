from django.test import TestCase
from django.contrib.auth import get_user_model


class UserModelTestCase(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            full_name='test', email='test@gmail.com',
            phone_number='09999999999', beo='hi my name is test',
            password='test123123'
        )

        self.super_user = get_user_model().objects.create_superuser(
            full_name='super test', email='supertest@gmail.com',
            phone_number='01111111111', beo='hi my name is supertest',
            password='supertest123123'
        )

    def test_str_method(self):
        self.assertEqual(str(self.user), 'test@gmail.com')
        self.assertEqual(str(self.super_user), 'supertest@gmail.com')

        self.assertNotEqual(str(self.user), 'supertest@gmail.com')
        self.assertNotEqual(str(self.super_user), 'test@gmail.com')

    def test_user_created(self):
        self.assertTrue(isinstance(self.user, get_user_model()))
        self.assertEqual(self.user.email, 'test@gmail.com')
        self.assertEqual(self.user.phone_number, '09999999999')
        self.assertNotEqual(self.user.phone_number, '01111111111')

    def test_superuser_created(self):
        self.assertTrue(isinstance(self.super_user, get_user_model()))
        self.assertEqual(self.super_user.email, 'supertest@gmail.com')
        self.assertEqual(self.super_user.phone_number, '01111111111')
        self.assertNotEqual(self.super_user.phone_number, '09999999999')


    def test_user_is_active(self):
        self.assertFalse(self.user.is_active)
        self.assertTrue(self.super_user.is_active)

    def test_user_is_verify(self):
        self.assertIsNone(self.user.is_verify)


class UserManagerTestCase(TestCase):
    def test_create_user_without_email(self):
        with self.assertRaises(TypeError):
            user = get_user_model().objects.create_user(
                full_name='test'
            )

    def test_create_superuser_with_change_attribute(self):
        with self.assertRaises(ValueError):
            superuser = get_user_model().objects.create_superuser(
                phone_number="09999999999",
                full_name='test',
                email='test@test.com',
                password='test123123',
                is_staff=False,
            )

        with self.assertRaises(ValueError):
            superuser = get_user_model().objects.create_superuser(
                phone_number="09999999999",
                full_name='test',
                email='test@test.com',
                password='test123123',
                is_superuser=False,
            )
