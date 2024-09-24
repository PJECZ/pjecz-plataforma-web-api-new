"""
Unit tests for peritos tipos
"""

import unittest

import requests

from tests.load_env import config


class TestPeritosTipos(unittest.TestCase):
    """Tests for peritos tipos"""

    def test_get_peritos_tipos(self):
        """Test GET method for peritos tipos"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/peritos_tipos",
                headers={"X-Api-Key": config["api_key"]},
                timeout=config["timeout"],
            )
        except requests.exceptions.ConnectionError as error:
            self.fail(error)
        self.assertEqual(response.status_code, 200)
        contenido = response.json()
        self.assertEqual("success" in contenido, True)
        self.assertEqual(contenido["success"], True)
        self.assertEqual("message" in contenido, True)
        self.assertEqual("items" in contenido, True)

    def test_get_perito_tipo_by_id(self):
        """Test GET method for peritos tipos by id"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/peritos_tipos/1",
                headers={"X-Api-Key": config["api_key"]},
                timeout=config["timeout"],
            )
        except requests.exceptions.ConnectionError as error:
            self.fail(error)
        self.assertEqual(response.status_code, 200)
        contenido = response.json()
        self.assertEqual("success" in contenido, True)
        self.assertEqual(contenido["success"], True)
        self.assertEqual(contenido["id"], 1)


if __name__ == "__main__":
    unittest.main()
