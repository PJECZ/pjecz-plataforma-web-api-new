"""
Unit tests for audiencias
"""

import unittest

import requests

from tests.load_env import config


class TestAudiencias(unittest.TestCase):
    """Tests for audiencias"""

    def test_get_audiencias_datatable(self):
        """Test GET method for audiencias datatable"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/audiencias/datatable",
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

    def test_get_audiencias(self):
        """Test GET method for audiencias"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/audiencias",
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

    def test_get_audiencias_by_autoridad_id(self):
        """Test GET method for audiencias by autoridad_id"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/audiencias",
                headers={"X-Api-Key": config["api_key"]},
                params={"autoridad_id": 35},
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
            self.assertEqual(item["autoridad_id"], 35)

    def test_get_audiencias_by_autoridad_id_by_fecha(self):
        """Test GET method for audiencias by autoridad_id by fecha"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/audiencias",
                headers={"X-Api-Key": config["api_key"]},
                params={"autoridad_id": 35, "fecha": "2023-05-11"},
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
            self.assertEqual(item["autoridad_id"], 35)
            self.assertEqual(item["tiempo"].split("T")[0], "2023-05-11")

    def test_get_audiencias_by_autoridad_clave(self):
        """Test GET method for audiencias by autoridad_clave"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/audiencias",
                headers={"X-Api-Key": config["api_key"]},
                params={"autoridad_clave": "SLT-J1-FAM"},
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
            self.assertEqual(item["autoridad_id"], 35)

    def test_get_audiencias_by_autoridad_clave_by_fecha(self):
        """Test GET method for audiencias by autoridad_clave by fecha"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/audiencias",
                headers={"X-Api-Key": config["api_key"]},
                params={"autoridad_clave": "SLT-J1-FAM", "fecha": "2023-05-11"},
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
            self.assertEqual(item["autoridad_id"], 35)
            self.assertEqual(item["tiempo"].split("T")[0], "2023-05-11")

    def test_get_audiencia_by_id(self):
        """Test GET method for audiencia by id"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/audiencias/1",
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
