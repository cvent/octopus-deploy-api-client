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

from octopus_deploy_swagger_client.models.release_changes import ReleaseChanges  # noqa: F401,E501


class DeploymentResource(object):
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
        'release_id': 'str',
        'environment_id': 'str',
        'tenant_id': 'str',
        'force_package_download': 'bool',
        'force_package_redeployment': 'bool',
        'skip_actions': 'list[str]',
        'specific_machine_ids': 'list[str]',
        'excluded_machine_ids': 'list[str]',
        'deployment_process_id': 'str',
        'manifest_variable_set_id': 'str',
        'task_id': 'str',
        'project_id': 'str',
        'channel_id': 'str',
        'use_guided_failure': 'bool',
        'comments': 'str',
        'form_values': 'dict(str, str)',
        'queue_time': 'datetime',
        'queue_time_expiry': 'datetime',
        'name': 'str',
        'created': 'datetime',
        'changes': 'list[ReleaseChanges]',
        'space_id': 'str',
        'last_modified_on': 'datetime',
        'last_modified_by': 'str',
        'links': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'Id',
        'release_id': 'ReleaseId',
        'environment_id': 'EnvironmentId',
        'tenant_id': 'TenantId',
        'force_package_download': 'ForcePackageDownload',
        'force_package_redeployment': 'ForcePackageRedeployment',
        'skip_actions': 'SkipActions',
        'specific_machine_ids': 'SpecificMachineIds',
        'excluded_machine_ids': 'ExcludedMachineIds',
        'deployment_process_id': 'DeploymentProcessId',
        'manifest_variable_set_id': 'ManifestVariableSetId',
        'task_id': 'TaskId',
        'project_id': 'ProjectId',
        'channel_id': 'ChannelId',
        'use_guided_failure': 'UseGuidedFailure',
        'comments': 'Comments',
        'form_values': 'FormValues',
        'queue_time': 'QueueTime',
        'queue_time_expiry': 'QueueTimeExpiry',
        'name': 'Name',
        'created': 'Created',
        'changes': 'Changes',
        'space_id': 'SpaceId',
        'last_modified_on': 'LastModifiedOn',
        'last_modified_by': 'LastModifiedBy',
        'links': 'Links'
    }

    def __init__(self, id=None, release_id=None, environment_id=None, tenant_id=None, force_package_download=None, force_package_redeployment=None, skip_actions=None, specific_machine_ids=None, excluded_machine_ids=None, deployment_process_id=None, manifest_variable_set_id=None, task_id=None, project_id=None, channel_id=None, use_guided_failure=None, comments=None, form_values=None, queue_time=None, queue_time_expiry=None, name=None, created=None, changes=None, space_id=None, last_modified_on=None, last_modified_by=None, links=None):  # noqa: E501
        """DeploymentResource - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._release_id = None
        self._environment_id = None
        self._tenant_id = None
        self._force_package_download = None
        self._force_package_redeployment = None
        self._skip_actions = None
        self._specific_machine_ids = None
        self._excluded_machine_ids = None
        self._deployment_process_id = None
        self._manifest_variable_set_id = None
        self._task_id = None
        self._project_id = None
        self._channel_id = None
        self._use_guided_failure = None
        self._comments = None
        self._form_values = None
        self._queue_time = None
        self._queue_time_expiry = None
        self._name = None
        self._created = None
        self._changes = None
        self._space_id = None
        self._last_modified_on = None
        self._last_modified_by = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.release_id = release_id
        self.environment_id = environment_id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if force_package_download is not None:
            self.force_package_download = force_package_download
        if force_package_redeployment is not None:
            self.force_package_redeployment = force_package_redeployment
        if skip_actions is not None:
            self.skip_actions = skip_actions
        if specific_machine_ids is not None:
            self.specific_machine_ids = specific_machine_ids
        if excluded_machine_ids is not None:
            self.excluded_machine_ids = excluded_machine_ids
        if deployment_process_id is not None:
            self.deployment_process_id = deployment_process_id
        if manifest_variable_set_id is not None:
            self.manifest_variable_set_id = manifest_variable_set_id
        if task_id is not None:
            self.task_id = task_id
        if project_id is not None:
            self.project_id = project_id
        if channel_id is not None:
            self.channel_id = channel_id
        if use_guided_failure is not None:
            self.use_guided_failure = use_guided_failure
        if comments is not None:
            self.comments = comments
        if form_values is not None:
            self.form_values = form_values
        if queue_time is not None:
            self.queue_time = queue_time
        if queue_time_expiry is not None:
            self.queue_time_expiry = queue_time_expiry
        if name is not None:
            self.name = name
        if created is not None:
            self.created = created
        if changes is not None:
            self.changes = changes
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
        """Gets the id of this DeploymentResource.  # noqa: E501


        :return: The id of this DeploymentResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeploymentResource.


        :param id: The id of this DeploymentResource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def release_id(self):
        """Gets the release_id of this DeploymentResource.  # noqa: E501


        :return: The release_id of this DeploymentResource.  # noqa: E501
        :rtype: str
        """
        return self._release_id

    @release_id.setter
    def release_id(self, release_id):
        """Sets the release_id of this DeploymentResource.


        :param release_id: The release_id of this DeploymentResource.  # noqa: E501
        :type: str
        """
        if release_id is None:
            raise ValueError("Invalid value for `release_id`, must not be `None`")  # noqa: E501

        self._release_id = release_id

    @property
    def environment_id(self):
        """Gets the environment_id of this DeploymentResource.  # noqa: E501


        :return: The environment_id of this DeploymentResource.  # noqa: E501
        :rtype: str
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        """Sets the environment_id of this DeploymentResource.


        :param environment_id: The environment_id of this DeploymentResource.  # noqa: E501
        :type: str
        """
        if environment_id is None:
            raise ValueError("Invalid value for `environment_id`, must not be `None`")  # noqa: E501

        self._environment_id = environment_id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this DeploymentResource.  # noqa: E501


        :return: The tenant_id of this DeploymentResource.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this DeploymentResource.


        :param tenant_id: The tenant_id of this DeploymentResource.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def force_package_download(self):
        """Gets the force_package_download of this DeploymentResource.  # noqa: E501


        :return: The force_package_download of this DeploymentResource.  # noqa: E501
        :rtype: bool
        """
        return self._force_package_download

    @force_package_download.setter
    def force_package_download(self, force_package_download):
        """Sets the force_package_download of this DeploymentResource.


        :param force_package_download: The force_package_download of this DeploymentResource.  # noqa: E501
        :type: bool
        """

        self._force_package_download = force_package_download

    @property
    def force_package_redeployment(self):
        """Gets the force_package_redeployment of this DeploymentResource.  # noqa: E501


        :return: The force_package_redeployment of this DeploymentResource.  # noqa: E501
        :rtype: bool
        """
        return self._force_package_redeployment

    @force_package_redeployment.setter
    def force_package_redeployment(self, force_package_redeployment):
        """Sets the force_package_redeployment of this DeploymentResource.


        :param force_package_redeployment: The force_package_redeployment of this DeploymentResource.  # noqa: E501
        :type: bool
        """

        self._force_package_redeployment = force_package_redeployment

    @property
    def skip_actions(self):
        """Gets the skip_actions of this DeploymentResource.  # noqa: E501


        :return: The skip_actions of this DeploymentResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._skip_actions

    @skip_actions.setter
    def skip_actions(self, skip_actions):
        """Sets the skip_actions of this DeploymentResource.


        :param skip_actions: The skip_actions of this DeploymentResource.  # noqa: E501
        :type: list[str]
        """

        self._skip_actions = skip_actions

    @property
    def specific_machine_ids(self):
        """Gets the specific_machine_ids of this DeploymentResource.  # noqa: E501


        :return: The specific_machine_ids of this DeploymentResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._specific_machine_ids

    @specific_machine_ids.setter
    def specific_machine_ids(self, specific_machine_ids):
        """Sets the specific_machine_ids of this DeploymentResource.


        :param specific_machine_ids: The specific_machine_ids of this DeploymentResource.  # noqa: E501
        :type: list[str]
        """

        self._specific_machine_ids = specific_machine_ids

    @property
    def excluded_machine_ids(self):
        """Gets the excluded_machine_ids of this DeploymentResource.  # noqa: E501


        :return: The excluded_machine_ids of this DeploymentResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._excluded_machine_ids

    @excluded_machine_ids.setter
    def excluded_machine_ids(self, excluded_machine_ids):
        """Sets the excluded_machine_ids of this DeploymentResource.


        :param excluded_machine_ids: The excluded_machine_ids of this DeploymentResource.  # noqa: E501
        :type: list[str]
        """

        self._excluded_machine_ids = excluded_machine_ids

    @property
    def deployment_process_id(self):
        """Gets the deployment_process_id of this DeploymentResource.  # noqa: E501


        :return: The deployment_process_id of this DeploymentResource.  # noqa: E501
        :rtype: str
        """
        return self._deployment_process_id

    @deployment_process_id.setter
    def deployment_process_id(self, deployment_process_id):
        """Sets the deployment_process_id of this DeploymentResource.


        :param deployment_process_id: The deployment_process_id of this DeploymentResource.  # noqa: E501
        :type: str
        """

        self._deployment_process_id = deployment_process_id

    @property
    def manifest_variable_set_id(self):
        """Gets the manifest_variable_set_id of this DeploymentResource.  # noqa: E501


        :return: The manifest_variable_set_id of this DeploymentResource.  # noqa: E501
        :rtype: str
        """
        return self._manifest_variable_set_id

    @manifest_variable_set_id.setter
    def manifest_variable_set_id(self, manifest_variable_set_id):
        """Sets the manifest_variable_set_id of this DeploymentResource.


        :param manifest_variable_set_id: The manifest_variable_set_id of this DeploymentResource.  # noqa: E501
        :type: str
        """

        self._manifest_variable_set_id = manifest_variable_set_id

    @property
    def task_id(self):
        """Gets the task_id of this DeploymentResource.  # noqa: E501


        :return: The task_id of this DeploymentResource.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this DeploymentResource.


        :param task_id: The task_id of this DeploymentResource.  # noqa: E501
        :type: str
        """

        self._task_id = task_id

    @property
    def project_id(self):
        """Gets the project_id of this DeploymentResource.  # noqa: E501


        :return: The project_id of this DeploymentResource.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this DeploymentResource.


        :param project_id: The project_id of this DeploymentResource.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def channel_id(self):
        """Gets the channel_id of this DeploymentResource.  # noqa: E501


        :return: The channel_id of this DeploymentResource.  # noqa: E501
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """Sets the channel_id of this DeploymentResource.


        :param channel_id: The channel_id of this DeploymentResource.  # noqa: E501
        :type: str
        """

        self._channel_id = channel_id

    @property
    def use_guided_failure(self):
        """Gets the use_guided_failure of this DeploymentResource.  # noqa: E501


        :return: The use_guided_failure of this DeploymentResource.  # noqa: E501
        :rtype: bool
        """
        return self._use_guided_failure

    @use_guided_failure.setter
    def use_guided_failure(self, use_guided_failure):
        """Sets the use_guided_failure of this DeploymentResource.


        :param use_guided_failure: The use_guided_failure of this DeploymentResource.  # noqa: E501
        :type: bool
        """

        self._use_guided_failure = use_guided_failure

    @property
    def comments(self):
        """Gets the comments of this DeploymentResource.  # noqa: E501


        :return: The comments of this DeploymentResource.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this DeploymentResource.


        :param comments: The comments of this DeploymentResource.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def form_values(self):
        """Gets the form_values of this DeploymentResource.  # noqa: E501


        :return: The form_values of this DeploymentResource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._form_values

    @form_values.setter
    def form_values(self, form_values):
        """Sets the form_values of this DeploymentResource.


        :param form_values: The form_values of this DeploymentResource.  # noqa: E501
        :type: dict(str, str)
        """

        self._form_values = form_values

    @property
    def queue_time(self):
        """Gets the queue_time of this DeploymentResource.  # noqa: E501


        :return: The queue_time of this DeploymentResource.  # noqa: E501
        :rtype: datetime
        """
        return self._queue_time

    @queue_time.setter
    def queue_time(self, queue_time):
        """Sets the queue_time of this DeploymentResource.


        :param queue_time: The queue_time of this DeploymentResource.  # noqa: E501
        :type: datetime
        """

        self._queue_time = queue_time

    @property
    def queue_time_expiry(self):
        """Gets the queue_time_expiry of this DeploymentResource.  # noqa: E501


        :return: The queue_time_expiry of this DeploymentResource.  # noqa: E501
        :rtype: datetime
        """
        return self._queue_time_expiry

    @queue_time_expiry.setter
    def queue_time_expiry(self, queue_time_expiry):
        """Sets the queue_time_expiry of this DeploymentResource.


        :param queue_time_expiry: The queue_time_expiry of this DeploymentResource.  # noqa: E501
        :type: datetime
        """

        self._queue_time_expiry = queue_time_expiry

    @property
    def name(self):
        """Gets the name of this DeploymentResource.  # noqa: E501


        :return: The name of this DeploymentResource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeploymentResource.


        :param name: The name of this DeploymentResource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def created(self):
        """Gets the created of this DeploymentResource.  # noqa: E501


        :return: The created of this DeploymentResource.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this DeploymentResource.


        :param created: The created of this DeploymentResource.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def changes(self):
        """Gets the changes of this DeploymentResource.  # noqa: E501


        :return: The changes of this DeploymentResource.  # noqa: E501
        :rtype: list[ReleaseChanges]
        """
        return self._changes

    @changes.setter
    def changes(self, changes):
        """Sets the changes of this DeploymentResource.


        :param changes: The changes of this DeploymentResource.  # noqa: E501
        :type: list[ReleaseChanges]
        """

        self._changes = changes

    @property
    def space_id(self):
        """Gets the space_id of this DeploymentResource.  # noqa: E501


        :return: The space_id of this DeploymentResource.  # noqa: E501
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this DeploymentResource.


        :param space_id: The space_id of this DeploymentResource.  # noqa: E501
        :type: str
        """

        self._space_id = space_id

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this DeploymentResource.  # noqa: E501


        :return: The last_modified_on of this DeploymentResource.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this DeploymentResource.


        :param last_modified_on: The last_modified_on of this DeploymentResource.  # noqa: E501
        :type: datetime
        """

        self._last_modified_on = last_modified_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this DeploymentResource.  # noqa: E501


        :return: The last_modified_by of this DeploymentResource.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this DeploymentResource.


        :param last_modified_by: The last_modified_by of this DeploymentResource.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def links(self):
        """Gets the links of this DeploymentResource.  # noqa: E501


        :return: The links of this DeploymentResource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this DeploymentResource.


        :param links: The links of this DeploymentResource.  # noqa: E501
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
        if issubclass(DeploymentResource, dict):
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
        if not isinstance(other, DeploymentResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
