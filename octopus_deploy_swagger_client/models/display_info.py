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

from octopus_deploy_swagger_client.models.list_api_metadata import ListApiMetadata  # noqa: F401,E501
from octopus_deploy_swagger_client.models.options_metadata import OptionsMetadata  # noqa: F401,E501
from octopus_deploy_swagger_client.models.property_applicability import PropertyApplicability  # noqa: F401,E501


class DisplayInfo(object):
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
        'required': 'bool',
        'read_only': 'bool',
        'label': 'str',
        'description': 'str',
        'options': 'OptionsMetadata',
        'list_api': 'ListApiMetadata',
        'show_copy_to_clipboard': 'bool',
        'property_applicability': 'PropertyApplicability'
    }

    attribute_map = {
        'required': 'Required',
        'read_only': 'ReadOnly',
        'label': 'Label',
        'description': 'Description',
        'options': 'Options',
        'list_api': 'ListApi',
        'show_copy_to_clipboard': 'ShowCopyToClipboard',
        'property_applicability': 'PropertyApplicability'
    }

    def __init__(self, required=None, read_only=None, label=None, description=None, options=None, list_api=None, show_copy_to_clipboard=None, property_applicability=None):  # noqa: E501
        """DisplayInfo - a model defined in Swagger"""  # noqa: E501

        self._required = None
        self._read_only = None
        self._label = None
        self._description = None
        self._options = None
        self._list_api = None
        self._show_copy_to_clipboard = None
        self._property_applicability = None
        self.discriminator = None

        if required is not None:
            self.required = required
        if read_only is not None:
            self.read_only = read_only
        if label is not None:
            self.label = label
        if description is not None:
            self.description = description
        if options is not None:
            self.options = options
        if list_api is not None:
            self.list_api = list_api
        if show_copy_to_clipboard is not None:
            self.show_copy_to_clipboard = show_copy_to_clipboard
        if property_applicability is not None:
            self.property_applicability = property_applicability

    @property
    def required(self):
        """Gets the required of this DisplayInfo.  # noqa: E501


        :return: The required of this DisplayInfo.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this DisplayInfo.


        :param required: The required of this DisplayInfo.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def read_only(self):
        """Gets the read_only of this DisplayInfo.  # noqa: E501


        :return: The read_only of this DisplayInfo.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this DisplayInfo.


        :param read_only: The read_only of this DisplayInfo.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def label(self):
        """Gets the label of this DisplayInfo.  # noqa: E501


        :return: The label of this DisplayInfo.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this DisplayInfo.


        :param label: The label of this DisplayInfo.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def description(self):
        """Gets the description of this DisplayInfo.  # noqa: E501


        :return: The description of this DisplayInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DisplayInfo.


        :param description: The description of this DisplayInfo.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def options(self):
        """Gets the options of this DisplayInfo.  # noqa: E501


        :return: The options of this DisplayInfo.  # noqa: E501
        :rtype: OptionsMetadata
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this DisplayInfo.


        :param options: The options of this DisplayInfo.  # noqa: E501
        :type: OptionsMetadata
        """

        self._options = options

    @property
    def list_api(self):
        """Gets the list_api of this DisplayInfo.  # noqa: E501


        :return: The list_api of this DisplayInfo.  # noqa: E501
        :rtype: ListApiMetadata
        """
        return self._list_api

    @list_api.setter
    def list_api(self, list_api):
        """Sets the list_api of this DisplayInfo.


        :param list_api: The list_api of this DisplayInfo.  # noqa: E501
        :type: ListApiMetadata
        """

        self._list_api = list_api

    @property
    def show_copy_to_clipboard(self):
        """Gets the show_copy_to_clipboard of this DisplayInfo.  # noqa: E501


        :return: The show_copy_to_clipboard of this DisplayInfo.  # noqa: E501
        :rtype: bool
        """
        return self._show_copy_to_clipboard

    @show_copy_to_clipboard.setter
    def show_copy_to_clipboard(self, show_copy_to_clipboard):
        """Sets the show_copy_to_clipboard of this DisplayInfo.


        :param show_copy_to_clipboard: The show_copy_to_clipboard of this DisplayInfo.  # noqa: E501
        :type: bool
        """

        self._show_copy_to_clipboard = show_copy_to_clipboard

    @property
    def property_applicability(self):
        """Gets the property_applicability of this DisplayInfo.  # noqa: E501


        :return: The property_applicability of this DisplayInfo.  # noqa: E501
        :rtype: PropertyApplicability
        """
        return self._property_applicability

    @property_applicability.setter
    def property_applicability(self, property_applicability):
        """Sets the property_applicability of this DisplayInfo.


        :param property_applicability: The property_applicability of this DisplayInfo.  # noqa: E501
        :type: PropertyApplicability
        """

        self._property_applicability = property_applicability

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
        if issubclass(DisplayInfo, dict):
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
        if not isinstance(other, DisplayInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
