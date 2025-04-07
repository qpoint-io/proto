// @generated by protoc-gen-es v2.2.5 with parameter "target=ts"
// @generated from file qpoint/type/v1/request.proto (package qpoint.type.v1, syntax proto3)
/* eslint-disable */

import type { GenFile, GenMessage } from "@bufbuild/protobuf/codegenv1";
import { fileDesc, messageDesc } from "@bufbuild/protobuf/codegenv1";
import { file_buf_validate_validate } from "../../../buf/validate/validate_pb";
import type { Timestamp } from "@bufbuild/protobuf/wkt";
import { file_google_protobuf_timestamp } from "@bufbuild/protobuf/wkt";
import type { Message } from "@bufbuild/protobuf";

/**
 * Describes the file qpoint/type/v1/request.proto.
 */
export const file_qpoint_type_v1_request: GenFile = /*@__PURE__*/
  fileDesc("ChxxcG9pbnQvdHlwZS92MS9yZXF1ZXN0LnByb3RvEg5xcG9pbnQudHlwZS52MSL+AwoHUmVxdWVzdBI1Cgl0aW1lc3RhbXAYASABKAsyGi5nb29nbGUucHJvdG9idWYuVGltZXN0YW1wQga6SAPIAQESGQoJZGlyZWN0aW9uGAIgASgJQga6SAPIAQESHQoNY29ubmVjdGlvbl9pZBgDIAEoCUIGukgDyAEBEhMKC2VuZHBvaW50X2lkGAUgASgJEhEKCXZlbmRvcl9pZBgGIAEoCRISCgJpZBgHIAEoCUIGukgDyAEBEgsKA3VybBgIIAEoCRIMCgRwYXRoGAkgASgJEg4KBm1ldGhvZBgKIAEoCRIOCgZzdGF0dXMYCyABKA0SEAoIZHVyYXRpb24YDCABKAQSFAoMY29udGVudF90eXBlGA0gASgJEhAKCGNhdGVnb3J5GA4gASgJEg0KBWFnZW50GA8gASgJEgwKBHRhZ3MYECADKAkSFgoOYnl0ZXNfcmVjZWl2ZWQYFSABKAQSEgoKYnl0ZXNfc2VudBgWIAEoBBI1CgphdXRoX3Rva2VuGBcgASgLMiEucXBvaW50LnR5cGUudjEuUmVxdWVzdC5BdXRoVG9rZW4aRQoJQXV0aFRva2VuEgwKBG1hc2sYASABKAkSDAoEaGFzaBgCIAEoCRIOCgZzb3VyY2UYAyABKAkSDAoEdHlwZRgEIAEoCUoECAQQBUoECBEQFUK1AQoSY29tLnFwb2ludC50eXBlLnYxQgxSZXF1ZXN0UHJvdG9QAVo3Z2l0aHViLmNvbS9xcG9pbnQtaW8vcHJvdG8vZ2VuL2dvL3Fwb2ludC90eXBlL3YxO3R5cGV2MaICA1FUWKoCDlFwb2ludC5UeXBlLlYxygIOUXBvaW50XFR5cGVcVjHiAhpRcG9pbnRcVHlwZVxWMVxHUEJNZXRhZGF0YeoCEFFwb2ludDo6VHlwZTo6VjFiBnByb3RvMw", [file_buf_validate_validate, file_google_protobuf_timestamp]);

/**
 * @generated from message qpoint.type.v1.Request
 */
export type Request = Message<"qpoint.type.v1.Request"> & {
  /**
   * @generated from field: google.protobuf.Timestamp timestamp = 1;
   */
  timestamp?: Timestamp;

  /**
   * @generated from field: string direction = 2;
   */
  direction: string;

  /**
   * @generated from field: string connection_id = 3;
   */
  connectionId: string;

  /**
   * @generated from field: string endpoint_id = 5;
   */
  endpointId: string;

  /**
   * @generated from field: string vendor_id = 6;
   */
  vendorId: string;

  /**
   * @generated from field: string id = 7;
   */
  id: string;

  /**
   * @generated from field: string url = 8;
   */
  url: string;

  /**
   * @generated from field: string path = 9;
   */
  path: string;

  /**
   * @generated from field: string method = 10;
   */
  method: string;

  /**
   * @generated from field: uint32 status = 11;
   */
  status: number;

  /**
   * @generated from field: uint64 duration = 12;
   */
  duration: bigint;

  /**
   * @generated from field: string content_type = 13;
   */
  contentType: string;

  /**
   * @generated from field: string category = 14;
   */
  category: string;

  /**
   * @generated from field: string agent = 15;
   */
  agent: string;

  /**
   * @generated from field: repeated string tags = 16;
   */
  tags: string[];

  /**
   * @generated from field: uint64 bytes_received = 21;
   */
  bytesReceived: bigint;

  /**
   * @generated from field: uint64 bytes_sent = 22;
   */
  bytesSent: bigint;

  /**
   * @generated from field: qpoint.type.v1.Request.AuthToken auth_token = 23;
   */
  authToken?: Request_AuthToken;
};

/**
 * Describes the message qpoint.type.v1.Request.
 * Use `create(RequestSchema)` to create a new message.
 */
export const RequestSchema: GenMessage<Request> = /*@__PURE__*/
  messageDesc(file_qpoint_type_v1_request, 0);

/**
 * @generated from message qpoint.type.v1.Request.AuthToken
 */
export type Request_AuthToken = Message<"qpoint.type.v1.Request.AuthToken"> & {
  /**
   * @generated from field: string mask = 1;
   */
  mask: string;

  /**
   * hash is a 32-byte SHA-256 hash of the auth token.
   *
   * @generated from field: string hash = 2;
   */
  hash: string;

  /**
   * @generated from field: string source = 3;
   */
  source: string;

  /**
   * @generated from field: string type = 4;
   */
  type: string;
};

/**
 * Describes the message qpoint.type.v1.Request.AuthToken.
 * Use `create(Request_AuthTokenSchema)` to create a new message.
 */
export const Request_AuthTokenSchema: GenMessage<Request_AuthToken> = /*@__PURE__*/
  messageDesc(file_qpoint_type_v1_request, 0, 0);

