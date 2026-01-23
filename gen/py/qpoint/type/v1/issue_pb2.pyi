from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Issue(_message.Message):
    __slots__ = ["connection_id", "direction", "endpoint_id", "error", "method", "path", "request_id", "status", "tags", "timestamp", "triggers", "url", "vendor_id"]
    class Trigger(_message.Message):
        __slots__ = ["condition", "description", "plugin"]
        CONDITION_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        PLUGIN_FIELD_NUMBER: _ClassVar[int]
        condition: str
        description: str
        plugin: str
        def __init__(self, plugin: _Optional[str] = ..., condition: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    VENDOR_ID_FIELD_NUMBER: _ClassVar[int]
    connection_id: str
    direction: str
    endpoint_id: str
    error: str
    method: str
    path: str
    request_id: str
    status: int
    tags: _containers.RepeatedScalarFieldContainer[str]
    timestamp: _timestamp_pb2.Timestamp
    triggers: _containers.RepeatedCompositeFieldContainer[Issue.Trigger]
    url: str
    vendor_id: str
    def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., connection_id: _Optional[str] = ..., request_id: _Optional[str] = ..., direction: _Optional[str] = ..., endpoint_id: _Optional[str] = ..., vendor_id: _Optional[str] = ..., error: _Optional[str] = ..., url: _Optional[str] = ..., path: _Optional[str] = ..., method: _Optional[str] = ..., status: _Optional[int] = ..., tags: _Optional[_Iterable[str]] = ..., triggers: _Optional[_Iterable[_Union[Issue.Trigger, _Mapping]]] = ...) -> None: ...
