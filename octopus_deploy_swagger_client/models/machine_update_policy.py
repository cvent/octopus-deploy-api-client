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


class MachineUpdatePolicy(object):
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
        'calamari_update_behavior': 'str',
        'tentacle_update_behavior': 'str',
        'tentacle_update_account_id': 'str'
    }

    attribute_map = {
        'calamari_update_behavior': 'CalamariUpdateBehavior',
        'tentacle_update_behavior': 'TentacleUpdateBehavior',
        'tentacle_update_account_id': 'TentacleUpdateAccountId'
    }

    def __init__(self, calamari_update_behavior=None, tentacle_update_behavior=None, tentacle_update_account_id=None):  # noqa: E501
        """MachineUpdatePolicy - a model defined in Swagger"""  # noqa: E501

        self._calamari_update_behavior = None
        self._tentacle_update_behavior = None
        self._tentacle_update_account_id = None
        self.discriminator = None

        if calamari_update_behavior is not None:
            self.calamari_update_behavior = calamari_update_behavior
        if tentacle_update_behavior is not None:
            self.tentacle_update_behavior = tentacle_update_behavior
        if tentacle_update_account_id is not None:
            self.tentacle_update_account_id = tentacle_update_account_id

    @property
    def calamari_update_behavior(self):
        """Gets the calamari_update_behavior of this MachineUpdatePolicy.  # noqa: E501


        :return: The calamari_update_behavior of this MachineUpdatePolicy.  # noqa: E501
        :rtype: str
        """
        return self._calamari_update_behavior

    @calamari_update_behavior.setter
    def calamari_update_behavior(self, calamari_update_behavior):
        """Sets the calamari_update_behavior of this MachineUpdatePolicy.


        :param calamari_update_behavior: The calamari_update_behavior of this MachineUpdatePolicy.  # noqa: E501
        :type: str
        """
        allowed_values = ["UpdateOnDeployment", "UpdateOnNewMachine", "UpdateAlways"]  # noqa: E501
        if calamari_update_behavior not in allowed_values:
            raise ValueError(
                "Invalid value for `calamari_update_behavior` ({0}), must be one of {1}"  # noqa: E501
                .format(calamari_update_behavior, allowed_values)
            )

        self._calamari_update_behavior = calamari_update_behavior

    @property
    def tentacle_update_behavior(self):
        """Gets the tentacle_update_behavior of this MachineUpdatePolicy.  # noqa: E501


        :return: The tentacle_update_behavior of this MachineUpdatePolicy.  # noqa: E501
        :rtype: str
        """
        return self._tentacle_update_behavior

    @tentacle_update_behavior.setter
    def tentacle_update_behavior(self, tentacle_update_behavior):
        """Sets the tentacle_update_behavior of this MachineUpdatePolicy.


        :param tentacle_update_behavior: The tentacle_update_behavior of this MachineUpdatePolicy.  # noqa: E501
        :type: str
        """
        allowed_values = ["NeverUpdate", "Update"]  # noqa: E501
        if tentacle_update_behavior not in allowed_values:
            raise ValueError(
                "Invalid value for `tentacle_update_behavior` ({0}), must be one of {1}"  # noqa: E501
                .format(tentacle_update_behavior, allowed_values)
            )

        self._tentacle_update_behavior = tentacle_update_behavior

    @property
    def tentacle_update_account_id(self):
        """Gets the tentacle_update_account_id of this MachineUpdatePolicy.  # noqa: E501


        :return: The tentacle_update_account_id of this MachineUpdatePolicy.  # noqa: E501
        :rtype: str
        """
        return self._tentacle_update_account_id

    @tentacle_update_account_id.setter
    def tentacle_update_account_id(self, tentacle_update_account_id):
        """Sets the tentacle_update_account_id of this MachineUpdatePolicy.


        :param tentacle_update_account_id: The tentacle_update_account_id of this MachineUpdatePolicy.  # noqa: E501
        :type: str
        """

        self._tentacle_update_account_id = tentacle_update_account_id

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
        if issubclass(MachineUpdatePolicy, dict):
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
        if not isinstance(other, MachineUpdatePolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
