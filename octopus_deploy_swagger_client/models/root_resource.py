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


class RootResource(object):
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
        'application': 'str',
        'version': 'str',
        'api_version': 'str',
        'installation_id': 'str',
        'is_early_access_program': 'bool',
        'has_long_term_support': 'bool',
        'last_modified_on': 'datetime',
        'last_modified_by': 'str',
        'links': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'Id',
        'application': 'Application',
        'version': 'Version',
        'api_version': 'ApiVersion',
        'installation_id': 'InstallationId',
        'is_early_access_program': 'IsEarlyAccessProgram',
        'has_long_term_support': 'HasLongTermSupport',
        'last_modified_on': 'LastModifiedOn',
        'last_modified_by': 'LastModifiedBy',
        'links': 'Links'
    }

    def __init__(self, id=None, application=None, version=None, api_version=None, installation_id=None, is_early_access_program=False, has_long_term_support=False, last_modified_on=None, last_modified_by=None, links=None):  # noqa: E501
        """RootResource - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._application = None
        self._version = None
        self._api_version = None
        self._installation_id = None
        self._is_early_access_program = None
        self._has_long_term_support = None
        self._last_modified_on = None
        self._last_modified_by = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if application is not None:
            self.application = application
        if version is not None:
            self.version = version
        if api_version is not None:
            self.api_version = api_version
        if installation_id is not None:
            self.installation_id = installation_id
        if is_early_access_program is not None:
            self.is_early_access_program = is_early_access_program
        if has_long_term_support is not None:
            self.has_long_term_support = has_long_term_support
        if last_modified_on is not None:
            self.last_modified_on = last_modified_on
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this RootResource.  # noqa: E501


        :return: The id of this RootResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RootResource.


        :param id: The id of this RootResource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def application(self):
        """Gets the application of this RootResource.  # noqa: E501


        :return: The application of this RootResource.  # noqa: E501
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this RootResource.


        :param application: The application of this RootResource.  # noqa: E501
        :type: str
        """

        self._application = application

    @property
    def version(self):
        """Gets the version of this RootResource.  # noqa: E501


        :return: The version of this RootResource.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this RootResource.


        :param version: The version of this RootResource.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def api_version(self):
        """Gets the api_version of this RootResource.  # noqa: E501


        :return: The api_version of this RootResource.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this RootResource.


        :param api_version: The api_version of this RootResource.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def installation_id(self):
        """Gets the installation_id of this RootResource.  # noqa: E501


        :return: The installation_id of this RootResource.  # noqa: E501
        :rtype: str
        """
        return self._installation_id

    @installation_id.setter
    def installation_id(self, installation_id):
        """Sets the installation_id of this RootResource.


        :param installation_id: The installation_id of this RootResource.  # noqa: E501
        :type: str
        """

        self._installation_id = installation_id

    @property
    def is_early_access_program(self):
        """Gets the is_early_access_program of this RootResource.  # noqa: E501


        :return: The is_early_access_program of this RootResource.  # noqa: E501
        :rtype: bool
        """
        return self._is_early_access_program

    @is_early_access_program.setter
    def is_early_access_program(self, is_early_access_program):
        """Sets the is_early_access_program of this RootResource.


        :param is_early_access_program: The is_early_access_program of this RootResource.  # noqa: E501
        :type: bool
        """

        self._is_early_access_program = is_early_access_program

    @property
    def has_long_term_support(self):
        """Gets the has_long_term_support of this RootResource.  # noqa: E501


        :return: The has_long_term_support of this RootResource.  # noqa: E501
        :rtype: bool
        """
        return self._has_long_term_support

    @has_long_term_support.setter
    def has_long_term_support(self, has_long_term_support):
        """Sets the has_long_term_support of this RootResource.


        :param has_long_term_support: The has_long_term_support of this RootResource.  # noqa: E501
        :type: bool
        """

        self._has_long_term_support = has_long_term_support

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this RootResource.  # noqa: E501


        :return: The last_modified_on of this RootResource.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this RootResource.


        :param last_modified_on: The last_modified_on of this RootResource.  # noqa: E501
        :type: datetime
        """

        self._last_modified_on = last_modified_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this RootResource.  # noqa: E501


        :return: The last_modified_by of this RootResource.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this RootResource.


        :param last_modified_by: The last_modified_by of this RootResource.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def links(self):
        """Gets the links of this RootResource.  # noqa: E501


        :return: The links of this RootResource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this RootResource.


        :param links: The links of this RootResource.  # noqa: E501
        :type: dict(str, str)
        """

        self._links = links

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
        if issubclass(RootResource, dict):
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
        if not isinstance(other, RootResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
