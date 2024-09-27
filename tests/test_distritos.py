"""
Unit tests for distritos
"""

import unittest

import requests

from tests.load_env import config


class TestDistritos(unittest.TestCase):
    """Tests for distritos"""

    def test_get_distritos(self):
        """Test GET method for distritos"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/distritos",
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

    def test_get_distritos_by_es_distrito_judicial(self):
        """Test GET method for distritos by es_distrito_judicial"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/distritos",
                headers={"X-Api-Key": config["api_key"]},
                params={"es_distrito_judicial": 1},
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
        for item in contenido["items"]:
            self.assertEqual(item["es_distrito_judicial"], 1)

    def test_get_distritos_by_es_distrito(self):
        """Test GET method for distritos by es_distrito"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/distritos",
                headers={"X-Api-Key": config["api_key"]},
                params={"es_distrito": 1},
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
        for item in contenido["items"]:
            self.assertEqual(item["es_distrito"], 1)

    def test_get_distritos_by_es_jurisdiccional(self):
        """Test GET method for distritos by es_jurisdiccional"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/distritos",
                headers={"X-Api-Key": config["api_key"]},
                params={"es_jurisdiccional": 1},
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
        for item in contenido["items"]:
            self.assertEqual(item["es_jurisdiccional"], 1)

    def test_get_distrito_by_clave(self):
        """Test GET method for distrito by clave"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/distritos/dslt",
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
        self.assertEqual(contenido["clave"], "DSLT")


if __name__ == "__main__":
    unittest.main()
