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

from octopus_deploy_swagger_client.models.library_variable_set_release_usage_entry import LibraryVariableSetReleaseUsageEntry  # noqa: F401,E501


class LibraryVariableSetProjectUsage(object):
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
        'project_slug': 'str',
        'project_name': 'str',
        'project_id': 'str',
        'releases': 'list[LibraryVariableSetReleaseUsageEntry]',
        'is_currently_being_used_in_project': 'bool'
    }

    attribute_map = {
        'project_slug': 'ProjectSlug',
        'project_name': 'ProjectName',
        'project_id': 'ProjectId',
        'releases': 'Releases',
        'is_currently_being_used_in_project': 'IsCurrentlyBeingUsedInProject'
    }

    def __init__(self, project_slug=None, project_name=None, project_id=None, releases=None, is_currently_being_used_in_project=None):  # noqa: E501
        """LibraryVariableSetProjectUsage - a model defined in Swagger"""  # noqa: E501

        self._project_slug = None
        self._project_name = None
        self._project_id = None
        self._releases = None
        self._is_currently_being_used_in_project = None
        self.discriminator = None

        if project_slug is not None:
            self.project_slug = project_slug
        if project_name is not None:
            self.project_name = project_name
        if project_id is not None:
            self.project_id = project_id
        if releases is not None:
            self.releases = releases
        if is_currently_being_used_in_project is not None:
            self.is_currently_being_used_in_project = is_currently_being_used_in_project

    @property
    def project_slug(self):
        """Gets the project_slug of this LibraryVariableSetProjectUsage.  # noqa: E501


        :return: The project_slug of this LibraryVariableSetProjectUsage.  # noqa: E501
        :rtype: str
        """
        return self._project_slug

    @project_slug.setter
    def project_slug(self, project_slug):
        """Sets the project_slug of this LibraryVariableSetProjectUsage.


        :param project_slug: The project_slug of this LibraryVariableSetProjectUsage.  # noqa: E501
        :type: str
        """

        self._project_slug = project_slug

    @property
    def project_name(self):
        """Gets the project_name of this LibraryVariableSetProjectUsage.  # noqa: E501


        :return: The project_name of this LibraryVariableSetProjectUsage.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this LibraryVariableSetProjectUsage.


        :param project_name: The project_name of this LibraryVariableSetProjectUsage.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def project_id(self):
        """Gets the project_id of this LibraryVariableSetProjectUsage.  # noqa: E501


        :return: The project_id of this LibraryVariableSetProjectUsage.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this LibraryVariableSetProjectUsage.


        :param project_id: The project_id of this LibraryVariableSetProjectUsage.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def releases(self):
        """Gets the releases of this LibraryVariableSetProjectUsage.  # noqa: E501


        :return: The releases of this LibraryVariableSetProjectUsage.  # noqa: E501
        :rtype: list[LibraryVariableSetReleaseUsageEntry]
        """
        return self._releases

    @releases.setter
    def releases(self, releases):
        """Sets the releases of this LibraryVariableSetProjectUsage.


        :param releases: The releases of this LibraryVariableSetProjectUsage.  # noqa: E501
        :type: list[LibraryVariableSetReleaseUsageEntry]
        """

        self._releases = releases

    @property
    def is_currently_being_used_in_project(self):
        """Gets the is_currently_being_used_in_project of this LibraryVariableSetProjectUsage.  # noqa: E501


        :return: The is_currently_being_used_in_project of this LibraryVariableSetProjectUsage.  # noqa: E501
        :rtype: bool
        """
        return self._is_currently_being_used_in_project

    @is_currently_being_used_in_project.setter
    def is_currently_being_used_in_project(self, is_currently_being_used_in_project):
        """Sets the is_currently_being_used_in_project of this LibraryVariableSetProjectUsage.


        :param is_currently_being_used_in_project: The is_currently_being_used_in_project of this LibraryVariableSetProjectUsage.  # noqa: E501
        :type: bool
        """

        self._is_currently_being_used_in_project = is_currently_being_used_in_project

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
        if issubclass(LibraryVariableSetProjectUsage, dict):
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
        if not isinstance(other, LibraryVariableSetProjectUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
