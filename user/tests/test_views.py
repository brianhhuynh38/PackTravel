from django.test import TestCase, Client
from django.urls import reverse
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from unittest.mock import patch
import hashlib


class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = "testuser"
        self.password = "testpass"
        self.user = User.objects.create_user(
            username=self.username, password=self.password
        )
    
    @patch("your_app.views.intializeDB")
    def test_index_authenticated_user(self, mock_initialize):
        self.client.force_login(self.user)
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/home.html")
        self.assertEqual(response.context["username"], self.username)

    def test_index_anonymous_user(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/home.html")
        self.assertIsNone(response.context["username"])

    @patch("your_app.views.intializeDB")
    def test_register_new_user(self, mock_initialize):
        response = self.client.post(reverse("register"), {
            "username": "newuser",
            "unityid": "u123456",
            "first_name": "New",
            "last_name": "User",
            "email": "newuser@example.com",
            "password1": "newpassword123",
            "password2": "newpassword123",
            "phone_number": "1234567890"
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("index", args=["newuser"]))
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_register_existing_user(self):
        response = self.client.post(reverse("register"), {
            "username": self.username,
            "unityid": "u123456",
            "first_name": "Existing",
            "last_name": "User",
            "email": "existinguser@example.com",
            "password1": self.password,
            "password2": self.password,
            "phone_number": "0987654321"
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/register.html")

    def test_logout(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("index"))
        self.assertNotIn("_auth_user_id", self.client.session)

    @patch("your_app.views.intializeDB")
    def test_login_valid_credentials(self, mock_initialize):
        response = self.client.post(reverse("login"), {
            "username": self.username,
            "password": self.password
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("index", args=[self.username]))

    def test_login_invalid_credentials(self):
        response = self.client.post(reverse("login"), {
            "username": self.username,
            "password": "wrongpassword"
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/login.html")

    @patch("your_app.views.intializeDB")
    def test_my_rides_not_logged_in(self, mock_initialize):
        response = self.client.get(reverse("my_rides"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("index"))
    
    @patch("your_app.views.intializeDB")
    @patch("your_app.views.ridesDB.find")
    def test_my_rides_logged_in(self, mock_find, mock_initialize):
        self.client.force_login(self.user)
        mock_find.return_value = [{"_id": "ride1", "owner": self.username}]
        response = self.client.get(reverse("my_rides"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/myride.html")
        self.assertEqual(response.context["rides"][0]["id"], "ride1")

    @patch("your_app.views.intializeDB")
    @patch("your_app.views.ridesDB.delete_one")
    def test_delete_ride_owner(self, mock_delete, mock_initialize):
        self.client.force_login(self.user)
        session = self.client.session
        session["username"] = self.username
        session.save()
        response = self.client.get(reverse("delete_ride", args=["ride_id"]))
        mock_delete.assert_called_once_with({"_id": "ride_id"})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("my_rides"))
