from datetime import datetime
from unittest.mock import patch

from django.test import TestCase


class PingTestCase(TestCase):
    def test_ping(self):
        fecha_esperada = "2024-03-20T12:00:00"
        with patch("myapp.views.datetime") as mock_datetime:
            mock_datetime.now.return_value = datetime.fromisoformat(fecha_esperada)
            response = self.client.get("/ping/")
            self.assertEqual(response.status_code, 200)
            data = response.json()
            self.assertEqual(data["ping"], "pong")
            self.assertIsInstance(data["date"], str)
            self.assertEqual(data["date"], fecha_esperada)