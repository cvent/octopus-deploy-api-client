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

from octopus_deploy_swagger_client.models.deployment_action_resource import DeploymentActionResource  # noqa: F401,E501
from octopus_deploy_swagger_client.models.property_value_resource import PropertyValueResource  # noqa: F401,E501


class DeploymentStepResource(object):
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
        'id': 'str',
        'name': 'str',
        'package_requirement': 'str',
        'properties': 'dict(str, PropertyValueResource)',
        'condition': 'str',
        'start_trigger': 'str',
        'actions': 'list[DeploymentActionResource]'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'package_requirement': 'PackageRequirement',
        'properties': 'Properties',
        'condition': 'Condition',
        'start_trigger': 'StartTrigger',
        'actions': 'Actions'
    }

    def __init__(self, id=None, name=None, package_requirement=None, properties=None, condition=None, start_trigger=None, actions=None):  # noqa: E501
        """DeploymentStepResource - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._package_requirement = None
        self._properties = None
        self._condition = None
        self._start_trigger = None
        self._actions = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if package_requirement is not None:
            self.package_requirement = package_requirement
        if properties is not None:
            self.properties = properties
        if condition is not None:
            self.condition = condition
        if start_trigger is not None:
            self.start_trigger = start_trigger
        if actions is not None:
            self.actions = actions

    @property
    def id(self):
        """Gets the id of this DeploymentStepResource.  # noqa: E501


        :return: The id of this DeploymentStepResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeploymentStepResource.


        :param id: The id of this DeploymentStepResource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DeploymentStepResource.  # noqa: E501


        :return: The name of this DeploymentStepResource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeploymentStepResource.


        :param name: The name of this DeploymentStepResource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def package_requirement(self):
        """Gets the package_requirement of this DeploymentStepResource.  # noqa: E501


        :return: The package_requirement of this DeploymentStepResource.  # noqa: E501
        :rtype: str
        """
        return self._package_requirement

    @package_requirement.setter
    def package_requirement(self, package_requirement):
        """Sets the package_requirement of this DeploymentStepResource.


        :param package_requirement: The package_requirement of this DeploymentStepResource.  # noqa: E501
        :type: str
        """
        allowed_values = ["LetOctopusDecide", "BeforePackageAcquisition", "AfterPackageAcquisition"]  # noqa: E501
        if package_requirement not in allowed_values:
            raise ValueError(
                "Invalid value for `package_requirement` ({0}), must be one of {1}"  # noqa: E501
                .format(package_requirement, allowed_values)
            )

        self._package_requirement = package_requirement

    @property
    def properties(self):
        """Gets the properties of this DeploymentStepResource.  # noqa: E501


        :return: The properties of this DeploymentStepResource.  # noqa: E501
        :rtype: dict(str, PropertyValueResource)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this DeploymentStepResource.


        :param properties: The properties of this DeploymentStepResource.  # noqa: E501
        :type: dict(str, PropertyValueResource)
        """

        self._properties = properties

    @property
    def condition(self):
        """Gets the condition of this DeploymentStepResource.  # noqa: E501


        :return: The condition of this DeploymentStepResource.  # noqa: E501
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this DeploymentStepResource.


        :param condition: The condition of this DeploymentStepResource.  # noqa: E501
        :type: str
        """
        allowed_values = ["Success", "Failure", "Always", "Variable"]  # noqa: E501
        if condition not in allowed_values:
            raise ValueError(
                "Invalid value for `condition` ({0}), must be one of {1}"  # noqa: E501
                .format(condition, allowed_values)
            )

        self._condition = condition

    @property
    def start_trigger(self):
        """Gets the start_trigger of this DeploymentStepResource.  # noqa: E501


        :return: The start_trigger of this DeploymentStepResource.  # noqa: E501
        :rtype: str
        """
        return self._start_trigger

    @start_trigger.setter
    def start_trigger(self, start_trigger):
        """Sets the start_trigger of this DeploymentStepResource.


        :param start_trigger: The start_trigger of this DeploymentStepResource.  # noqa: E501
        :type: str
        """
        allowed_values = ["StartAfterPrevious", "StartWithPrevious"]  # noqa: E501
        if start_trigger not in allowed_values:
            raise ValueError(
                "Invalid value for `start_trigger` ({0}), must be one of {1}"  # noqa: E501
                .format(start_trigger, allowed_values)
            )

        self._start_trigger = start_trigger

    @property
    def actions(self):
        """Gets the actions of this DeploymentStepResource.  # noqa: E501


        :return: The actions of this DeploymentStepResource.  # noqa: E501
        :rtype: list[DeploymentActionResource]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this DeploymentStepResource.


        :param actions: The actions of this DeploymentStepResource.  # noqa: E501
        :type: list[DeploymentActionResource]
        """

        self._actions = actions

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
        if issubclass(DeploymentStepResource, dict):
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
        if not isinstance(other, DeploymentStepResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other