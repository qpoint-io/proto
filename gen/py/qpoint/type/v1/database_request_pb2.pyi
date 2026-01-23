from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DatabaseRequest(_message.Message):
    __slots__ = ["id", "timestamp", "direction", "connection_id", "endpoint_id", "database_type", "statement", "result_type", "is_error", "error_msg", "affected_count", "result_count", "duration", "bytes_received", "bytes_sent", "tags"]
    ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    RESULT_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    AFFECTED_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESULT_COUNT_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    BYTES_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    BYTES_SENT_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    timestamp: _timestamp_pb2.Timestamp
    direction: str
    connection_id: str
    endpoint_id: str
    database_type: str
    statement: str
    result_type: str
    is_error: bool
    error_msg: str
    affected_count: int
    result_count: int
    duration: int
    bytes_received: int
    bytes_sent: int
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., direction: _Optional[str] = ..., connection_id: _Optional[str] = ..., endpoint_id: _Optional[str] = ..., database_type: _Optional[str] = ..., statement: _Optional[str] = ..., result_type: _Optional[str] = ..., is_error: bool = ..., error_msg: _Optional[str] = ..., affected_count: _Optional[int] = ..., result_count: _Optional[int] = ..., duration: _Optional[int] = ..., bytes_received: _Optional[int] = ..., bytes_sent: _Optional[int] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...
