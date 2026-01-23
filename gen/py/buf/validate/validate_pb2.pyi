from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
FIELD_FIELD_NUMBER: _ClassVar[int]
IGNORE_ALWAYS: Ignore
IGNORE_IF_DEFAULT_VALUE: Ignore
IGNORE_IF_UNPOPULATED: Ignore
IGNORE_UNSPECIFIED: Ignore
KNOWN_REGEX_HTTP_HEADER_NAME: KnownRegex
KNOWN_REGEX_HTTP_HEADER_VALUE: KnownRegex
KNOWN_REGEX_UNSPECIFIED: KnownRegex
MESSAGE_FIELD_NUMBER: _ClassVar[int]
ONEOF_FIELD_NUMBER: _ClassVar[int]
PREDEFINED_FIELD_NUMBER: _ClassVar[int]
field: _descriptor.FieldDescriptor
message: _descriptor.FieldDescriptor
oneof: _descriptor.FieldDescriptor
predefined: _descriptor.FieldDescriptor

class AnyRules(_message.Message):
    __slots__ = ["not_in"]
    IN_FIELD_NUMBER: _ClassVar[int]
    NOT_IN_FIELD_NUMBER: _ClassVar[int]
    not_in: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, not_in: _Optional[_Iterable[str]] = ..., **kwargs) -> None: ...

class BoolRules(_message.Message):
    __slots__ = ["const", "example"]
    CONST_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    Extensions: _python_message._ExtensionDict
    const: bool
    example: _containers.RepeatedScalarFieldContainer[bool]
    def __init__(self, const: bool = ..., example: _Optional[_Iterable[bool]] = ...) -> None: ...

class BytesRules(_message.Message):
    __slots__ = ["const", "contains", "example", "ip", "ipv4", "ipv6", "len", "max_len", "min_len", "not_in", "pattern", "prefix", "suffix"]
    CONST_FIELD_NUMBER: _ClassVar[int]
    CONTAINS_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    Extensions: _python_message._ExtensionDict
    IN_FIELD_NUMBER: _ClassVar[int]
    IPV4_FIELD_NUMBER: _ClassVar[int]
    IPV6_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    MAX_LEN_FIELD_NUMBER: _ClassVar[int]
    MIN_LEN_FIELD_NUMBER: _ClassVar[int]
    NOT_IN_FIELD_NUMBER: _ClassVar[int]
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    SUFFIX_FIELD_NUMBER: _ClassVar[int]
    const: bytes
    contains: bytes
    example: _containers.RepeatedScalarFieldContainer[bytes]
    ip: bool
    ipv4: bool
    ipv6: bool
    len: int
    max_len: int
    min_len: int
    not_in: _containers.RepeatedScalarFieldContainer[bytes]
    pattern: str
    prefix: bytes
    suffix: bytes
    def __init__(self, const: _Optional[bytes] = ..., len: _Optional[int] = ..., min_len: _Optional[int] = ..., max_len: _Optional[int] = ..., pattern: _Optional[str] = ..., prefix: _Optional[bytes] = ..., suffix: _Optional[bytes] = ..., contains: _Optional[bytes] = ..., not_in: _Optional[_Iterable[bytes]] = ..., ip: bool = ..., ipv4: bool = ..., ipv6: bool = ..., example: _Optional[_Iterable[bytes]] = ..., **kwargs) -> None: ...

class Constraint(_message.Message):
    __slots__ = ["expression", "id", "message"]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    expression: str
    id: str
    message: str
    def __init__(self, id: _Optional[str] = ..., message: _Optional[str] = ..., expression: _Optional[str] = ...) -> None: ...

