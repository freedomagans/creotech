from django.test import TestCase
from rest_framework.test import APIClient
from .models import Inquiry

class InquiriesAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.valid_inquiry_data = {
            "name": "Test User",
            "email": "test@example.com",
            "subject": "Test Inquiry",
            "message": "This is a test message",
            "inquiry_type": "contact"
        }

    def test_create_inquiry_valid_data(self):
        """Test that POST /api/inquiries/ with valid data returns 201 and creates a record"""
        initial_count = Inquiry.objects.count()
        response = self.client.post(
            '/api/inquiries/',
            self.valid_inquiry_data,
            format='json'
        )
        # Verify response status is 201 Created
        self.assertEqual(response.status_code, 201)
        # Verify a new record was created in the database
        self.assertEqual(Inquiry.objects.count(), initial_count + 1)
        # Verify the created record has the correct data
        new_inquiry = Inquiry.objects.latest('id')
        self.assertEqual(new_inquiry.name, "Test User")
        self.assertEqual(new_inquiry.email, "test@example.com")

    def test_create_inquiry_missing_email(self):
        """Test that POST missing required email field returns 400 Bad Request"""
        invalid_data = self.valid_inquiry_data.copy()
        del invalid_data['email']  # Remove required field
        response = self.client.post(
            '/api/inquiries/',
            invalid_data,
            format='json'
        )
        # Verify response status is 400 Bad Request
        self.assertEqual(response.status_code, 400)
        # Verify email error is in the response
        self.assertIn('email', response.data)
        # Verify no new record was created
        self.assertEqual(Inquiry.objects.count(), 0)