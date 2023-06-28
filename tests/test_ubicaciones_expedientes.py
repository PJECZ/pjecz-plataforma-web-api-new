"""
Unit tests for ubicaciones de expedientes category
"""
import unittest

import requests

from tests.load_env import config


class TestUbicacionesExpedientes(unittest.TestCase):
    """Tests for ubicaciones de expedientes category"""

    def test_get_ubicaciones_expedientes(self):
        """Test GET method for ubicaciones_expedientes"""
        response = requests.get(
            f"{config['host']}/v3/ubicaciones_expedientes",
            headers={"X-Api-Key": config["api_key"]},
            timeout=config["timeout"],
        )
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