class DoubleRules(_message.Message):
    __slots__ = ["const", "example", "finite", "gt", "gte", "lt", "lte", "not_in"]
    CONST_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    Extensions: _python_message._ExtensionDict
    FINITE_FIELD_NUMBER: _ClassVar[int]
    GTE_FIELD_NUMBER: _ClassVar[int]
    GT_FIELD_NUMBER: _ClassVar[int]
    IN_FIELD_NUMBER: _ClassVar[int]
    LTE_FIELD_NUMBER: _ClassVar[int]
    LT_FIELD_NUMBER: _ClassVar[int]
    NOT_IN_FIELD_NUMBER: _ClassVar[int]
    const: float
    example: _containers.RepeatedScalarFieldContainer[float]
    finite: bool
    gt: float
    gte: float
    lt: float
    lte: float
    not_in: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, const: _Optional[float] = ..., lt: _Optional[float] = ..., lte: _Optional[float] = ..., gt: _Optional[float] = ..., gte: _Optional[float] = ..., not_in: _Optional[_Iterable[float]] = ..., finite: bool = ..., example: _Optional[_Iterable[float]] = ..., **kwargs) -> None: ...

class DurationRules(_message.Message):
    __slots__ = ["const", "example", "gt", "gte", "lt", "lte", "not_in"]
    CONST_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    Extensions: _python_message._ExtensionDict
    GTE_FIELD_NUMBER: _ClassVar[int]
    GT_FIELD_NUMBER: _ClassVar[int]
    IN_FIELD_NUMBER: _ClassVar[int]
    LTE_FIELD_NUMBER: _ClassVar[int]
    LT_FIELD_NUMBER: _ClassVar[int]
    NOT_IN_FIELD_NUMBER: _ClassVar[int]
    const: _duration_pb2.Duration
    example: _containers.RepeatedCompositeFieldContainer[_duration_pb2.Duration]
    gt: _duration_pb2.Duration
    gte: _duration_pb2.Duration
    lt: _duration_pb2.Duration
    lte: _duration_pb2.Duration
    not_in: _containers.RepeatedCompositeFieldContainer[_duration_pb2.Duration]
    def __init__(self, const: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., lt: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., lte: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., gt: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., gte: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., not_in: _Optional[_Iterable[_Union[_duration_pb2.Duration, _Mapping]]] = ..., example: _Optional[_Iterable[_Union[_duration_pb2.Duration, _Mapping]]] = ..., **kwargs) -> None: ...

class EnumRules(_message.Message):
    __slots__ = ["const", "defined_only", "example", "not_in"]
    CONST_FIELD_NUMBER: _ClassVar[int]
    DEFINED_ONLY_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    Extensions: _python_message._ExtensionDict
    IN_FIELD_NUMBER: _ClassVar[int]
    NOT_IN_FIELD_NUMBER: _ClassVar[int]
    const: int
    defined_only: bool
    example: _containers.RepeatedScalarFieldContainer[int]
    not_in: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, const: _Optional[int] = ..., defined_only: bool = ..., not_in: _Optional[_Iterable[int]] = ..., example: _Optional[_Iterable[int]] = ..., **kwargs) -> None: ...

