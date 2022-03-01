# Azure Communication Rooms client library for Python
This package contains a Python SDK for Azure Communication Services for Rooms.
Read more about Azure Communication Services [here](https://docs.microsoft.com/azure/communication-services/overview)

## _Disclaimer_

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please 
refer to https://github.com/Azure/azure-sdk-for-python/issues/20691_

## Getting started

### Installating the package

```bash
python -m pip install azure-communication-rooms
```

#### Prequisites

- Python 3.6 or later is required to use this package.
- You need an [Azure subscription][azure_sub] to use this package.
- A deployed Communication Services resource. You can use the [Azure Portal](https://docs.microsoft.com/azure/communication-services/quickstarts/create-communication-resource?tabs=windows&pivots=platform-azp) or the [Azure PowerShell](https://docs.microsoft.com/powershell/module/az.communication/new-azcommunicationservice) to set it up.

#### Create with an Azure Active Directory Credential
To use an [Azure Active Directory (AAD) token credential][authenticate_with_token],
provide an instance of the desired credential type obtained from the
[azure-identity][azure_identity_credentials] library.

To authenticate with AAD, you must first [pip][pip] install [`azure-identity`][azure_identity_pip]

After setup, you can choose which type of [credential][azure_identity_credentials] from azure.identity to use.
As an example, [DefaultAzureCredential][default_azure_credential] can be used to authenticate the client:

Set the values of the client ID, tenant ID, and client secret of the AAD application as environment variables:
`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_CLIENT_SECRET`

Use the returned token credential to authenticate the client:

```python
from azure.communication.rooms import RoomsClient
from azure.identity import DefaultAzureCredential
client = RoomsClient(endpoint='<endpoint>', credential=DefaultAzureCredential())
```
Alternatively you can use Connection String to the deployed resource

```python
from azure.communication.rooms import RoomsClient
from azure.identity import DefaultAzureCredential
client = RoomsClient.from_connection_string(conn_str='<connection_str>' )
```
## Examples

Once the client is initialized, following object can be used to interact with the service:

```python
from azure.communication.rooms import RoomsClient, RoomRequest

room_request = RoomRequest(
    valid_from="start-datetime",
    valid_until="meeting-end-datetime"
    participants={"first-participant":{}, "second-participant":{}},
    )
```
- `valid_from`: A datetime object from which room will start existing
- `valid_until`: A datetime object after which room meeting would end
- `paritcipants`: A dict with MRI's of invitees to the room
All the above attributes are optional. The service provides default values of valid_unti and
valid_from if the are missing.
RoomRequest can be used in following method invokations:

`Create Room`
```python
from azure.communication.rooms import RoomsClient, RoomRequest
from azure.core.exceptions import HttpResponseError

client = RoomsClient.from_connection_string(conn_str='<connection_str>' )
room_request = RoomRequest(
    valid_from="start-datetime",
    valid_until="meeting-end-datetime"
    participants={"first-participant":{}, "second-participant":{}},
    )
try:
    response = client.create_room(room_request=room_request)
except HttpResponseError as e:
    print('service responds error: {}'.format(e.response.json()))

```
`Update Room`
```python
from azure.communication.rooms import RoomsClient, RoomRequest
from azure.core.exceptions import HttpResponseError

client = RoomsClient.from_connection_string(conn_str='<connection_str>' )
update_room_request = RoomRequest(
    valid_from="new-start-datetime",
    valid_until="new-meeting-end-datetime"
    participants={"first-participant":{}, "second-participant":{}},
    )
try:
    response = client.update_room(
        room_id="id of the room to be updated",
        room_request=update_room_request)
except HttpResponseError as e:
    print('service responds error: {}'.format(e.response.json()))

```

`Delete a Room`
```python
from azure.communication.rooms import RoomsClient, RoomRequest
from azure.core.exceptions import HttpResponseError

client = RoomsClient.from_connection_string(conn_str='<connection_str>' )
try:
    client.delete_room(
        room_id="id of the room to be deleted")
except HttpResponseError as e:
    print('service responds error: {}'.format(e.response.json()))

```

### More sample code

Please take a look at the [samples](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/communication/azure-communication-rooms/samples) directory for detailed examples of how to use this library to create and manage rooms.

## Next steps

More examples are coming soon...

## Provide Feedback

If you encounter any bugs or have suggestions, please file an issue in the [Issues](https://github.com/Azure/azure-sdk-for-python/issues) section of the project

## Contributing

This project welcomes contributions and suggestions. Most contributions require
you to agree to a Contributor License Agreement (CLA) declaring that you have
the right to, and actually do, grant us the rights to use your contribution.
For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether
you need to provide a CLA and decorate the PR appropriately (e.g., label,
comment). Simply follow the instructions provided by the bot. You will only
need to do this once across all repos using our CLA.

This project has adopted the
[Microsoft Open Source Code of Conduct][code_of_conduct]. For more information,
see the Code of Conduct FAQ or contact opencode@microsoft.com with any
additional questions or comments.

<!-- LINKS -->
[code_of_conduct]: https://opensource.microsoft.com/codeofconduct/
[authenticate_with_token]: https://docs.microsoft.com/azure/cognitive-services/authentication?tabs=powershell#authenticate-with-an-authentication-token
[azure_identity_credentials]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/identity/azure-identity#credentials
[azure_identity_pip]: https://pypi.org/project/azure-identity/
[default_azure_credential]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/identity/azure-identity#defaultazurecredential
[pip]: https://pypi.org/project/pip/
[azure_sub]: https://azure.microsoft.com/free/
