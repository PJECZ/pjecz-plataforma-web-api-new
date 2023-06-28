"""
Unit tests for listas de acuerdos category
"""
import unittest

import requests

from tests.load_env import config


class TestListasDeAcuerdos(unittest.TestCase):
    """Tests for listas de acuerdos category"""

    def test_get_listas_de_acuerdos(self):
        """Test GET method for listas de acuerdos"""
        response = requests.get(
            f"{config['host']}/v3/listas_de_acuerdos",
            headers={"X-Api-Key": config["api_key"]},
            timeout=config["timeout"],
        )
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
