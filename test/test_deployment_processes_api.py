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
from octopus_deploy_client.deployment_processes_api import DeploymentProcessesApi  # noqa: E501
from octopus_deploy_swagger_client.rest import ApiException


class TestDeploymentProcessesApi(unittest.TestCase):
    """DeploymentProcessesApi unit test stubs"""

    def setUp(self):
        self.api = octopus_deploy_client.deployment_processes_api.DeploymentProcessesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_custom_action_response_descriptor_octopus_server_web_api_actions_deployment_process_update_action(self):
        """Test case for custom_action_response_descriptor_octopus_server_web_api_actions_deployment_process_update_action

        """
        pass

    def test_custom_action_response_descriptor_octopus_server_web_api_actions_deployment_process_update_action_spaces(self):
        """Test case for custom_action_response_descriptor_octopus_server_web_api_actions_deployment_process_update_action_spaces

        """
        pass

    def test_custom_action_response_descriptor_octopus_server_web_api_actions_release_template_action(self):
        """Test case for custom_action_response_descriptor_octopus_server_web_api_actions_release_template_action

        """
        pass

    def test_custom_action_response_descriptor_octopus_server_web_api_actions_release_template_action_spaces(self):
        """Test case for custom_action_response_descriptor_octopus_server_web_api_actions_release_template_action_spaces

        """
        pass

    def test_index_response_descriptor_projects_deployment_process_deployment_process_resource(self):
        """Test case for index_response_descriptor_projects_deployment_process_deployment_process_resource

        Get a list of DeploymentProcessResources  # noqa: E501
        """
        pass

    def test_index_response_descriptor_projects_deployment_process_deployment_process_resource_spaces(self):
        """Test case for index_response_descriptor_projects_deployment_process_deployment_process_resource_spaces

        Get a list of DeploymentProcessResources  # noqa: E501
        """
        pass

    def test_load_response_descriptor_projects_deployment_process_deployment_process_resource(self):
        """Test case for load_response_descriptor_projects_deployment_process_deployment_process_resource

        Get a DeploymentProcessResource by ID  # noqa: E501
        """
        pass

    def test_load_response_descriptor_projects_deployment_process_deployment_process_resource_spaces(self):
        """Test case for load_response_descriptor_projects_deployment_process_deployment_process_resource_spaces

        Get a DeploymentProcessResource by ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