class FieldConstraints(_message.Message):
    __slots__ = ["any", "bool", "bytes", "cel", "double", "duration", "enum", "fixed32", "fixed64", "float", "ignore", "int32", "int64", "map", "repeated", "required", "sfixed32", "sfixed64", "sint32", "sint64", "string", "timestamp", "uint32", "uint64"]
    ANY_FIELD_NUMBER: _ClassVar[int]
    BOOL_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_NUMBER: _ClassVar[int]
    CEL_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_NUMBER: _ClassVar[int]
    FIXED32_FIELD_NUMBER: _ClassVar[int]
    FIXED64_FIELD_NUMBER: _ClassVar[int]
    FLOAT_FIELD_NUMBER: _ClassVar[int]
    IGNORE_FIELD_NUMBER: _ClassVar[int]
    INT32_FIELD_NUMBER: _ClassVar[int]
    INT64_FIELD_NUMBER: _ClassVar[int]
    MAP_FIELD_NUMBER: _ClassVar[int]
    REPEATED_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    SFIXED32_FIELD_NUMBER: _ClassVar[int]
    SFIXED64_FIELD_NUMBER: _ClassVar[int]
    SINT32_FIELD_NUMBER: _ClassVar[int]
    SINT64_FIELD_NUMBER: _ClassVar[int]
    STRING_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UINT32_FIELD_NUMBER: _ClassVar[int]
    UINT64_FIELD_NUMBER: _ClassVar[int]
    any: AnyRules
    bool: BoolRules
    bytes: BytesRules
    cel: _containers.RepeatedCompositeFieldContainer[Constraint]
    double: DoubleRules
    duration: DurationRules
    enum: EnumRules
    fixed32: Fixed32Rules
    fixed64: Fixed64Rules
    float: FloatRules
    ignore: Ignore
    int32: Int32Rules
    int64: Int64Rules
    map: MapRules
    repeated: RepeatedRules
    required: bool
    sfixed32: SFixed32Rules
    sfixed64: SFixed64Rules
    sint32: SInt32Rules
    sint64: SInt64Rules
    string: StringRules
    timestamp: TimestampRules
    uint32: UInt32Rules
    uint64: UInt64Rules
    def __init__(self, cel: _Optional[_Iterable[_Union[Constraint, _Mapping]]] = ..., required: bool = ..., ignore: _Optional[_Union[Ignore, str]] = ..., float: _Optional[_Union[FloatRules, _Mapping]] = ..., double: _Optional[_Union[DoubleRules, _Mapping]] = ..., int32: _Optional[_Union[Int32Rules, _Mapping]] = ..., int64: _Optional[_Union[Int64Rules, _Mapping]] = ..., uint32: _Optional[_Union[UInt32Rules, _Mapping]] = ..., uint64: _Optional[_Union[UInt64Rules, _Mapping]] = ..., sint32: _Optional[_Union[SInt32Rules, _Mapping]] = ..., sint64: _Optional[_Union[SInt64Rules, _Mapping]] = ..., fixed32: _Optional[_Union[Fixed32Rules, _Mapping]] = ..., fixed64: _Optional[_Union[Fixed64Rules, _Mapping]] = ..., sfixed32: _Optional[_Union[SFixed32Rules, _Mapping]] = ..., sfixed64: _Optional[_Union[SFixed64Rules, _Mapping]] = ..., bool: _Optional[_Union[BoolRules, _Mapping]] = ..., string: _Optional[_Union[StringRules, _Mapping]] = ..., bytes: _Optional[_Union[BytesRules, _Mapping]] = ..., enum: _Optional[_Union[EnumRules, _Mapping]] = ..., repeated: _Optional[_Union[RepeatedRules, _Mapping]] = ..., map: _Optional[_Union[MapRules, _Mapping]] = ..., any: _Optional[_Union[AnyRules, _Mapping]] = ..., duration: _Optional[_Union[DurationRules, _Mapping]] = ..., timestamp: _Optional[_Union[TimestampRules, _Mapping]] = ...) -> None: ...

class FieldPath(_message.Message):
    __slots__ = ["elements"]
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    elements: _containers.RepeatedCompositeFieldContainer[FieldPathElement]
    def __init__(self, elements: _Optional[_Iterable[_Union[FieldPathElement, _Mapping]]] = ...) -> None: ...

class FieldPathElement(_message.Message):
    __slots__ = ["bool_key", "field_name", "field_number", "field_type", "index", "int_key", "key_type", "string_key", "uint_key", "value_type"]
    BOOL_KEY_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    FIELD_NUMBER_FIELD_NUMBER: _ClassVar[int]
    FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    INT_KEY_FIELD_NUMBER: _ClassVar[int]
    KEY_TYPE_FIELD_NUMBER: _ClassVar[int]
    STRING_KEY_FIELD_NUMBER: _ClassVar[int]
    UINT_KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    bool_key: bool
    field_name: str
    field_number: int
    field_type: _descriptor_pb2.FieldDescriptorProto.Type
    index: int
    int_key: int
    key_type: _descriptor_pb2.FieldDescriptorProto.Type
    string_key: str
    uint_key: int
    value_type: _descriptor_pb2.FieldDescriptorProto.Type
    def __init__(self, field_number: _Optional[int] = ..., field_name: _Optional[str] = ..., field_type: _Optional[_Union[_descriptor_pb2.FieldDescriptorProto.Type, str]] = ..., key_type: _Optional[_Union[_descriptor_pb2.FieldDescriptorProto.Type, str]] = ..., value_type: _Optional[_Union[_descriptor_pb2.FieldDescriptorProto.Type, str]] = ..., index: _Optional[int] = ..., bool_key: bool = ..., int_key: _Optional[int] = ..., uint_key: _Optional[int] = ..., string_key: _Optional[str] = ...) -> None: ...

