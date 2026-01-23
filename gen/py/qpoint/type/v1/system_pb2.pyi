from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
DIRECTION_EGRESS: Direction
DIRECTION_EGRESS_EXTERNAL: Direction
DIRECTION_EGRESS_INTERNAL: Direction
DIRECTION_INGRESS: Direction
DIRECTION_UNSPECIFIED: Direction
L7_PROTOCOL_DNS: L7Protocol
L7_PROTOCOL_GRPC: L7Protocol
L7_PROTOCOL_HTTP1: L7Protocol
L7_PROTOCOL_HTTP2: L7Protocol
L7_PROTOCOL_HTTP3: L7Protocol
L7_PROTOCOL_OTHER: L7Protocol
L7_PROTOCOL_UNSPECIFIED: L7Protocol
SOCKET_PROTOCOL_ICMP: SocketProtocol
SOCKET_PROTOCOL_RAW: SocketProtocol
SOCKET_PROTOCOL_TCP: SocketProtocol
SOCKET_PROTOCOL_UDP: SocketProtocol
SOCKET_PROTOCOL_UNSPECIFIED: SocketProtocol
TLS_VERSION_UNSPECIFIED: TlsVersion
TLS_VERSION_V1_0: TlsVersion
TLS_VERSION_V1_1: TlsVersion
TLS_VERSION_V1_2: TlsVersion
TLS_VERSION_V1_3: TlsVersion

class Address(_message.Message):
    __slots__ = ["ip", "port"]
    IP_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    ip: str
    port: int
    def __init__(self, ip: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class Container(_message.Message):
    __slots__ = ["id", "image", "name", "pod"]
    ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    POD_FIELD_NUMBER: _ClassVar[int]
    id: str
    image: str
    name: str
    pod: Pod
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., image: _Optional[str] = ..., pod: _Optional[_Union[Pod, _Mapping]] = ...) -> None: ...

class Pod(_message.Message):
    __slots__ = ["name", "namespace"]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    namespace: str
    def __init__(self, name: _Optional[str] = ..., namespace: _Optional[str] = ...) -> None: ...

class Direction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class TlsVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class SocketProtocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class L7Protocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
