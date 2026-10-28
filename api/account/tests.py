from django.test import TestCase
from django.conf import settings
from django.db import IntegrityError, transaction

from rest_framework import status
from rest_framework.test import APITestCase

from account.models import User

ACCESS = settings.JWT_COOKIE["ACCESS"]
REFRESH = settings.JWT_COOKIE["REFRESH"]
USERNAME = "maria"
PASSWORD = "S3nh@-Forte!2026"

class UserModelTests(TestCase):
    def test_create_user_hashes_password(self):
        user = User.objects.create_user(username=USERNAME, password=PASSWORD)

        self.assertNotEqual(user.password, PASSWORD)
        self.assertTrue(user.check_password(PASSWORD))

class RegisterTests(APITestCase):
    def test_unique_username(self):
        user = User.objects.create_user(username=USERNAME, password=PASSWORD)

        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                User.objects.create_user(username=USERNAME, password=PASSWORD)

