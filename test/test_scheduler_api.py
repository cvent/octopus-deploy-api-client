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
from octopus_deploy_client.scheduler_api import SchedulerApi  # noqa: E501
from octopus_deploy_swagger_client.rest import ApiException


class TestSchedulerApi(unittest.TestCase):
    """SchedulerApi unit test stubs"""

    def setUp(self):
        self.api = octopus_deploy_client.scheduler_api.SchedulerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_custom_action_response_descriptor_octopus_server_web_api_actions_scheduled_task_details_responder(self):
        """Test case for custom_action_response_descriptor_octopus_server_web_api_actions_scheduled_task_details_responder

        """
        pass

    def test_custom_action_response_descriptor_octopus_server_web_api_actions_scheduled_task_raw_details_responder(self):
        """Test case for custom_action_response_descriptor_octopus_server_web_api_actions_scheduled_task_raw_details_responder

        """
        pass

    def test_custom_action_response_descriptor_octopus_server_web_api_actions_scheduler_get_responder(self):
        """Test case for custom_action_response_descriptor_octopus_server_web_api_actions_scheduler_get_responder

        """
        pass

    def test_custom_action_response_descriptor_octopus_server_web_api_actions_scheduler_start_responder(self):
        """Test case for custom_action_response_descriptor_octopus_server_web_api_actions_scheduler_start_responder

        """
        pass

    def test_custom_action_response_descriptor_octopus_server_web_api_actions_scheduler_stop_responder(self):
        """Test case for custom_action_response_descriptor_octopus_server_web_api_actions_scheduler_stop_responder

        """
        pass

    def test_custom_action_response_descriptor_octopus_server_web_api_actions_scheduler_trigger_responder(self):
        """Test case for custom_action_response_descriptor_octopus_server_web_api_actions_scheduler_trigger_responder

        """
        pass


if __name__ == '__main__':
    unittest.main()