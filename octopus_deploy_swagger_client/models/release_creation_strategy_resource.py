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

from octopus_deploy_swagger_client.models.deployment_action_package_resource import DeploymentActionPackageResource  # noqa: F401,E501


class ReleaseCreationStrategyResource(object):
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
        'channel_id': 'str',
        'release_creation_package': 'DeploymentActionPackageResource'
    }

    attribute_map = {
        'channel_id': 'ChannelId',
        'release_creation_package': 'ReleaseCreationPackage'
    }

    def __init__(self, channel_id=None, release_creation_package=None):  # noqa: E501
        """ReleaseCreationStrategyResource - a model defined in Swagger"""  # noqa: E501

        self._channel_id = None
        self._release_creation_package = None
        self.discriminator = None

        if channel_id is not None:
            self.channel_id = channel_id
        if release_creation_package is not None:
            self.release_creation_package = release_creation_package

    @property
    def channel_id(self):
        """Gets the channel_id of this ReleaseCreationStrategyResource.  # noqa: E501


        :return: The channel_id of this ReleaseCreationStrategyResource.  # noqa: E501
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """Sets the channel_id of this ReleaseCreationStrategyResource.


        :param channel_id: The channel_id of this ReleaseCreationStrategyResource.  # noqa: E501
        :type: str
        """

        self._channel_id = channel_id

    @property
    def release_creation_package(self):
        """Gets the release_creation_package of this ReleaseCreationStrategyResource.  # noqa: E501


        :return: The release_creation_package of this ReleaseCreationStrategyResource.  # noqa: E501
        :rtype: DeploymentActionPackageResource
        """
        return self._release_creation_package

    @release_creation_package.setter
    def release_creation_package(self, release_creation_package):
        """Sets the release_creation_package of this ReleaseCreationStrategyResource.


        :param release_creation_package: The release_creation_package of this ReleaseCreationStrategyResource.  # noqa: E501
        :type: DeploymentActionPackageResource
        """

        self._release_creation_package = release_creation_package

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
        if issubclass(ReleaseCreationStrategyResource, dict):
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
        if not isinstance(other, ReleaseCreationStrategyResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
