from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Request(_message.Message):
    __slots__ = ["agent", "auth_token", "bytes_received", "bytes_sent", "category", "connection_id", "content_type", "direction", "duration", "endpoint_id", "id", "method", "path", "status", "tags", "timestamp", "url", "vendor_id"]
    class AuthToken(_message.Message):
        __slots__ = ["hash", "mask", "source", "type"]
        HASH_FIELD_NUMBER: _ClassVar[int]
        MASK_FIELD_NUMBER: _ClassVar[int]
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        hash: str
        mask: str
        source: str
        type: str
        def __init__(self, mask: _Optional[str] = ..., hash: _Optional[str] = ..., source: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...
    AGENT_FIELD_NUMBER: _ClassVar[int]
    AUTH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    BYTES_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    BYTES_SENT_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    VENDOR_ID_FIELD_NUMBER: _ClassVar[int]
    agent: str
    auth_token: Request.AuthToken
    bytes_received: int
    bytes_sent: int
    category: str
    connection_id: str
    content_type: str
    direction: str
    duration: int
    endpoint_id: str
    id: str
    method: str
    path: str
    status: int
    tags: _containers.RepeatedScalarFieldContainer[str]
    timestamp: _timestamp_pb2.Timestamp
    url: str
    vendor_id: str
    def __init__(self, id: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., direction: _Optional[str] = ..., connection_id: _Optional[str] = ..., endpoint_id: _Optional[str] = ..., vendor_id: _Optional[str] = ..., url: _Optional[str] = ..., path: _Optional[str] = ..., method: _Optional[str] = ..., status: _Optional[int] = ..., duration: _Optional[int] = ..., content_type: _Optional[str] = ..., category: _Optional[str] = ..., agent: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., bytes_received: _Optional[int] = ..., bytes_sent: _Optional[int] = ..., auth_token: _Optional[_Union[Request.AuthToken, _Mapping]] = ...) -> None: ...
