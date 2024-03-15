from django.test import TestCase, Client
from django.urls import reverse
from ..models import UserDetails
from rest_framework import status
import json
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken

class UserSignUpViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('user_signup')

    def test_user_signup(self):
        data = {
            'user_name': 'Test User',
            'user_phone': '1234567890',
            'user_email': 'test@example.com',
            'password': 'testpassword',
            'location': 'Test Location'
        }
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class UserSignInViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.signin_url = reverse('user_login')
        hased_pw = make_password('testpassword')
        UserDetails.objects.create(
            user_name='Test User', 
            user_phone='1234567890', 
            user_email='test@example.com', 
            password=hased_pw, 
            location='Test Location'
        )

    def test_user_signin(self):
        data = {
            'user_email': 'test@example.com',
            'password': 'testpassword'
        }
        response = self.client.post(self.signin_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class UserProfileViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserDetails.objects.create(
            user_name='Test User', 
            user_phone='1234567890', 
            user_email='test@example.com', 
            password='testpassword', 
            location='Test Location'
        )

        self.profile_url = reverse('user_profile', kwargs={'user_id': self.user.id})
        self.token = RefreshToken.for_user(self.user)

    def test_user_profile_view(self):
        response = self.client.get(self.profile_url, HTTP_AUTHORIZATION=f'Token {self.token.access_token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class UserEditProfileViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserDetails.objects.create(
            user_name='Test User', 
            user_phone='1234567890', 
            user_email='test@example.com', 
            password='testpassword', 
            location='Test Location'
        )

        self.edit_profile_url = reverse('user_edit_profile', kwargs={'user_id': self.user.id})
        self.token = RefreshToken.for_user(self.user)

    def test_user_edit_profile(self):
        data = {
            'user_name': 'Updated User',
            'user_phone': '9876543210',
            'user_email': 'updated@example.com',
            'password': 'updatedpassword',
            'location': 'Updated Location'
        }

        json_data = json.dumps(data)
        content_type = 'application/json'
        response = self.client.put(
            self.edit_profile_url, 
            data=json_data, 
            content_type=content_type, 
            HTTP_AUTHORIZATION=f'Token {self.token.access_token}'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
