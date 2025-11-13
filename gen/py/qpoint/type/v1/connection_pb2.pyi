from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from qpoint.type.v1 import system_pb2 as _system_pb2
from qpoint.type.v1 import tag_pb2 as _tag_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Connection(_message.Message):
    __slots__ = ["id", "timestamp", "direction", "endpoint_id", "vendor_id", "part", "finalized", "tags", "socket_protocol", "l7_protocol", "tls_version", "system", "source", "destination", "bytes_received", "bytes_sent", "tls_probe_types_detected", "tls_probe_introspected", "labels"]
    class System(_message.Message):
        __slots__ = ["hostname", "agent", "agent_instance"]
        HOSTNAME_FIELD_NUMBER: _ClassVar[int]
        AGENT_FIELD_NUMBER: _ClassVar[int]
        AGENT_INSTANCE_FIELD_NUMBER: _ClassVar[int]
        hostname: str
        agent: str
        agent_instance: str
        def __init__(self, hostname: _Optional[str] = ..., agent: _Optional[str] = ..., agent_instance: _Optional[str] = ...) -> None: ...
    class Endpoint(_message.Message):
        __slots__ = ["local", "remote"]
        class Local(_message.Message):
            __slots__ = ["address", "hostname", "exe", "user", "container", "user_id"]
            ADDRESS_FIELD_NUMBER: _ClassVar[int]
            HOSTNAME_FIELD_NUMBER: _ClassVar[int]
            EXE_FIELD_NUMBER: _ClassVar[int]
            USER_FIELD_NUMBER: _ClassVar[int]
            CONTAINER_FIELD_NUMBER: _ClassVar[int]
            USER_ID_FIELD_NUMBER: _ClassVar[int]
            address: _system_pb2.Address
            hostname: str
            exe: str
            user: str
            container: _system_pb2.Container
            user_id: int
            def __init__(self, address: _Optional[_Union[_system_pb2.Address, _Mapping]] = ..., hostname: _Optional[str] = ..., exe: _Optional[str] = ..., user: _Optional[str] = ..., container: _Optional[_Union[_system_pb2.Container, _Mapping]] = ..., user_id: _Optional[int] = ...) -> None: ...
        class Remote(_message.Message):
            __slots__ = ["address"]
            ADDRESS_FIELD_NUMBER: _ClassVar[int]
            address: _system_pb2.Address
            def __init__(self, address: _Optional[_Union[_system_pb2.Address, _Mapping]] = ...) -> None: ...
        LOCAL_FIELD_NUMBER: _ClassVar[int]
        REMOTE_FIELD_NUMBER: _ClassVar[int]
        local: Connection.Endpoint.Local
        remote: Connection.Endpoint.Remote
        def __init__(self, local: _Optional[_Union[Connection.Endpoint.Local, _Mapping]] = ..., remote: _Optional[_Union[Connection.Endpoint.Remote, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    VENDOR_ID_FIELD_NUMBER: _ClassVar[int]
    PART_FIELD_NUMBER: _ClassVar[int]
    FINALIZED_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    SOCKET_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    L7_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    TLS_VERSION_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    BYTES_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    BYTES_SENT_FIELD_NUMBER: _ClassVar[int]
    TLS_PROBE_TYPES_DETECTED_FIELD_NUMBER: _ClassVar[int]
    TLS_PROBE_INTROSPECTED_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    id: str
    timestamp: _timestamp_pb2.Timestamp
    direction: _system_pb2.Direction
    endpoint_id: str
    vendor_id: str
    part: int
    finalized: bool
    tags: _containers.RepeatedCompositeFieldContainer[_tag_pb2.Tag]
    socket_protocol: _system_pb2.SocketProtocol
    l7_protocol: _system_pb2.L7Protocol
    tls_version: _system_pb2.TlsVersion
    system: Connection.System
    source: Connection.Endpoint
    destination: Connection.Endpoint
    bytes_received: int
    bytes_sent: int
    tls_probe_types_detected: _containers.RepeatedScalarFieldContainer[str]
    tls_probe_introspected: bool
    labels: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., direction: _Optional[_Union[_system_pb2.Direction, str]] = ..., endpoint_id: _Optional[str] = ..., vendor_id: _Optional[str] = ..., part: _Optional[int] = ..., finalized: bool = ..., tags: _Optional[_Iterable[_Union[_tag_pb2.Tag, _Mapping]]] = ..., socket_protocol: _Optional[_Union[_system_pb2.SocketProtocol, str]] = ..., l7_protocol: _Optional[_Union[_system_pb2.L7Protocol, str]] = ..., tls_version: _Optional[_Union[_system_pb2.TlsVersion, str]] = ..., system: _Optional[_Union[Connection.System, _Mapping]] = ..., source: _Optional[_Union[Connection.Endpoint, _Mapping]] = ..., destination: _Optional[_Union[Connection.Endpoint, _Mapping]] = ..., bytes_received: _Optional[int] = ..., bytes_sent: _Optional[int] = ..., tls_probe_types_detected: _Optional[_Iterable[str]] = ..., tls_probe_introspected: bool = ..., labels: _Optional[_Iterable[str]] = ...) -> None: ...
