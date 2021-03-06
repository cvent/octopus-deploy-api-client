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

from octopus_deploy_swagger_client.models.commit_details import CommitDetails  # noqa: F401,E501
from octopus_deploy_swagger_client.models.work_item_link import WorkItemLink  # noqa: F401,E501


class ReleasePackageMetadataResource(object):
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
        'version': 'str',
        'build_environment': 'str',
        'build_number': 'str',
        'build_url': 'str',
        'vcs_type': 'str',
        'vcs_root': 'str',
        'vcs_commit_number': 'str',
        'vcs_commit_url': 'str',
        'issue_tracker_name': 'str',
        'work_items': 'list[WorkItemLink]',
        'commits': 'list[CommitDetails]'
    }

    attribute_map = {
        'package_id': 'PackageId',
        'version': 'Version',
        'build_environment': 'BuildEnvironment',
        'build_number': 'BuildNumber',
        'build_url': 'BuildUrl',
        'vcs_type': 'VcsType',
        'vcs_root': 'VcsRoot',
        'vcs_commit_number': 'VcsCommitNumber',
        'vcs_commit_url': 'VcsCommitUrl',
        'issue_tracker_name': 'IssueTrackerName',
        'work_items': 'WorkItems',
        'commits': 'Commits'
    }

    def __init__(self, package_id=None, version=None, build_environment=None, build_number=None, build_url=None, vcs_type=None, vcs_root=None, vcs_commit_number=None, vcs_commit_url=None, issue_tracker_name=None, work_items=None, commits=None):  # noqa: E501
        """ReleasePackageMetadataResource - a model defined in Swagger"""  # noqa: E501

        self._package_id = None
        self._version = None
        self._build_environment = None
        self._build_number = None
        self._build_url = None
        self._vcs_type = None
        self._vcs_root = None
        self._vcs_commit_number = None
        self._vcs_commit_url = None
        self._issue_tracker_name = None
        self._work_items = None
        self._commits = None
        self.discriminator = None

        if package_id is not None:
            self.package_id = package_id
        if version is not None:
            self.version = version
        if build_environment is not None:
            self.build_environment = build_environment
        if build_number is not None:
            self.build_number = build_number
        if build_url is not None:
            self.build_url = build_url
        if vcs_type is not None:
            self.vcs_type = vcs_type
        if vcs_root is not None:
            self.vcs_root = vcs_root
        if vcs_commit_number is not None:
            self.vcs_commit_number = vcs_commit_number
        if vcs_commit_url is not None:
            self.vcs_commit_url = vcs_commit_url
        if issue_tracker_name is not None:
            self.issue_tracker_name = issue_tracker_name
        if work_items is not None:
            self.work_items = work_items
        if commits is not None:
            self.commits = commits

    @property
    def package_id(self):
        """Gets the package_id of this ReleasePackageMetadataResource.  # noqa: E501


        :return: The package_id of this ReleasePackageMetadataResource.  # noqa: E501
        :rtype: str
        """
        return self._package_id

    @package_id.setter
    def package_id(self, package_id):
        """Sets the package_id of this ReleasePackageMetadataResource.


        :param package_id: The package_id of this ReleasePackageMetadataResource.  # noqa: E501
        :type: str
        """

        self._package_id = package_id

    @property
    def version(self):
        """Gets the version of this ReleasePackageMetadataResource.  # noqa: E501


        :return: The version of this ReleasePackageMetadataResource.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ReleasePackageMetadataResource.


        :param version: The version of this ReleasePackageMetadataResource.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def build_environment(self):
        """Gets the build_environment of this ReleasePackageMetadataResource.  # noqa: E501


        :return: The build_environment of this ReleasePackageMetadataResource.  # noqa: E501
        :rtype: str
        """
        return self._build_environment

    @build_environment.setter
    def build_environment(self, build_environment):
        """Sets the build_environment of this ReleasePackageMetadataResource.


        :param build_environment: The build_environment of this ReleasePackageMetadataResource.  # noqa: E501
        :type: str
        """

        self._build_environment = build_environment

    @property
    def build_number(self):
        """Gets the build_number of this ReleasePackageMetadataResource.  # noqa: E501


        :return: The build_number of this ReleasePackageMetadataResource.  # noqa: E501
        :rtype: str
        """
        return self._build_number

    @build_number.setter
    def build_number(self, build_number):
        """Sets the build_number of this ReleasePackageMetadataResource.


        :param build_number: The build_number of this ReleasePackageMetadataResource.  # noqa: E501
        :type: str
        """

        self._build_number = build_number

    @property
    def build_url(self):
        """Gets the build_url of this ReleasePackageMetadataResource.  # noqa: E501


        :return: The build_url of this ReleasePackageMetadataResource.  # noqa: E501
        :rtype: str
        """
        return self._build_url

    @build_url.setter
    def build_url(self, build_url):
        """Sets the build_url of this ReleasePackageMetadataResource.


        :param build_url: The build_url of this ReleasePackageMetadataResource.  # noqa: E501
        :type: str
        """

        self._build_url = build_url

    @property
    def vcs_type(self):
        """Gets the vcs_type of this ReleasePackageMetadataResource.  # noqa: E501


        :return: The vcs_type of this ReleasePackageMetadataResource.  # noqa: E501
        :rtype: str
        """
        return self._vcs_type

    @vcs_type.setter
    def vcs_type(self, vcs_type):
        """Sets the vcs_type of this ReleasePackageMetadataResource.


        :param vcs_type: The vcs_type of this ReleasePackageMetadataResource.  # noqa: E501
        :type: str
        """

        self._vcs_type = vcs_type

    @property
    def vcs_root(self):
        """Gets the vcs_root of this ReleasePackageMetadataResource.  # noqa: E501


        :return: The vcs_root of this ReleasePackageMetadataResource.  # noqa: E501
        :rtype: str
        """
        return self._vcs_root

    @vcs_root.setter
    def vcs_root(self, vcs_root):
        """Sets the vcs_root of this ReleasePackageMetadataResource.


        :param vcs_root: The vcs_root of this ReleasePackageMetadataResource.  # noqa: E501
        :type: str
        """

        self._vcs_root = vcs_root

    @property
    def vcs_commit_number(self):
        """Gets the vcs_commit_number of this ReleasePackageMetadataResource.  # noqa: E501


        :return: The vcs_commit_number of this ReleasePackageMetadataResource.  # noqa: E501
        :rtype: str
        """
        return self._vcs_commit_number

    @vcs_commit_number.setter
    def vcs_commit_number(self, vcs_commit_number):
        """Sets the vcs_commit_number of this ReleasePackageMetadataResource.


        :param vcs_commit_number: The vcs_commit_number of this ReleasePackageMetadataResource.  # noqa: E501
        :type: str
        """

        self._vcs_commit_number = vcs_commit_number

    @property
    def vcs_commit_url(self):
        """Gets the vcs_commit_url of this ReleasePackageMetadataResource.  # noqa: E501


        :return: The vcs_commit_url of this ReleasePackageMetadataResource.  # noqa: E501
        :rtype: str
        """
        return self._vcs_commit_url

    @vcs_commit_url.setter
    def vcs_commit_url(self, vcs_commit_url):
        """Sets the vcs_commit_url of this ReleasePackageMetadataResource.


        :param vcs_commit_url: The vcs_commit_url of this ReleasePackageMetadataResource.  # noqa: E501
        :type: str
        """

        self._vcs_commit_url = vcs_commit_url

    @property
    def issue_tracker_name(self):
        """Gets the issue_tracker_name of this ReleasePackageMetadataResource.  # noqa: E501


        :return: The issue_tracker_name of this ReleasePackageMetadataResource.  # noqa: E501
        :rtype: str
        """
        return self._issue_tracker_name

    @issue_tracker_name.setter
    def issue_tracker_name(self, issue_tracker_name):
        """Sets the issue_tracker_name of this ReleasePackageMetadataResource.


        :param issue_tracker_name: The issue_tracker_name of this ReleasePackageMetadataResource.  # noqa: E501
        :type: str
        """

        self._issue_tracker_name = issue_tracker_name

    @property
    def work_items(self):
        """Gets the work_items of this ReleasePackageMetadataResource.  # noqa: E501


        :return: The work_items of this ReleasePackageMetadataResource.  # noqa: E501
        :rtype: list[WorkItemLink]
        """
        return self._work_items

    @work_items.setter
    def work_items(self, work_items):
        """Sets the work_items of this ReleasePackageMetadataResource.


        :param work_items: The work_items of this ReleasePackageMetadataResource.  # noqa: E501
        :type: list[WorkItemLink]
        """

        self._work_items = work_items

    @property
    def commits(self):
        """Gets the commits of this ReleasePackageMetadataResource.  # noqa: E501


        :return: The commits of this ReleasePackageMetadataResource.  # noqa: E501
        :rtype: list[CommitDetails]
        """
        return self._commits

    @commits.setter
    def commits(self, commits):
        """Sets the commits of this ReleasePackageMetadataResource.


        :param commits: The commits of this ReleasePackageMetadataResource.  # noqa: E501
        :type: list[CommitDetails]
        """

        self._commits = commits

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
        if issubclass(ReleasePackageMetadataResource, dict):
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
        if not isinstance(other, ReleasePackageMetadataResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
