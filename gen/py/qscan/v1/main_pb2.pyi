from qpoint.type.v1 import artifact_pb2 as _artifact_pb2
from qpoint.type.v1 import pii_pb2 as _pii_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetNextJobRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetNextJobResponse(_message.Message):
    __slots__ = ["artifact", "org_id", "scan_id"]
    ARTIFACT_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    SCAN_ID_FIELD_NUMBER: _ClassVar[int]
    artifact: _artifact_pb2.Artifact
    org_id: str
    scan_id: str
    def __init__(self, scan_id: _Optional[str] = ..., org_id: _Optional[str] = ..., artifact: _Optional[_Union[_artifact_pb2.Artifact, _Mapping]] = ...) -> None: ...

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

class SubmitJobReportError(_message.Message):
    __slots__ = ["error_text"]
    ERROR_TEXT_FIELD_NUMBER: _ClassVar[int]
    error_text: str
    def __init__(self, error_text: _Optional[str] = ...) -> None: ...

class SubmitJobReportRequest(_message.Message):
    __slots__ = ["result", "scan_id"]
    class Result(_message.Message):
        __slots__ = ["error", "success"]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        SUCCESS_FIELD_NUMBER: _ClassVar[int]
        error: SubmitJobReportError
        success: SubmitJobReportSuccess
        def __init__(self, success: _Optional[_Union[SubmitJobReportSuccess, _Mapping]] = ..., error: _Optional[_Union[SubmitJobReportError, _Mapping]] = ...) -> None: ...
    RESULT_FIELD_NUMBER: _ClassVar[int]
    SCAN_ID_FIELD_NUMBER: _ClassVar[int]
    result: SubmitJobReportRequest.Result
    scan_id: str
    def __init__(self, scan_id: _Optional[str] = ..., result: _Optional[_Union[SubmitJobReportRequest.Result, _Mapping]] = ...) -> None: ...

class SubmitJobReportResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SubmitJobReportSuccess(_message.Message):
    __slots__ = ["artifact", "pii_entities"]
    ARTIFACT_FIELD_NUMBER: _ClassVar[int]
    PII_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    artifact: _artifact_pb2.Artifact
    pii_entities: _containers.RepeatedCompositeFieldContainer[_pii_pb2.PIIEntity]
    def __init__(self, artifact: _Optional[_Union[_artifact_pb2.Artifact, _Mapping]] = ..., pii_entities: _Optional[_Iterable[_Union[_pii_pb2.PIIEntity, _Mapping]]] = ...) -> None: ...
