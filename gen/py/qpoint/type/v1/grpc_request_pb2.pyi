from qpoint.type.v1 import request_pb2 as _request_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GrpcRequest(_message.Message):
    __slots__ = ["request", "grpc_service", "grpc_method", "grpc_status", "grpc_status_name", "grpc_message"]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    GRPC_SERVICE_FIELD_NUMBER: _ClassVar[int]
    GRPC_METHOD_FIELD_NUMBER: _ClassVar[int]
    GRPC_STATUS_FIELD_NUMBER: _ClassVar[int]
    GRPC_STATUS_NAME_FIELD_NUMBER: _ClassVar[int]
    GRPC_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    request: _request_pb2.Request
    grpc_service: str
    grpc_method: str
    grpc_status: str
    grpc_status_name: str
    grpc_message: str
    def __init__(self, request: _Optional[_Union[_request_pb2.Request, _Mapping]] = ..., grpc_service: _Optional[str] = ..., grpc_method: _Optional[str] = ..., grpc_status: _Optional[str] = ..., grpc_status_name: _Optional[str] = ..., grpc_message: _Optional[str] = ...) -> None: ...
