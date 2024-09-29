"""
Unit tests for sentencias
"""

import unittest

import requests

from tests.load_env import config


class TestSentencias(unittest.TestCase):
    """Tests for sentencias"""

    def test_get_sentencias_datatable(self):
        """Test GET method for sentencias"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/sentencias/datatable",
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

    def test_get_sentencias(self):
        """Test GET method for sentencias"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/sentencias",
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

    def test_get_sentencias_by_autoridad_id(self):
        """Test GET method for sentencias by autoridad_id"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/sentencias",
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

    def test_get_sentencias_by_autoridad_id_by_expediente(self):
        """Test GET method for sentencias by autoridad_id 37 by expediente 197/2019"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/sentencias",
                headers={"X-Api-Key": config["api_key"]},
                params={"autoridad_id": 37, "expediente": "197/2019"},
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
            self.assertEqual(item["expediente"], "197/2019")

    def test_get_sentencias_by_autoridad_id_by_sentencia(self):
        """Test GET method for sentencias by autoridad_id by sentencia"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/sentencias",
                headers={"X-Api-Key": config["api_key"]},
                params={"autoridad_id": 37, "sentencia": "160/2021"},
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
            self.assertEqual(item["sentencia"], "160/2021")

    def test_get_sentencias_by_autoridad_clave(self):
        """Test GET method for sentencias by autoridad_clave"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/sentencias",
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

    def test_get_sentencias_by_autoridad_clave_by_expediente(self):
        """Test GET method for sentencias by autoridad_clave SLT-J2-CIV by expediente 197/2019"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/sentencias",
                headers={"X-Api-Key": config["api_key"]},
                params={"autoridad_clave": "SLT-J2-CIV", "expediente": "197/2019"},
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
            self.assertEqual(item["expediente"], "197/2019")

    def test_get_sentencias_by_autoridad_clave_by_sentencia(self):
        """Test GET method for sentencias by autoridad_clave SLT-J2-CIV by sentencia 160/2021"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/sentencias",
                headers={"X-Api-Key": config["api_key"]},
                params={"autoridad_clave": "SLT-J2-CIV", "sentencia": "160/2021"},
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
            self.assertEqual(item["sentencia"], "160/2021")

    def test_get_sentencia_by_id(self):
        """Test GET method for sentencias by id"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/sentencias/1",
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
