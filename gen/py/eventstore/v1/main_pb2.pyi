from qpoint.type.v1 import artifact_pb2 as _artifact_pb2
from qpoint.type.v1 import connection_pb2 as _connection_pb2
from qpoint.type.v1 import issue_pb2 as _issue_pb2
from qpoint.type.v1 import pii_pb2 as _pii_pb2
from qpoint.type.v1 import request_pb2 as _request_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PingRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PingResponse(_message.Message):
    __slots__ = ["org_id"]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class Event(_message.Message):
    __slots__ = ["request", "issue", "artifact", "pii_entity", "connection"]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    ISSUE_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_FIELD_NUMBER: _ClassVar[int]
    PII_ENTITY_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    request: _request_pb2.Request
    issue: _issue_pb2.Issue
    artifact: _artifact_pb2.Artifact
    pii_entity: _pii_pb2.PIIEntity
    connection: _connection_pb2.Connection
    def __init__(self, request: _Optional[_Union[_request_pb2.Request, _Mapping]] = ..., issue: _Optional[_Union[_issue_pb2.Issue, _Mapping]] = ..., artifact: _Optional[_Union[_artifact_pb2.Artifact, _Mapping]] = ..., pii_entity: _Optional[_Union[_pii_pb2.PIIEntity, _Mapping]] = ..., connection: _Optional[_Union[_connection_pb2.Connection, _Mapping]] = ...) -> None: ...

class IngestRequest(_message.Message):
    __slots__ = ["events"]
    class Event(_message.Message):
        __slots__ = ["request", "issue", "artifact", "pii_entity", "connection"]
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        ISSUE_FIELD_NUMBER: _ClassVar[int]
        ARTIFACT_FIELD_NUMBER: _ClassVar[int]
        PII_ENTITY_FIELD_NUMBER: _ClassVar[int]
        CONNECTION_FIELD_NUMBER: _ClassVar[int]
        request: _request_pb2.Request
        issue: _issue_pb2.Issue
        artifact: _artifact_pb2.Artifact
        pii_entity: _pii_pb2.PIIEntity
        connection: _connection_pb2.Connection
        def __init__(self, request: _Optional[_Union[_request_pb2.Request, _Mapping]] = ..., issue: _Optional[_Union[_issue_pb2.Issue, _Mapping]] = ..., artifact: _Optional[_Union[_artifact_pb2.Artifact, _Mapping]] = ..., pii_entity: _Optional[_Union[_pii_pb2.PIIEntity, _Mapping]] = ..., connection: _Optional[_Union[_connection_pb2.Connection, _Mapping]] = ...) -> None: ...
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[IngestRequest.Event]
    def __init__(self, events: _Optional[_Iterable[_Union[IngestRequest.Event, _Mapping]]] = ...) -> None: ...

class IngestResponse(_message.Message):
    __slots__ = ["total_accepted_count", "accepted_count"]
    TOTAL_ACCEPTED_COUNT_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_COUNT_FIELD_NUMBER: _ClassVar[int]
    total_accepted_count: int
    accepted_count: int
    def __init__(self, total_accepted_count: _Optional[int] = ..., accepted_count: _Optional[int] = ...) -> None: ...

class IngestBatchRequest(_message.Message):
    __slots__ = ["events"]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[Event]
    def __init__(self, events: _Optional[_Iterable[_Union[Event, _Mapping]]] = ...) -> None: ...

class IngestBatchResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
