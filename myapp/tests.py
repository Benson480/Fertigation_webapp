from django.test import Client, TestCase
from .models import Fertilizer

# Create your tests here.

class DashboardViewTest(TestCase):
    def test_dashboard_view_when_not_authenticated(self):
        # Create a test client
        client = Client()

        # Log out the user (simulate an authenticated user being logged out)
        client.logout()

        # Make a GET request to the dashboard view
        response = client.get('/dashboard/')

        # Assert that the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # Assert that the response redirected to the expected URL (login page)
        self.assertRedirects(response, '/login/?next=/dashboard/', target_status_code=200)

    def test_dashboard_view_when_authenticated(self):
        # Create a test client
        client = Client()

        # Authenticate a user (simulate a logged-in user)
        user = Fertilizer.objects.create_user(username='testuser', password='testpassword')
        client.force_login(user)

        # Make a GET request to the dashboard view
        response = client.get('/dashboard/')

        # Assert that the response status code is 200 (success)
        self.assertEqual(response.status_code, 200)

        # Add more assertions specific to the behavior of the dashboard view when authenticated
        # For example, you might want to check the content of the response or other view-specific behavior.