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


class AuthenticationProviderElement(object):
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
        'name': 'str',
        'identity_type': 'str',
        'forms_login_enabled': 'bool',
        'links': 'dict(str, str)',
        'javascript_links': 'list[str]',
        'css_links': 'list[str]'
    }

    attribute_map = {
        'name': 'Name',
        'identity_type': 'IdentityType',
        'forms_login_enabled': 'FormsLoginEnabled',
        'links': 'Links',
        'javascript_links': 'JavascriptLinks',
        'css_links': 'CSSLinks'
    }

    def __init__(self, name=None, identity_type=None, forms_login_enabled=None, links=None, javascript_links=None, css_links=None):  # noqa: E501
        """AuthenticationProviderElement - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._identity_type = None
        self._forms_login_enabled = None
        self._links = None
        self._javascript_links = None
        self._css_links = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if identity_type is not None:
            self.identity_type = identity_type
        if forms_login_enabled is not None:
            self.forms_login_enabled = forms_login_enabled
        if links is not None:
            self.links = links
        if javascript_links is not None:
            self.javascript_links = javascript_links
        if css_links is not None:
            self.css_links = css_links

    @property
    def name(self):
        """Gets the name of this AuthenticationProviderElement.  # noqa: E501


        :return: The name of this AuthenticationProviderElement.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AuthenticationProviderElement.


        :param name: The name of this AuthenticationProviderElement.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def identity_type(self):
        """Gets the identity_type of this AuthenticationProviderElement.  # noqa: E501


        :return: The identity_type of this AuthenticationProviderElement.  # noqa: E501
        :rtype: str
        """
        return self._identity_type

    @identity_type.setter
    def identity_type(self, identity_type):
        """Sets the identity_type of this AuthenticationProviderElement.


        :param identity_type: The identity_type of this AuthenticationProviderElement.  # noqa: E501
        :type: str
        """
        allowed_values = ["Guest", "UsernamePassword", "ActiveDirectory", "OAuth"]  # noqa: E501
        if identity_type not in allowed_values:
            raise ValueError(
                "Invalid value for `identity_type` ({0}), must be one of {1}"  # noqa: E501
                .format(identity_type, allowed_values)
            )

        self._identity_type = identity_type

    @property
    def forms_login_enabled(self):
        """Gets the forms_login_enabled of this AuthenticationProviderElement.  # noqa: E501


        :return: The forms_login_enabled of this AuthenticationProviderElement.  # noqa: E501
        :rtype: bool
        """
        return self._forms_login_enabled

    @forms_login_enabled.setter
    def forms_login_enabled(self, forms_login_enabled):
        """Sets the forms_login_enabled of this AuthenticationProviderElement.


        :param forms_login_enabled: The forms_login_enabled of this AuthenticationProviderElement.  # noqa: E501
        :type: bool
        """

        self._forms_login_enabled = forms_login_enabled

    @property
    def links(self):
        """Gets the links of this AuthenticationProviderElement.  # noqa: E501


        :return: The links of this AuthenticationProviderElement.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AuthenticationProviderElement.


        :param links: The links of this AuthenticationProviderElement.  # noqa: E501
        :type: dict(str, str)
        """

        self._links = links

    @property
    def javascript_links(self):
        """Gets the javascript_links of this AuthenticationProviderElement.  # noqa: E501


        :return: The javascript_links of this AuthenticationProviderElement.  # noqa: E501
        :rtype: list[str]
        """
        return self._javascript_links

    @javascript_links.setter
    def javascript_links(self, javascript_links):
        """Sets the javascript_links of this AuthenticationProviderElement.


        :param javascript_links: The javascript_links of this AuthenticationProviderElement.  # noqa: E501
        :type: list[str]
        """

        self._javascript_links = javascript_links

    @property
    def css_links(self):
        """Gets the css_links of this AuthenticationProviderElement.  # noqa: E501


        :return: The css_links of this AuthenticationProviderElement.  # noqa: E501
        :rtype: list[str]
        """
        return self._css_links

    @css_links.setter
    def css_links(self, css_links):
        """Sets the css_links of this AuthenticationProviderElement.


        :param css_links: The css_links of this AuthenticationProviderElement.  # noqa: E501
        :type: list[str]
        """

        self._css_links = css_links

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
        if issubclass(AuthenticationProviderElement, dict):
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
        if not isinstance(other, AuthenticationProviderElement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
