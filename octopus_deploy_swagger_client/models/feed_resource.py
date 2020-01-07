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


class FeedResource(object):
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
        'feed_type': 'str',
        'package_acquisition_location_options': 'list[str]',
        'space_id': 'str',
        'last_modified_on': 'datetime',
        'last_modified_by': 'str',
        'links': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'feed_type': 'FeedType',
        'package_acquisition_location_options': 'PackageAcquisitionLocationOptions',
        'space_id': 'SpaceId',
        'last_modified_on': 'LastModifiedOn',
        'last_modified_by': 'LastModifiedBy',
        'links': 'Links'
    }

    def __init__(self, id=None, name=None, feed_type=None, package_acquisition_location_options=None, space_id=None, last_modified_on=None, last_modified_by=None, links=None):  # noqa: E501
        """FeedResource - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._feed_type = None
        self._package_acquisition_location_options = None
        self._space_id = None
        self._last_modified_on = None
        self._last_modified_by = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if feed_type is not None:
            self.feed_type = feed_type
        if package_acquisition_location_options is not None:
            self.package_acquisition_location_options = package_acquisition_location_options
        if space_id is not None:
            self.space_id = space_id
        if last_modified_on is not None:
            self.last_modified_on = last_modified_on
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this FeedResource.  # noqa: E501


        :return: The id of this FeedResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FeedResource.


        :param id: The id of this FeedResource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this FeedResource.  # noqa: E501


        :return: The name of this FeedResource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FeedResource.


        :param name: The name of this FeedResource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def feed_type(self):
        """Gets the feed_type of this FeedResource.  # noqa: E501


        :return: The feed_type of this FeedResource.  # noqa: E501
        :rtype: str
        """
        return self._feed_type

    @feed_type.setter
    def feed_type(self, feed_type):
        """Sets the feed_type of this FeedResource.


        :param feed_type: The feed_type of this FeedResource.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "NuGet", "Docker", "Maven", "OctopusProject", "GitHub", "Helm", "AwsElasticContainerRegistry", "BuiltIn"]  # noqa: E501
        if feed_type not in allowed_values:
            raise ValueError(
                "Invalid value for `feed_type` ({0}), must be one of {1}"  # noqa: E501
                .format(feed_type, allowed_values)
            )

        self._feed_type = feed_type

    @property
    def package_acquisition_location_options(self):
        """Gets the package_acquisition_location_options of this FeedResource.  # noqa: E501


        :return: The package_acquisition_location_options of this FeedResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._package_acquisition_location_options

    @package_acquisition_location_options.setter
    def package_acquisition_location_options(self, package_acquisition_location_options):
        """Sets the package_acquisition_location_options of this FeedResource.


        :param package_acquisition_location_options: The package_acquisition_location_options of this FeedResource.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["Server", "ExecutionTarget", "NotAcquired"]  # noqa: E501
        if not set(package_acquisition_location_options).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `package_acquisition_location_options` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(package_acquisition_location_options) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._package_acquisition_location_options = package_acquisition_location_options

    @property
    def space_id(self):
        """Gets the space_id of this FeedResource.  # noqa: E501


        :return: The space_id of this FeedResource.  # noqa: E501
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this FeedResource.


        :param space_id: The space_id of this FeedResource.  # noqa: E501
        :type: str
        """

        self._space_id = space_id

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this FeedResource.  # noqa: E501


        :return: The last_modified_on of this FeedResource.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this FeedResource.


        :param last_modified_on: The last_modified_on of this FeedResource.  # noqa: E501
        :type: datetime
        """

        self._last_modified_on = last_modified_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this FeedResource.  # noqa: E501


        :return: The last_modified_by of this FeedResource.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this FeedResource.


        :param last_modified_by: The last_modified_by of this FeedResource.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def links(self):
        """Gets the links of this FeedResource.  # noqa: E501


        :return: The links of this FeedResource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this FeedResource.


        :param links: The links of this FeedResource.  # noqa: E501
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
        if issubclass(FeedResource, dict):
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
        if not isinstance(other, FeedResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other