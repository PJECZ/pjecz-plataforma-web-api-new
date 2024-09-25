"""
Unit tests for repsvm
"""

import unittest

import requests

from tests.load_env import config


class TestREPSVM(unittest.TestCase):
    """Tests for repsvm"""

    def test_get_repsvm_agresores_datatable(self):
        """Test GET method for repsvm_agresores datatable"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/repsvm_agresores/datatable",
                headers={"X-Api-Key": config["api_key"]},
                timeout=config["timeout"],
            )
        except requests.exceptions.ConnectionError as error:
            self.fail(error)
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

    def test_get_repsvm_agresores(self):
        """Test GET method for repsvm_agresores"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/repsvm_agresores/paginado",
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
        self.assertEqual("total" in contenido, True)
        self.assertEqual("limit" in contenido, True)
        self.assertEqual("offset" in contenido, True)
        self.assertEqual("items" in contenido, True)

    def test_get_repsvm_agresores_by_distrito_id_6(self):
        """Test GET method for repsvm_agresores by distrito_id 6"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/repsvm_agresores/paginado",
                headers={"X-Api-Key": config["api_key"]},
                params={"distrito_id": 6},
                timeout=config["timeout"],
            )
        except requests.exceptions.ConnectionError as error:
            self.fail(error)
        self.assertEqual(response.status_code, 200)
        contenido = response.json()
        self.assertEqual(contenido["success"], True)
        self.assertEqual("items" in contenido, True)
        for item in contenido["items"]:
            self.assertEqual(item["distrito_id"], 6)

    def test_get_repsvm_agresores_by_distrito_id_6_by_nombre(self):
        """Test GET method for repsvm_agresores by distrito_id 6 by nombre PEDRO"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/repsvm_agresores/paginado",
                headers={"X-Api-Key": config["api_key"]},
                params={"distrito_id": 6, "nombre": "PEDRO"},
                timeout=config["timeout"],
            )
        except requests.exceptions.ConnectionError as error:
            self.fail(error)
        self.assertEqual(response.status_code, 200)
        contenido = response.json()
        self.assertEqual(contenido["success"], True)
        self.assertEqual("items" in contenido, True)
        for item in contenido["items"]:
            self.assertEqual(item["distrito_id"], 6)
            self.assertIn("PEDRO", item["nombre"])

    def test_get_repsvm_agresores_by_distrito_clave_dtrc(self):
        """Test GET method for repsvm_agresores by distrito_clave DTRC"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/repsvm_agresores/paginado",
                headers={"X-Api-Key": config["api_key"]},
                params={"distrito_clave": "DTRC"},
                timeout=config["timeout"],
            )
        except requests.exceptions.ConnectionError as error:
            self.fail(error)
        self.assertEqual(response.status_code, 200)
        contenido = response.json()
        self.assertEqual(contenido["success"], True)
        self.assertEqual("items" in contenido, True)
        for item in contenido["items"]:
            self.assertEqual(item["distrito_clave"], "DTRC")

    def test_get_repsvm_agresores_by_distrito_clave_dtrc_by_nombre(self):
        """Test GET method for repsvm_agresores by distrito_clave DTRC by nombre PEDRO"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/repsvm_agresores/paginado",
                headers={"X-Api-Key": config["api_key"]},
                params={"distrito_clave": "DTRC", "nombre": "PEDRO"},
                timeout=config["timeout"],
            )
        except requests.exceptions.ConnectionError as error:
            self.fail(error)
        self.assertEqual(response.status_code, 200)
        contenido = response.json()
        self.assertEqual(contenido["success"], True)
        self.assertEqual("items" in contenido, True)
        for item in contenido["items"]:
            self.assertEqual(item["distrito_clave"], "DTRC")
            self.assertIn("PEDRO", item["nombre"])

    def test_get_repsvm_agresores_by_id(self):
        """Test GET method for repsvm_agresores by id"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/repsvm_agresores/777",
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
        self.assertEqual(contenido["id"], 777)


if __name__ == "__main__":
    unittest.main()
