from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RedisRequest(_message.Message):
    __slots__ = ["arg_count", "args", "bytes_received", "bytes_sent", "command", "connection_id", "direction", "duration", "endpoint_id", "error_msg", "id", "is_error", "key_pattern", "result_type", "tags", "timestamp"]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    ARG_COUNT_FIELD_NUMBER: _ClassVar[int]
    BYTES_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    BYTES_SENT_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_ERROR_FIELD_NUMBER: _ClassVar[int]
    KEY_PATTERN_FIELD_NUMBER: _ClassVar[int]
    RESULT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    arg_count: int
    args: _containers.RepeatedScalarFieldContainer[str]
    bytes_received: int
    bytes_sent: int
    command: str
    connection_id: str
    direction: str
    duration: int
    endpoint_id: str
    error_msg: str
    id: str
    is_error: bool
    key_pattern: str
    result_type: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., direction: _Optional[str] = ..., connection_id: _Optional[str] = ..., endpoint_id: _Optional[str] = ..., command: _Optional[str] = ..., args: _Optional[_Iterable[str]] = ..., arg_count: _Optional[int] = ..., result_type: _Optional[str] = ..., is_error: bool = ..., error_msg: _Optional[str] = ..., duration: _Optional[int] = ..., bytes_received: _Optional[int] = ..., bytes_sent: _Optional[int] = ..., key_pattern: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...
