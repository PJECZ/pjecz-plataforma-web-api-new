"""
Unit tests for redam category
"""
import unittest

import requests

from tests.load_env import config


class TestREDAM(unittest.TestCase):
    """Tests for redam category"""

    def test_get_redam(self):
        """Test GET method for redam"""
        response = requests.get(
            f"{config['host']}/v3/redam",
            headers={"X-Api-Key": config["api_key"]},
            timeout=config["timeout"],
        )
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
