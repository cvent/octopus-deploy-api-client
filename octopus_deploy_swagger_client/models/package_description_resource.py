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


class PackageDescriptionResource(object):
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
        'links': 'dict(str, str)',
        'name': 'str',
        'latest_version': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'links': 'Links',
        'name': 'Name',
        'latest_version': 'LatestVersion',
        'description': 'Description'
    }

    def __init__(self, id=None, links=None, name=None, latest_version=None, description=None):  # noqa: E501
        """PackageDescriptionResource - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._links = None
        self._name = None
        self._latest_version = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if links is not None:
            self.links = links
        if name is not None:
            self.name = name
        if latest_version is not None:
            self.latest_version = latest_version
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this PackageDescriptionResource.  # noqa: E501


        :return: The id of this PackageDescriptionResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PackageDescriptionResource.


        :param id: The id of this PackageDescriptionResource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def links(self):
        """Gets the links of this PackageDescriptionResource.  # noqa: E501


        :return: The links of this PackageDescriptionResource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PackageDescriptionResource.


        :param links: The links of this PackageDescriptionResource.  # noqa: E501
        :type: dict(str, str)
        """

        self._links = links

    @property
    def name(self):
        """Gets the name of this PackageDescriptionResource.  # noqa: E501


        :return: The name of this PackageDescriptionResource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PackageDescriptionResource.


        :param name: The name of this PackageDescriptionResource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def latest_version(self):
        """Gets the latest_version of this PackageDescriptionResource.  # noqa: E501


        :return: The latest_version of this PackageDescriptionResource.  # noqa: E501
        :rtype: str
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        """Sets the latest_version of this PackageDescriptionResource.


        :param latest_version: The latest_version of this PackageDescriptionResource.  # noqa: E501
        :type: str
        """

        self._latest_version = latest_version

    @property
    def description(self):
        """Gets the description of this PackageDescriptionResource.  # noqa: E501


        :return: The description of this PackageDescriptionResource.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PackageDescriptionResource.


        :param description: The description of this PackageDescriptionResource.  # noqa: E501
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
        if issubclass(PackageDescriptionResource, dict):
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
        if not isinstance(other, PackageDescriptionResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other