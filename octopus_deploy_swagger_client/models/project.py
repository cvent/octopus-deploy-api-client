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

from octopus_deploy_swagger_client.models.action_template_parameter_resource import ActionTemplateParameterResource  # noqa: F401,E501
from octopus_deploy_swagger_client.models.property_value_resource import PropertyValueResource  # noqa: F401,E501


class Project(object):
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
        'project_id': 'str',
        'project_name': 'str',
        'templates': 'list[ActionTemplateParameterResource]',
        'variables': 'dict(str, dict(str, PropertyValueResource))',
        'links': 'dict(str, str)'
    }

    attribute_map = {
        'project_id': 'ProjectId',
        'project_name': 'ProjectName',
        'templates': 'Templates',
        'variables': 'Variables',
        'links': 'Links'
    }

    def __init__(self, project_id=None, project_name=None, templates=None, variables=None, links=None):  # noqa: E501
        """Project - a model defined in Swagger"""  # noqa: E501

        self._project_id = None
        self._project_name = None
        self._templates = None
        self._variables = None
        self._links = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if templates is not None:
            self.templates = templates
        if variables is not None:
            self.variables = variables
        if links is not None:
            self.links = links

    @property
    def project_id(self):
        """Gets the project_id of this Project.  # noqa: E501


        :return: The project_id of this Project.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Project.


        :param project_id: The project_id of this Project.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this Project.  # noqa: E501


        :return: The project_name of this Project.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this Project.


        :param project_name: The project_name of this Project.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def templates(self):
        """Gets the templates of this Project.  # noqa: E501


        :return: The templates of this Project.  # noqa: E501
        :rtype: list[ActionTemplateParameterResource]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        """Sets the templates of this Project.


        :param templates: The templates of this Project.  # noqa: E501
        :type: list[ActionTemplateParameterResource]
        """

        self._templates = templates

    @property
    def variables(self):
        """Gets the variables of this Project.  # noqa: E501


        :return: The variables of this Project.  # noqa: E501
        :rtype: dict(str, dict(str, PropertyValueResource))
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """Sets the variables of this Project.


        :param variables: The variables of this Project.  # noqa: E501
        :type: dict(str, dict(str, PropertyValueResource))
        """

        self._variables = variables

    @property
    def links(self):
        """Gets the links of this Project.  # noqa: E501


        :return: The links of this Project.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Project.


        :param links: The links of this Project.  # noqa: E501
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
        if issubclass(Project, dict):
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
        if not isinstance(other, Project):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other