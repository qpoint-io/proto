from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PIIEntity(_message.Message):
    __slots__ = ["timestamp", "connection_id", "request_id", "endpoint_id", "vendor_id", "tags", "entity_type", "score", "source", "field_path", "value_hash", "request_method", "request_path"]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    VENDOR_ID_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    FIELD_PATH_FIELD_NUMBER: _ClassVar[int]
    VALUE_HASH_FIELD_NUMBER: _ClassVar[int]
    REQUEST_METHOD_FIELD_NUMBER: _ClassVar[int]
    REQUEST_PATH_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    connection_id: str
    request_id: str
    endpoint_id: str
    vendor_id: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    entity_type: str
    score: float
    source: str
    field_path: str
    value_hash: str
    request_method: str
    request_path: str
    def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., connection_id: _Optional[str] = ..., request_id: _Optional[str] = ..., endpoint_id: _Optional[str] = ..., vendor_id: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., entity_type: _Optional[str] = ..., score: _Optional[float] = ..., source: _Optional[str] = ..., field_path: _Optional[str] = ..., value_hash: _Optional[str] = ..., request_method: _Optional[str] = ..., request_path: _Optional[str] = ...) -> None: ...
