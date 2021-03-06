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

from octopus_deploy_swagger_client.models.package_notes_result import PackageNotesResult  # noqa: F401,E501


class PackageNote(object):
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
        'package_id': 'str',
        'feed_id': 'str',
        'version': 'str',
        'notes': 'PackageNotesResult'
    }

    attribute_map = {
        'package_id': 'PackageId',
        'feed_id': 'FeedId',
        'version': 'Version',
        'notes': 'Notes'
    }

    def __init__(self, package_id=None, feed_id=None, version=None, notes=None):  # noqa: E501
        """PackageNote - a model defined in Swagger"""  # noqa: E501

        self._package_id = None
        self._feed_id = None
        self._version = None
        self._notes = None
        self.discriminator = None

        if package_id is not None:
            self.package_id = package_id
        if feed_id is not None:
            self.feed_id = feed_id
        if version is not None:
            self.version = version
        if notes is not None:
            self.notes = notes

    @property
    def package_id(self):
        """Gets the package_id of this PackageNote.  # noqa: E501


        :return: The package_id of this PackageNote.  # noqa: E501
        :rtype: str
        """
        return self._package_id

    @package_id.setter
    def package_id(self, package_id):
        """Sets the package_id of this PackageNote.


        :param package_id: The package_id of this PackageNote.  # noqa: E501
        :type: str
        """

        self._package_id = package_id

    @property
    def feed_id(self):
        """Gets the feed_id of this PackageNote.  # noqa: E501


        :return: The feed_id of this PackageNote.  # noqa: E501
        :rtype: str
        """
        return self._feed_id

    @feed_id.setter
    def feed_id(self, feed_id):
        """Sets the feed_id of this PackageNote.


        :param feed_id: The feed_id of this PackageNote.  # noqa: E501
        :type: str
        """

        self._feed_id = feed_id

    @property
    def version(self):
        """Gets the version of this PackageNote.  # noqa: E501


        :return: The version of this PackageNote.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PackageNote.


        :param version: The version of this PackageNote.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def notes(self):
        """Gets the notes of this PackageNote.  # noqa: E501


        :return: The notes of this PackageNote.  # noqa: E501
        :rtype: PackageNotesResult
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this PackageNote.


        :param notes: The notes of this PackageNote.  # noqa: E501
        :type: PackageNotesResult
        """

        self._notes = notes

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
        if issubclass(PackageNote, dict):
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
        if not isinstance(other, PackageNote):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