class Fixed32Rules(_message.Message):
    __slots__ = ["const", "example", "gt", "gte", "lt", "lte", "not_in"]
    CONST_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    Extensions: _python_message._ExtensionDict
    GTE_FIELD_NUMBER: _ClassVar[int]
    GT_FIELD_NUMBER: _ClassVar[int]
    IN_FIELD_NUMBER: _ClassVar[int]
    LTE_FIELD_NUMBER: _ClassVar[int]
    LT_FIELD_NUMBER: _ClassVar[int]
    NOT_IN_FIELD_NUMBER: _ClassVar[int]
    const: int
    example: _containers.RepeatedScalarFieldContainer[int]
    gt: int
    gte: int
    lt: int
    lte: int
    not_in: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, const: _Optional[int] = ..., lt: _Optional[int] = ..., lte: _Optional[int] = ..., gt: _Optional[int] = ..., gte: _Optional[int] = ..., not_in: _Optional[_Iterable[int]] = ..., example: _Optional[_Iterable[int]] = ..., **kwargs) -> None: ...

class Fixed64Rules(_message.Message):
    __slots__ = ["const", "example", "gt", "gte", "lt", "lte", "not_in"]
    CONST_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    Extensions: _python_message._ExtensionDict
    GTE_FIELD_NUMBER: _ClassVar[int]
    GT_FIELD_NUMBER: _ClassVar[int]
    IN_FIELD_NUMBER: _ClassVar[int]
    LTE_FIELD_NUMBER: _ClassVar[int]
    LT_FIELD_NUMBER: _ClassVar[int]
    NOT_IN_FIELD_NUMBER: _ClassVar[int]
    const: int
    example: _containers.RepeatedScalarFieldContainer[int]
    gt: int
    gte: int
    lt: int
    lte: int
    not_in: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, const: _Optional[int] = ..., lt: _Optional[int] = ..., lte: _Optional[int] = ..., gt: _Optional[int] = ..., gte: _Optional[int] = ..., not_in: _Optional[_Iterable[int]] = ..., example: _Optional[_Iterable[int]] = ..., **kwargs) -> None: ...

class FloatRules(_message.Message):
    __slots__ = ["const", "example", "finite", "gt", "gte", "lt", "lte", "not_in"]
    CONST_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    Extensions: _python_message._ExtensionDict
    FINITE_FIELD_NUMBER: _ClassVar[int]
    GTE_FIELD_NUMBER: _ClassVar[int]
    GT_FIELD_NUMBER: _ClassVar[int]
    IN_FIELD_NUMBER: _ClassVar[int]
    LTE_FIELD_NUMBER: _ClassVar[int]
    LT_FIELD_NUMBER: _ClassVar[int]
    NOT_IN_FIELD_NUMBER: _ClassVar[int]
    const: float
    example: _containers.RepeatedScalarFieldContainer[float]
    finite: bool
    gt: float
    gte: float
    lt: float
    lte: float
    not_in: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, const: _Optional[float] = ..., lt: _Optional[float] = ..., lte: _Optional[float] = ..., gt: _Optional[float] = ..., gte: _Optional[float] = ..., not_in: _Optional[_Iterable[float]] = ..., finite: bool = ..., example: _Optional[_Iterable[float]] = ..., **kwargs) -> None: ...

class Int32Rules(_message.Message):
    __slots__ = ["const", "example", "gt", "gte", "lt", "lte", "not_in"]
    CONST_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    Extensions: _python_message._ExtensionDict
    GTE_FIELD_NUMBER: _ClassVar[int]
    GT_FIELD_NUMBER: _ClassVar[int]
    IN_FIELD_NUMBER: _ClassVar[int]
    LTE_FIELD_NUMBER: _ClassVar[int]
    LT_FIELD_NUMBER: _ClassVar[int]
    NOT_IN_FIELD_NUMBER: _ClassVar[int]
    const: int
    example: _containers.RepeatedScalarFieldContainer[int]
    gt: int
    gte: int
    lt: int
    lte: int
    not_in: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, const: _Optional[int] = ..., lt: _Optional[int] = ..., lte: _Optional[int] = ..., gt: _Optional[int] = ..., gte: _Optional[int] = ..., not_in: _Optional[_Iterable[int]] = ..., example: _Optional[_Iterable[int]] = ..., **kwargs) -> None: ...

