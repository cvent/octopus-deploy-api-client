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

from octopus_deploy_swagger_client.models.property_value_resource import PropertyValueResource  # noqa: F401,E501


class ActionTemplateParameterResource(object):
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
        'label': 'str',
        'help_text': 'str',
        'default_value': 'PropertyValueResource',
        'display_settings': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'label': 'Label',
        'help_text': 'HelpText',
        'default_value': 'DefaultValue',
        'display_settings': 'DisplaySettings'
    }

    def __init__(self, id=None, name=None, label=None, help_text=None, default_value=None, display_settings=None):  # noqa: E501
        """ActionTemplateParameterResource - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._label = None
        self._help_text = None
        self._default_value = None
        self._display_settings = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if label is not None:
            self.label = label
        if help_text is not None:
            self.help_text = help_text
        if default_value is not None:
            self.default_value = default_value
        if display_settings is not None:
            self.display_settings = display_settings

    @property
    def id(self):
        """Gets the id of this ActionTemplateParameterResource.  # noqa: E501


        :return: The id of this ActionTemplateParameterResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ActionTemplateParameterResource.


        :param id: The id of this ActionTemplateParameterResource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ActionTemplateParameterResource.  # noqa: E501


        :return: The name of this ActionTemplateParameterResource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ActionTemplateParameterResource.


        :param name: The name of this ActionTemplateParameterResource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def label(self):
        """Gets the label of this ActionTemplateParameterResource.  # noqa: E501


        :return: The label of this ActionTemplateParameterResource.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ActionTemplateParameterResource.


        :param label: The label of this ActionTemplateParameterResource.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def help_text(self):
        """Gets the help_text of this ActionTemplateParameterResource.  # noqa: E501


        :return: The help_text of this ActionTemplateParameterResource.  # noqa: E501
        :rtype: str
        """
        return self._help_text

    @help_text.setter
    def help_text(self, help_text):
        """Sets the help_text of this ActionTemplateParameterResource.


        :param help_text: The help_text of this ActionTemplateParameterResource.  # noqa: E501
        :type: str
        """

        self._help_text = help_text

    @property
    def default_value(self):
        """Gets the default_value of this ActionTemplateParameterResource.  # noqa: E501


        :return: The default_value of this ActionTemplateParameterResource.  # noqa: E501
        :rtype: PropertyValueResource
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this ActionTemplateParameterResource.


        :param default_value: The default_value of this ActionTemplateParameterResource.  # noqa: E501
        :type: PropertyValueResource
        """

        self._default_value = default_value

    @property
    def display_settings(self):
        """Gets the display_settings of this ActionTemplateParameterResource.  # noqa: E501


        :return: The display_settings of this ActionTemplateParameterResource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._display_settings

    @display_settings.setter
    def display_settings(self, display_settings):
        """Sets the display_settings of this ActionTemplateParameterResource.


        :param display_settings: The display_settings of this ActionTemplateParameterResource.  # noqa: E501
        :type: dict(str, str)
        """

        self._display_settings = display_settings

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
        if issubclass(ActionTemplateParameterResource, dict):
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
        if not isinstance(other, ActionTemplateParameterResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
