"""
Unit tests for materias tipos juicios
"""

import unittest

import requests

from tests.load_env import config


class TestMateriasTiposJuicios(unittest.TestCase):
    """Tests for materias tipos juicios"""

    def test_get_materias_tipos_juicios(self):
        """Test GET method for materias tipos juicios"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/materias_tipos_juicios",
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

    def test_get_materias_tipos_juicios_by_materia_id_2(self):
        """Test GET method for materias tipos juicios by materia_id=2"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/materias_tipos_juicios",
                headers={"X-Api-Key": config["api_key"]},
                params={"materia_id": 2},
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
        for item in contenido["items"]:
            self.assertEqual(item["materia_id"], 2)

    def test_get_materias_tipos_juicios_by_materia_clave_fam(self):
        """Test GET method for materias tipos juicios by materia_clave=FAM"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/materias_tipos_juicios",
                headers={"X-Api-Key": config["api_key"]},
                params={"materia_clave": "FAM"},
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
        for item in contenido["items"]:
            self.assertEqual(item["materia_clave"], "FAM")

    def test_get_materia_tipo_juicio_by_id(self):
        """Test GET method for materia_tipo_juicio by id"""
        try:
            response = requests.get(
                url=f"{config['host']}/v3/materias_tipos_juicios/1",
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
