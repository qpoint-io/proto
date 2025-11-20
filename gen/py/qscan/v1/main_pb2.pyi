from qpoint.type.v1 import artifact_pb2 as _artifact_pb2
from qpoint.type.v1 import pii_pb2 as _pii_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PingRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PingResponse(_message.Message):
    __slots__ = ["org_id", "service"]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    service: str
    def __init__(self, org_id: _Optional[str] = ..., service: _Optional[str] = ...) -> None: ...

class GetNextJobRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetNextJobResponse(_message.Message):
    __slots__ = ["scan_id", "artifact"]
    SCAN_ID_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_FIELD_NUMBER: _ClassVar[int]
    scan_id: str
    artifact: _artifact_pb2.Artifact
    def __init__(self, scan_id: _Optional[str] = ..., artifact: _Optional[_Union[_artifact_pb2.Artifact, _Mapping]] = ...) -> None: ...

class SubmitJobReportRequest(_message.Message):
    __slots__ = ["scan_id", "result"]
    class Result(_message.Message):
        __slots__ = ["success", "error"]
        SUCCESS_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        success: SubmitJobReportSuccess
        error: SubmitJobReportError
        def __init__(self, success: _Optional[_Union[SubmitJobReportSuccess, _Mapping]] = ..., error: _Optional[_Union[SubmitJobReportError, _Mapping]] = ...) -> None: ...
    SCAN_ID_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    scan_id: str
    result: SubmitJobReportRequest.Result
    def __init__(self, scan_id: _Optional[str] = ..., result: _Optional[_Union[SubmitJobReportRequest.Result, _Mapping]] = ...) -> None: ...

class SubmitJobReportSuccess(_message.Message):
    __slots__ = ["artifact", "pii_entities"]
    ARTIFACT_FIELD_NUMBER: _ClassVar[int]
    PII_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    artifact: _artifact_pb2.Artifact
    pii_entities: _containers.RepeatedCompositeFieldContainer[_pii_pb2.PIIEntity]
    def __init__(self, artifact: _Optional[_Union[_artifact_pb2.Artifact, _Mapping]] = ..., pii_entities: _Optional[_Iterable[_Union[_pii_pb2.PIIEntity, _Mapping]]] = ...) -> None: ...

class SubmitJobReportError(_message.Message):
    __slots__ = ["error_text"]
    ERROR_TEXT_FIELD_NUMBER: _ClassVar[int]
    error_text: str
    def __init__(self, error_text: _Optional[str] = ...) -> None: ...

class SubmitJobReportResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
