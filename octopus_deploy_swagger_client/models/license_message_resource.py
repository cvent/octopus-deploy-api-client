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


class LicenseMessageResource(object):
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
        'message': 'str',
        'disposition': 'str'
    }

    attribute_map = {
        'message': 'Message',
        'disposition': 'Disposition'
    }

    def __init__(self, message=None, disposition=None):  # noqa: E501
        """LicenseMessageResource - a model defined in Swagger"""  # noqa: E501

        self._message = None
        self._disposition = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if disposition is not None:
            self.disposition = disposition

    @property
    def message(self):
        """Gets the message of this LicenseMessageResource.  # noqa: E501


        :return: The message of this LicenseMessageResource.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this LicenseMessageResource.


        :param message: The message of this LicenseMessageResource.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def disposition(self):
        """Gets the disposition of this LicenseMessageResource.  # noqa: E501


        :return: The disposition of this LicenseMessageResource.  # noqa: E501
        :rtype: str
        """
        return self._disposition

    @disposition.setter
    def disposition(self, disposition):
        """Sets the disposition of this LicenseMessageResource.


        :param disposition: The disposition of this LicenseMessageResource.  # noqa: E501
        :type: str
        """
        allowed_values = ["Information", "Warning", "Error"]  # noqa: E501
        if disposition not in allowed_values:
            raise ValueError(
                "Invalid value for `disposition` ({0}), must be one of {1}"  # noqa: E501
                .format(disposition, allowed_values)
            )

        self._disposition = disposition

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
        if issubclass(LicenseMessageResource, dict):
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
        if not isinstance(other, LicenseMessageResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other