# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class Resource(Model):
    """Resource.

    Common fields that are returned in the response for all Azure Resource
    Manager resources.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. E.g.
     "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class AzureEntityResource(Resource):
    """Entity Resource.

    The resource model definition for an Azure Resource Manager resource with
    an etag.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. E.g.
     "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
    :vartype type: str
    :ivar etag: Resource Etag.
    :vartype etag: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(AzureEntityResource, self).__init__(**kwargs)
        self.etag = None


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class TrackedResource(Resource):
    """Tracked Resource.

    The resource model definition for an Azure Resource Manager tracked top
    level resource which has 'tags' and a 'location'.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. E.g.
     "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives
    :type location: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(self, *, location: str, tags=None, **kwargs) -> None:
        super(TrackedResource, self).__init__(**kwargs)
        self.tags = tags
        self.location = location


class Creator(TrackedResource):
    """An Azure resource which represents Maps Creator product and provides
    ability to manage private location data.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. E.g.
     "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives
    :type location: str
    :param properties: Required. The Creator resource properties.
    :type properties: ~azure.mgmt.maps.models.CreatorProperties
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'properties': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'CreatorProperties'},
    }

    def __init__(self, *, location: str, properties, tags=None, **kwargs) -> None:
        super(Creator, self).__init__(tags=tags, location=location, **kwargs)
        self.properties = properties


class CreatorProperties(Model):
    """Creator resource properties.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar provisioning_state: The state of the resource provisioning, terminal
     states: Succeeded, Failed, Canceled
    :vartype provisioning_state: str
    :param storage_units: Required. The storage units to be allocated. Integer
     values from 1 to 100, inclusive.
    :type storage_units: int
    """

    _validation = {
        'provisioning_state': {'readonly': True},
        'storage_units': {'required': True, 'maximum': 100, 'minimum': 1},
    }

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'storage_units': {'key': 'storageUnits', 'type': 'int'},
    }

    def __init__(self, *, storage_units: int, **kwargs) -> None:
        super(CreatorProperties, self).__init__(**kwargs)
        self.provisioning_state = None
        self.storage_units = storage_units


class CreatorUpdateParameters(Model):
    """Parameters used to update an existing Creator resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param tags: Gets or sets a list of key value pairs that describe the
     resource. These tags can be used in viewing and grouping this resource
     (across resource groups). A maximum of 15 tags can be provided for a
     resource. Each tag must have a key no greater than 128 characters and
     value no greater than 256 characters.
    :type tags: dict[str, str]
    :ivar provisioning_state: The state of the resource provisioning, terminal
     states: Succeeded, Failed, Canceled
    :vartype provisioning_state: str
    :param storage_units: Required. The storage units to be allocated. Integer
     values from 1 to 100, inclusive.
    :type storage_units: int
    """

    _validation = {
        'provisioning_state': {'readonly': True},
        'storage_units': {'required': True, 'maximum': 100, 'minimum': 1},
    }

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'storage_units': {'key': 'properties.storageUnits', 'type': 'int'},
    }

    def __init__(self, *, storage_units: int, tags=None, **kwargs) -> None:
        super(CreatorUpdateParameters, self).__init__(**kwargs)
        self.tags = tags
        self.provisioning_state = None
        self.storage_units = storage_units


class Dimension(Model):
    """Dimension of map account, for example API Category, Api Name, Result Type,
    and Response Code.

    :param name: Display name of dimension.
    :type name: str
    :param display_name: Display name of dimension.
    :type display_name: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
    }

    def __init__(self, *, name: str=None, display_name: str=None, **kwargs) -> None:
        super(Dimension, self).__init__(**kwargs)
        self.name = name
        self.display_name = display_name


class ErrorAdditionalInfo(Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: object
    """

    _validation = {
        'type': {'readonly': True},
        'info': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'info': {'key': 'info', 'type': 'object'},
    }

    def __init__(self, **kwargs) -> None:
        super(ErrorAdditionalInfo, self).__init__(**kwargs)
        self.type = None
        self.info = None