class Int64Rules(_message.Message):
    __slots__ = ["const", "example", "gt", "gte", "lt", "lte", "not_in"]
    CONST_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    Extensions: _python_message._ExtensionDict
    GTE_FIELD_NUMBER: _ClassVar[int]
    GT_FIELD_NUMBER: _ClassVar[int]
    IN_FIELD_NUMBER: _ClassVar[int]
    LTE_FIELD_NUMBER: _ClassVar[int]
    LT_FIELD_NUMBER: _ClassVar[int]
    NOT_IN_FIELD_NUMBER: _ClassVar[int]
    const: int
    example: _containers.RepeatedScalarFieldContainer[int]
    gt: int
    gte: int
    lt: int
    lte: int
    not_in: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, const: _Optional[int] = ..., lt: _Optional[int] = ..., lte: _Optional[int] = ..., gt: _Optional[int] = ..., gte: _Optional[int] = ..., not_in: _Optional[_Iterable[int]] = ..., example: _Optional[_Iterable[int]] = ..., **kwargs) -> None: ...

class MapRules(_message.Message):
    __slots__ = ["keys", "max_pairs", "min_pairs", "values"]
    Extensions: _python_message._ExtensionDict
    KEYS_FIELD_NUMBER: _ClassVar[int]
    MAX_PAIRS_FIELD_NUMBER: _ClassVar[int]
    MIN_PAIRS_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    keys: FieldConstraints
    max_pairs: int
    min_pairs: int
    values: FieldConstraints
    def __init__(self, min_pairs: _Optional[int] = ..., max_pairs: _Optional[int] = ..., keys: _Optional[_Union[FieldConstraints, _Mapping]] = ..., values: _Optional[_Union[FieldConstraints, _Mapping]] = ...) -> None: ...

class MessageConstraints(_message.Message):
    __slots__ = ["cel", "disabled"]
    CEL_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    cel: _containers.RepeatedCompositeFieldContainer[Constraint]
    disabled: bool
    def __init__(self, disabled: bool = ..., cel: _Optional[_Iterable[_Union[Constraint, _Mapping]]] = ...) -> None: ...

class OneofConstraints(_message.Message):
    __slots__ = ["required"]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    required: bool
    def __init__(self, required: bool = ...) -> None: ...

class PredefinedConstraints(_message.Message):
    __slots__ = ["cel"]
    CEL_FIELD_NUMBER: _ClassVar[int]
    cel: _containers.RepeatedCompositeFieldContainer[Constraint]
    def __init__(self, cel: _Optional[_Iterable[_Union[Constraint, _Mapping]]] = ...) -> None: ...

class RepeatedRules(_message.Message):
    __slots__ = ["items", "max_items", "min_items", "unique"]
    Extensions: _python_message._ExtensionDict
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    MAX_ITEMS_FIELD_NUMBER: _ClassVar[int]
    MIN_ITEMS_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_FIELD_NUMBER: _ClassVar[int]
    items: FieldConstraints
    max_items: int
    min_items: int
    unique: bool
    def __init__(self, min_items: _Optional[int] = ..., max_items: _Optional[int] = ..., unique: bool = ..., items: _Optional[_Union[FieldConstraints, _Mapping]] = ...) -> None: ...

class SFixed32Rules(_message.Message):
    __slots__ = ["const", "example", "gt", "gte", "lt", "lte", "not_in"]
    CONST_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    Extensions: _python_message._ExtensionDict
    GTE_FIELD_NUMBER: _ClassVar[int]
    GT_FIELD_NUMBER: _ClassVar[int]
    IN_FIELD_NUMBER: _ClassVar[int]
    LTE_FIELD_NUMBER: _ClassVar[int]
    LT_FIELD_NUMBER: _ClassVar[int]
    NOT_IN_FIELD_NUMBER: _ClassVar[int]
    const: int
    example: _containers.RepeatedScalarFieldContainer[int]
    gt: int
    gte: int
    lt: int
    lte: int
    not_in: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, const: _Optional[int] = ..., lt: _Optional[int] = ..., lte: _Optional[int] = ..., gt: _Optional[int] = ..., gte: _Optional[int] = ..., not_in: _Optional[_Iterable[int]] = ..., example: _Optional[_Iterable[int]] = ..., **kwargs) -> None: ...

