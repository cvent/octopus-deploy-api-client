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


class ServerConfigurationResource(object):
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
        'server_uri': 'str',
        'last_modified_on': 'datetime',
        'last_modified_by': 'str',
        'links': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'Id',
        'server_uri': 'ServerUri',
        'last_modified_on': 'LastModifiedOn',
        'last_modified_by': 'LastModifiedBy',
        'links': 'Links'
    }

    def __init__(self, id=None, server_uri=None, last_modified_on=None, last_modified_by=None, links=None):  # noqa: E501
        """ServerConfigurationResource - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._server_uri = None
        self._last_modified_on = None
        self._last_modified_by = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if server_uri is not None:
            self.server_uri = server_uri
        if last_modified_on is not None:
            self.last_modified_on = last_modified_on
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this ServerConfigurationResource.  # noqa: E501


        :return: The id of this ServerConfigurationResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ServerConfigurationResource.


        :param id: The id of this ServerConfigurationResource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def server_uri(self):
        """Gets the server_uri of this ServerConfigurationResource.  # noqa: E501


        :return: The server_uri of this ServerConfigurationResource.  # noqa: E501
        :rtype: str
        """
        return self._server_uri

    @server_uri.setter
    def server_uri(self, server_uri):
        """Sets the server_uri of this ServerConfigurationResource.


        :param server_uri: The server_uri of this ServerConfigurationResource.  # noqa: E501
        :type: str
        """

        self._server_uri = server_uri

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this ServerConfigurationResource.  # noqa: E501


        :return: The last_modified_on of this ServerConfigurationResource.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this ServerConfigurationResource.


        :param last_modified_on: The last_modified_on of this ServerConfigurationResource.  # noqa: E501
        :type: datetime
        """

        self._last_modified_on = last_modified_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this ServerConfigurationResource.  # noqa: E501


        :return: The last_modified_by of this ServerConfigurationResource.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this ServerConfigurationResource.


        :param last_modified_by: The last_modified_by of this ServerConfigurationResource.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def links(self):
        """Gets the links of this ServerConfigurationResource.  # noqa: E501


        :return: The links of this ServerConfigurationResource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ServerConfigurationResource.


        :param links: The links of this ServerConfigurationResource.  # noqa: E501
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
        if issubclass(ServerConfigurationResource, dict):
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
        if not isinstance(other, ServerConfigurationResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
