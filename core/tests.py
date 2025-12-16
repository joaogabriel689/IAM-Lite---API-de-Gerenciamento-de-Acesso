from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from core.models import AcessRequest, AuditLog


class AcessRequestAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="john", password="123")
        self.list_url = "/api/acess-requests/"
        self.detail_url = lambda pk: f"/api/acess-requests/{pk}/"

    def test_create_acess_request(self):
        data = {
            "user_request": self.user.id,
            "source": "website",
            "reason": "test reason",
            "status": "pending",
            "date_request": "2025-12-07",
            "date_approved": None,
            "admin_approved": None
        }

        response = self.client.post(self.list_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AcessRequest.objects.count(), 1)
        self.assertEqual(AcessRequest.objects.first().reason, "test reason")

    def test_list_acess_requests(self):
        AcessRequest.objects.create(
            user_request=self.user,
            source="website",
            reason="example",
            status="pending"
        )

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_acess_request(self):
        request_obj = AcessRequest.objects.create(
            user_request=self.user,
            source="website",
            reason="teste",
            status="pending"
        )

        data = {
            "user_request": self.user.id,
            "source": "website",
            "reason": "updated",
            "status": "approved",
            "date_request": "2025-12-07",
            "date_approved": "2025-12-08",
            "admin_approved": self.user.id
        }

        response = self.client.put(self.detail_url(request_obj.id), data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(AcessRequest.objects.first().reason, "updated")

    def test_delete_acess_request(self):
        request_obj = AcessRequest.objects.create(
            user_request=self.user,
            source="website",
            reason="delete-me",
            status="pending"
        )

        response = self.client.delete(self.detail_url(request_obj.id))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(AcessRequest.objects.count(), 0)


class AuditLogAPITests(APITestCase):

    def setUp(self):
        self.list_url = "/api/audit-logs/"
        self.user = User.objects.create_user(username="admin", password="123")

    def test_list_audit_logs(self):
        AuditLog.objects.create(
            action="create",
            user_action=self.user,
            target="TestObject",
            details="Object created"
        )

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class UserAPITests(APITestCase):

    def setUp(self):
        self.list_url = "/api/users/"
        self.detail_url = lambda pk: f"/api/users/{pk}/"

    def test_create_user(self):
        data = {
            "username": "maria",
            "email": "maria@example.com",
            "first_name": "Maria",
            "last_name": "Silva",
            "is_staff": False,
            "is_active": True
        }

        response = self.client.post(self.list_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().username, "maria")

    def test_list_users(self):
        User.objects.create_user(username="jose", password="123")

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_user(self):
        user = User.objects.create_user(username="carlos", password="123")

        response = self.client.get(self.detail_url(user.id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "carlos")

    def test_update_user(self):
        user = User.objects.create_user(username="ana", password="123")

        data = {
            "username": "ana_updated",
            "email": "ana@example.com",
            "first_name": "Ana",
            "last_name": "Souza",
            "is_staff": False,
            "is_active": True
        }

        response = self.client.put(self.detail_url(user.id), data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get(id=user.id).username, "ana_updated")

    def test_delete_user(self):
        user = User.objects.create_user(username="pedro", password="123")

        response = self.client.delete(self.detail_url(user.id))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)
