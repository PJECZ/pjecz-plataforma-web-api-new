"""
Unit tests for glosas category
"""
import unittest

import requests

from tests.load_env import config


class TestGlosas(unittest.TestCase):
    """Tests for glosas category"""

    def test_get_glosas(self):
        """Test GET method for glosas"""
        response = requests.get(
            f"{config['host']}/v3/glosas",
            headers={"X-Api-Key": config["api_key"]},
            timeout=config["timeout"],
        )
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
