from django.test import TestCase
from rest_framework.test import APIClient
from .models import Service

class ServiceAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create a test service
        self.test_service = Service.objects.create(
                    title="Web Development",
                    short_description="Building modern web applications",
                    full_description="Full stack web development services",
                    slug="web-development"
                )

    def test_services_list_endpoint(self):
        """Test that GET /api/services/ returns 200 OK"""
        response = self.client.get('/api/services/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_service_detail_existing_slug(self):
        """Test that GET /api/services/<slug>/ returns 200 for existing service"""
        response = self.client.get('/api/services/web-development/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], "Web Development")

    def test_service_detail_nonexistent_slug(self):
        """Test that GET /api/services/<invalid-slug>/ returns 404"""
        response = self.client.get('/api/services/invalid-slug/')
        self.assertEqual(response.status_code, 404)