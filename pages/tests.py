from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.

class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_place(self): # see if the homepage works correctly and returns HTTP 200 (OK) response
        response = self.client.get("/") # goes to the homepage??
        self.assertEqual(response.status_code, 200) # sees if response code is equal to 200

    def test_url_available_by_name(self): # checks to see if /home works & returns HTTP 200 (OK) response
        response = self.client.get(reverse("home")) # matches generates url based on url name
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  # confirming that the template being used is home.html
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "pages/home.html")

    def test_template_content(self): # checking if correct html is on the page & incorrect is not
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Homepage</h1>")
        self.assertNotContains(response, "Not on the page")

    def test_about_status_code(self): # checking if about page is working correct
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200) # sees if response code is equal to 200
