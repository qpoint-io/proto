from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PIIEntity(_message.Message):
    __slots__ = ["connection_id", "endpoint_id", "entity_type", "field_path", "request_id", "request_method", "request_path", "score", "source", "tags", "timestamp", "value_hash", "vendor_id"]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    FIELD_PATH_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_METHOD_FIELD_NUMBER: _ClassVar[int]
    REQUEST_PATH_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    VALUE_HASH_FIELD_NUMBER: _ClassVar[int]
    VENDOR_ID_FIELD_NUMBER: _ClassVar[int]
    connection_id: str
    endpoint_id: str
    entity_type: str
    field_path: str
    request_id: str
    request_method: str
    request_path: str
    score: float
    source: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    timestamp: _timestamp_pb2.Timestamp
    value_hash: str
    vendor_id: str
    def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., connection_id: _Optional[str] = ..., request_id: _Optional[str] = ..., endpoint_id: _Optional[str] = ..., vendor_id: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., entity_type: _Optional[str] = ..., score: _Optional[float] = ..., source: _Optional[str] = ..., field_path: _Optional[str] = ..., value_hash: _Optional[str] = ..., request_method: _Optional[str] = ..., request_path: _Optional[str] = ...) -> None: ...
