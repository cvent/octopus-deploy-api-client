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

from octopus_deploy_swagger_client.models.sensitive_value import SensitiveValue  # noqa: F401,E501


class ProxyResource(object):
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
        'host': 'str',
        'port': 'int',
        'proxy_type': 'str',
        'username': 'str',
        'password': 'SensitiveValue',
        'space_id': 'str',
        'last_modified_on': 'datetime',
        'last_modified_by': 'str',
        'links': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'host': 'Host',
        'port': 'Port',
        'proxy_type': 'ProxyType',
        'username': 'Username',
        'password': 'Password',
        'space_id': 'SpaceId',
        'last_modified_on': 'LastModifiedOn',
        'last_modified_by': 'LastModifiedBy',
        'links': 'Links'
    }

    def __init__(self, id=None, name=None, host=None, port=None, proxy_type=None, username=None, password=None, space_id=None, last_modified_on=None, last_modified_by=None, links=None):  # noqa: E501
        """ProxyResource - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._host = None
        self._port = None
        self._proxy_type = None
        self._username = None
        self._password = None
        self._space_id = None
        self._last_modified_on = None
        self._last_modified_by = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if proxy_type is not None:
            self.proxy_type = proxy_type
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
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
        """Gets the id of this ProxyResource.  # noqa: E501


        :return: The id of this ProxyResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProxyResource.


        :param id: The id of this ProxyResource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ProxyResource.  # noqa: E501


        :return: The name of this ProxyResource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProxyResource.


        :param name: The name of this ProxyResource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def host(self):
        """Gets the host of this ProxyResource.  # noqa: E501


        :return: The host of this ProxyResource.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this ProxyResource.


        :param host: The host of this ProxyResource.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def port(self):
        """Gets the port of this ProxyResource.  # noqa: E501


        :return: The port of this ProxyResource.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ProxyResource.


        :param port: The port of this ProxyResource.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def proxy_type(self):
        """Gets the proxy_type of this ProxyResource.  # noqa: E501


        :return: The proxy_type of this ProxyResource.  # noqa: E501
        :rtype: str
        """
        return self._proxy_type

    @proxy_type.setter
    def proxy_type(self, proxy_type):
        """Sets the proxy_type of this ProxyResource.


        :param proxy_type: The proxy_type of this ProxyResource.  # noqa: E501
        :type: str
        """

        self._proxy_type = proxy_type

    @property
    def username(self):
        """Gets the username of this ProxyResource.  # noqa: E501


        :return: The username of this ProxyResource.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ProxyResource.


        :param username: The username of this ProxyResource.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this ProxyResource.  # noqa: E501


        :return: The password of this ProxyResource.  # noqa: E501
        :rtype: SensitiveValue
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ProxyResource.


        :param password: The password of this ProxyResource.  # noqa: E501
        :type: SensitiveValue
        """

        self._password = password

    @property
    def space_id(self):
        """Gets the space_id of this ProxyResource.  # noqa: E501


        :return: The space_id of this ProxyResource.  # noqa: E501
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this ProxyResource.


        :param space_id: The space_id of this ProxyResource.  # noqa: E501
        :type: str
        """

        self._space_id = space_id

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this ProxyResource.  # noqa: E501


        :return: The last_modified_on of this ProxyResource.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this ProxyResource.


        :param last_modified_on: The last_modified_on of this ProxyResource.  # noqa: E501
        :type: datetime
        """

        self._last_modified_on = last_modified_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this ProxyResource.  # noqa: E501


        :return: The last_modified_by of this ProxyResource.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this ProxyResource.


        :param last_modified_by: The last_modified_by of this ProxyResource.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def links(self):
        """Gets the links of this ProxyResource.  # noqa: E501


        :return: The links of this ProxyResource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ProxyResource.


        :param links: The links of this ProxyResource.  # noqa: E501
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
        if issubclass(ProxyResource, dict):
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
        if not isinstance(other, ProxyResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