class SFixed64Rules(_message.Message):
    __slots__ = ["const", "example", "gt", "gte", "lt", "lte", "not_in"]
    CONST_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    Extensions: _python_message._ExtensionDict
    GTE_FIELD_NUMBER: _ClassVar[int]
    GT_FIELD_NUMBER: _ClassVar[int]
    IN_FIELD_NUMBER: _ClassVar[int]
    LTE_FIELD_NUMBER: _ClassVar[int]
    LT_FIELD_NUMBER: _ClassVar[int]
    NOT_IN_FIELD_NUMBER: _ClassVar[int]
    const: int
    example: _containers.RepeatedScalarFieldContainer[int]
    gt: int
    gte: int
    lt: int
    lte: int
    not_in: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, const: _Optional[int] = ..., lt: _Optional[int] = ..., lte: _Optional[int] = ..., gt: _Optional[int] = ..., gte: _Optional[int] = ..., not_in: _Optional[_Iterable[int]] = ..., example: _Optional[_Iterable[int]] = ..., **kwargs) -> None: ...

class SInt32Rules(_message.Message):
    __slots__ = ["const", "example", "gt", "gte", "lt", "lte", "not_in"]
    CONST_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    Extensions: _python_message._ExtensionDict
    GTE_FIELD_NUMBER: _ClassVar[int]
    GT_FIELD_NUMBER: _ClassVar[int]
    IN_FIELD_NUMBER: _ClassVar[int]
    LTE_FIELD_NUMBER: _ClassVar[int]
    LT_FIELD_NUMBER: _ClassVar[int]
    NOT_IN_FIELD_NUMBER: _ClassVar[int]
    const: int
    example: _containers.RepeatedScalarFieldContainer[int]
    gt: int
    gte: int
    lt: int
    lte: int
    not_in: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, const: _Optional[int] = ..., lt: _Optional[int] = ..., lte: _Optional[int] = ..., gt: _Optional[int] = ..., gte: _Optional[int] = ..., not_in: _Optional[_Iterable[int]] = ..., example: _Optional[_Iterable[int]] = ..., **kwargs) -> None: ...

class SInt64Rules(_message.Message):
    __slots__ = ["const", "example", "gt", "gte", "lt", "lte", "not_in"]
    CONST_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    Extensions: _python_message._ExtensionDict
    GTE_FIELD_NUMBER: _ClassVar[int]
    GT_FIELD_NUMBER: _ClassVar[int]
    IN_FIELD_NUMBER: _ClassVar[int]
    LTE_FIELD_NUMBER: _ClassVar[int]
    LT_FIELD_NUMBER: _ClassVar[int]
    NOT_IN_FIELD_NUMBER: _ClassVar[int]
    const: int
    example: _containers.RepeatedScalarFieldContainer[int]
    gt: int
    gte: int
    lt: int
    lte: int
    not_in: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, const: _Optional[int] = ..., lt: _Optional[int] = ..., lte: _Optional[int] = ..., gt: _Optional[int] = ..., gte: _Optional[int] = ..., not_in: _Optional[_Iterable[int]] = ..., example: _Optional[_Iterable[int]] = ..., **kwargs) -> None: ...

