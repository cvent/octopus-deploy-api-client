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


class VariableResourceScope(object):
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
        'project': 'list[str]',
        'environment': 'list[str]',
        'machine': 'list[str]',
        'role': 'list[str]',
        'target_role': 'list[str]',
        'action': 'list[str]',
        'user': 'list[str]',
        'trigger': 'list[str]',
        'parent_deployment': 'list[str]',
        'private': 'list[str]',
        'channel': 'list[str]',
        'tenant_tag': 'list[str]',
        'tenant': 'list[str]'
    }

    attribute_map = {
        'project': 'Project',
        'environment': 'Environment',
        'machine': 'Machine',
        'role': 'Role',
        'target_role': 'TargetRole',
        'action': 'Action',
        'user': 'User',
        'trigger': 'Trigger',
        'parent_deployment': 'ParentDeployment',
        'private': 'Private',
        'channel': 'Channel',
        'tenant_tag': 'TenantTag',
        'tenant': 'Tenant'
    }

    def __init__(self, project=None, environment=None, machine=None, role=None, target_role=None, action=None, user=None, trigger=None, parent_deployment=None, private=None, channel=None, tenant_tag=None, tenant=None):  # noqa: E501
        """VariableResourceScope - a model defined in Swagger"""  # noqa: E501

        self._project = None
        self._environment = None
        self._machine = None
        self._role = None
        self._target_role = None
        self._action = None
        self._user = None
        self._trigger = None
        self._parent_deployment = None
        self._private = None
        self._channel = None
        self._tenant_tag = None
        self._tenant = None
        self.discriminator = None

        if project is not None:
            self.project = project
        if environment is not None:
            self.environment = environment
        if machine is not None:
            self.machine = machine
        if role is not None:
            self.role = role
        if target_role is not None:
            self.target_role = target_role
        if action is not None:
            self.action = action
        if user is not None:
            self.user = user
        if trigger is not None:
            self.trigger = trigger
        if parent_deployment is not None:
            self.parent_deployment = parent_deployment
        if private is not None:
            self.private = private
        if channel is not None:
            self.channel = channel
        if tenant_tag is not None:
            self.tenant_tag = tenant_tag
        if tenant is not None:
            self.tenant = tenant

    @property
    def project(self):
        """Gets the project of this VariableResourceScope.  # noqa: E501


        :return: The project of this VariableResourceScope.  # noqa: E501
        :rtype: list[str]
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this VariableResourceScope.


        :param project: The project of this VariableResourceScope.  # noqa: E501
        :type: list[str]
        """

        self._project = project

    @property
    def environment(self):
        """Gets the environment of this VariableResourceScope.  # noqa: E501


        :return: The environment of this VariableResourceScope.  # noqa: E501
        :rtype: list[str]
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this VariableResourceScope.


        :param environment: The environment of this VariableResourceScope.  # noqa: E501
        :type: list[str]
        """

        self._environment = environment

    @property
    def machine(self):
        """Gets the machine of this VariableResourceScope.  # noqa: E501


        :return: The machine of this VariableResourceScope.  # noqa: E501
        :rtype: list[str]
        """
        return self._machine

    @machine.setter
    def machine(self, machine):
        """Sets the machine of this VariableResourceScope.


        :param machine: The machine of this VariableResourceScope.  # noqa: E501
        :type: list[str]
        """

        self._machine = machine

    @property
    def role(self):
        """Gets the role of this VariableResourceScope.  # noqa: E501


        :return: The role of this VariableResourceScope.  # noqa: E501
        :rtype: list[str]
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this VariableResourceScope.


        :param role: The role of this VariableResourceScope.  # noqa: E501
        :type: list[str]
        """

        self._role = role

    @property
    def target_role(self):
        """Gets the target_role of this VariableResourceScope.  # noqa: E501


        :return: The target_role of this VariableResourceScope.  # noqa: E501
        :rtype: list[str]
        """
        return self._target_role

    @target_role.setter
    def target_role(self, target_role):
        """Sets the target_role of this VariableResourceScope.


        :param target_role: The target_role of this VariableResourceScope.  # noqa: E501
        :type: list[str]
        """

        self._target_role = target_role

    @property
    def action(self):
        """Gets the action of this VariableResourceScope.  # noqa: E501


        :return: The action of this VariableResourceScope.  # noqa: E501
        :rtype: list[str]
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this VariableResourceScope.


        :param action: The action of this VariableResourceScope.  # noqa: E501
        :type: list[str]
        """

        self._action = action

    @property
    def user(self):
        """Gets the user of this VariableResourceScope.  # noqa: E501


        :return: The user of this VariableResourceScope.  # noqa: E501
        :rtype: list[str]
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this VariableResourceScope.


        :param user: The user of this VariableResourceScope.  # noqa: E501
        :type: list[str]
        """

        self._user = user

    @property
    def trigger(self):
        """Gets the trigger of this VariableResourceScope.  # noqa: E501


        :return: The trigger of this VariableResourceScope.  # noqa: E501
        :rtype: list[str]
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this VariableResourceScope.


        :param trigger: The trigger of this VariableResourceScope.  # noqa: E501
        :type: list[str]
        """

        self._trigger = trigger

    @property
    def parent_deployment(self):
        """Gets the parent_deployment of this VariableResourceScope.  # noqa: E501


        :return: The parent_deployment of this VariableResourceScope.  # noqa: E501
        :rtype: list[str]
        """
        return self._parent_deployment

    @parent_deployment.setter
    def parent_deployment(self, parent_deployment):
        """Sets the parent_deployment of this VariableResourceScope.


        :param parent_deployment: The parent_deployment of this VariableResourceScope.  # noqa: E501
        :type: list[str]
        """

        self._parent_deployment = parent_deployment

    @property
    def private(self):
        """Gets the private of this VariableResourceScope.  # noqa: E501


        :return: The private of this VariableResourceScope.  # noqa: E501
        :rtype: list[str]
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this VariableResourceScope.


        :param private: The private of this VariableResourceScope.  # noqa: E501
        :type: list[str]
        """

        self._private = private

    @property
    def channel(self):
        """Gets the channel of this VariableResourceScope.  # noqa: E501


        :return: The channel of this VariableResourceScope.  # noqa: E501
        :rtype: list[str]
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this VariableResourceScope.


        :param channel: The channel of this VariableResourceScope.  # noqa: E501
        :type: list[str]
        """

        self._channel = channel

    @property
    def tenant_tag(self):
        """Gets the tenant_tag of this VariableResourceScope.  # noqa: E501


        :return: The tenant_tag of this VariableResourceScope.  # noqa: E501
        :rtype: list[str]
        """
        return self._tenant_tag

    @tenant_tag.setter
    def tenant_tag(self, tenant_tag):
        """Sets the tenant_tag of this VariableResourceScope.


        :param tenant_tag: The tenant_tag of this VariableResourceScope.  # noqa: E501
        :type: list[str]
        """

        self._tenant_tag = tenant_tag

    @property
    def tenant(self):
        """Gets the tenant of this VariableResourceScope.  # noqa: E501


        :return: The tenant of this VariableResourceScope.  # noqa: E501
        :rtype: list[str]
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this VariableResourceScope.


        :param tenant: The tenant of this VariableResourceScope.  # noqa: E501
        :type: list[str]
        """

        self._tenant = tenant

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
        if issubclass(VariableResourceScope, dict):
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
        if not isinstance(other, VariableResourceScope):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
