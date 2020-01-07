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


class UserRolesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_response_descriptor_users_user_role_user_role_resource(self, **kwargs):  # noqa: E501
        """Create a UserRoleResource  # noqa: E501

        Creates a custom user role definition.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_response_descriptor_users_user_role_user_role_resource(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserRoleResource user_role_resource: The UserRoleResource resource to create
        :return: UserRoleResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_response_descriptor_users_user_role_user_role_resource_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_response_descriptor_users_user_role_user_role_resource_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_response_descriptor_users_user_role_user_role_resource_with_http_info(self, **kwargs):  # noqa: E501
        """Create a UserRoleResource  # noqa: E501

        Creates a custom user role definition.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_response_descriptor_users_user_role_user_role_resource_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserRoleResource user_role_resource: The UserRoleResource resource to create
        :return: UserRoleResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_role_resource']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_response_descriptor_users_user_role_user_role_resource" % key
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
        if 'user_role_resource' in params:
            body_params = params['user_role_resource']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyQuery', 'NugetApiKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/api/userroles', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserRoleResource',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_on_background_response_descriptor_users_user_role_user_role_resource(self, id, **kwargs):  # noqa: E501
        """Delete a UserRoleResource by ID  # noqa: E501

        Deletes an existing user role.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_on_background_response_descriptor_users_user_role_user_role_resource(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the UserRoleResource to delete (required)
        :return: TaskResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_on_background_response_descriptor_users_user_role_user_role_resource_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_on_background_response_descriptor_users_user_role_user_role_resource_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_on_background_response_descriptor_users_user_role_user_role_resource_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete a UserRoleResource by ID  # noqa: E501

        Deletes an existing user role.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_on_background_response_descriptor_users_user_role_user_role_resource_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the UserRoleResource to delete (required)
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
                    " to method delete_on_background_response_descriptor_users_user_role_user_role_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_on_background_response_descriptor_users_user_role_user_role_resource`")  # noqa: E501

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
            '/api/userroles/{id}', 'DELETE',
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

    def index_response_descriptor_users_user_role_user_role_resource(self, **kwargs):  # noqa: E501
        """Get a list of UserRoleResources  # noqa: E501

        Lists all of the user roles in the current Octopus Deploy instance. The results will be sorted alphabetically by name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.index_response_descriptor_users_user_role_user_role_resource(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: Number of items to skip
        :param int take: Number of items to take
        :return: ResourceCollectionUserRoleResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.index_response_descriptor_users_user_role_user_role_resource_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.index_response_descriptor_users_user_role_user_role_resource_with_http_info(**kwargs)  # noqa: E501
            return data

    def index_response_descriptor_users_user_role_user_role_resource_with_http_info(self, **kwargs):  # noqa: E501
        """Get a list of UserRoleResources  # noqa: E501

        Lists all of the user roles in the current Octopus Deploy instance. The results will be sorted alphabetically by name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.index_response_descriptor_users_user_role_user_role_resource_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: Number of items to skip
        :param int take: Number of items to take
        :return: ResourceCollectionUserRoleResource
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
                    " to method index_response_descriptor_users_user_role_user_role_resource" % key
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
            '/api/userroles', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourceCollectionUserRoleResource',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_all_response_descriptor_users_user_role_user_role_resource(self, **kwargs):  # noqa: E501
        """Get a list of UserRoleResources  # noqa: E501

        Lists all of the user roles in the current Octopus Deploy instance. The results will be sorted alphabetically by name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_all_response_descriptor_users_user_role_user_role_resource(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[UserRoleResource]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_all_response_descriptor_users_user_role_user_role_resource_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_all_response_descriptor_users_user_role_user_role_resource_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_all_response_descriptor_users_user_role_user_role_resource_with_http_info(self, **kwargs):  # noqa: E501
        """Get a list of UserRoleResources  # noqa: E501

        Lists all of the user roles in the current Octopus Deploy instance. The results will be sorted alphabetically by name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_all_response_descriptor_users_user_role_user_role_resource_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[UserRoleResource]
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
                    " to method list_all_response_descriptor_users_user_role_user_role_resource" % key
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
            '/api/userroles/all', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[UserRoleResource]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def load_response_descriptor_users_user_role_user_role_resource(self, id, **kwargs):  # noqa: E501
        """Get a UserRoleResource by ID  # noqa: E501

        Gets a single user role by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.load_response_descriptor_users_user_role_user_role_resource(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the UserRoleResource to load (required)
        :return: UserRoleResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.load_response_descriptor_users_user_role_user_role_resource_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.load_response_descriptor_users_user_role_user_role_resource_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def load_response_descriptor_users_user_role_user_role_resource_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get a UserRoleResource by ID  # noqa: E501

        Gets a single user role by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.load_response_descriptor_users_user_role_user_role_resource_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the UserRoleResource to load (required)
        :return: UserRoleResource
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
                    " to method load_response_descriptor_users_user_role_user_role_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `load_response_descriptor_users_user_role_user_role_resource`")  # noqa: E501

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
            '/api/userroles/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserRoleResource',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def modify_response_descriptor_users_user_role_user_role_resource(self, id, **kwargs):  # noqa: E501
        """Modify a UserRoleResource by ID  # noqa: E501

        Modifies an existing user role definition.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_response_descriptor_users_user_role_user_role_resource(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the UserRoleResource to modify (required)
        :param UserRoleResource user_role_resource: The UserRoleResource resource to create
        :return: UserRoleResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_response_descriptor_users_user_role_user_role_resource_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_response_descriptor_users_user_role_user_role_resource_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def modify_response_descriptor_users_user_role_user_role_resource_with_http_info(self, id, **kwargs):  # noqa: E501
        """Modify a UserRoleResource by ID  # noqa: E501

        Modifies an existing user role definition.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_response_descriptor_users_user_role_user_role_resource_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the UserRoleResource to modify (required)
        :param UserRoleResource user_role_resource: The UserRoleResource resource to create
        :return: UserRoleResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'user_role_resource']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method modify_response_descriptor_users_user_role_user_role_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `modify_response_descriptor_users_user_role_user_role_resource`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'user_role_resource' in params:
            body_params = params['user_role_resource']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyQuery', 'NugetApiKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/api/userroles/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserRoleResource',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
