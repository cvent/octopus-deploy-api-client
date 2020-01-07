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


class PermissionDescription(object):
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
        'supported_restrictions': 'list[str]',
        'can_apply_at_system_level': 'bool',
        'can_apply_at_space_level': 'bool',
        'description': 'str'
    }

    attribute_map = {
        'supported_restrictions': 'SupportedRestrictions',
        'can_apply_at_system_level': 'CanApplyAtSystemLevel',
        'can_apply_at_space_level': 'CanApplyAtSpaceLevel',
        'description': 'Description'
    }

    def __init__(self, supported_restrictions=None, can_apply_at_system_level=None, can_apply_at_space_level=None, description=None):  # noqa: E501
        """PermissionDescription - a model defined in Swagger"""  # noqa: E501

        self._supported_restrictions = None
        self._can_apply_at_system_level = None
        self._can_apply_at_space_level = None
        self._description = None
        self.discriminator = None

        if supported_restrictions is not None:
            self.supported_restrictions = supported_restrictions
        if can_apply_at_system_level is not None:
            self.can_apply_at_system_level = can_apply_at_system_level
        if can_apply_at_space_level is not None:
            self.can_apply_at_space_level = can_apply_at_space_level
        if description is not None:
            self.description = description

    @property
    def supported_restrictions(self):
        """Gets the supported_restrictions of this PermissionDescription.  # noqa: E501


        :return: The supported_restrictions of this PermissionDescription.  # noqa: E501
        :rtype: list[str]
        """
        return self._supported_restrictions

    @supported_restrictions.setter
    def supported_restrictions(self, supported_restrictions):
        """Sets the supported_restrictions of this PermissionDescription.


        :param supported_restrictions: The supported_restrictions of this PermissionDescription.  # noqa: E501
        :type: list[str]
        """

        self._supported_restrictions = supported_restrictions

    @property
    def can_apply_at_system_level(self):
        """Gets the can_apply_at_system_level of this PermissionDescription.  # noqa: E501


        :return: The can_apply_at_system_level of this PermissionDescription.  # noqa: E501
        :rtype: bool
        """
        return self._can_apply_at_system_level

    @can_apply_at_system_level.setter
    def can_apply_at_system_level(self, can_apply_at_system_level):
        """Sets the can_apply_at_system_level of this PermissionDescription.


        :param can_apply_at_system_level: The can_apply_at_system_level of this PermissionDescription.  # noqa: E501
        :type: bool
        """

        self._can_apply_at_system_level = can_apply_at_system_level

    @property
    def can_apply_at_space_level(self):
        """Gets the can_apply_at_space_level of this PermissionDescription.  # noqa: E501


        :return: The can_apply_at_space_level of this PermissionDescription.  # noqa: E501
        :rtype: bool
        """
        return self._can_apply_at_space_level

    @can_apply_at_space_level.setter
    def can_apply_at_space_level(self, can_apply_at_space_level):
        """Sets the can_apply_at_space_level of this PermissionDescription.


        :param can_apply_at_space_level: The can_apply_at_space_level of this PermissionDescription.  # noqa: E501
        :type: bool
        """

        self._can_apply_at_space_level = can_apply_at_space_level

    @property
    def description(self):
        """Gets the description of this PermissionDescription.  # noqa: E501


        :return: The description of this PermissionDescription.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PermissionDescription.


        :param description: The description of this PermissionDescription.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(PermissionDescription, dict):
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
        if not isinstance(other, PermissionDescription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other