class ErrorDetail(Model):
    """The error detail.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~azure.mgmt.maps.models.ErrorDetail]
    :ivar additional_info: The error additional info.
    :vartype additional_info:
     list[~azure.mgmt.maps.models.ErrorAdditionalInfo]
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'target': {'readonly': True},
        'details': {'readonly': True},
        'additional_info': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorDetail]'},
        'additional_info': {'key': 'additionalInfo', 'type': '[ErrorAdditionalInfo]'},
    }

    def __init__(self, **kwargs) -> None:
        super(ErrorDetail, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class ErrorResponse(Model):
    """Error response.

    Common error response for all Azure Resource Manager APIs to return error
    details for failed operations. (This also follows the OData error response
    format.).

    :param error: The error object.
    :type error: ~azure.mgmt.maps.models.ErrorDetail
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDetail'},
    }

    def __init__(self, *, error=None, **kwargs) -> None:
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = error


class ErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorResponseException, self).__init__(deserialize, response, 'ErrorResponse', *args)


class MapsAccount(TrackedResource):
    """An Azure resource which represents access to a suite of Maps REST APIs.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. E.g.
     "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives
    :type location: str
    :param sku: Required. The SKU of this account.
    :type sku: ~azure.mgmt.maps.models.Sku
    :param kind: Get or Set Kind property. Possible values include: 'Gen1',
     'Gen2'. Default value: "Gen1" .
    :type kind: str or ~azure.mgmt.maps.models.Kind
    :ivar system_data: The system meta data relating to this resource.
    :vartype system_data: ~azure.mgmt.maps.models.SystemData
    :param properties: The map account properties.
    :type properties: ~azure.mgmt.maps.models.MapsAccountProperties
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'sku': {'required': True},
        'system_data': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'kind': {'key': 'kind', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'properties': {'key': 'properties', 'type': 'MapsAccountProperties'},
    }

    def __init__(self, *, location: str, sku, tags=None, kind="Gen1", properties=None, **kwargs) -> None:
        super(MapsAccount, self).__init__(tags=tags, location=location, **kwargs)
        self.sku = sku
        self.kind = kind
        self.system_data = None
        self.properties = properties


class MapsAccountKeys(Model):
    """The set of keys which can be used to access the Maps REST APIs. Two keys
    are provided for key rotation without interruption.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar primary_key_last_updated: The last updated date and time of the
     primary key.
    :vartype primary_key_last_updated: str
    :ivar primary_key: The primary key for accessing the Maps REST APIs.
    :vartype primary_key: str
    :ivar secondary_key: The secondary key for accessing the Maps REST APIs.
    :vartype secondary_key: str
    :ivar secondary_key_last_updated: The last updated date and time of the
     secondary key.
    :vartype secondary_key_last_updated: str
    """

    _validation = {
        'primary_key_last_updated': {'readonly': True},
        'primary_key': {'readonly': True},
        'secondary_key': {'readonly': True},
        'secondary_key_last_updated': {'readonly': True},
    }

    _attribute_map = {
        'primary_key_last_updated': {'key': 'primaryKeyLastUpdated', 'type': 'str'},
        'primary_key': {'key': 'primaryKey', 'type': 'str'},
        'secondary_key': {'key': 'secondaryKey', 'type': 'str'},
        'secondary_key_last_updated': {'key': 'secondaryKeyLastUpdated', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(MapsAccountKeys, self).__init__(**kwargs)
        self.primary_key_last_updated = None
        self.primary_key = None
        self.secondary_key = None
        self.secondary_key_last_updated = None


class MapsAccountProperties(Model):
    """Additional Map account properties.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar unique_id: A unique identifier for the maps account
    :vartype unique_id: str
    :param disable_local_auth: Allows toggle functionality on Azure Policy to
     disable Azure Maps local authentication support. This will disable Shared
     Keys authentication from any usage. Default value: False .
    :type disable_local_auth: bool
    :ivar provisioning_state: the state of the provisioning.
    :vartype provisioning_state: str
    """

    _validation = {
        'unique_id': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'unique_id': {'key': 'uniqueId', 'type': 'str'},
        'disable_local_auth': {'key': 'disableLocalAuth', 'type': 'bool'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
    }

    def __init__(self, *, disable_local_auth: bool=False, **kwargs) -> None:
        super(MapsAccountProperties, self).__init__(**kwargs)
        self.unique_id = None
        self.disable_local_auth = disable_local_auth
        self.provisioning_state = None


class MapsAccountUpdateParameters(Model):
    """Parameters used to update an existing Maps Account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param tags: Gets or sets a list of key value pairs that describe the
     resource. These tags can be used in viewing and grouping this resource
     (across resource groups). A maximum of 15 tags can be provided for a
     resource. Each tag must have a key no greater than 128 characters and
     value no greater than 256 characters.
    :type tags: dict[str, str]
    :param kind: Get or Set Kind property. Possible values include: 'Gen1',
     'Gen2'. Default value: "Gen1" .
    :type kind: str or ~azure.mgmt.maps.models.Kind
    :param sku: The SKU of this account.
    :type sku: ~azure.mgmt.maps.models.Sku
    :ivar unique_id: A unique identifier for the maps account
    :vartype unique_id: str
    :param disable_local_auth: Allows toggle functionality on Azure Policy to
     disable Azure Maps local authentication support. This will disable Shared
     Keys authentication from any usage. Default value: False .
    :type disable_local_auth: bool
    :ivar provisioning_state: the state of the provisioning.
    :vartype provisioning_state: str
    """

    _validation = {
        'unique_id': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'kind': {'key': 'kind', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'unique_id': {'key': 'properties.uniqueId', 'type': 'str'},
        'disable_local_auth': {'key': 'properties.disableLocalAuth', 'type': 'bool'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, *, tags=None, kind="Gen1", sku=None, disable_local_auth: bool=False, **kwargs) -> None:
        super(MapsAccountUpdateParameters, self).__init__(**kwargs)
        self.tags = tags
        self.kind = kind
        self.sku = sku
        self.unique_id = None
        self.disable_local_auth = disable_local_auth
        self.provisioning_state = None


class MapsKeySpecification(Model):
    """Whether the operation refers to the primary or secondary key.

    All required parameters must be populated in order to send to Azure.

    :param key_type: Required. Whether the operation refers to the primary or
     secondary key. Possible values include: 'primary', 'secondary'
    :type key_type: str or ~azure.mgmt.maps.models.KeyType
    """

    _validation = {
        'key_type': {'required': True},
    }

    _attribute_map = {
        'key_type': {'key': 'keyType', 'type': 'str'},
    }

    def __init__(self, *, key_type, **kwargs) -> None:
        super(MapsKeySpecification, self).__init__(**kwargs)
        self.key_type = key_type


class MetricSpecification(Model):
    """Metric specification of operation.

    :param name: Name of metric specification.
    :type name: str
    :param display_name: Display name of metric specification.
    :type display_name: str
    :param display_description: Display description of metric specification.
    :type display_description: str
    :param unit: Unit could be Count.
    :type unit: str
    :param dimensions: Dimensions of map account.
    :type dimensions: list[~azure.mgmt.maps.models.Dimension]
    :param aggregation_type: Aggregation type could be Average.
    :type aggregation_type: str
    :param fill_gap_with_zero: The property to decide fill gap with zero or
     not.
    :type fill_gap_with_zero: bool
    :param category: The category this metric specification belong to, could
     be Capacity.
    :type category: str
    :param resource_id_dimension_name_override: Account Resource Id.
    :type resource_id_dimension_name_override: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'display_description': {'key': 'displayDescription', 'type': 'str'},
        'unit': {'key': 'unit', 'type': 'str'},
        'dimensions': {'key': 'dimensions', 'type': '[Dimension]'},
        'aggregation_type': {'key': 'aggregationType', 'type': 'str'},
        'fill_gap_with_zero': {'key': 'fillGapWithZero', 'type': 'bool'},
        'category': {'key': 'category', 'type': 'str'},
        'resource_id_dimension_name_override': {'key': 'resourceIdDimensionNameOverride', 'type': 'str'},
    }

    def __init__(self, *, name: str=None, display_name: str=None, display_description: str=None, unit: str=None, dimensions=None, aggregation_type: str=None, fill_gap_with_zero: bool=None, category: str=None, resource_id_dimension_name_override: str=None, **kwargs) -> None:
        super(MetricSpecification, self).__init__(**kwargs)
        self.name = name
        self.display_name = display_name
        self.display_description = display_description
        self.unit = unit
        self.dimensions = dimensions
        self.aggregation_type = aggregation_type
        self.fill_gap_with_zero = fill_gap_with_zero
        self.category = category
        self.resource_id_dimension_name_override = resource_id_dimension_name_override


