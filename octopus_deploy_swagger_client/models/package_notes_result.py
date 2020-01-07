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


class PackageNotesResult(object):
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
        'succeeded': 'bool',
        'notes': 'str',
        'failure_reason': 'str',
        'display_message': 'str'
    }

    attribute_map = {
        'succeeded': 'Succeeded',
        'notes': 'Notes',
        'failure_reason': 'FailureReason',
        'display_message': 'DisplayMessage'
    }

    def __init__(self, succeeded=None, notes=None, failure_reason=None, display_message=None):  # noqa: E501
        """PackageNotesResult - a model defined in Swagger"""  # noqa: E501

        self._succeeded = None
        self._notes = None
        self._failure_reason = None
        self._display_message = None
        self.discriminator = None

        if succeeded is not None:
            self.succeeded = succeeded
        if notes is not None:
            self.notes = notes
        if failure_reason is not None:
            self.failure_reason = failure_reason
        if display_message is not None:
            self.display_message = display_message

    @property
    def succeeded(self):
        """Gets the succeeded of this PackageNotesResult.  # noqa: E501


        :return: The succeeded of this PackageNotesResult.  # noqa: E501
        :rtype: bool
        """
        return self._succeeded

    @succeeded.setter
    def succeeded(self, succeeded):
        """Sets the succeeded of this PackageNotesResult.


        :param succeeded: The succeeded of this PackageNotesResult.  # noqa: E501
        :type: bool
        """

        self._succeeded = succeeded

    @property
    def notes(self):
        """Gets the notes of this PackageNotesResult.  # noqa: E501


        :return: The notes of this PackageNotesResult.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this PackageNotesResult.


        :param notes: The notes of this PackageNotesResult.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def failure_reason(self):
        """Gets the failure_reason of this PackageNotesResult.  # noqa: E501


        :return: The failure_reason of this PackageNotesResult.  # noqa: E501
        :rtype: str
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """Sets the failure_reason of this PackageNotesResult.


        :param failure_reason: The failure_reason of this PackageNotesResult.  # noqa: E501
        :type: str
        """

        self._failure_reason = failure_reason

    @property
    def display_message(self):
        """Gets the display_message of this PackageNotesResult.  # noqa: E501


        :return: The display_message of this PackageNotesResult.  # noqa: E501
        :rtype: str
        """
        return self._display_message

    @display_message.setter
    def display_message(self, display_message):
        """Sets the display_message of this PackageNotesResult.


        :param display_message: The display_message of this PackageNotesResult.  # noqa: E501
        :type: str
        """

        self._display_message = display_message

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
        if issubclass(PackageNotesResult, dict):
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
        if not isinstance(other, PackageNotesResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
