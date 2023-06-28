"""
Unit tests for repsvm category
"""
import unittest

import requests

from tests.load_env import config


class TestREPSVM(unittest.TestCase):
    """Tests for repsvm category"""

    def test_get_repsvm(self):
        """Test GET method for repsvm_agresores"""
        response = requests.get(
            f"{config['host']}/v3/repsvm_agresores",
            headers={"X-Api-Key": config["api_key"]},
            timeout=config["timeout"],
        )
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
