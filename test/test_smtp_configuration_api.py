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
from octopus_deploy_client.smtp_configuration_api import SmtpConfigurationApi  # noqa: E501
from octopus_deploy_swagger_client.rest import ApiException


class TestSmtpConfigurationApi(unittest.TestCase):
    """SmtpConfigurationApi unit test stubs"""

    def setUp(self):
        self.api = octopus_deploy_client.smtp_configuration_api.SmtpConfigurationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_custom_action_response_descriptor_octopus_server_web_api_actions_smtp_configuration_get_action(self):
        """Test case for custom_action_response_descriptor_octopus_server_web_api_actions_smtp_configuration_get_action

        """
        pass

    def test_custom_action_response_descriptor_octopus_server_web_api_actions_smtp_configuration_update_action(self):
        """Test case for custom_action_response_descriptor_octopus_server_web_api_actions_smtp_configuration_update_action

        """
        pass

    def test_custom_action_response_descriptor_octopus_server_web_api_actions_smtp_is_configured_responder(self):
        """Test case for custom_action_response_descriptor_octopus_server_web_api_actions_smtp_is_configured_responder

        """
        pass


if __name__ == '__main__':
    unittest.main()
