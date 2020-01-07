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


class TaskResource(object):
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
        'space_id': 'str',
        'name': 'str',
        'description': 'str',
        'arguments': 'dict(str, object)',
        'state': 'str',
        'completed': 'str',
        'queue_time': 'datetime',
        'queue_time_expiry': 'datetime',
        'start_time': 'datetime',
        'last_updated_time': 'datetime',
        'completed_time': 'datetime',
        'server_node': 'str',
        'duration': 'str',
        'error_message': 'str',
        'has_been_picked_up_by_processor': 'bool',
        'is_completed': 'bool',
        'finished_successfully': 'bool',
        'has_pending_interruptions': 'bool',
        'can_rerun': 'bool',
        'has_warnings_or_errors': 'bool',
        'last_modified_on': 'datetime',
        'last_modified_by': 'str',
        'links': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'Id',
        'space_id': 'SpaceId',
        'name': 'Name',
        'description': 'Description',
        'arguments': 'Arguments',
        'state': 'State',
        'completed': 'Completed',
        'queue_time': 'QueueTime',
        'queue_time_expiry': 'QueueTimeExpiry',
        'start_time': 'StartTime',
        'last_updated_time': 'LastUpdatedTime',
        'completed_time': 'CompletedTime',
        'server_node': 'ServerNode',
        'duration': 'Duration',
        'error_message': 'ErrorMessage',
        'has_been_picked_up_by_processor': 'HasBeenPickedUpByProcessor',
        'is_completed': 'IsCompleted',
        'finished_successfully': 'FinishedSuccessfully',
        'has_pending_interruptions': 'HasPendingInterruptions',
        'can_rerun': 'CanRerun',
        'has_warnings_or_errors': 'HasWarningsOrErrors',
        'last_modified_on': 'LastModifiedOn',
        'last_modified_by': 'LastModifiedBy',
        'links': 'Links'
    }

    def __init__(self, id=None, space_id=None, name=None, description=None, arguments=None, state=None, completed=None, queue_time=None, queue_time_expiry=None, start_time=None, last_updated_time=None, completed_time=None, server_node=None, duration=None, error_message=None, has_been_picked_up_by_processor=None, is_completed=None, finished_successfully=None, has_pending_interruptions=None, can_rerun=None, has_warnings_or_errors=None, last_modified_on=None, last_modified_by=None, links=None):  # noqa: E501
        """TaskResource - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._space_id = None
        self._name = None
        self._description = None
        self._arguments = None
        self._state = None
        self._completed = None
        self._queue_time = None
        self._queue_time_expiry = None
        self._start_time = None
        self._last_updated_time = None
        self._completed_time = None
        self._server_node = None
        self._duration = None
        self._error_message = None
        self._has_been_picked_up_by_processor = None
        self._is_completed = None
        self._finished_successfully = None
        self._has_pending_interruptions = None
        self._can_rerun = None
        self._has_warnings_or_errors = None
        self._last_modified_on = None
        self._last_modified_by = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if space_id is not None:
            self.space_id = space_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if arguments is not None:
            self.arguments = arguments
        if state is not None:
            self.state = state
        if completed is not None:
            self.completed = completed
        if queue_time is not None:
            self.queue_time = queue_time
        if queue_time_expiry is not None:
            self.queue_time_expiry = queue_time_expiry
        if start_time is not None:
            self.start_time = start_time
        if last_updated_time is not None:
            self.last_updated_time = last_updated_time
        if completed_time is not None:
            self.completed_time = completed_time
        if server_node is not None:
            self.server_node = server_node
        if duration is not None:
            self.duration = duration
        if error_message is not None:
            self.error_message = error_message
        if has_been_picked_up_by_processor is not None:
            self.has_been_picked_up_by_processor = has_been_picked_up_by_processor
        if is_completed is not None:
            self.is_completed = is_completed
        if finished_successfully is not None:
            self.finished_successfully = finished_successfully
        if has_pending_interruptions is not None:
            self.has_pending_interruptions = has_pending_interruptions
        if can_rerun is not None:
            self.can_rerun = can_rerun
        if has_warnings_or_errors is not None:
            self.has_warnings_or_errors = has_warnings_or_errors
        if last_modified_on is not None:
            self.last_modified_on = last_modified_on
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this TaskResource.  # noqa: E501


        :return: The id of this TaskResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskResource.


        :param id: The id of this TaskResource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def space_id(self):
        """Gets the space_id of this TaskResource.  # noqa: E501


        :return: The space_id of this TaskResource.  # noqa: E501
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this TaskResource.


        :param space_id: The space_id of this TaskResource.  # noqa: E501
        :type: str
        """

        self._space_id = space_id

    @property
    def name(self):
        """Gets the name of this TaskResource.  # noqa: E501


        :return: The name of this TaskResource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaskResource.


        :param name: The name of this TaskResource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this TaskResource.  # noqa: E501


        :return: The description of this TaskResource.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TaskResource.


        :param description: The description of this TaskResource.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def arguments(self):
        """Gets the arguments of this TaskResource.  # noqa: E501


        :return: The arguments of this TaskResource.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this TaskResource.


        :param arguments: The arguments of this TaskResource.  # noqa: E501
        :type: dict(str, object)
        """

        self._arguments = arguments

    @property
    def state(self):
        """Gets the state of this TaskResource.  # noqa: E501


        :return: The state of this TaskResource.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TaskResource.


        :param state: The state of this TaskResource.  # noqa: E501
        :type: str
        """
        allowed_values = ["Queued", "Executing", "Failed", "Canceled", "TimedOut", "Success", "Cancelling"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def completed(self):
        """Gets the completed of this TaskResource.  # noqa: E501


        :return: The completed of this TaskResource.  # noqa: E501
        :rtype: str
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """Sets the completed of this TaskResource.


        :param completed: The completed of this TaskResource.  # noqa: E501
        :type: str
        """

        self._completed = completed

    @property
    def queue_time(self):
        """Gets the queue_time of this TaskResource.  # noqa: E501


        :return: The queue_time of this TaskResource.  # noqa: E501
        :rtype: datetime
        """
        return self._queue_time

    @queue_time.setter
    def queue_time(self, queue_time):
        """Sets the queue_time of this TaskResource.


        :param queue_time: The queue_time of this TaskResource.  # noqa: E501
        :type: datetime
        """

        self._queue_time = queue_time

    @property
    def queue_time_expiry(self):
        """Gets the queue_time_expiry of this TaskResource.  # noqa: E501


        :return: The queue_time_expiry of this TaskResource.  # noqa: E501
        :rtype: datetime
        """
        return self._queue_time_expiry

    @queue_time_expiry.setter
    def queue_time_expiry(self, queue_time_expiry):
        """Sets the queue_time_expiry of this TaskResource.


        :param queue_time_expiry: The queue_time_expiry of this TaskResource.  # noqa: E501
        :type: datetime
        """

        self._queue_time_expiry = queue_time_expiry

    @property
    def start_time(self):
        """Gets the start_time of this TaskResource.  # noqa: E501


        :return: The start_time of this TaskResource.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this TaskResource.


        :param start_time: The start_time of this TaskResource.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def last_updated_time(self):
        """Gets the last_updated_time of this TaskResource.  # noqa: E501


        :return: The last_updated_time of this TaskResource.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated_time

    @last_updated_time.setter
    def last_updated_time(self, last_updated_time):
        """Sets the last_updated_time of this TaskResource.


        :param last_updated_time: The last_updated_time of this TaskResource.  # noqa: E501
        :type: datetime
        """

        self._last_updated_time = last_updated_time

    @property
    def completed_time(self):
        """Gets the completed_time of this TaskResource.  # noqa: E501


        :return: The completed_time of this TaskResource.  # noqa: E501
        :rtype: datetime
        """
        return self._completed_time

    @completed_time.setter
    def completed_time(self, completed_time):
        """Sets the completed_time of this TaskResource.


        :param completed_time: The completed_time of this TaskResource.  # noqa: E501
        :type: datetime
        """

        self._completed_time = completed_time

    @property
    def server_node(self):
        """Gets the server_node of this TaskResource.  # noqa: E501


        :return: The server_node of this TaskResource.  # noqa: E501
        :rtype: str
        """
        return self._server_node

    @server_node.setter
    def server_node(self, server_node):
        """Sets the server_node of this TaskResource.


        :param server_node: The server_node of this TaskResource.  # noqa: E501
        :type: str
        """

        self._server_node = server_node

    @property
    def duration(self):
        """Gets the duration of this TaskResource.  # noqa: E501


        :return: The duration of this TaskResource.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this TaskResource.


        :param duration: The duration of this TaskResource.  # noqa: E501
        :type: str
        """

        self._duration = duration

    @property
    def error_message(self):
        """Gets the error_message of this TaskResource.  # noqa: E501


        :return: The error_message of this TaskResource.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this TaskResource.


        :param error_message: The error_message of this TaskResource.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def has_been_picked_up_by_processor(self):
        """Gets the has_been_picked_up_by_processor of this TaskResource.  # noqa: E501


        :return: The has_been_picked_up_by_processor of this TaskResource.  # noqa: E501
        :rtype: bool
        """
        return self._has_been_picked_up_by_processor

    @has_been_picked_up_by_processor.setter
    def has_been_picked_up_by_processor(self, has_been_picked_up_by_processor):
        """Sets the has_been_picked_up_by_processor of this TaskResource.


        :param has_been_picked_up_by_processor: The has_been_picked_up_by_processor of this TaskResource.  # noqa: E501
        :type: bool
        """

        self._has_been_picked_up_by_processor = has_been_picked_up_by_processor

    @property
    def is_completed(self):
        """Gets the is_completed of this TaskResource.  # noqa: E501


        :return: The is_completed of this TaskResource.  # noqa: E501
        :rtype: bool
        """
        return self._is_completed

    @is_completed.setter
    def is_completed(self, is_completed):
        """Sets the is_completed of this TaskResource.


        :param is_completed: The is_completed of this TaskResource.  # noqa: E501
        :type: bool
        """

        self._is_completed = is_completed

    @property
    def finished_successfully(self):
        """Gets the finished_successfully of this TaskResource.  # noqa: E501


        :return: The finished_successfully of this TaskResource.  # noqa: E501
        :rtype: bool
        """
        return self._finished_successfully

    @finished_successfully.setter
    def finished_successfully(self, finished_successfully):
        """Sets the finished_successfully of this TaskResource.


        :param finished_successfully: The finished_successfully of this TaskResource.  # noqa: E501
        :type: bool
        """

        self._finished_successfully = finished_successfully

    @property
    def has_pending_interruptions(self):
        """Gets the has_pending_interruptions of this TaskResource.  # noqa: E501


        :return: The has_pending_interruptions of this TaskResource.  # noqa: E501
        :rtype: bool
        """
        return self._has_pending_interruptions

    @has_pending_interruptions.setter
    def has_pending_interruptions(self, has_pending_interruptions):
        """Sets the has_pending_interruptions of this TaskResource.


        :param has_pending_interruptions: The has_pending_interruptions of this TaskResource.  # noqa: E501
        :type: bool
        """

        self._has_pending_interruptions = has_pending_interruptions

    @property
    def can_rerun(self):
        """Gets the can_rerun of this TaskResource.  # noqa: E501


        :return: The can_rerun of this TaskResource.  # noqa: E501
        :rtype: bool
        """
        return self._can_rerun

    @can_rerun.setter
    def can_rerun(self, can_rerun):
        """Sets the can_rerun of this TaskResource.


        :param can_rerun: The can_rerun of this TaskResource.  # noqa: E501
        :type: bool
        """

        self._can_rerun = can_rerun

    @property
    def has_warnings_or_errors(self):
        """Gets the has_warnings_or_errors of this TaskResource.  # noqa: E501


        :return: The has_warnings_or_errors of this TaskResource.  # noqa: E501
        :rtype: bool
        """
        return self._has_warnings_or_errors

    @has_warnings_or_errors.setter
    def has_warnings_or_errors(self, has_warnings_or_errors):
        """Sets the has_warnings_or_errors of this TaskResource.


        :param has_warnings_or_errors: The has_warnings_or_errors of this TaskResource.  # noqa: E501
        :type: bool
        """

        self._has_warnings_or_errors = has_warnings_or_errors

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this TaskResource.  # noqa: E501


        :return: The last_modified_on of this TaskResource.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this TaskResource.


        :param last_modified_on: The last_modified_on of this TaskResource.  # noqa: E501
        :type: datetime
        """

        self._last_modified_on = last_modified_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this TaskResource.  # noqa: E501


        :return: The last_modified_by of this TaskResource.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this TaskResource.


        :param last_modified_by: The last_modified_by of this TaskResource.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def links(self):
        """Gets the links of this TaskResource.  # noqa: E501


        :return: The links of this TaskResource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this TaskResource.


        :param links: The links of this TaskResource.  # noqa: E501
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
        if issubclass(TaskResource, dict):
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
        if not isinstance(other, TaskResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
