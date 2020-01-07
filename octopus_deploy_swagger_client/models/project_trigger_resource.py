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

from octopus_deploy_swagger_client.models.trigger_action_resource import TriggerActionResource  # noqa: F401,E501
from octopus_deploy_swagger_client.models.trigger_filter_resource import TriggerFilterResource  # noqa: F401,E501


class ProjectTriggerResource(object):
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
        'name': 'str',
        'project_id': 'str',
        'is_disabled': 'bool',
        'filter': 'TriggerFilterResource',
        'action': 'TriggerActionResource',
        'space_id': 'str',
        'last_modified_on': 'datetime',
        'last_modified_by': 'str',
        'links': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'project_id': 'ProjectId',
        'is_disabled': 'IsDisabled',
        'filter': 'Filter',
        'action': 'Action',
        'space_id': 'SpaceId',
        'last_modified_on': 'LastModifiedOn',
        'last_modified_by': 'LastModifiedBy',
        'links': 'Links'
    }

    def __init__(self, id=None, name=None, project_id=None, is_disabled=None, filter=None, action=None, space_id=None, last_modified_on=None, last_modified_by=None, links=None):  # noqa: E501
        """ProjectTriggerResource - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._project_id = None
        self._is_disabled = None
        self._filter = None
        self._action = None
        self._space_id = None
        self._last_modified_on = None
        self._last_modified_by = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if is_disabled is not None:
            self.is_disabled = is_disabled
        if filter is not None:
            self.filter = filter
        if action is not None:
            self.action = action
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
        """Gets the id of this ProjectTriggerResource.  # noqa: E501


        :return: The id of this ProjectTriggerResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectTriggerResource.


        :param id: The id of this ProjectTriggerResource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ProjectTriggerResource.  # noqa: E501


        :return: The name of this ProjectTriggerResource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectTriggerResource.


        :param name: The name of this ProjectTriggerResource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this ProjectTriggerResource.  # noqa: E501


        :return: The project_id of this ProjectTriggerResource.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ProjectTriggerResource.


        :param project_id: The project_id of this ProjectTriggerResource.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def is_disabled(self):
        """Gets the is_disabled of this ProjectTriggerResource.  # noqa: E501


        :return: The is_disabled of this ProjectTriggerResource.  # noqa: E501
        :rtype: bool
        """
        return self._is_disabled

    @is_disabled.setter
    def is_disabled(self, is_disabled):
        """Sets the is_disabled of this ProjectTriggerResource.


        :param is_disabled: The is_disabled of this ProjectTriggerResource.  # noqa: E501
        :type: bool
        """

        self._is_disabled = is_disabled

    @property
    def filter(self):
        """Gets the filter of this ProjectTriggerResource.  # noqa: E501


        :return: The filter of this ProjectTriggerResource.  # noqa: E501
        :rtype: TriggerFilterResource
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this ProjectTriggerResource.


        :param filter: The filter of this ProjectTriggerResource.  # noqa: E501
        :type: TriggerFilterResource
        """

        self._filter = filter

    @property
    def action(self):
        """Gets the action of this ProjectTriggerResource.  # noqa: E501


        :return: The action of this ProjectTriggerResource.  # noqa: E501
        :rtype: TriggerActionResource
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ProjectTriggerResource.


        :param action: The action of this ProjectTriggerResource.  # noqa: E501
        :type: TriggerActionResource
        """

        self._action = action

    @property
    def space_id(self):
        """Gets the space_id of this ProjectTriggerResource.  # noqa: E501


        :return: The space_id of this ProjectTriggerResource.  # noqa: E501
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this ProjectTriggerResource.


        :param space_id: The space_id of this ProjectTriggerResource.  # noqa: E501
        :type: str
        """

        self._space_id = space_id

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this ProjectTriggerResource.  # noqa: E501


        :return: The last_modified_on of this ProjectTriggerResource.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this ProjectTriggerResource.


        :param last_modified_on: The last_modified_on of this ProjectTriggerResource.  # noqa: E501
        :type: datetime
        """

        self._last_modified_on = last_modified_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this ProjectTriggerResource.  # noqa: E501


        :return: The last_modified_by of this ProjectTriggerResource.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this ProjectTriggerResource.


        :param last_modified_by: The last_modified_by of this ProjectTriggerResource.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def links(self):
        """Gets the links of this ProjectTriggerResource.  # noqa: E501


        :return: The links of this ProjectTriggerResource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ProjectTriggerResource.


        :param links: The links of this ProjectTriggerResource.  # noqa: E501
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
        if issubclass(ProjectTriggerResource, dict):
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
        if not isinstance(other, ProjectTriggerResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
