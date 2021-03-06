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

from octopus_deploy_swagger_client.models.deployment_resource import DeploymentResource  # noqa: F401,E501
from octopus_deploy_swagger_client.models.task_resource import TaskResource  # noqa: F401,E501


class PhaseDeploymentResource(object):
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
        'task': 'TaskResource',
        'deployment': 'DeploymentResource'
    }

    attribute_map = {
        'task': 'Task',
        'deployment': 'Deployment'
    }

    def __init__(self, task=None, deployment=None):  # noqa: E501
        """PhaseDeploymentResource - a model defined in Swagger"""  # noqa: E501

        self._task = None
        self._deployment = None
        self.discriminator = None

        if task is not None:
            self.task = task
        if deployment is not None:
            self.deployment = deployment

    @property
    def task(self):
        """Gets the task of this PhaseDeploymentResource.  # noqa: E501


        :return: The task of this PhaseDeploymentResource.  # noqa: E501
        :rtype: TaskResource
        """
        return self._task

    @task.setter
    def task(self, task):
        """Sets the task of this PhaseDeploymentResource.


        :param task: The task of this PhaseDeploymentResource.  # noqa: E501
        :type: TaskResource
        """

        self._task = task

    @property
    def deployment(self):
        """Gets the deployment of this PhaseDeploymentResource.  # noqa: E501


        :return: The deployment of this PhaseDeploymentResource.  # noqa: E501
        :rtype: DeploymentResource
        """
        return self._deployment

    @deployment.setter
    def deployment(self, deployment):
        """Sets the deployment of this PhaseDeploymentResource.


        :param deployment: The deployment of this PhaseDeploymentResource.  # noqa: E501
        :type: DeploymentResource
        """

        self._deployment = deployment

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
        if issubclass(PhaseDeploymentResource, dict):
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
        if not isinstance(other, PhaseDeploymentResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
