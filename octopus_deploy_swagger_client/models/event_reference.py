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


class EventReference(object):
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
        'referenced_document_id': 'str',
        'start_index': 'int',
        'length': 'int'
    }

    attribute_map = {
        'referenced_document_id': 'ReferencedDocumentId',
        'start_index': 'StartIndex',
        'length': 'Length'
    }

    def __init__(self, referenced_document_id=None, start_index=None, length=None):  # noqa: E501
        """EventReference - a model defined in Swagger"""  # noqa: E501

        self._referenced_document_id = None
        self._start_index = None
        self._length = None
        self.discriminator = None

        if referenced_document_id is not None:
            self.referenced_document_id = referenced_document_id
        if start_index is not None:
            self.start_index = start_index
        if length is not None:
            self.length = length

    @property
    def referenced_document_id(self):
        """Gets the referenced_document_id of this EventReference.  # noqa: E501


        :return: The referenced_document_id of this EventReference.  # noqa: E501
        :rtype: str
        """
        return self._referenced_document_id

    @referenced_document_id.setter
    def referenced_document_id(self, referenced_document_id):
        """Sets the referenced_document_id of this EventReference.


        :param referenced_document_id: The referenced_document_id of this EventReference.  # noqa: E501
        :type: str
        """

        self._referenced_document_id = referenced_document_id

    @property
    def start_index(self):
        """Gets the start_index of this EventReference.  # noqa: E501


        :return: The start_index of this EventReference.  # noqa: E501
        :rtype: int
        """
        return self._start_index

    @start_index.setter
    def start_index(self, start_index):
        """Sets the start_index of this EventReference.


        :param start_index: The start_index of this EventReference.  # noqa: E501
        :type: int
        """

        self._start_index = start_index

    @property
    def length(self):
        """Gets the length of this EventReference.  # noqa: E501


        :return: The length of this EventReference.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this EventReference.


        :param length: The length of this EventReference.  # noqa: E501
        :type: int
        """

        self._length = length

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
        if issubclass(EventReference, dict):
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
        if not isinstance(other, EventReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
