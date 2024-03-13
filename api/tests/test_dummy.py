from django.test import TestCase
from django.urls import reverse
import json

# Create your tests here.

class GetDummyJsonViewTest(TestCase):
    def test_get_dummy_json_view_with_params(self):
        # Prepare request parameters
        url = reverse('get_dummy_json')
        params = {'name': 'Hello', 'email': 'hello@world.com'}
        response = self.client.get(url, params)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)

        expected_data = {
            "name": "Hello",
            "email": "hello@world.com",
            "other_data": "value",
        }

        self.assertDictEqual(response_data, expected_data)

    def test_get_dummy_json_view_without_params(self):
        url = reverse('get_dummy_json')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)

        expected_data = {
            "name": "",
            "email": "",
            "other_data": "value",
        }

        self.assertDictEqual(response_data, expected_data)
