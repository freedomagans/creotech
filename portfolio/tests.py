from django.test import TestCase
from rest_framework.test import APIClient
from .models import Project, ProjectImage

class PortfolioAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create test project
        self.test_project = Project.objects.create(
            title="E-Commerce Platform",
            short_description="A modern e-commerce solution",
            full_description="Full-featured online store with payment integration",
            category="Web Development",
            slug="ecommerce-platform"
        )
        # Create test image for the project
        self.test_image = ProjectImage.objects.create(
            project=self.test_project,
            image="test_image.jpg"
        )

    def test_portfolio_list_endpoint(self):
        """Test that GET /api/portfolio/ returns 200 OK"""
        response = self.client.get('/api/portfolio/')
        self.assertEqual(response.status_code, 200)
        # Verify at least one project is returned
        self.assertGreater(len(response.data), 0)

    def test_portfolio_detail_existing_slug(self):
        """Test that GET /api/portfolio/<slug>/ returns 200 for existing project"""
        response = self.client.get('/api/portfolio/ecommerce-platform/')
        self.assertEqual(response.status_code, 200)

    def test_portfolio_detail_nonexistent_slug(self):
        """Test that GET /api/portfolio/<invalid-slug>/ returns 404"""
        response = self.client.get('/api/portfolio/nonexistent-project/')
        self.assertEqual(response.status_code, 404)

    def test_gallery_images_is_list_in_response(self):
        """Test that gallery_images appears as a list in the detail response"""
        response = self.client.get('/api/portfolio/ecommerce-platform/')
        self.assertEqual(response.status_code, 200)
        # Verify gallery_images exists and is a list
        self.assertIn('gallery_images', response.data)
        self.assertIsInstance(response.data['gallery_images'], list)
        # Verify the test image is in the list
        self.assertGreater(len(response.data['gallery_images']), 0)