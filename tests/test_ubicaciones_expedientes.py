"""
Unit tests for ubicaciones de expedientes
"""

import unittest

import requests

from tests.load_env import config


class TestUbicacionesExpedientes(unittest.TestCase):
    """Tests for ubicaciones de expedientes"""

    def test_get_ubicaciones_expedientes_datatable(self):
        """Test GET method for ubicaciones_expedientes datatable"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/ubicaciones_expedientes/datatable",
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

    def test_get_ubicaciones_expedientes(self):
        """Test GET method for ubicaciones_expedientes"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/ubicaciones_expedientes/paginado",
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

    def test_get_ubicaciones_expedientes_by_autoridad_id_37(self):
        """Test GET method for ubicaciones_expedientes by autoridad_id 37"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/ubicaciones_expedientes/paginado",
                headers={"X-Api-Key": config["api_key"]},
                params={"autoridad_id": 37},
                timeout=config["timeout"],
            )
        except requests.exceptions.ConnectionError as error:
            self.fail(error)
        self.assertEqual(response.status_code, 200)
        contenido = response.json()
        self.assertEqual(contenido["success"], True)
        self.assertEqual("items" in contenido, True)
        for item in contenido["items"]:
            self.assertEqual(item["autoridad_id"], 37)

    def test_get_ubicaciones_expedientes_by_autoridad_id_37_and_expediente(self):
        """Test GET method for ubicaciones_expedientes by autoridad_id 37 and expediente 140/2023"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/ubicaciones_expedientes/paginado",
                headers={"X-Api-Key": config["api_key"]},
                params={"autoridad_id": 37, "expediente": "140/2023"},
                timeout=config["timeout"],
            )
        except requests.exceptions.ConnectionError as error:
            self.fail(error)
        self.assertEqual(response.status_code, 200)
        contenido = response.json()
        self.assertEqual(contenido["success"], True)
        self.assertEqual("items" in contenido, True)
        for item in contenido["items"]:
            self.assertEqual(item["autoridad_id"], 37)

    def test_get_ubicaciones_expedientes_by_autoridad_clave_stl_j2_civ(self):
        """Test GET method for ubicaciones_expedientes by autoridad_clave SLT-J2-CIV"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/ubicaciones_expedientes/paginado",
                headers={"X-Api-Key": config["api_key"]},
                params={"autoridad_clave": "SLT-J2-CIV"},
                timeout=config["timeout"],
            )
        except requests.exceptions.ConnectionError as error:
            self.fail(error)
        self.assertEqual(response.status_code, 200)
        contenido = response.json()
        self.assertEqual(contenido["success"], True)
        self.assertEqual("items" in contenido, True)
        for item in contenido["items"]:
            self.assertEqual(item["autoridad_clave"], "SLT-J2-CIV")

    def test_get_ubicaciones_expedientes_by_autoridad_clave_stl_j2_civ_and_expediente(self):
        """Test GET method for ubicaciones_expedientes by autoridad_clave SLT-J2-CIV and expediente 140/2023"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/ubicaciones_expedientes/paginado",
                headers={"X-Api-Key": config["api_key"]},
                params={"autoridad_clave": "SLT-J2-CIV", "expediente": "140/2023"},
                timeout=config["timeout"],
            )
        except requests.exceptions.ConnectionError as error:
            self.fail(error)
        self.assertEqual(response.status_code, 200)
        contenido = response.json()
        self.assertEqual(contenido["success"], True)
        self.assertEqual("items" in contenido, True)
        for item in contenido["items"]:
            self.assertEqual(item["autoridad_clave"], "SLT-J2-CIV")

    def test_get_ubicacion_expediente_by_id(self):
        """Test GET method for ubicaciones_expedientes by id"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/ubicaciones_expedientes/2",
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
        self.assertEqual(contenido["id"], 2)


if __name__ == "__main__":
    unittest.main()
