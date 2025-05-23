// @generated by protoc-gen-es v2.2.5 with parameter "target=ts"
// @generated from file eventstore/v1/main.proto (package eventstore.v1, syntax proto3)
/* eslint-disable */

import type { GenFile, GenMessage, GenService } from "@bufbuild/protobuf/codegenv1";
import { fileDesc, messageDesc, serviceDesc } from "@bufbuild/protobuf/codegenv1";
import type { Artifact } from "../../qpoint/type/v1/artifact_pb";
import { file_qpoint_type_v1_artifact } from "../../qpoint/type/v1/artifact_pb";
import type { Connection } from "../../qpoint/type/v1/connection_pb";
import { file_qpoint_type_v1_connection } from "../../qpoint/type/v1/connection_pb";
import type { Issue } from "../../qpoint/type/v1/issue_pb";
import { file_qpoint_type_v1_issue } from "../../qpoint/type/v1/issue_pb";
import type { PIIEntity } from "../../qpoint/type/v1/pii_pb";
import { file_qpoint_type_v1_pii } from "../../qpoint/type/v1/pii_pb";
import type { Request } from "../../qpoint/type/v1/request_pb";
import { file_qpoint_type_v1_request } from "../../qpoint/type/v1/request_pb";
import type { Message } from "@bufbuild/protobuf";

/**
 * Describes the file eventstore/v1/main.proto.
 */
export const file_eventstore_v1_main: GenFile = /*@__PURE__*/
  fileDesc("ChhldmVudHN0b3JlL3YxL21haW4ucHJvdG8SDWV2ZW50c3RvcmUudjEiDQoLUGluZ1JlcXVlc3QiHgoMUGluZ1Jlc3BvbnNlEg4KBm9yZ19pZBgBIAEoCSK7AgoNSW5nZXN0UmVxdWVzdBIyCgZldmVudHMYASADKAsyIi5ldmVudHN0b3JlLnYxLkluZ2VzdFJlcXVlc3QuRXZlbnQa9QEKBUV2ZW50EioKB3JlcXVlc3QYASABKAsyFy5xcG9pbnQudHlwZS52MS5SZXF1ZXN0SAASJgoFaXNzdWUYAiABKAsyFS5xcG9pbnQudHlwZS52MS5Jc3N1ZUgAEiwKCGFydGlmYWN0GAMgASgLMhgucXBvaW50LnR5cGUudjEuQXJ0aWZhY3RIABIvCgpwaWlfZW50aXR5GAQgASgLMhkucXBvaW50LnR5cGUudjEuUElJRW50aXR5SAASMAoKY29ubmVjdGlvbhgFIAEoCzIaLnFwb2ludC50eXBlLnYxLkNvbm5lY3Rpb25IAEIHCgVldmVudCJGCg5Jbmdlc3RSZXNwb25zZRIcChR0b3RhbF9hY2NlcHRlZF9jb3VudBgBIAEoDRIWCg5hY2NlcHRlZF9jb3VudBgCIAEoDTKjAQoRRXZlbnRTdG9yZVNlcnZpY2USQQoEUGluZxIaLmV2ZW50c3RvcmUudjEuUGluZ1JlcXVlc3QaGy5ldmVudHN0b3JlLnYxLlBpbmdSZXNwb25zZSIAEksKBkluZ2VzdBIcLmV2ZW50c3RvcmUudjEuSW5nZXN0UmVxdWVzdBodLmV2ZW50c3RvcmUudjEuSW5nZXN0UmVzcG9uc2UiACgBMAFCsQEKEWNvbS5ldmVudHN0b3JlLnYxQglNYWluUHJvdG9QAVo8Z2l0aHViLmNvbS9xcG9pbnQtaW8vcHJvdG8vZ2VuL2dvL2V2ZW50c3RvcmUvdjE7ZXZlbnRzdG9yZXYxogIDRVhYqgINRXZlbnRzdG9yZS5WMcoCDUV2ZW50c3RvcmVcVjHiAhlFdmVudHN0b3JlXFYxXEdQQk1ldGFkYXRh6gIORXZlbnRzdG9yZTo6VjFiBnByb3RvMw", [file_qpoint_type_v1_artifact, file_qpoint_type_v1_connection, file_qpoint_type_v1_issue, file_qpoint_type_v1_pii, file_qpoint_type_v1_request]);

