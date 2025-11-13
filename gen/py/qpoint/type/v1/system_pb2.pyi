from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Direction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DIRECTION_UNSPECIFIED: _ClassVar[Direction]
    DIRECTION_INGRESS: _ClassVar[Direction]
    DIRECTION_EGRESS: _ClassVar[Direction]
    DIRECTION_EGRESS_INTERNAL: _ClassVar[Direction]
    DIRECTION_EGRESS_EXTERNAL: _ClassVar[Direction]

class TlsVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    TLS_VERSION_UNSPECIFIED: _ClassVar[TlsVersion]
    TLS_VERSION_V1_0: _ClassVar[TlsVersion]
    TLS_VERSION_V1_1: _ClassVar[TlsVersion]
    TLS_VERSION_V1_2: _ClassVar[TlsVersion]
    TLS_VERSION_V1_3: _ClassVar[TlsVersion]

class SocketProtocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SOCKET_PROTOCOL_UNSPECIFIED: _ClassVar[SocketProtocol]
    SOCKET_PROTOCOL_TCP: _ClassVar[SocketProtocol]
    SOCKET_PROTOCOL_UDP: _ClassVar[SocketProtocol]
    SOCKET_PROTOCOL_ICMP: _ClassVar[SocketProtocol]
    SOCKET_PROTOCOL_RAW: _ClassVar[SocketProtocol]

class L7Protocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    L7_PROTOCOL_UNSPECIFIED: _ClassVar[L7Protocol]
    L7_PROTOCOL_HTTP1: _ClassVar[L7Protocol]
    L7_PROTOCOL_HTTP2: _ClassVar[L7Protocol]
    L7_PROTOCOL_HTTP3: _ClassVar[L7Protocol]
    L7_PROTOCOL_DNS: _ClassVar[L7Protocol]
    L7_PROTOCOL_GRPC: _ClassVar[L7Protocol]
    L7_PROTOCOL_OTHER: _ClassVar[L7Protocol]
DIRECTION_UNSPECIFIED: Direction
DIRECTION_INGRESS: Direction
DIRECTION_EGRESS: Direction
DIRECTION_EGRESS_INTERNAL: Direction
DIRECTION_EGRESS_EXTERNAL: Direction
TLS_VERSION_UNSPECIFIED: TlsVersion
TLS_VERSION_V1_0: TlsVersion
TLS_VERSION_V1_1: TlsVersion
TLS_VERSION_V1_2: TlsVersion
TLS_VERSION_V1_3: TlsVersion
SOCKET_PROTOCOL_UNSPECIFIED: SocketProtocol
SOCKET_PROTOCOL_TCP: SocketProtocol
SOCKET_PROTOCOL_UDP: SocketProtocol
SOCKET_PROTOCOL_ICMP: SocketProtocol
SOCKET_PROTOCOL_RAW: SocketProtocol
L7_PROTOCOL_UNSPECIFIED: L7Protocol
L7_PROTOCOL_HTTP1: L7Protocol
L7_PROTOCOL_HTTP2: L7Protocol
L7_PROTOCOL_HTTP3: L7Protocol
L7_PROTOCOL_DNS: L7Protocol
L7_PROTOCOL_GRPC: L7Protocol
L7_PROTOCOL_OTHER: L7Protocol

class Pod(_message.Message):
    __slots__ = ["name", "namespace"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    name: str
    namespace: str
    def __init__(self, name: _Optional[str] = ..., namespace: _Optional[str] = ...) -> None: ...

class Container(_message.Message):
    __slots__ = ["id", "name", "image", "pod"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    POD_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    image: str
    pod: Pod
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., image: _Optional[str] = ..., pod: _Optional[_Union[Pod, _Mapping]] = ...) -> None: ...

class Address(_message.Message):
    __slots__ = ["ip", "port"]
    IP_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    ip: str
    port: int
    def __init__(self, ip: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...
