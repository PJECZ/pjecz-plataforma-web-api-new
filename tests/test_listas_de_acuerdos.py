"""
Unit tests for listas de acuerdos
"""

import unittest

import requests

from tests.load_env import config


class TestListasDeAcuerdos(unittest.TestCase):
    """Tests for listas de acuerdos"""

    def test_get_listas_de_acuerdos_datatable(self):
        """Test GET method for listas de acuerdos datatable"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/listas_de_acuerdos/datatable",
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

    def test_get_listas_de_acuerdos(self):
        """Test GET method for listas de acuerdos"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/listas_de_acuerdos",
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

    def test_get_listas_de_acuerdos_by_autoridad_id(self):
        """Test GET method for listas_de_acuerdos by autoridad_id"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/listas_de_acuerdos",
                headers={"X-Api-Key": config["api_key"]},
                params={"autoridad_id": 37},
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
            self.assertEqual(item["autoridad_id"], 37)

    def test_get_listas_de_acuerdos_by_autoridad_id_by_fechas(self):
        """Test GET method for listas_de_acuerdos by autoridad_id fecha_desde and fecha_hasta"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/listas_de_acuerdos",
                headers={"X-Api-Key": config["api_key"]},
                params={
                    "autoridad_id": 37,
                    "fecha_desde": "2020-01-01",
                    "fecha_hasta": "2020-01-31",
                },
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
            self.assertEqual(item["autoridad_id"], 37)
            self.assertGreaterEqual(item["fecha"], "2020-01-01")
            self.assertLessEqual(item["fecha"], "2020-01-31")

    def test_get_listas_de_acuerdos_by_autoridad_clave(self):
        """Test GET method for listas_de_acuerdos by autoridad_clave"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/listas_de_acuerdos",
                headers={"X-Api-Key": config["api_key"]},
                params={"autoridad_clave": "SLT-J2-CIV"},
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
            self.assertEqual(item["autoridad_clave"], "SLT-J2-CIV")

    def test_get_listas_de_acuerdos_by_autoridad_clave_by_fechas(self):
        """Test GET method for listas_de_acuerdos by autoridad_clave fecha_desde and fecha_hasta"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/listas_de_acuerdos",
                headers={"X-Api-Key": config["api_key"]},
                params={
                    "autoridad_clave": "SLT-J2-CIV",
                    "fecha_desde": "2020-01-01",
                    "fecha_hasta": "2020-01-31",
                },
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
            self.assertEqual(item["autoridad_clave"], "SLT-J2-CIV")
            self.assertGreaterEqual(item["fecha"], "2020-01-01")
            self.assertLessEqual(item["fecha"], "2020-01-31")

    def test_get_lista_de_acuerdos_by_id(self):
        """Test GET method for listas_de_acuerdos by id"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/listas_de_acuerdos/1",
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
