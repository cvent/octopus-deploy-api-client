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
from octopus_deploy_client.external_security_groups_api import ExternalSecurityGroupsApi  # noqa: E501
from octopus_deploy_swagger_client.rest import ApiException


class TestExternalSecurityGroupsApi(unittest.TestCase):
    """ExternalSecurityGroupsApi unit test stubs"""

    def setUp(self):
        self.api = octopus_deploy_client.external_security_groups_api.ExternalSecurityGroupsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_custom_action_response_descriptor_octopus_server_web_api_actions_list_providers_that_support_external_security_groups_responder(self):
        """Test case for custom_action_response_descriptor_octopus_server_web_api_actions_list_providers_that_support_external_security_groups_responder

        """
        pass


if __name__ == '__main__':
    unittest.main()
