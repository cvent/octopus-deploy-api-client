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
from octopus_deploy_client.octopus_server_nodes_api import OctopusServerNodesApi  # noqa: E501
from octopus_deploy_swagger_client.rest import ApiException


class TestOctopusServerNodesApi(unittest.TestCase):
    """OctopusServerNodesApi unit test stubs"""

    def setUp(self):
        self.api = octopus_deploy_client.octopus_server_nodes_api.OctopusServerNodesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_custom_action_response_descriptor_octopus_server_web_api_actions_load_balancer_ping_responder(self):
        """Test case for custom_action_response_descriptor_octopus_server_web_api_actions_load_balancer_ping_responder

        """
        pass

    def test_custom_action_response_descriptor_octopus_server_web_api_actions_octopus_server_cluster_summary_responder(self):
        """Test case for custom_action_response_descriptor_octopus_server_web_api_actions_octopus_server_cluster_summary_responder

        """
        pass

    def test_custom_action_response_descriptor_octopus_server_web_api_actions_octopus_server_node_details_responder(self):
        """Test case for custom_action_response_descriptor_octopus_server_web_api_actions_octopus_server_node_details_responder

        """
        pass

    def test_delete_on_background_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource(self):
        """Test case for delete_on_background_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource

        Delete a OctopusServerNodeResource by ID  # noqa: E501
        """
        pass

    def test_index_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource(self):
        """Test case for index_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource

        Get a list of OctopusServerNodeResources  # noqa: E501
        """
        pass

    def test_list_all_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource(self):
        """Test case for list_all_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource

        Get a list of OctopusServerNodeResources  # noqa: E501
        """
        pass

    def test_load_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource(self):
        """Test case for load_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource

        Get a OctopusServerNodeResource by ID  # noqa: E501
        """
        pass

    def test_modify_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource(self):
        """Test case for modify_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource

        Modify a OctopusServerNodeResource by ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()