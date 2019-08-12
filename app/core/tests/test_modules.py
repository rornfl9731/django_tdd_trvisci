from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """이메일로 새로운 유저 생성 테스트"""
        email = 'test@naver.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """새로운 유저의 이메일 대소문자 테스트"""
        email = "test@NAVER.COM"
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """이메일없는 유저 생성할때 에러발생 테스트"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """슈퍼유저 생성 테스트"""
        user = get_user_model().objects.create_superuser(
            "test@naver.com",
            'rlawlsdn1'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
