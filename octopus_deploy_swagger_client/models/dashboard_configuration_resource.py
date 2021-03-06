# coding: utf-8

"""
    Octopus Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2019.6.7+Branch.tags-2019.6.7.Sha.aa18dc6809953218c66f57eff7d26481d9b23d6a
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DashboardConfigurationResource(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'included_project_group_ids': 'list[str]',
        'included_project_ids': 'list[str]',
        'included_environment_ids': 'list[str]',
        'included_tenant_ids': 'list[str]',
        'project_limit': 'int',
        'included_tenant_tags': 'list[str]',
        'space_id': 'str',
        'last_modified_on': 'datetime',
        'last_modified_by': 'str',
        'links': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'Id',
        'included_project_group_ids': 'IncludedProjectGroupIds',
        'included_project_ids': 'IncludedProjectIds',
        'included_environment_ids': 'IncludedEnvironmentIds',
        'included_tenant_ids': 'IncludedTenantIds',
        'project_limit': 'ProjectLimit',
        'included_tenant_tags': 'IncludedTenantTags',
        'space_id': 'SpaceId',
        'last_modified_on': 'LastModifiedOn',
        'last_modified_by': 'LastModifiedBy',
        'links': 'Links'
    }

    def __init__(self, id=None, included_project_group_ids=None, included_project_ids=None, included_environment_ids=None, included_tenant_ids=None, project_limit=None, included_tenant_tags=None, space_id=None, last_modified_on=None, last_modified_by=None, links=None):  # noqa: E501
        """DashboardConfigurationResource - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._included_project_group_ids = None
        self._included_project_ids = None
        self._included_environment_ids = None
        self._included_tenant_ids = None
        self._project_limit = None
        self._included_tenant_tags = None
        self._space_id = None
        self._last_modified_on = None
        self._last_modified_by = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if included_project_group_ids is not None:
            self.included_project_group_ids = included_project_group_ids
        if included_project_ids is not None:
            self.included_project_ids = included_project_ids
        if included_environment_ids is not None:
            self.included_environment_ids = included_environment_ids
        if included_tenant_ids is not None:
            self.included_tenant_ids = included_tenant_ids
        if project_limit is not None:
            self.project_limit = project_limit
        if included_tenant_tags is not None:
            self.included_tenant_tags = included_tenant_tags
        if space_id is not None:
            self.space_id = space_id
        if last_modified_on is not None:
            self.last_modified_on = last_modified_on
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this DashboardConfigurationResource.  # noqa: E501


        :return: The id of this DashboardConfigurationResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DashboardConfigurationResource.


        :param id: The id of this DashboardConfigurationResource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def included_project_group_ids(self):
        """Gets the included_project_group_ids of this DashboardConfigurationResource.  # noqa: E501


        :return: The included_project_group_ids of this DashboardConfigurationResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._included_project_group_ids

    @included_project_group_ids.setter
    def included_project_group_ids(self, included_project_group_ids):
        """Sets the included_project_group_ids of this DashboardConfigurationResource.


        :param included_project_group_ids: The included_project_group_ids of this DashboardConfigurationResource.  # noqa: E501
        :type: list[str]
        """

        self._included_project_group_ids = included_project_group_ids

    @property
    def included_project_ids(self):
        """Gets the included_project_ids of this DashboardConfigurationResource.  # noqa: E501


        :return: The included_project_ids of this DashboardConfigurationResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._included_project_ids

    @included_project_ids.setter
    def included_project_ids(self, included_project_ids):
        """Sets the included_project_ids of this DashboardConfigurationResource.


        :param included_project_ids: The included_project_ids of this DashboardConfigurationResource.  # noqa: E501
        :type: list[str]
        """

        self._included_project_ids = included_project_ids

    @property
    def included_environment_ids(self):
        """Gets the included_environment_ids of this DashboardConfigurationResource.  # noqa: E501


        :return: The included_environment_ids of this DashboardConfigurationResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._included_environment_ids

    @included_environment_ids.setter
    def included_environment_ids(self, included_environment_ids):
        """Sets the included_environment_ids of this DashboardConfigurationResource.


        :param included_environment_ids: The included_environment_ids of this DashboardConfigurationResource.  # noqa: E501
        :type: list[str]
        """

        self._included_environment_ids = included_environment_ids

    @property
    def included_tenant_ids(self):
        """Gets the included_tenant_ids of this DashboardConfigurationResource.  # noqa: E501


        :return: The included_tenant_ids of this DashboardConfigurationResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._included_tenant_ids

    @included_tenant_ids.setter
    def included_tenant_ids(self, included_tenant_ids):
        """Sets the included_tenant_ids of this DashboardConfigurationResource.


        :param included_tenant_ids: The included_tenant_ids of this DashboardConfigurationResource.  # noqa: E501
        :type: list[str]
        """

        self._included_tenant_ids = included_tenant_ids

    @property
    def project_limit(self):
        """Gets the project_limit of this DashboardConfigurationResource.  # noqa: E501


        :return: The project_limit of this DashboardConfigurationResource.  # noqa: E501
        :rtype: int
        """
        return self._project_limit

    @project_limit.setter
    def project_limit(self, project_limit):
        """Sets the project_limit of this DashboardConfigurationResource.


        :param project_limit: The project_limit of this DashboardConfigurationResource.  # noqa: E501
        :type: int
        """

        self._project_limit = project_limit

    @property
    def included_tenant_tags(self):
        """Gets the included_tenant_tags of this DashboardConfigurationResource.  # noqa: E501


        :return: The included_tenant_tags of this DashboardConfigurationResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._included_tenant_tags

    @included_tenant_tags.setter
    def included_tenant_tags(self, included_tenant_tags):
        """Sets the included_tenant_tags of this DashboardConfigurationResource.


        :param included_tenant_tags: The included_tenant_tags of this DashboardConfigurationResource.  # noqa: E501
        :type: list[str]
        """

        self._included_tenant_tags = included_tenant_tags

    @property
    def space_id(self):
        """Gets the space_id of this DashboardConfigurationResource.  # noqa: E501


        :return: The space_id of this DashboardConfigurationResource.  # noqa: E501
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this DashboardConfigurationResource.


        :param space_id: The space_id of this DashboardConfigurationResource.  # noqa: E501
        :type: str
        """

        self._space_id = space_id

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this DashboardConfigurationResource.  # noqa: E501


        :return: The last_modified_on of this DashboardConfigurationResource.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this DashboardConfigurationResource.


        :param last_modified_on: The last_modified_on of this DashboardConfigurationResource.  # noqa: E501
        :type: datetime
        """

        self._last_modified_on = last_modified_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this DashboardConfigurationResource.  # noqa: E501


        :return: The last_modified_by of this DashboardConfigurationResource.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this DashboardConfigurationResource.


        :param last_modified_by: The last_modified_by of this DashboardConfigurationResource.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def links(self):
        """Gets the links of this DashboardConfigurationResource.  # noqa: E501


        :return: The links of this DashboardConfigurationResource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this DashboardConfigurationResource.


        :param links: The links of this DashboardConfigurationResource.  # noqa: E501
        :type: dict(str, str)
        """

        self._links = links

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DashboardConfigurationResource, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DashboardConfigurationResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