class StringRules(_message.Message):
    __slots__ = ["address", "const", "contains", "email", "example", "host_and_port", "hostname", "ip", "ip_prefix", "ip_with_prefixlen", "ipv4", "ipv4_prefix", "ipv4_with_prefixlen", "ipv6", "ipv6_prefix", "ipv6_with_prefixlen", "len", "len_bytes", "max_bytes", "max_len", "min_bytes", "min_len", "not_contains", "not_in", "pattern", "prefix", "strict", "suffix", "tuuid", "uri", "uri_ref", "uuid", "well_known_regex"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CONST_FIELD_NUMBER: _ClassVar[int]
    CONTAINS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    Extensions: _python_message._ExtensionDict
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    HOST_AND_PORT_FIELD_NUMBER: _ClassVar[int]
    IN_FIELD_NUMBER: _ClassVar[int]
    IPV4_FIELD_NUMBER: _ClassVar[int]
    IPV4_PREFIX_FIELD_NUMBER: _ClassVar[int]
    IPV4_WITH_PREFIXLEN_FIELD_NUMBER: _ClassVar[int]
    IPV6_FIELD_NUMBER: _ClassVar[int]
    IPV6_PREFIX_FIELD_NUMBER: _ClassVar[int]
    IPV6_WITH_PREFIXLEN_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    IP_PREFIX_FIELD_NUMBER: _ClassVar[int]
    IP_WITH_PREFIXLEN_FIELD_NUMBER: _ClassVar[int]
    LEN_BYTES_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    MAX_BYTES_FIELD_NUMBER: _ClassVar[int]
    MAX_LEN_FIELD_NUMBER: _ClassVar[int]
    MIN_BYTES_FIELD_NUMBER: _ClassVar[int]
    MIN_LEN_FIELD_NUMBER: _ClassVar[int]
    NOT_CONTAINS_FIELD_NUMBER: _ClassVar[int]
    NOT_IN_FIELD_NUMBER: _ClassVar[int]
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    STRICT_FIELD_NUMBER: _ClassVar[int]
    SUFFIX_FIELD_NUMBER: _ClassVar[int]
    TUUID_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    URI_REF_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    WELL_KNOWN_REGEX_FIELD_NUMBER: _ClassVar[int]
    address: bool
    const: str
    contains: str
    email: bool
    example: _containers.RepeatedScalarFieldContainer[str]
    host_and_port: bool
    hostname: bool
    ip: bool
    ip_prefix: bool
    ip_with_prefixlen: bool
    ipv4: bool
    ipv4_prefix: bool
    ipv4_with_prefixlen: bool
    ipv6: bool
    ipv6_prefix: bool
    ipv6_with_prefixlen: bool
    len: int
    len_bytes: int
    max_bytes: int
    max_len: int
    min_bytes: int
    min_len: int
    not_contains: str
    not_in: _containers.RepeatedScalarFieldContainer[str]
    pattern: str
    prefix: str
    strict: bool
    suffix: str
    tuuid: bool
    uri: bool
    uri_ref: bool
    uuid: bool
    well_known_regex: KnownRegex
    def __init__(self, const: _Optional[str] = ..., len: _Optional[int] = ..., min_len: _Optional[int] = ..., max_len: _Optional[int] = ..., len_bytes: _Optional[int] = ..., min_bytes: _Optional[int] = ..., max_bytes: _Optional[int] = ..., pattern: _Optional[str] = ..., prefix: _Optional[str] = ..., suffix: _Optional[str] = ..., contains: _Optional[str] = ..., not_contains: _Optional[str] = ..., not_in: _Optional[_Iterable[str]] = ..., email: bool = ..., hostname: bool = ..., ip: bool = ..., ipv4: bool = ..., ipv6: bool = ..., uri: bool = ..., uri_ref: bool = ..., address: bool = ..., uuid: bool = ..., tuuid: bool = ..., ip_with_prefixlen: bool = ..., ipv4_with_prefixlen: bool = ..., ipv6_with_prefixlen: bool = ..., ip_prefix: bool = ..., ipv4_prefix: bool = ..., ipv6_prefix: bool = ..., host_and_port: bool = ..., well_known_regex: _Optional[_Union[KnownRegex, str]] = ..., strict: bool = ..., example: _Optional[_Iterable[str]] = ..., **kwargs) -> None: ...

class TimestampRules(_message.Message):
    __slots__ = ["const", "example", "gt", "gt_now", "gte", "lt", "lt_now", "lte", "within"]
    CONST_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    Extensions: _python_message._ExtensionDict
    GTE_FIELD_NUMBER: _ClassVar[int]
    GT_FIELD_NUMBER: _ClassVar[int]
    GT_NOW_FIELD_NUMBER: _ClassVar[int]
    LTE_FIELD_NUMBER: _ClassVar[int]
    LT_FIELD_NUMBER: _ClassVar[int]
    LT_NOW_FIELD_NUMBER: _ClassVar[int]
    WITHIN_FIELD_NUMBER: _ClassVar[int]
    const: _timestamp_pb2.Timestamp
    example: _containers.RepeatedCompositeFieldContainer[_timestamp_pb2.Timestamp]
    gt: _timestamp_pb2.Timestamp
    gt_now: bool
    gte: _timestamp_pb2.Timestamp
    lt: _timestamp_pb2.Timestamp
    lt_now: bool
    lte: _timestamp_pb2.Timestamp
    within: _duration_pb2.Duration
    def __init__(self, const: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., lt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., lte: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., lt_now: bool = ..., gt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., gte: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., gt_now: bool = ..., within: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., example: _Optional[_Iterable[_Union[_timestamp_pb2.Timestamp, _Mapping]]] = ...) -> None: ...

class UInt32Rules(_message.Message):
    __slots__ = ["const", "example", "gt", "gte", "lt", "lte", "not_in"]
    CONST_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    Extensions: _python_message._ExtensionDict
    GTE_FIELD_NUMBER: _ClassVar[int]
    GT_FIELD_NUMBER: _ClassVar[int]
    IN_FIELD_NUMBER: _ClassVar[int]
    LTE_FIELD_NUMBER: _ClassVar[int]
    LT_FIELD_NUMBER: _ClassVar[int]
    NOT_IN_FIELD_NUMBER: _ClassVar[int]
    const: int
    example: _containers.RepeatedScalarFieldContainer[int]
    gt: int
    gte: int
    lt: int
    lte: int
    not_in: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, const: _Optional[int] = ..., lt: _Optional[int] = ..., lte: _Optional[int] = ..., gt: _Optional[int] = ..., gte: _Optional[int] = ..., not_in: _Optional[_Iterable[int]] = ..., example: _Optional[_Iterable[int]] = ..., **kwargs) -> None: ...