/**
 * @generated from message eventstore.v1.PingRequest
 */
export type PingRequest = Message<"eventstore.v1.PingRequest"> & {
};

/**
 * Describes the message eventstore.v1.PingRequest.
 * Use `create(PingRequestSchema)` to create a new message.
 */
export const PingRequestSchema: GenMessage<PingRequest> = /*@__PURE__*/
  messageDesc(file_eventstore_v1_main, 0);

/**
 * @generated from message eventstore.v1.PingResponse
 */
export type PingResponse = Message<"eventstore.v1.PingResponse"> & {
  /**
   * @generated from field: string org_id = 1;
   */
  orgId: string;
};

/**
 * Describes the message eventstore.v1.PingResponse.
 * Use `create(PingResponseSchema)` to create a new message.
 */
export const PingResponseSchema: GenMessage<PingResponse> = /*@__PURE__*/
  messageDesc(file_eventstore_v1_main, 1);

/**
 * @generated from message eventstore.v1.IngestRequest
 */
export type IngestRequest = Message<"eventstore.v1.IngestRequest"> & {
  /**
   * @generated from field: repeated eventstore.v1.IngestRequest.Event events = 1;
   */
  events: IngestRequest_Event[];
};

/**
 * Describes the message eventstore.v1.IngestRequest.
 * Use `create(IngestRequestSchema)` to create a new message.
 */
export const IngestRequestSchema: GenMessage<IngestRequest> = /*@__PURE__*/
  messageDesc(file_eventstore_v1_main, 2);

/**
 * @generated from message eventstore.v1.IngestRequest.Event
 */
export type IngestRequest_Event = Message<"eventstore.v1.IngestRequest.Event"> & {
  /**
   * @generated from oneof eventstore.v1.IngestRequest.Event.event
   */
  event: {
    /**
     * @generated from field: qpoint.type.v1.Request request = 1;
     */
    value: Request;
    case: "request";
  } | {
    /**
     * @generated from field: qpoint.type.v1.Issue issue = 2;
     */
    value: Issue;
    case: "issue";
  } | {
    /**
     * @generated from field: qpoint.type.v1.Artifact artifact = 3;
     */
    value: Artifact;
    case: "artifact";
  } | {
    /**
     * @generated from field: qpoint.type.v1.PIIEntity pii_entity = 4;
     */
    value: PIIEntity;
    case: "piiEntity";
  } | {
    /**
     * @generated from field: qpoint.type.v1.Connection connection = 5;
     */
    value: Connection;
    case: "connection";
  } | { case: undefined; value?: undefined };
};

/**
 * Describes the message eventstore.v1.IngestRequest.Event.
 * Use `create(IngestRequest_EventSchema)` to create a new message.
 */
export const IngestRequest_EventSchema: GenMessage<IngestRequest_Event> = /*@__PURE__*/
  messageDesc(file_eventstore_v1_main, 2, 0);

/**
 * @generated from message eventstore.v1.IngestResponse
 */
export type IngestResponse = Message<"eventstore.v1.IngestResponse"> & {
  /**
   * total_accepted_count is the total number of events accepted by the server since the beginning of the stream.
   *
   * @generated from field: uint32 total_accepted_count = 1;
   */
  totalAcceptedCount: number;

  /**
   * accepted_count is the number of events accepted by the server since the last IngestResponse.
   *
   * @generated from field: uint32 accepted_count = 2;
   */
  acceptedCount: number;
};

/**
 * Describes the message eventstore.v1.IngestResponse.
 * Use `create(IngestResponseSchema)` to create a new message.
 */
export const IngestResponseSchema: GenMessage<IngestResponse> = /*@__PURE__*/
  messageDesc(file_eventstore_v1_main, 3);

/**
 * @generated from service eventstore.v1.EventStoreService
 */
export const EventStoreService: GenService<{
  /**
   * @generated from rpc eventstore.v1.EventStoreService.Ping
   */
  ping: {
    methodKind: "unary";
    input: typeof PingRequestSchema;
    output: typeof PingResponseSchema;
  },
  /**
   * @generated from rpc eventstore.v1.EventStoreService.Ingest
   */
  ingest: {
    methodKind: "bidi_streaming";
    input: typeof IngestRequestSchema;
    output: typeof IngestResponseSchema;
  },
}> = /*@__PURE__*/
  serviceDesc(file_eventstore_v1_main, 0);

