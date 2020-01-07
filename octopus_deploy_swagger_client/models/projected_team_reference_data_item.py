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


class ProjectedTeamReferenceDataItem(object):
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
        'is_directly_assigned': 'bool',
        'external_group_names': 'list[str]',
        'space_id': 'str',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'is_directly_assigned': 'IsDirectlyAssigned',
        'external_group_names': 'ExternalGroupNames',
        'space_id': 'SpaceId',
        'id': 'Id',
        'name': 'Name'
    }

    def __init__(self, is_directly_assigned=None, external_group_names=None, space_id=None, id=None, name=None):  # noqa: E501
        """ProjectedTeamReferenceDataItem - a model defined in Swagger"""  # noqa: E501

        self._is_directly_assigned = None
        self._external_group_names = None
        self._space_id = None
        self._id = None
        self._name = None
        self.discriminator = None

        if is_directly_assigned is not None:
            self.is_directly_assigned = is_directly_assigned
        if external_group_names is not None:
            self.external_group_names = external_group_names
        if space_id is not None:
            self.space_id = space_id
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def is_directly_assigned(self):
        """Gets the is_directly_assigned of this ProjectedTeamReferenceDataItem.  # noqa: E501


        :return: The is_directly_assigned of this ProjectedTeamReferenceDataItem.  # noqa: E501
        :rtype: bool
        """
        return self._is_directly_assigned

    @is_directly_assigned.setter
    def is_directly_assigned(self, is_directly_assigned):
        """Sets the is_directly_assigned of this ProjectedTeamReferenceDataItem.


        :param is_directly_assigned: The is_directly_assigned of this ProjectedTeamReferenceDataItem.  # noqa: E501
        :type: bool
        """

        self._is_directly_assigned = is_directly_assigned

    @property
    def external_group_names(self):
        """Gets the external_group_names of this ProjectedTeamReferenceDataItem.  # noqa: E501


        :return: The external_group_names of this ProjectedTeamReferenceDataItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._external_group_names

    @external_group_names.setter
    def external_group_names(self, external_group_names):
        """Sets the external_group_names of this ProjectedTeamReferenceDataItem.


        :param external_group_names: The external_group_names of this ProjectedTeamReferenceDataItem.  # noqa: E501
        :type: list[str]
        """

        self._external_group_names = external_group_names

    @property
    def space_id(self):
        """Gets the space_id of this ProjectedTeamReferenceDataItem.  # noqa: E501


        :return: The space_id of this ProjectedTeamReferenceDataItem.  # noqa: E501
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this ProjectedTeamReferenceDataItem.


        :param space_id: The space_id of this ProjectedTeamReferenceDataItem.  # noqa: E501
        :type: str
        """

        self._space_id = space_id

    @property
    def id(self):
        """Gets the id of this ProjectedTeamReferenceDataItem.  # noqa: E501


        :return: The id of this ProjectedTeamReferenceDataItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectedTeamReferenceDataItem.


        :param id: The id of this ProjectedTeamReferenceDataItem.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ProjectedTeamReferenceDataItem.  # noqa: E501


        :return: The name of this ProjectedTeamReferenceDataItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectedTeamReferenceDataItem.


        :param name: The name of this ProjectedTeamReferenceDataItem.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(ProjectedTeamReferenceDataItem, dict):
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
        if not isinstance(other, ProjectedTeamReferenceDataItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other