class UInt64Rules(_message.Message):
    __slots__ = ["const", "example", "gt", "gte", "lt", "lte", "not_in"]
    CONST_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    Extensions: _python_message._ExtensionDict
    GTE_FIELD_NUMBER: _ClassVar[int]
    GT_FIELD_NUMBER: _ClassVar[int]
    IN_FIELD_NUMBER: _ClassVar[int]
    LTE_FIELD_NUMBER: _ClassVar[int]
    LT_FIELD_NUMBER: _ClassVar[int]
    NOT_IN_FIELD_NUMBER: _ClassVar[int]
    const: int
    example: _containers.RepeatedScalarFieldContainer[int]
    gt: int
    gte: int
    lt: int
    lte: int
    not_in: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, const: _Optional[int] = ..., lt: _Optional[int] = ..., lte: _Optional[int] = ..., gt: _Optional[int] = ..., gte: _Optional[int] = ..., not_in: _Optional[_Iterable[int]] = ..., example: _Optional[_Iterable[int]] = ..., **kwargs) -> None: ...

class Violation(_message.Message):
    __slots__ = ["constraint_id", "field", "for_key", "message", "rule"]
    CONSTRAINT_ID_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    FOR_KEY_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    constraint_id: str
    field: FieldPath
    for_key: bool
    message: str
    rule: FieldPath
    def __init__(self, field: _Optional[_Union[FieldPath, _Mapping]] = ..., rule: _Optional[_Union[FieldPath, _Mapping]] = ..., constraint_id: _Optional[str] = ..., message: _Optional[str] = ..., for_key: bool = ...) -> None: ...

class Violations(_message.Message):
    __slots__ = ["violations"]
    VIOLATIONS_FIELD_NUMBER: _ClassVar[int]
    violations: _containers.RepeatedCompositeFieldContainer[Violation]
    def __init__(self, violations: _Optional[_Iterable[_Union[Violation, _Mapping]]] = ...) -> None: ...

class Ignore(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class KnownRegex(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
