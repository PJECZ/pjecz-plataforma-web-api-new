"""
Unit tests for epocas
"""

import unittest

import requests

from tests.load_env import config


class TestEpocas(unittest.TestCase):
    """Tests for epocas"""

    def test_get_epocas(self):
        """Test GET method for epocas"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/epocas",
                headers={"X-Api-Key": config["api_key"]},
                timeout=config["timeout"],
            )
        except requests.exceptions.ConnectionError as error:
            self.fail(f"Connection error: {error}")
        except requests.exceptions.Timeout as error:
            self.fail(f"Timeout error: {error}")
        self.assertEqual(response.status_code, 200)
        contenido = response.json()
        self.assertEqual("success" in contenido, True)
        self.assertEqual(contenido["success"], True)
        self.assertEqual("message" in contenido, True)
        self.assertEqual("items" in contenido, True)

    def test_get_epoca_by_id(self):
        """Test GET method for epoca by id"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/epocas/1",
                headers={"X-Api-Key": config["api_key"]},
                timeout=config["timeout"],
            )
        except requests.exceptions.ConnectionError as error:
            self.fail(f"Connection error: {error}")
        except requests.exceptions.Timeout as error:
            self.fail(f"Timeout error: {error}")
        self.assertEqual(response.status_code, 200)
        contenido = response.json()
        self.assertEqual("success" in contenido, True)
        self.assertEqual(contenido["success"], True)
        self.assertEqual(contenido["id"], 1)

    def test_get_epoca_by_id_success_false(self):
        """Test GET method for epoca by id success false"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/epocas/999",
                headers={"X-Api-Key": config["api_key"]},
                timeout=config["timeout"],
            )
        except requests.exceptions.ConnectionError as error:
            self.fail(f"Connection error: {error}")
        except requests.exceptions.Timeout as error:
            self.fail(f"Timeout error: {error}")
        self.assertEqual(response.status_code, 200)
        contenido = response.json()
        self.assertEqual("success" in contenido, True)
        self.assertEqual(contenido["success"], False)


if __name__ == "__main__":
    unittest.main()
