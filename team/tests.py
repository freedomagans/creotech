from django.test import TestCase
from rest_framework.test import APIClient
from .models import TeamMember

class TeamAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create active team member (should appear in list)
        self.active_member = TeamMember.objects.create(
            name="John Doe",
            role="Lead Developer",
            bio="Full stack developer with 10+ years experience",
            is_active=True,
            slug="john-doe"
        )
        # Create inactive team member (should NOT appear in list)
        self.inactive_member = TeamMember.objects.create(
            name="Jane Smith",
            role="Designer",
            bio="UI/UX designer",
            is_active=False,
            slug="jane-smith"
        )

    def test_team_list_endpoint(self):
        """Test that GET /api/team/ returns 200 OK"""
        response = self.client.get('/api/team/')
        self.assertEqual(response.status_code, 200)

    def test_team_detail_existing_slug(self):
        """Test that GET /api/team/<slug>/ returns 200 for existing active member"""
        response = self.client.get('/api/team/john-doe/')
        self.assertEqual(response.status_code, 200)

    def test_team_detail_nonexistent_slug(self):
        """Test that GET /api/team/<invalid-slug>/ returns 404"""
        response = self.client.get('/api/team/nonexistent-member/')
        self.assertEqual(response.status_code, 404)

    def test_inactive_member_not_in_list(self):
        """Test that is_active=False members do NOT appear in the list response"""
        response = self.client.get('/api/team/')
        self.assertEqual(response.status_code, 200)
        # Extract all member slugs from the response
        member_slugs = [item['slug'] for item in response.data]
        # Active member should be present
        self.assertIn('john-doe', member_slugs)
        # Inactive member should NOT be present
        self.assertNotIn('jane-smith', member_slugs)
        # List should only contain the active member
        self.assertEqual(len(response.data), 1)