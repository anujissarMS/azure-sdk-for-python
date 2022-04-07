# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from msrest import Serializer

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace

from .. import models as _models
from .._vendor import _convert_request, _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Optional, TypeVar
    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False
# fmt: off

def build_create_room_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2022-02-01")  # type: str
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json, text/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/rooms")

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        _header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_get_room_request(
    room_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2022-02-01")  # type: str

    accept = "application/json, text/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/rooms/{roomId}")
    path_format_arguments = {
        "roomId": _SERIALIZER.url("room_id", room_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_update_room_request(
    room_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2022-02-01")  # type: str
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json, text/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/rooms/{roomId}")
    path_format_arguments = {
        "roomId": _SERIALIZER.url("room_id", room_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        _header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PATCH",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_delete_room_request(
    room_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2022-02-01")  # type: str

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/rooms/{roomId}")
    path_format_arguments = {
        "roomId": _SERIALIZER.url("room_id", room_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )

# fmt: on
class RoomsOperations(object):
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.communication.rooms.AzureCommunicationRoomsService`'s
        :attr:`rooms` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        args = list(args)
        self._client = args.pop(0) if args else kwargs.pop("client")
        self._config = args.pop(0) if args else kwargs.pop("config")
        self._serialize = args.pop(0) if args else kwargs.pop("serializer")
        self._deserialize = args.pop(0) if args else kwargs.pop("deserializer")


    @distributed_trace
    def create_room(
        self,
        create_room_request=None,  # type: Optional["_models.CreateRoomRequest"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.CreateRoomResponse"
        """Creates a new room.

        Creates a new room.

        :param create_room_request: The create room request body. Default value is None.
        :type create_room_request: ~azure.communication.rooms.models.CreateRoomRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CreateRoomResponse, or the result of cls(response)
        :rtype: ~azure.communication.rooms.models.CreateRoomResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.CreateRoomResponse"]
        error_map = {
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            401: lambda response: ClientAuthenticationError(response=response, model=self._deserialize(_models.CommunicationErrorResponse, response)),
            403: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.CommunicationErrorResponse, response)),
            500: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.CommunicationErrorResponse, response)),
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2022-02-01")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        if create_room_request is not None:
            _json = self._serialize.body(create_room_request, 'CreateRoomRequest')
        else:
            _json = None

        request = build_create_room_request(
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.create_room.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('CreateRoomResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_room.metadata = {'url': "/rooms"}  # type: ignore


    @distributed_trace
    def get_room(
        self,
        room_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.RoomModel"
        """Retrieves an existing room by Id.

        Retrieves an existing room by Id.

        :param room_id: The id of the room requested.
        :type room_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RoomModel, or the result of cls(response)
        :rtype: ~azure.communication.rooms.models.RoomModel
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.RoomModel"]
        error_map = {
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            401: lambda response: ClientAuthenticationError(response=response, model=self._deserialize(_models.CommunicationErrorResponse, response)),
            403: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.CommunicationErrorResponse, response)),
            500: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.CommunicationErrorResponse, response)),
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2022-02-01")  # type: str

        
        request = build_get_room_request(
            room_id=room_id,
            api_version=api_version,
            template_url=self.get_room.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('RoomModel', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_room.metadata = {'url': "/rooms/{roomId}"}  # type: ignore


    @distributed_trace
    def update_room(
        self,
        room_id,  # type: str
        patch_room_request=None,  # type: Optional["_models.UpdateRoomRequest"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.UpdateRoomResponse"
        """Update a room with given changes.

        Update a room with given changes.

        :param room_id: The id of the room requested.
        :type room_id: str
        :param patch_room_request:  Default value is None.
        :type patch_room_request: ~azure.communication.rooms.models.UpdateRoomRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: UpdateRoomResponse, or the result of cls(response)
        :rtype: ~azure.communication.rooms.models.UpdateRoomResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.UpdateRoomResponse"]
        error_map = {
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            401: lambda response: ClientAuthenticationError(response=response, model=self._deserialize(_models.CommunicationErrorResponse, response)),
            403: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.CommunicationErrorResponse, response)),
            500: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.CommunicationErrorResponse, response)),
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2022-02-01")  # type: str
        content_type = kwargs.pop('content_type', "application/merge-patch+json")  # type: Optional[str]

        if patch_room_request is not None:
            _json = self._serialize.body(patch_room_request, 'UpdateRoomRequest')
        else:
            _json = None

        request = build_update_room_request(
            room_id=room_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.update_room.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('UpdateRoomResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update_room.metadata = {'url': "/rooms/{roomId}"}  # type: ignore


    @distributed_trace
    def delete_room(  # pylint: disable=inconsistent-return-statements
        self,
        room_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete a room.

        Delete a room.

        :param room_id: The id of the room requested.
        :type room_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            401: lambda response: ClientAuthenticationError(response=response, model=self._deserialize(_models.CommunicationErrorResponse, response)),
            403: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.CommunicationErrorResponse, response)),
            500: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.CommunicationErrorResponse, response)),
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2022-02-01")  # type: str

        
        request = build_delete_room_request(
            room_id=room_id,
            api_version=api_version,
            template_url=self.delete_room.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    delete_room.metadata = {'url': "/rooms/{roomId}"}  # type: ignore

