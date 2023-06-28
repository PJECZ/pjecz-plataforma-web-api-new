"""
Unit tests for sentencias category
"""
import unittest

import requests

from tests.load_env import config


class TestSentencias(unittest.TestCase):
    """Tests for sentencias category"""

    def test_get_sentencias(self):
        """Test GET method for sentencias"""
        response = requests.get(
            f"{config['host']}/v3/sentencias",
            headers={"X-Api-Key": config["api_key"]},
            timeout=config["timeout"],
        )
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
