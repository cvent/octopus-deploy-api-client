# coding: utf-8

"""
    Octopus Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2019.6.7+Branch.tags-2019.6.7.Sha.aa18dc6809953218c66f57eff7d26481d9b23d6a
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from octopus_deploy_swagger_client.api_client import ApiClient


class ApiKeysApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def custom_action_response_descriptor_octopus_server_web_api_actions_create_api_key_action(self, user_id, **kwargs):  # noqa: E501
        """custom_action_response_descriptor_octopus_server_web_api_actions_create_api_key_action  # noqa: E501

        Generates a new API key for the specified user. The API key returned in the result must be saved by the caller, as it cannot be retrieved subsequently from the Octopus server.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_action_response_descriptor_octopus_server_web_api_actions_create_api_key_action(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: ID of the user (required)
        :return: ApiKeyResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.custom_action_response_descriptor_octopus_server_web_api_actions_create_api_key_action_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.custom_action_response_descriptor_octopus_server_web_api_actions_create_api_key_action_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def custom_action_response_descriptor_octopus_server_web_api_actions_create_api_key_action_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """custom_action_response_descriptor_octopus_server_web_api_actions_create_api_key_action  # noqa: E501

        Generates a new API key for the specified user. The API key returned in the result must be saved by the caller, as it cannot be retrieved subsequently from the Octopus server.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_action_response_descriptor_octopus_server_web_api_actions_create_api_key_action_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: ID of the user (required)
        :return: ApiKeyResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method custom_action_response_descriptor_octopus_server_web_api_actions_create_api_key_action" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `custom_action_response_descriptor_octopus_server_web_api_actions_create_api_key_action`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyQuery', 'NugetApiKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/api/users/{userId}/apikeys', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiKeyResource',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def custom_query_response_descriptor_octopus_server_web_api_actions_index_api_keys_responder(self, user_id, **kwargs):  # noqa: E501
        """custom_query_response_descriptor_octopus_server_web_api_actions_index_api_keys_responder  # noqa: E501

        Lists all API keys for a user, returning the most recent results first.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_query_response_descriptor_octopus_server_web_api_actions_index_api_keys_responder(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: ID of the user (required)
        :return: ResourceCollectionApiKeyResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.custom_query_response_descriptor_octopus_server_web_api_actions_index_api_keys_responder_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.custom_query_response_descriptor_octopus_server_web_api_actions_index_api_keys_responder_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def custom_query_response_descriptor_octopus_server_web_api_actions_index_api_keys_responder_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """custom_query_response_descriptor_octopus_server_web_api_actions_index_api_keys_responder  # noqa: E501

        Lists all API keys for a user, returning the most recent results first.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_query_response_descriptor_octopus_server_web_api_actions_index_api_keys_responder_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: ID of the user (required)
        :return: ResourceCollectionApiKeyResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method custom_query_response_descriptor_octopus_server_web_api_actions_index_api_keys_responder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `custom_query_response_descriptor_octopus_server_web_api_actions_index_api_keys_responder`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyQuery', 'NugetApiKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/api/users/{userId}/apikeys', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourceCollectionApiKeyResource',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_on_background_response_descriptor_users_api_key_api_key_resource(self, id, **kwargs):  # noqa: E501
        """Delete a ApiKeyResource by ID  # noqa: E501

        Revokes an existing API key.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_on_background_response_descriptor_users_api_key_api_key_resource(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the ApiKeyResource to delete (required)
        :return: TaskResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_on_background_response_descriptor_users_api_key_api_key_resource_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_on_background_response_descriptor_users_api_key_api_key_resource_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_on_background_response_descriptor_users_api_key_api_key_resource_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete a ApiKeyResource by ID  # noqa: E501

        Revokes an existing API key.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_on_background_response_descriptor_users_api_key_api_key_resource_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the ApiKeyResource to delete (required)
        :return: TaskResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_on_background_response_descriptor_users_api_key_api_key_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_on_background_response_descriptor_users_api_key_api_key_resource`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyQuery', 'NugetApiKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/api/users/{userId}/apikeys/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaskResource',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def load_response_descriptor_users_api_key_api_key_resource(self, id, **kwargs):  # noqa: E501
        """Get a ApiKeyResource by ID  # noqa: E501

        Gets a API key by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.load_response_descriptor_users_api_key_api_key_resource(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the ApiKeyResource to load (required)
        :return: ApiKeyResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.load_response_descriptor_users_api_key_api_key_resource_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.load_response_descriptor_users_api_key_api_key_resource_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def load_response_descriptor_users_api_key_api_key_resource_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get a ApiKeyResource by ID  # noqa: E501

        Gets a API key by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.load_response_descriptor_users_api_key_api_key_resource_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the ApiKeyResource to load (required)
        :return: ApiKeyResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method load_response_descriptor_users_api_key_api_key_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `load_response_descriptor_users_api_key_api_key_resource`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyQuery', 'NugetApiKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/api/users/{userId}/apikeys/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiKeyResource',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)