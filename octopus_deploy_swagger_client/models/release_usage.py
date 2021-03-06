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

from octopus_deploy_swagger_client.models.release_usage_entry import ReleaseUsageEntry  # noqa: F401,E501


class ReleaseUsage(object):
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
        'project_name': 'str',
        'project_id': 'str',
        'releases': 'list[ReleaseUsageEntry]'
    }

    attribute_map = {
        'project_name': 'ProjectName',
        'project_id': 'ProjectId',
        'releases': 'Releases'
    }

    def __init__(self, project_name=None, project_id=None, releases=None):  # noqa: E501
        """ReleaseUsage - a model defined in Swagger"""  # noqa: E501

        self._project_name = None
        self._project_id = None
        self._releases = None
        self.discriminator = None

        if project_name is not None:
            self.project_name = project_name
        if project_id is not None:
            self.project_id = project_id
        if releases is not None:
            self.releases = releases

    @property
    def project_name(self):
        """Gets the project_name of this ReleaseUsage.  # noqa: E501


        :return: The project_name of this ReleaseUsage.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ReleaseUsage.


        :param project_name: The project_name of this ReleaseUsage.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def project_id(self):
        """Gets the project_id of this ReleaseUsage.  # noqa: E501


        :return: The project_id of this ReleaseUsage.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ReleaseUsage.


        :param project_id: The project_id of this ReleaseUsage.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def releases(self):
        """Gets the releases of this ReleaseUsage.  # noqa: E501


        :return: The releases of this ReleaseUsage.  # noqa: E501
        :rtype: list[ReleaseUsageEntry]
        """
        return self._releases

    @releases.setter
    def releases(self, releases):
        """Sets the releases of this ReleaseUsage.


        :param releases: The releases of this ReleaseUsage.  # noqa: E501
        :type: list[ReleaseUsageEntry]
        """

        self._releases = releases

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
        if issubclass(ReleaseUsage, dict):
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
        if not isinstance(other, ReleaseUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
