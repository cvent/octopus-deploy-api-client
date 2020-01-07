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

from octopus_deploy_swagger_client.models.phase_deployment_resource import PhaseDeploymentResource  # noqa: F401,E501


class PhaseProgressionResource(object):
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
        'blocked': 'bool',
        'progress': 'str',
        'deployments': 'list[PhaseDeploymentResource]',
        'automatic_deployment_targets': 'list[str]',
        'optional_deployment_targets': 'list[str]',
        'minimum_environments_before_promotion': 'int',
        'is_optional_phase': 'bool'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'blocked': 'Blocked',
        'progress': 'Progress',
        'deployments': 'Deployments',
        'automatic_deployment_targets': 'AutomaticDeploymentTargets',
        'optional_deployment_targets': 'OptionalDeploymentTargets',
        'minimum_environments_before_promotion': 'MinimumEnvironmentsBeforePromotion',
        'is_optional_phase': 'IsOptionalPhase'
    }

    def __init__(self, id=None, name=None, blocked=None, progress=None, deployments=None, automatic_deployment_targets=None, optional_deployment_targets=None, minimum_environments_before_promotion=None, is_optional_phase=None):  # noqa: E501
        """PhaseProgressionResource - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._blocked = None
        self._progress = None
        self._deployments = None
        self._automatic_deployment_targets = None
        self._optional_deployment_targets = None
        self._minimum_environments_before_promotion = None
        self._is_optional_phase = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if blocked is not None:
            self.blocked = blocked
        if progress is not None:
            self.progress = progress
        if deployments is not None:
            self.deployments = deployments
        if automatic_deployment_targets is not None:
            self.automatic_deployment_targets = automatic_deployment_targets
        if optional_deployment_targets is not None:
            self.optional_deployment_targets = optional_deployment_targets
        if minimum_environments_before_promotion is not None:
            self.minimum_environments_before_promotion = minimum_environments_before_promotion
        if is_optional_phase is not None:
            self.is_optional_phase = is_optional_phase

    @property
    def id(self):
        """Gets the id of this PhaseProgressionResource.  # noqa: E501


        :return: The id of this PhaseProgressionResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PhaseProgressionResource.


        :param id: The id of this PhaseProgressionResource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this PhaseProgressionResource.  # noqa: E501


        :return: The name of this PhaseProgressionResource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PhaseProgressionResource.


        :param name: The name of this PhaseProgressionResource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def blocked(self):
        """Gets the blocked of this PhaseProgressionResource.  # noqa: E501


        :return: The blocked of this PhaseProgressionResource.  # noqa: E501
        :rtype: bool
        """
        return self._blocked

    @blocked.setter
    def blocked(self, blocked):
        """Sets the blocked of this PhaseProgressionResource.


        :param blocked: The blocked of this PhaseProgressionResource.  # noqa: E501
        :type: bool
        """

        self._blocked = blocked

    @property
    def progress(self):
        """Gets the progress of this PhaseProgressionResource.  # noqa: E501


        :return: The progress of this PhaseProgressionResource.  # noqa: E501
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this PhaseProgressionResource.


        :param progress: The progress of this PhaseProgressionResource.  # noqa: E501
        :type: str
        """
        allowed_values = ["Pending", "Current", "Complete"]  # noqa: E501
        if progress not in allowed_values:
            raise ValueError(
                "Invalid value for `progress` ({0}), must be one of {1}"  # noqa: E501
                .format(progress, allowed_values)
            )

        self._progress = progress

    @property
    def deployments(self):
        """Gets the deployments of this PhaseProgressionResource.  # noqa: E501


        :return: The deployments of this PhaseProgressionResource.  # noqa: E501
        :rtype: list[PhaseDeploymentResource]
        """
        return self._deployments

    @deployments.setter
    def deployments(self, deployments):
        """Sets the deployments of this PhaseProgressionResource.


        :param deployments: The deployments of this PhaseProgressionResource.  # noqa: E501
        :type: list[PhaseDeploymentResource]
        """

        self._deployments = deployments

    @property
    def automatic_deployment_targets(self):
        """Gets the automatic_deployment_targets of this PhaseProgressionResource.  # noqa: E501


        :return: The automatic_deployment_targets of this PhaseProgressionResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._automatic_deployment_targets

    @automatic_deployment_targets.setter
    def automatic_deployment_targets(self, automatic_deployment_targets):
        """Sets the automatic_deployment_targets of this PhaseProgressionResource.


        :param automatic_deployment_targets: The automatic_deployment_targets of this PhaseProgressionResource.  # noqa: E501
        :type: list[str]
        """

        self._automatic_deployment_targets = automatic_deployment_targets

    @property
    def optional_deployment_targets(self):
        """Gets the optional_deployment_targets of this PhaseProgressionResource.  # noqa: E501


        :return: The optional_deployment_targets of this PhaseProgressionResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._optional_deployment_targets

    @optional_deployment_targets.setter
    def optional_deployment_targets(self, optional_deployment_targets):
        """Sets the optional_deployment_targets of this PhaseProgressionResource.


        :param optional_deployment_targets: The optional_deployment_targets of this PhaseProgressionResource.  # noqa: E501
        :type: list[str]
        """

        self._optional_deployment_targets = optional_deployment_targets

    @property
    def minimum_environments_before_promotion(self):
        """Gets the minimum_environments_before_promotion of this PhaseProgressionResource.  # noqa: E501


        :return: The minimum_environments_before_promotion of this PhaseProgressionResource.  # noqa: E501
        :rtype: int
        """
        return self._minimum_environments_before_promotion

    @minimum_environments_before_promotion.setter
    def minimum_environments_before_promotion(self, minimum_environments_before_promotion):
        """Sets the minimum_environments_before_promotion of this PhaseProgressionResource.


        :param minimum_environments_before_promotion: The minimum_environments_before_promotion of this PhaseProgressionResource.  # noqa: E501
        :type: int
        """

        self._minimum_environments_before_promotion = minimum_environments_before_promotion

    @property
    def is_optional_phase(self):
        """Gets the is_optional_phase of this PhaseProgressionResource.  # noqa: E501


        :return: The is_optional_phase of this PhaseProgressionResource.  # noqa: E501
        :rtype: bool
        """
        return self._is_optional_phase

    @is_optional_phase.setter
    def is_optional_phase(self, is_optional_phase):
        """Sets the is_optional_phase of this PhaseProgressionResource.


        :param is_optional_phase: The is_optional_phase of this PhaseProgressionResource.  # noqa: E501
        :type: bool
        """

        self._is_optional_phase = is_optional_phase

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
        if issubclass(PhaseProgressionResource, dict):
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
        if not isinstance(other, PhaseProgressionResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other