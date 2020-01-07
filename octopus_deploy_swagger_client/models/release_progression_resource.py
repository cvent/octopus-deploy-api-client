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

from octopus_deploy_swagger_client.models.channel_resource import ChannelResource  # noqa: F401,E501
from octopus_deploy_swagger_client.models.dashboard_item_resource import DashboardItemResource  # noqa: F401,E501
from octopus_deploy_swagger_client.models.release_resource import ReleaseResource  # noqa: F401,E501
from octopus_deploy_swagger_client.models.retention_period import RetentionPeriod  # noqa: F401,E501


class ReleaseProgressionResource(object):
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
        'release': 'ReleaseResource',
        'channel': 'ChannelResource',
        'deployments': 'dict(str, list[DashboardItemResource])',
        'next_deployments': 'list[str]',
        'has_unresolved_defect': 'bool',
        'release_retention_period': 'RetentionPeriod',
        'tentacle_retention_period': 'RetentionPeriod'
    }

    attribute_map = {
        'release': 'Release',
        'channel': 'Channel',
        'deployments': 'Deployments',
        'next_deployments': 'NextDeployments',
        'has_unresolved_defect': 'HasUnresolvedDefect',
        'release_retention_period': 'ReleaseRetentionPeriod',
        'tentacle_retention_period': 'TentacleRetentionPeriod'
    }

    def __init__(self, release=None, channel=None, deployments=None, next_deployments=None, has_unresolved_defect=None, release_retention_period=None, tentacle_retention_period=None):  # noqa: E501
        """ReleaseProgressionResource - a model defined in Swagger"""  # noqa: E501

        self._release = None
        self._channel = None
        self._deployments = None
        self._next_deployments = None
        self._has_unresolved_defect = None
        self._release_retention_period = None
        self._tentacle_retention_period = None
        self.discriminator = None

        if release is not None:
            self.release = release
        if channel is not None:
            self.channel = channel
        if deployments is not None:
            self.deployments = deployments
        if next_deployments is not None:
            self.next_deployments = next_deployments
        if has_unresolved_defect is not None:
            self.has_unresolved_defect = has_unresolved_defect
        if release_retention_period is not None:
            self.release_retention_period = release_retention_period
        if tentacle_retention_period is not None:
            self.tentacle_retention_period = tentacle_retention_period

    @property
    def release(self):
        """Gets the release of this ReleaseProgressionResource.  # noqa: E501


        :return: The release of this ReleaseProgressionResource.  # noqa: E501
        :rtype: ReleaseResource
        """
        return self._release

    @release.setter
    def release(self, release):
        """Sets the release of this ReleaseProgressionResource.


        :param release: The release of this ReleaseProgressionResource.  # noqa: E501
        :type: ReleaseResource
        """

        self._release = release

    @property
    def channel(self):
        """Gets the channel of this ReleaseProgressionResource.  # noqa: E501


        :return: The channel of this ReleaseProgressionResource.  # noqa: E501
        :rtype: ChannelResource
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this ReleaseProgressionResource.


        :param channel: The channel of this ReleaseProgressionResource.  # noqa: E501
        :type: ChannelResource
        """

        self._channel = channel

    @property
    def deployments(self):
        """Gets the deployments of this ReleaseProgressionResource.  # noqa: E501


        :return: The deployments of this ReleaseProgressionResource.  # noqa: E501
        :rtype: dict(str, list[DashboardItemResource])
        """
        return self._deployments

    @deployments.setter
    def deployments(self, deployments):
        """Sets the deployments of this ReleaseProgressionResource.


        :param deployments: The deployments of this ReleaseProgressionResource.  # noqa: E501
        :type: dict(str, list[DashboardItemResource])
        """

        self._deployments = deployments

    @property
    def next_deployments(self):
        """Gets the next_deployments of this ReleaseProgressionResource.  # noqa: E501


        :return: The next_deployments of this ReleaseProgressionResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._next_deployments

    @next_deployments.setter
    def next_deployments(self, next_deployments):
        """Sets the next_deployments of this ReleaseProgressionResource.


        :param next_deployments: The next_deployments of this ReleaseProgressionResource.  # noqa: E501
        :type: list[str]
        """

        self._next_deployments = next_deployments

    @property
    def has_unresolved_defect(self):
        """Gets the has_unresolved_defect of this ReleaseProgressionResource.  # noqa: E501


        :return: The has_unresolved_defect of this ReleaseProgressionResource.  # noqa: E501
        :rtype: bool
        """
        return self._has_unresolved_defect

    @has_unresolved_defect.setter
    def has_unresolved_defect(self, has_unresolved_defect):
        """Sets the has_unresolved_defect of this ReleaseProgressionResource.


        :param has_unresolved_defect: The has_unresolved_defect of this ReleaseProgressionResource.  # noqa: E501
        :type: bool
        """

        self._has_unresolved_defect = has_unresolved_defect

    @property
    def release_retention_period(self):
        """Gets the release_retention_period of this ReleaseProgressionResource.  # noqa: E501


        :return: The release_retention_period of this ReleaseProgressionResource.  # noqa: E501
        :rtype: RetentionPeriod
        """
        return self._release_retention_period

    @release_retention_period.setter
    def release_retention_period(self, release_retention_period):
        """Sets the release_retention_period of this ReleaseProgressionResource.


        :param release_retention_period: The release_retention_period of this ReleaseProgressionResource.  # noqa: E501
        :type: RetentionPeriod
        """

        self._release_retention_period = release_retention_period

    @property
    def tentacle_retention_period(self):
        """Gets the tentacle_retention_period of this ReleaseProgressionResource.  # noqa: E501


        :return: The tentacle_retention_period of this ReleaseProgressionResource.  # noqa: E501
        :rtype: RetentionPeriod
        """
        return self._tentacle_retention_period

    @tentacle_retention_period.setter
    def tentacle_retention_period(self, tentacle_retention_period):
        """Sets the tentacle_retention_period of this ReleaseProgressionResource.


        :param tentacle_retention_period: The tentacle_retention_period of this ReleaseProgressionResource.  # noqa: E501
        :type: RetentionPeriod
        """

        self._tentacle_retention_period = tentacle_retention_period

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
        if issubclass(ReleaseProgressionResource, dict):
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
        if not isinstance(other, ReleaseProgressionResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
