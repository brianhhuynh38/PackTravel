from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch
from bson import ObjectId
import hashlib
from user.views import userDB, ridesDB
from utils import get_client

client = None
db = None
userDB = None
ridesDB = None
routesDB = None

class UserViewTests(TestCase):
    
    def setUp(self):
        self.client = Client()

    @patch('user.views.userDB')
    def test_register_user(self, mock_userDB):
        form_data = {
            "username": "testuser",
            "unityid": "u123456",
            "first_name": "Test",
            "last_name": "User",
            "email": "testuser@example.com",
            "password1": "password123",
            "phone_number": "1234567890"
        }
        mock_userDB.find_one.return_value = None  # No existing user
        response = self.client.post(reverse('register'), data=form_data)
        self.assertEqual(response.status_code, 302)  # Redirect after success

    @patch('user.views.userDB')
    def test_login_user(self, mock_userDB):
        login_data = {
            "username": "testuser",
            "password": "password123"
        }
        hashed_password = hashlib.sha256(login_data["password"].encode()).hexdigest()
        mock_userDB.find_one.return_value = {
            "username": "testuser",
            "password": hashed_password,
            "unityid": "u123456",
            "fname": "Test",
            "lname": "User",
            "email": "testuser@example.com",
            "phone": "1234567890"
        }
        response = self.client.post(reverse('login'), data=login_data)
        #self.assertEqual(response.status_code, 200)  # Redirecting to login after login gives 200

    def test_logout_user(self):
        session = self.client.session
        session["username"] = "testuser"
        session.save()
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertNotIn("username", self.client.session)

    @patch('user.views.ridesDB')
    def test_my_rides(self, mock_ridesDB):
        session = self.client.session
        session["username"] = "testuser"
        session.save()
        mock_ridesDB.find.return_value = [{"_id": ObjectId(), "owner": "testuser", "destination": "City B"}]
        response = self.client.get(reverse('my_rides'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "testuser")

    @patch('user.views.ridesDB')
    @patch('user.views.userDB')
    def test_delete_ride(self, mock_userDB, mock_ridesDB):
        session = self.client.session
        session["username"] = "testuser"
        session.save()
        mock_userDB.find_one.return_value = {"username": "testuser"}
        mock_ridesDB.find_one.return_value = {"_id": ObjectId(), "owner": "testuser"}
        response = self.client.post(reverse('delete_ride', args=[str(ObjectId())]))
        self.assertEqual(response.status_code, 302)

    @patch('user.views.ridesDB')
    def test_requested_rides(self, mock_ridesDB):
        session = self.client.session
        session["username"] = "testuser"
        session.save()
        mock_ridesDB.aggregate.return_value = [
            {"_id": ObjectId(), "found_in_requested": True, "requested_users": ["testuser"]},
            {"_id": ObjectId(), "found_in_confirmed": True, "confirmed_users": ["testuser"]}
        ]
        response = self.client.get(reverse('requested_rides'))
        self.assertEqual(response.status_code, 200)
     
   
    def tearDown(self):
        # Delete all test users created during the test
        global client, db, userDB, ridesDB, routesDB
        if client is None:  # Initialize the client only if it's not already initialized
            client = get_client()
            db = client.SEProject  # Connect to your main database
        
        if db is not None:
            userDB = db.userData  # Ensure each collection is properly initialized
            ridesDB = db.rides
            routesDB = db.routes
        else:
            raise ConnectionError("Database connection could not be established.")
        userDB.delete_one({"username": "testuser"})
        # Clear any test rides
        #ridesDB.delete_many({"test_ride": True})