class OperationDetail(Model):
    """Operation detail payload.

    :param name: Name of the operation
    :type name: str
    :param is_data_action: Indicates whether the operation is a data action
    :type is_data_action: bool
    :param display: Display of the operation
    :type display: ~azure.mgmt.maps.models.OperationDisplay
    :param origin: Origin of the operation
    :type origin: str
    :param service_specification: One property of operation, include metric
     specifications.
    :type service_specification: ~azure.mgmt.maps.models.ServiceSpecification
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'is_data_action': {'key': 'isDataAction', 'type': 'bool'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
        'origin': {'key': 'origin', 'type': 'str'},
        'service_specification': {'key': 'properties.serviceSpecification', 'type': 'ServiceSpecification'},
    }

    def __init__(self, *, name: str=None, is_data_action: bool=None, display=None, origin: str=None, service_specification=None, **kwargs) -> None:
        super(OperationDetail, self).__init__(**kwargs)
        self.name = name
        self.is_data_action = is_data_action
        self.display = display
        self.origin = origin
        self.service_specification = service_specification


class OperationDisplay(Model):
    """Operation display payload.

    :param provider: Resource provider of the operation
    :type provider: str
    :param resource: Resource of the operation
    :type resource: str
    :param operation: Localized friendly name for the operation
    :type operation: str
    :param description: Localized friendly description for the operation
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, *, provider: str=None, resource: str=None, operation: str=None, description: str=None, **kwargs) -> None:
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation
        self.description = description


