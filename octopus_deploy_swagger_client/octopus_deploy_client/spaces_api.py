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


class SpacesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def custom_action_response_descriptor_octopus_server_web_api_actions_create_space_responder(self, **kwargs):  # noqa: E501
        """custom_action_response_descriptor_octopus_server_web_api_actions_create_space_responder  # noqa: E501

        Creates a new Space.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_action_response_descriptor_octopus_server_web_api_actions_create_space_responder(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: SpaceResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.custom_action_response_descriptor_octopus_server_web_api_actions_create_space_responder_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.custom_action_response_descriptor_octopus_server_web_api_actions_create_space_responder_with_http_info(**kwargs)  # noqa: E501
            return data

    def custom_action_response_descriptor_octopus_server_web_api_actions_create_space_responder_with_http_info(self, **kwargs):  # noqa: E501
        """custom_action_response_descriptor_octopus_server_web_api_actions_create_space_responder  # noqa: E501

        Creates a new Space.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_action_response_descriptor_octopus_server_web_api_actions_create_space_responder_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: SpaceResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method custom_action_response_descriptor_octopus_server_web_api_actions_create_space_responder" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/api/spaces', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SpaceResource',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def custom_action_response_descriptor_octopus_server_web_api_actions_delete_space_responder(self, id, **kwargs):  # noqa: E501
        """custom_action_response_descriptor_octopus_server_web_api_actions_delete_space_responder  # noqa: E501

        Deletes an existing project.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_action_response_descriptor_octopus_server_web_api_actions_delete_space_responder(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the resource (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.custom_action_response_descriptor_octopus_server_web_api_actions_delete_space_responder_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.custom_action_response_descriptor_octopus_server_web_api_actions_delete_space_responder_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def custom_action_response_descriptor_octopus_server_web_api_actions_delete_space_responder_with_http_info(self, id, **kwargs):  # noqa: E501
        """custom_action_response_descriptor_octopus_server_web_api_actions_delete_space_responder  # noqa: E501

        Deletes an existing project.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_action_response_descriptor_octopus_server_web_api_actions_delete_space_responder_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the resource (required)
        :return: None
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
                    " to method custom_action_response_descriptor_octopus_server_web_api_actions_delete_space_responder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `custom_action_response_descriptor_octopus_server_web_api_actions_delete_space_responder`")  # noqa: E501

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
            '/api/spaces/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def custom_action_response_descriptor_octopus_server_web_api_actions_modify_space_responder(self, id, **kwargs):  # noqa: E501
        """custom_action_response_descriptor_octopus_server_web_api_actions_modify_space_responder  # noqa: E501

        Modifies an existing space.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_action_response_descriptor_octopus_server_web_api_actions_modify_space_responder(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the resource (required)
        :return: SpaceResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.custom_action_response_descriptor_octopus_server_web_api_actions_modify_space_responder_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.custom_action_response_descriptor_octopus_server_web_api_actions_modify_space_responder_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def custom_action_response_descriptor_octopus_server_web_api_actions_modify_space_responder_with_http_info(self, id, **kwargs):  # noqa: E501
        """custom_action_response_descriptor_octopus_server_web_api_actions_modify_space_responder  # noqa: E501

        Modifies an existing space.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_action_response_descriptor_octopus_server_web_api_actions_modify_space_responder_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the resource (required)
        :return: SpaceResource
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
                    " to method custom_action_response_descriptor_octopus_server_web_api_actions_modify_space_responder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `custom_action_response_descriptor_octopus_server_web_api_actions_modify_space_responder`")  # noqa: E501

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
            '/api/spaces/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SpaceResource',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def custom_action_response_descriptor_octopus_server_web_api_actions_space_logo_get_responder(self, id, **kwargs):  # noqa: E501
        """custom_action_response_descriptor_octopus_server_web_api_actions_space_logo_get_responder  # noqa: E501

        Gets the logo associated with the space.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_action_response_descriptor_octopus_server_web_api_actions_space_logo_get_responder(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the resource (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.custom_action_response_descriptor_octopus_server_web_api_actions_space_logo_get_responder_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.custom_action_response_descriptor_octopus_server_web_api_actions_space_logo_get_responder_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def custom_action_response_descriptor_octopus_server_web_api_actions_space_logo_get_responder_with_http_info(self, id, **kwargs):  # noqa: E501
        """custom_action_response_descriptor_octopus_server_web_api_actions_space_logo_get_responder  # noqa: E501

        Gets the logo associated with the space.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_action_response_descriptor_octopus_server_web_api_actions_space_logo_get_responder_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the resource (required)
        :return: file
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
                    " to method custom_action_response_descriptor_octopus_server_web_api_actions_space_logo_get_responder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `custom_action_response_descriptor_octopus_server_web_api_actions_space_logo_get_responder`")  # noqa: E501

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
            ['image/png'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyQuery', 'NugetApiKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/api/spaces/{id}/logo', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def custom_action_response_descriptor_octopus_server_web_api_actions_space_logo_put_responder(self, id, **kwargs):  # noqa: E501
        """custom_action_response_descriptor_octopus_server_web_api_actions_space_logo_put_responder  # noqa: E501

        Updates the logo associated with the space.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_action_response_descriptor_octopus_server_web_api_actions_space_logo_put_responder(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the resource (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.custom_action_response_descriptor_octopus_server_web_api_actions_space_logo_put_responder_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.custom_action_response_descriptor_octopus_server_web_api_actions_space_logo_put_responder_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def custom_action_response_descriptor_octopus_server_web_api_actions_space_logo_put_responder_with_http_info(self, id, **kwargs):  # noqa: E501
        """custom_action_response_descriptor_octopus_server_web_api_actions_space_logo_put_responder  # noqa: E501

        Updates the logo associated with the space.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_action_response_descriptor_octopus_server_web_api_actions_space_logo_put_responder_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the resource (required)
        :return: None
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
                    " to method custom_action_response_descriptor_octopus_server_web_api_actions_space_logo_put_responder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `custom_action_response_descriptor_octopus_server_web_api_actions_space_logo_put_responder`")  # noqa: E501

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
            '/api/spaces/{id}/logo', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def custom_action_response_descriptor_octopus_server_web_api_actions_space_logo_put_responder_0(self, id, **kwargs):  # noqa: E501
        """custom_action_response_descriptor_octopus_server_web_api_actions_space_logo_put_responder_0  # noqa: E501

        Updates the logo associated with the space.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_action_response_descriptor_octopus_server_web_api_actions_space_logo_put_responder_0(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the resource (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.custom_action_response_descriptor_octopus_server_web_api_actions_space_logo_put_responder_0_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.custom_action_response_descriptor_octopus_server_web_api_actions_space_logo_put_responder_0_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def custom_action_response_descriptor_octopus_server_web_api_actions_space_logo_put_responder_0_with_http_info(self, id, **kwargs):  # noqa: E501
        """custom_action_response_descriptor_octopus_server_web_api_actions_space_logo_put_responder_0  # noqa: E501

        Updates the logo associated with the space.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.custom_action_response_descriptor_octopus_server_web_api_actions_space_logo_put_responder_0_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the resource (required)
        :return: None
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
                    " to method custom_action_response_descriptor_octopus_server_web_api_actions_space_logo_put_responder_0" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `custom_action_response_descriptor_octopus_server_web_api_actions_space_logo_put_responder_0`")  # noqa: E501

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
            '/api/spaces/{id}/logo', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def index_response_descriptor_spaces_space_space_resource(self, **kwargs):  # noqa: E501
        """Get a list of SpaceResources  # noqa: E501

        Lists all of the spaces in the supplied Octopus Deploy Space. The results will be sorted alphabetically by name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.index_response_descriptor_spaces_space_space_resource(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: Number of items to skip
        :param int take: Number of items to take
        :return: ResourceCollectionSpaceResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.index_response_descriptor_spaces_space_space_resource_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.index_response_descriptor_spaces_space_space_resource_with_http_info(**kwargs)  # noqa: E501
            return data

    def index_response_descriptor_spaces_space_space_resource_with_http_info(self, **kwargs):  # noqa: E501
        """Get a list of SpaceResources  # noqa: E501

        Lists all of the spaces in the supplied Octopus Deploy Space. The results will be sorted alphabetically by name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.index_response_descriptor_spaces_space_space_resource_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: Number of items to skip
        :param int take: Number of items to take
        :return: ResourceCollectionSpaceResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'take']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method index_response_descriptor_spaces_space_space_resource" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'take' in params:
            query_params.append(('take', params['take']))  # noqa: E501

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
            '/api/spaces', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourceCollectionSpaceResource',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_all_response_descriptor_spaces_space_space_resource(self, **kwargs):  # noqa: E501
        """Get a list of SpaceResources  # noqa: E501

        Lists all of the spaces in the supplied Octopus Deploy Space. The results will be sorted alphabetically by name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_all_response_descriptor_spaces_space_space_resource(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[SpaceResource]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_all_response_descriptor_spaces_space_space_resource_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_all_response_descriptor_spaces_space_space_resource_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_all_response_descriptor_spaces_space_space_resource_with_http_info(self, **kwargs):  # noqa: E501
        """Get a list of SpaceResources  # noqa: E501

        Lists all of the spaces in the supplied Octopus Deploy Space. The results will be sorted alphabetically by name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_all_response_descriptor_spaces_space_space_resource_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[SpaceResource]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_all_response_descriptor_spaces_space_space_resource" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/api/spaces/all', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SpaceResource]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def load_response_descriptor_spaces_space_space_resource(self, id, **kwargs):  # noqa: E501
        """Get a SpaceResource by ID  # noqa: E501

        Get a space  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.load_response_descriptor_spaces_space_space_resource(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the SpaceResource to load (required)
        :return: SpaceResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.load_response_descriptor_spaces_space_space_resource_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.load_response_descriptor_spaces_space_space_resource_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def load_response_descriptor_spaces_space_space_resource_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get a SpaceResource by ID  # noqa: E501

        Get a space  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.load_response_descriptor_spaces_space_space_resource_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the SpaceResource to load (required)
        :return: SpaceResource
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
                    " to method load_response_descriptor_spaces_space_space_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `load_response_descriptor_spaces_space_space_resource`")  # noqa: E501

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
            '/api/spaces/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SpaceResource',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
