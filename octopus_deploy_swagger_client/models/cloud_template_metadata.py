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

from octopus_deploy_swagger_client.models.metadata import Metadata  # noqa: F401,E501


class CloudTemplateMetadata(object):
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
        'metadata': 'Metadata',
        'values': 'object'
    }

    attribute_map = {
        'metadata': 'Metadata',
        'values': 'Values'
    }

    def __init__(self, metadata=None, values=None):  # noqa: E501
        """CloudTemplateMetadata - a model defined in Swagger"""  # noqa: E501

        self._metadata = None
        self._values = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        if values is not None:
            self.values = values

    @property
    def metadata(self):
        """Gets the metadata of this CloudTemplateMetadata.  # noqa: E501


        :return: The metadata of this CloudTemplateMetadata.  # noqa: E501
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CloudTemplateMetadata.


        :param metadata: The metadata of this CloudTemplateMetadata.  # noqa: E501
        :type: Metadata
        """

        self._metadata = metadata

    @property
    def values(self):
        """Gets the values of this CloudTemplateMetadata.  # noqa: E501


        :return: The values of this CloudTemplateMetadata.  # noqa: E501
        :rtype: object
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this CloudTemplateMetadata.


        :param values: The values of this CloudTemplateMetadata.  # noqa: E501
        :type: object
        """

        self._values = values

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
        if issubclass(CloudTemplateMetadata, dict):
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
        if not isinstance(other, CloudTemplateMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other