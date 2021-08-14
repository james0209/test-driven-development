from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest, HttpResponse
from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve("/")
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        # Create an  HttpRequest object, which Django will see when a user's browser asks for a page
        request = HttpRequest()

        # Pass to home_page view, which gives us a response
        response = HttpResponse()
        response = home_page(request)

        # Extract .content (raw bytes) of the response. Decode to HTML string
        html = response.content.decode("utf8")

        self.assertTrue(html.startswith("<html>"))
        self.assertIn("<title>To-Do lists</title>", html)
        self.assertTrue(html.endswith("</html>"))
