"""
Unit tests for edictos category
"""
import unittest

import requests

from tests.load_env import config


class TestEdictos(unittest.TestCase):
    """Tests for edictos category"""

    def test_get_edictos(self):
        """Test GET method for edictos"""
        response = requests.get(
            f"{config['host']}/v3/edictos",
            headers={"X-Api-Key": config["api_key"]},
            timeout=config["timeout"],
        )
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
