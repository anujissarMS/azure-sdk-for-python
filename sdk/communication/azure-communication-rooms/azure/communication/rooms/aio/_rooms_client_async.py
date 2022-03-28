# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from azure.core.tracing.decorator_async import distributed_trace_async
from azure.communication.rooms._models import CommunicationRoom
from .._generated.aio._azure_communication_rooms_service import AzureCommunicationRoomsService
from .._shared.utils import parse_connection_str, get_authentication_policy
from .._version import SDK_MONIKER
from .._generated.models import (
    CreateRoomRequest,
    UpdateRoomRequest
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Dict

class RoomsClient(object):
    """A client to interact with the AzureCommunicationService Rooms gateway.

    This client provides operations to manage rooms.

    :param str endpoint:
        The endpoint url for Azure Communication Service resource.
    :param AsyncTokenCredential credential:
        The AsyncTokenCredential we use to authenticate against the service.
    """
    def __init__(
            self, endpoint, # type: str
            credential, # type: AsyncTokenCredential
            **kwargs # type: Any
    ):
        # type: (...) -> None
        try:
            if not endpoint.lower().startswith('http'):
                endpoint = "https://" + endpoint
        except AttributeError:
            raise ValueError("Account URL must be a string.")

        if not credential:
            raise ValueError(
                "invalid credential from connection string.")

        self._endpoint = endpoint
        self._authentication_policy = get_authentication_policy(endpoint, credential, decode_url=True, is_async=True)
        self._rooms_service_client = AzureCommunicationRoomsService(
            self._endpoint,
            authentication_policy=self._authentication_policy,
            sdk_moniker=SDK_MONIKER,
            **kwargs)

    @classmethod
    def from_connection_string(cls, conn_str,  # type: str
            **kwargs  # type: Any
    ):
        # type: (...) -> RoomsClient
        """Create RoomsClient from a Connection String.

        :param str conn_str:
            A connection string to an Azure Communication Service resource.
        :returns: Instance of RoomsClient.
        :rtype: ~azure.communication.RoomsClient

        .. admonition:: Example:

            .. literalinclude:: ../samples/Rooms_sample.py
                :start-after: [START auth_from_connection_string]
                :end-before: [END auth_from_connection_string]
                :language: python
                :dedent: 8
                :caption: Creating the RoomsClient from a connection string.
        """
        endpoint, access_key = parse_connection_str(conn_str)

        return cls(endpoint, access_key, **kwargs)

    @distributed_trace_async
    async def create_room(
        self,
        valid_from=None, # type: Optional[datetime]
        valid_until=None, # type: Optional[datetime]
        participants=None, # type: Optional[Dict[str, Any]]
        **kwargs
    ):
        # type: (...) -> CommunicationRoom
        """Create a new room.

        :param valid_from: The timestamp from when the room is open for joining. The timestamp is in
         RFC3339 format: ``yyyy-MM-ddTHH:mm:ssZ``.
        :type valid_from: ~datetime
        :param valid_until: The timestamp from when the room can no longer be joined. The timestamp
         is in RFC3339 format: ``yyyy-MM-ddTHH:mm:ssZ``.
        :type valid_until: ~datetime
        :keyword participants: (Optional) Collection of identities invited to the room.
        :paramtype participants: dict[str, any]
        :returns: Created room.
        :rtype: ~azure.communication.rooms.CommunicationRoom
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        create_room_request = CreateRoomRequest(
            valid_from=valid_from,
            valid_until=valid_until,
            participants=participants
        )
        create_room_response = await self._rooms_service_client.rooms.create_room(
            create_room_request=create_room_request, **kwargs)
        return CommunicationRoom.from_create_room_response(create_room_response)

    @distributed_trace_async
    async def delete_room(
        self,
        room_id, # type: str
        **kwargs
    ):
        # type: (...) -> None
        """Delete room.

        :param room_id: Required. Id of room to be deleted
        :type room_id: str
        :returns: None.
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError

        """
        await self._rooms_service_client.rooms.delete_room(room_id=room_id, **kwargs)

    @distributed_trace_async
    async def update_room(
        self,
        room_id,
        valid_from=None, # type: Optional[datetime]
        valid_until=None, # type: Optional[datetime]
        **kwargs
    ):
        # type: (...) -> CommunicationRoom
        """Update a valid room's attributes

        :param room_id: Required. Id of room to be updated
        :type room_id: str
        :param valid_from: The timestamp from when the room is open for joining. The timestamp is in
         RFC3339 format: ``yyyy-MM-ddTHH:mm:ssZ``.
        :type valid_from: ~datetime
        :param valid_until: The timestamp from when the room can no longer be joined. The timestamp
         is in RFC3339 format: ``yyyy-MM-ddTHH:mm:ssZ``.
        :type valid_until: ~datetime
        :returns: Updated room.
        :rtype: ~azure.communication.rooms.CommunicationRoom
        :raises: ~azure.core.exceptions.HttpResponseError, ValueError

        """
        update_room_request = UpdateRoomRequest(
            valid_from=valid_from,
            valid_until=valid_until
        )
        update_room_response = await self._rooms_service_client.rooms.update_room(
            room_id=room_id, update_room_request=update_room_request, **kwargs)
        return CommunicationRoom.from_update_room_response(update_room_response)

    @distributed_trace_async
    async def get_room(
        self,
        room_id, # type: str
        **kwargs
    ):
        # type: (...) -> CommunicationRoom
        """Get a valid room

        :param room_id: Required. Id of room to be fetched
        :type room_id: str
        :returns: Room with current attributes.
        :rtype: ~azure.communication.rooms.CommunicationRoom
        :raises: ~azure.core.exceptions.HttpResponseError

        """
        get_room_response = await self._rooms_service_client.rooms.get_room(room_id=room_id, **kwargs)
        return CommunicationRoom.from_get_room_response(get_room_response)

    @distributed_trace_async
    async def add_participants(
        self,
        room_id, # type: str
        participants, # type: dict[str, Any]
        **kwargs
    ):
        # type: (...) -> CommunicationRoom
        """Add participants to a room
        :param room_id: Required. Id of room to be updated
        :type room_id: str
        :param participants: Required. Collection of identities invited to the room.
        :paramtype participants: dict[str, any]
        :returns: Updated room.
        :rtype: ~azure.communication.rooms.CommunicationRoom
        :raises: ~azure.core.exceptions.HttpResponseError, ValueError
        """
        update_room_request = UpdateRoomRequest(
            participants=participants
        )
        update_room_response = await self._rooms_service_client.rooms.update_room(
            room_id=room_id, update_room_request=update_room_request, **kwargs)
        return CommunicationRoom.from_update_room_response(update_room_response)

    @distributed_trace_async
    async def remove_participants(
        self,
        room_id, # type: str
        participants, # type: dict[str, Any]
        **kwargs
    ):
        # type: (...) -> CommunicationRoom
        """Remove participants from a room
        :param room_id: Required. Id of room to be updated
        :type room_id: str
        :param participants: Required. Collection of identities invited to the room.
        :paramtype participants: dict[str, any]
        :returns: Updated room.
        :rtype: ~azure.communication.rooms.CommunicationRoom
        :raises: ~azure.core.exceptions.HttpResponseError, ValueError
        """
        # set participants object to None
        for identity in participants.keys():
            participants[identity] = None
        update_room_request = UpdateRoomRequest(
            participants=participants
        )
        update_room_response = await self._rooms_service_client.rooms.update_room(
            room_id=room_id, update_room_request=update_room_request, **kwargs)
        return CommunicationRoom.from_update_room_response(update_room_response)

    @distributed_trace_async
    async def remove_all_participants(
        self,
        room_id, # type: str
        **kwargs
    ):
        # type: (...) -> CommunicationRoom
        """Remove all participants from a room
        :param room_id: Required. Id of room to be updated
        :type room_id: str
        :returns: Updated room.
        :rtype: ~azure.communication.rooms.CommunicationRoom
        :raises: ~azure.core.exceptions.HttpResponseError, ValueError
        """
        update_room_request = UpdateRoomRequest(
            participants={}
        )
        update_room_response = await self._rooms_service_client.rooms.update_room(
            room_id=room_id, update_room_request=update_room_request, **kwargs)
        return CommunicationRoom.from_update_room_response(update_room_response)

    async def __aenter__(self) -> "RoomsClient":
        await self._rooms_service_client.__aenter__()
        return self

    async def __aexit__(self, *args: "Any") -> None:
        await self.close()

    async def close(self) -> None:
        """Close the :class:
        `~azure.communication.rooms.aio.RoomsClient` session.
        """
        await self._rooms_service_client.__aexit__()