class ProxyResource(Resource):
    """Proxy Resource.

    The resource model definition for a Azure Resource Manager proxy resource.
    It will not have tags and a location.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. E.g.
     "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(ProxyResource, self).__init__(**kwargs)


class ServiceSpecification(Model):
    """One property of operation, include metric specifications.

    :param metric_specifications: Metric specifications of operation.
    :type metric_specifications:
     list[~azure.mgmt.maps.models.MetricSpecification]
    """

    _attribute_map = {
        'metric_specifications': {'key': 'metricSpecifications', 'type': '[MetricSpecification]'},
    }

    def __init__(self, *, metric_specifications=None, **kwargs) -> None:
        super(ServiceSpecification, self).__init__(**kwargs)
        self.metric_specifications = metric_specifications


class Sku(Model):
    """The SKU of the Maps Account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the SKU, in standard format (such as
     S0). Possible values include: 'S0', 'S1', 'G2'
    :type name: str or ~azure.mgmt.maps.models.Name
    :ivar tier: Gets the sku tier. This is based on the SKU name.
    :vartype tier: str
    """

    _validation = {
        'name': {'required': True},
        'tier': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
    }

    def __init__(self, *, name, **kwargs) -> None:
        super(Sku, self).__init__(**kwargs)
        self.name = name
        self.tier = None


class SystemData(Model):
    """Metadata pertaining to creation and last modification of the resource.

    :param created_by: The identity that created the resource.
    :type created_by: str
    :param created_by_type: The type of identity that created the resource.
     Possible values include: 'User', 'Application', 'ManagedIdentity', 'Key'
    :type created_by_type: str or ~azure.mgmt.maps.models.CreatedByType
    :param created_at: The timestamp of resource creation (UTC).
    :type created_at: datetime
    :param last_modified_by: The identity that last modified the resource.
    :type last_modified_by: str
    :param last_modified_by_type: The type of identity that last modified the
     resource. Possible values include: 'User', 'Application',
     'ManagedIdentity', 'Key'
    :type last_modified_by_type: str or ~azure.mgmt.maps.models.CreatedByType
    :param last_modified_at: The timestamp of resource last modification (UTC)
    :type last_modified_at: datetime
    """

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'str'},
        'created_by_type': {'key': 'createdByType', 'type': 'str'},
        'created_at': {'key': 'createdAt', 'type': 'iso-8601'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'str'},
        'last_modified_by_type': {'key': 'lastModifiedByType', 'type': 'str'},
        'last_modified_at': {'key': 'lastModifiedAt', 'type': 'iso-8601'},
    }

    def __init__(self, *, created_by: str=None, created_by_type=None, created_at=None, last_modified_by: str=None, last_modified_by_type=None, last_modified_at=None, **kwargs) -> None:
        super(SystemData, self).__init__(**kwargs)
        self.created_by = created_by
        self.created_by_type = created_by_type
        self.created_at = created_at
        self.last_modified_by = last_modified_by
        self.last_modified_by_type = last_modified_by_type
        self.last_modified_at = last_modified_at
