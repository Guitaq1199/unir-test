import http.client
import os
import unittest
from urllib.request import urlopen

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_divide_by_zero(self):
        url = f"{BASE_URL}/calc/divide/1/0"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertNotEqual(response.status, http.client.OK, f"Expected error for {url}")
        except Exception as e:
            
            from urllib.error import HTTPError

            if isinstance(e, HTTPError):
                self.assertEqual(e.code, http.client.BAD_REQUEST)
            else:
                raise

    def test_api_sqrt_and_log10(self):
        url = f"{BASE_URL}/calc/sqrt/4"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)

        url = f"{BASE_URL}/calc/log10/100"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
