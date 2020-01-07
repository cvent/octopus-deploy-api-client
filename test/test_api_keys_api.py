# coding: utf-8

"""
    Octopus Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2019.6.7+Branch.tags-2019.6.7.Sha.aa18dc6809953218c66f57eff7d26481d9b23d6a
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import octopus_deploy_swagger_client
from octopus_deploy_client.api_keys_api import ApiKeysApi  # noqa: E501
from octopus_deploy_swagger_client.rest import ApiException


class TestApiKeysApi(unittest.TestCase):
    """ApiKeysApi unit test stubs"""

    def setUp(self):
        self.api = octopus_deploy_client.api_keys_api.ApiKeysApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_custom_action_response_descriptor_octopus_server_web_api_actions_create_api_key_action(self):
        """Test case for custom_action_response_descriptor_octopus_server_web_api_actions_create_api_key_action

        """
        pass

    def test_custom_query_response_descriptor_octopus_server_web_api_actions_index_api_keys_responder(self):
        """Test case for custom_query_response_descriptor_octopus_server_web_api_actions_index_api_keys_responder

        """
        pass

    def test_delete_on_background_response_descriptor_users_api_key_api_key_resource(self):
        """Test case for delete_on_background_response_descriptor_users_api_key_api_key_resource

        Delete a ApiKeyResource by ID  # noqa: E501
        """
        pass

    def test_load_response_descriptor_users_api_key_api_key_resource(self):
        """Test case for load_response_descriptor_users_api_key_api_key_resource

        Get a ApiKeyResource by ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
