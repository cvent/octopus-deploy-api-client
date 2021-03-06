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


class AuthenticationProviderThatSupportsGroups(object):
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
        'is_role_based': 'bool',
        'supports_group_lookup': 'bool',
        'lookup_uri': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'is_role_based': 'IsRoleBased',
        'supports_group_lookup': 'SupportsGroupLookup',
        'lookup_uri': 'LookupUri'
    }

    def __init__(self, id=None, name=None, is_role_based=None, supports_group_lookup=None, lookup_uri=None):  # noqa: E501
        """AuthenticationProviderThatSupportsGroups - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._is_role_based = None
        self._supports_group_lookup = None
        self._lookup_uri = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if is_role_based is not None:
            self.is_role_based = is_role_based
        if supports_group_lookup is not None:
            self.supports_group_lookup = supports_group_lookup
        if lookup_uri is not None:
            self.lookup_uri = lookup_uri

    @property
    def id(self):
        """Gets the id of this AuthenticationProviderThatSupportsGroups.  # noqa: E501


        :return: The id of this AuthenticationProviderThatSupportsGroups.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuthenticationProviderThatSupportsGroups.


        :param id: The id of this AuthenticationProviderThatSupportsGroups.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this AuthenticationProviderThatSupportsGroups.  # noqa: E501


        :return: The name of this AuthenticationProviderThatSupportsGroups.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AuthenticationProviderThatSupportsGroups.


        :param name: The name of this AuthenticationProviderThatSupportsGroups.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def is_role_based(self):
        """Gets the is_role_based of this AuthenticationProviderThatSupportsGroups.  # noqa: E501


        :return: The is_role_based of this AuthenticationProviderThatSupportsGroups.  # noqa: E501
        :rtype: bool
        """
        return self._is_role_based

    @is_role_based.setter
    def is_role_based(self, is_role_based):
        """Sets the is_role_based of this AuthenticationProviderThatSupportsGroups.


        :param is_role_based: The is_role_based of this AuthenticationProviderThatSupportsGroups.  # noqa: E501
        :type: bool
        """

        self._is_role_based = is_role_based

    @property
    def supports_group_lookup(self):
        """Gets the supports_group_lookup of this AuthenticationProviderThatSupportsGroups.  # noqa: E501


        :return: The supports_group_lookup of this AuthenticationProviderThatSupportsGroups.  # noqa: E501
        :rtype: bool
        """
        return self._supports_group_lookup

    @supports_group_lookup.setter
    def supports_group_lookup(self, supports_group_lookup):
        """Sets the supports_group_lookup of this AuthenticationProviderThatSupportsGroups.


        :param supports_group_lookup: The supports_group_lookup of this AuthenticationProviderThatSupportsGroups.  # noqa: E501
        :type: bool
        """

        self._supports_group_lookup = supports_group_lookup

    @property
    def lookup_uri(self):
        """Gets the lookup_uri of this AuthenticationProviderThatSupportsGroups.  # noqa: E501


        :return: The lookup_uri of this AuthenticationProviderThatSupportsGroups.  # noqa: E501
        :rtype: str
        """
        return self._lookup_uri

    @lookup_uri.setter
    def lookup_uri(self, lookup_uri):
        """Sets the lookup_uri of this AuthenticationProviderThatSupportsGroups.


        :param lookup_uri: The lookup_uri of this AuthenticationProviderThatSupportsGroups.  # noqa: E501
        :type: str
        """

        self._lookup_uri = lookup_uri

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
        if issubclass(AuthenticationProviderThatSupportsGroups, dict):
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
        if not isinstance(other, AuthenticationProviderThatSupportsGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
