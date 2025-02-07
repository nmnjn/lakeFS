"""
    lakeFS API

    lakeFS HTTP API  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: services@treeverse.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import lakefs_client
from lakefs_client.api.config_api import ConfigApi  # noqa: E501


class TestConfigApi(unittest.TestCase):
    """ConfigApi unit test stubs"""

    def setUp(self):
        self.api = ConfigApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_lake_fs_version(self):
        """Test case for get_lake_fs_version

        """
        pass

    def test_get_setup_state(self):
        """Test case for get_setup_state

        check if the lakeFS installation is already set up  # noqa: E501
        """
        pass

    def test_get_storage_config(self):
        """Test case for get_storage_config

        """
        pass

    def test_setup(self):
        """Test case for setup

        setup lakeFS and create a first user  # noqa: E501
        """
        pass

    def test_setup_comm_prefs(self):
        """Test case for setup_comm_prefs

        setup communications preferences  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
