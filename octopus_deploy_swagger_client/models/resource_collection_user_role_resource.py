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

from octopus_deploy_swagger_client.models.user_role_resource import UserRoleResource  # noqa: F401,E501


class ResourceCollectionUserRoleResource(object):
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
        'item_type': 'str',
        'total_results': 'int',
        'items_per_page': 'int',
        'number_of_pages': 'int',
        'last_page_number': 'int',
        'items': 'list[UserRoleResource]',
        'last_modified_on': 'datetime',
        'last_modified_by': 'str',
        'links': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'Id',
        'item_type': 'ItemType',
        'total_results': 'TotalResults',
        'items_per_page': 'ItemsPerPage',
        'number_of_pages': 'NumberOfPages',
        'last_page_number': 'LastPageNumber',
        'items': 'Items',
        'last_modified_on': 'LastModifiedOn',
        'last_modified_by': 'LastModifiedBy',
        'links': 'Links'
    }

    def __init__(self, id=None, item_type=None, total_results=None, items_per_page=None, number_of_pages=None, last_page_number=None, items=None, last_modified_on=None, last_modified_by=None, links=None):  # noqa: E501
        """ResourceCollectionUserRoleResource - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._item_type = None
        self._total_results = None
        self._items_per_page = None
        self._number_of_pages = None
        self._last_page_number = None
        self._items = None
        self._last_modified_on = None
        self._last_modified_by = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if item_type is not None:
            self.item_type = item_type
        if total_results is not None:
            self.total_results = total_results
        if items_per_page is not None:
            self.items_per_page = items_per_page
        if number_of_pages is not None:
            self.number_of_pages = number_of_pages
        if last_page_number is not None:
            self.last_page_number = last_page_number
        if items is not None:
            self.items = items
        if last_modified_on is not None:
            self.last_modified_on = last_modified_on
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this ResourceCollectionUserRoleResource.  # noqa: E501


        :return: The id of this ResourceCollectionUserRoleResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResourceCollectionUserRoleResource.


        :param id: The id of this ResourceCollectionUserRoleResource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def item_type(self):
        """Gets the item_type of this ResourceCollectionUserRoleResource.  # noqa: E501


        :return: The item_type of this ResourceCollectionUserRoleResource.  # noqa: E501
        :rtype: str
        """
        return self._item_type

    @item_type.setter
    def item_type(self, item_type):
        """Sets the item_type of this ResourceCollectionUserRoleResource.


        :param item_type: The item_type of this ResourceCollectionUserRoleResource.  # noqa: E501
        :type: str
        """

        self._item_type = item_type

    @property
    def total_results(self):
        """Gets the total_results of this ResourceCollectionUserRoleResource.  # noqa: E501


        :return: The total_results of this ResourceCollectionUserRoleResource.  # noqa: E501
        :rtype: int
        """
        return self._total_results

    @total_results.setter
    def total_results(self, total_results):
        """Sets the total_results of this ResourceCollectionUserRoleResource.


        :param total_results: The total_results of this ResourceCollectionUserRoleResource.  # noqa: E501
        :type: int
        """

        self._total_results = total_results

    @property
    def items_per_page(self):
        """Gets the items_per_page of this ResourceCollectionUserRoleResource.  # noqa: E501


        :return: The items_per_page of this ResourceCollectionUserRoleResource.  # noqa: E501
        :rtype: int
        """
        return self._items_per_page

    @items_per_page.setter
    def items_per_page(self, items_per_page):
        """Sets the items_per_page of this ResourceCollectionUserRoleResource.


        :param items_per_page: The items_per_page of this ResourceCollectionUserRoleResource.  # noqa: E501
        :type: int
        """

        self._items_per_page = items_per_page

    @property
    def number_of_pages(self):
        """Gets the number_of_pages of this ResourceCollectionUserRoleResource.  # noqa: E501


        :return: The number_of_pages of this ResourceCollectionUserRoleResource.  # noqa: E501
        :rtype: int
        """
        return self._number_of_pages

    @number_of_pages.setter
    def number_of_pages(self, number_of_pages):
        """Sets the number_of_pages of this ResourceCollectionUserRoleResource.


        :param number_of_pages: The number_of_pages of this ResourceCollectionUserRoleResource.  # noqa: E501
        :type: int
        """

        self._number_of_pages = number_of_pages

    @property
    def last_page_number(self):
        """Gets the last_page_number of this ResourceCollectionUserRoleResource.  # noqa: E501


        :return: The last_page_number of this ResourceCollectionUserRoleResource.  # noqa: E501
        :rtype: int
        """
        return self._last_page_number

    @last_page_number.setter
    def last_page_number(self, last_page_number):
        """Sets the last_page_number of this ResourceCollectionUserRoleResource.


        :param last_page_number: The last_page_number of this ResourceCollectionUserRoleResource.  # noqa: E501
        :type: int
        """

        self._last_page_number = last_page_number

    @property
    def items(self):
        """Gets the items of this ResourceCollectionUserRoleResource.  # noqa: E501


        :return: The items of this ResourceCollectionUserRoleResource.  # noqa: E501
        :rtype: list[UserRoleResource]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ResourceCollectionUserRoleResource.


        :param items: The items of this ResourceCollectionUserRoleResource.  # noqa: E501
        :type: list[UserRoleResource]
        """

        self._items = items

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this ResourceCollectionUserRoleResource.  # noqa: E501


        :return: The last_modified_on of this ResourceCollectionUserRoleResource.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this ResourceCollectionUserRoleResource.


        :param last_modified_on: The last_modified_on of this ResourceCollectionUserRoleResource.  # noqa: E501
        :type: datetime
        """

        self._last_modified_on = last_modified_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this ResourceCollectionUserRoleResource.  # noqa: E501


        :return: The last_modified_by of this ResourceCollectionUserRoleResource.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this ResourceCollectionUserRoleResource.


        :param last_modified_by: The last_modified_by of this ResourceCollectionUserRoleResource.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def links(self):
        """Gets the links of this ResourceCollectionUserRoleResource.  # noqa: E501


        :return: The links of this ResourceCollectionUserRoleResource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ResourceCollectionUserRoleResource.


        :param links: The links of this ResourceCollectionUserRoleResource.  # noqa: E501
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
        if issubclass(ResourceCollectionUserRoleResource, dict):
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
        if not isinstance(other, ResourceCollectionUserRoleResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
