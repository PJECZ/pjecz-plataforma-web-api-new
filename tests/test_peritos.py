"""
Unit tests for peritos
"""

import unittest

import requests

from tests.load_env import config


class TestPeritos(unittest.TestCase):
    """Tests for peritos"""

    def test_get_peritos_datatable(self):
        """Test GET method for peritos datatable"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/peritos/datatable",
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
        self.assertEqual("error" in contenido, True)
        self.assertEqual("start" in contenido, True)
        self.assertEqual("length" in contenido, True)
        self.assertEqual("recordsTotal" in contenido, True)
        self.assertEqual("recordsFiltered" in contenido, True)
        self.assertEqual("data" in contenido, True)

    def test_get_peritos(self):
        """Test GET method for peritos"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/peritos",
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
        self.assertEqual("total" in contenido, True)
        self.assertEqual("limit" in contenido, True)
        self.assertEqual("offset" in contenido, True)
        self.assertEqual("items" in contenido, True)

    def test_get_peritos_by_perito_tipo_id(self):
        """Test GET method for peritos by tipo de perito"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/peritos",
                headers={"X-Api-Key": config["api_key"]},
                params={"perito_tipo_id": 15},
                timeout=config["timeout"],
            )
        except requests.exceptions.ConnectionError as error:
            self.fail(f"Connection error: {error}")
        except requests.exceptions.Timeout as error:
            self.fail(f"Timeout error: {error}")
        self.assertEqual(response.status_code, 200)
        contenido = response.json()
        self.assertEqual(contenido["success"], True)
        self.assertEqual("items" in contenido, True)
        for item in contenido["items"]:
            self.assertEqual(item["perito_tipo_id"], 15)

    def test_get_peritos_by_nombre(self):
        """Test GET method for peritos by nombre"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/peritos",
                headers={"X-Api-Key": config["api_key"]},
                params={"nombre": "JUAN"},
                timeout=config["timeout"],
            )
        except requests.exceptions.ConnectionError as error:
            self.fail(f"Connection error: {error}")
        except requests.exceptions.Timeout as error:
            self.fail(f"Timeout error: {error}")
        self.assertEqual(response.status_code, 200)
        contenido = response.json()
        self.assertEqual(contenido["success"], True)
        self.assertEqual("items" in contenido, True)
        for item in contenido["items"]:
            self.assertIn("JUAN", item["nombre"])

    def test_get_peritos_by_distrito_id(self):
        """Test GET method for peritos by distrito_id"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/peritos",
                headers={"X-Api-Key": config["api_key"]},
                params={"distrito_id": 6},
                timeout=config["timeout"],
            )
        except requests.exceptions.ConnectionError as error:
            self.fail(f"Connection error: {error}")
        except requests.exceptions.Timeout as error:
            self.fail(f"Timeout error: {error}")
        self.assertEqual(response.status_code, 200)
        contenido = response.json()
        self.assertEqual(contenido["success"], True)
        self.assertEqual("items" in contenido, True)
        for item in contenido["items"]:
            self.assertEqual(item["distrito_id"], 6)

    def test_get_peritos_by_distrito_id_by_perito_tipo_id(self):
        """Test GET method for peritos by distrito_id by tipo de perito"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/peritos",
                headers={"X-Api-Key": config["api_key"]},
                params={"distrito_id": 6, "perito_tipo_id": 15},
                timeout=config["timeout"],
            )
        except requests.exceptions.ConnectionError as error:
            self.fail(f"Connection error: {error}")
        except requests.exceptions.Timeout as error:
            self.fail(f"Timeout error: {error}")
        self.assertEqual(response.status_code, 200)
        contenido = response.json()
        self.assertEqual(contenido["success"], True)
        self.assertEqual("items" in contenido, True)
        for item in contenido["items"]:
            self.assertEqual(item["distrito_id"], 6)
            self.assertEqual(item["perito_tipo_id"], 15)

    def test_get_peritos_by_distrito_id_by_nombre(self):
        """Test GET method for peritos by distrito_id by nombre"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/peritos",
                headers={"X-Api-Key": config["api_key"]},
                params={"distrito_id": 6, "nombre": "JUAN"},
                timeout=config["timeout"],
            )
        except requests.exceptions.ConnectionError as error:
            self.fail(f"Connection error: {error}")
        except requests.exceptions.Timeout as error:
            self.fail(f"Timeout error: {error}")
        self.assertEqual(response.status_code, 200)
        contenido = response.json()
        self.assertEqual(contenido["success"], True)
        self.assertEqual("items" in contenido, True)
        for item in contenido["items"]:
            self.assertEqual(item["distrito_id"], 6)
            self.assertIn("JUAN", item["nombre"])

    def test_get_peritos_by_distrito_clave(self):
        """Test GET method for peritos by distrito_clave"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/peritos",
                headers={"X-Api-Key": config["api_key"]},
                params={"distrito_clave": "DTRC"},
                timeout=config["timeout"],
            )
        except requests.exceptions.ConnectionError as error:
            self.fail(f"Connection error: {error}")
        except requests.exceptions.Timeout as error:
            self.fail(f"Timeout error: {error}")
        self.assertEqual(response.status_code, 200)
        contenido = response.json()
        self.assertEqual(contenido["success"], True)
        self.assertEqual("items" in contenido, True)
        for item in contenido["items"]:
            self.assertEqual(item["distrito_clave"], "DTRC")

    def test_get_peritos_by_distrito_clave_by_perito_tipo_id(self):
        """Test GET method for peritos by distrito_clave by tipo de perito"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/peritos",
                headers={"X-Api-Key": config["api_key"]},
                params={"distrito_clave": "DTRC", "perito_tipo_id": 15},
                timeout=config["timeout"],
            )
        except requests.exceptions.ConnectionError as error:
            self.fail(f"Connection error: {error}")
        except requests.exceptions.Timeout as error:
            self.fail(f"Timeout error: {error}")
        self.assertEqual(response.status_code, 200)
        contenido = response.json()
        self.assertEqual(contenido["success"], True)
        self.assertEqual("items" in contenido, True)
        for item in contenido["items"]:
            self.assertEqual(item["distrito_clave"], "DTRC")
            self.assertEqual(item["perito_tipo_id"], 15)

    def test_get_peritos_by_distrito_clave_by_nombre(self):
        """Test GET method for peritos by distrito_clave by nombre"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/peritos",
                headers={"X-Api-Key": config["api_key"]},
                params={"distrito_clave": "DTRC", "nombre": "JUAN"},
                timeout=config["timeout"],
            )
        except requests.exceptions.ConnectionError as error:
            self.fail(f"Connection error: {error}")
        except requests.exceptions.Timeout as error:
            self.fail(f"Timeout error: {error}")
        self.assertEqual(response.status_code, 200)
        contenido = response.json()
        self.assertEqual(contenido["success"], True)
        self.assertEqual("items" in contenido, True)
        for item in contenido["items"]:
            self.assertEqual(item["distrito_clave"], "DTRC")
            self.assertIn("JUAN", item["nombre"])

    def test_get_perito_by_id(self):
        """Test GET method for peritos by id"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/peritos/1",
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
        self.assertEqual(contenido["id"], 1)


if __name__ == "__main__":
    unittest.main()
