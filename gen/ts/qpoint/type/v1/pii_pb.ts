// @generated by protoc-gen-es v2.2.5 with parameter "target=ts"
// @generated from file qpoint/type/v1/pii.proto (package qpoint.type.v1, syntax proto3)
/* eslint-disable */

import type { GenFile, GenMessage } from "@bufbuild/protobuf/codegenv1";
import { fileDesc, messageDesc } from "@bufbuild/protobuf/codegenv1";
import { file_buf_validate_validate } from "../../../buf/validate/validate_pb";
import type { Timestamp } from "@bufbuild/protobuf/wkt";
import { file_google_protobuf_timestamp } from "@bufbuild/protobuf/wkt";
import type { Message } from "@bufbuild/protobuf";

/**
 * Describes the file qpoint/type/v1/pii.proto.
 */
export const file_qpoint_type_v1_pii: GenFile = /*@__PURE__*/
  fileDesc("ChhxcG9pbnQvdHlwZS92MS9waWkucHJvdG8SDnFwb2ludC50eXBlLnYxIr0CCglQSUlFbnRpdHkSNQoJdGltZXN0YW1wGAEgASgLMhouZ29vZ2xlLnByb3RvYnVmLlRpbWVzdGFtcEIGukgDyAEBEh0KDWNvbm5lY3Rpb25faWQYAiABKAlCBrpIA8gBARIaCgpyZXF1ZXN0X2lkGAMgASgJQga6SAPIAQESEwoLZW5kcG9pbnRfaWQYBCABKAkSEQoJdmVuZG9yX2lkGAUgASgJEgwKBHRhZ3MYBiADKAkSEwoLZW50aXR5X3R5cGUYByABKAkSDQoFc2NvcmUYCCABKAISDgoGc291cmNlGAkgASgJEhIKCmZpZWxkX3BhdGgYCiABKAkSEgoKdmFsdWVfaGFzaBgLIAEoCRIWCg5yZXF1ZXN0X21ldGhvZBgMIAEoCRIUCgxyZXF1ZXN0X3BhdGgYDSABKAlCsQEKEmNvbS5xcG9pbnQudHlwZS52MUIIUGlpUHJvdG9QAVo3Z2l0aHViLmNvbS9xcG9pbnQtaW8vcHJvdG8vZ2VuL2dvL3Fwb2ludC90eXBlL3YxO3R5cGV2MaICA1FUWKoCDlFwb2ludC5UeXBlLlYxygIOUXBvaW50XFR5cGVcVjHiAhpRcG9pbnRcVHlwZVxWMVxHUEJNZXRhZGF0YeoCEFFwb2ludDo6VHlwZTo6VjFiBnByb3RvMw", [file_buf_validate_validate, file_google_protobuf_timestamp]);

/**
 * @generated from message qpoint.type.v1.PIIEntity
 */
export type PIIEntity = Message<"qpoint.type.v1.PIIEntity"> & {
  /**
   * @generated from field: google.protobuf.Timestamp timestamp = 1;
   */
  timestamp?: Timestamp;

  /**
   * @generated from field: string connection_id = 2;
   */
  connectionId: string;

  /**
   * @generated from field: string request_id = 3;
   */
  requestId: string;

  /**
   * @generated from field: string endpoint_id = 4;
   */
  endpointId: string;

  /**
   * @generated from field: string vendor_id = 5;
   */
  vendorId: string;

  /**
   * @generated from field: repeated string tags = 6;
   */
  tags: string[];

  /**
   * @generated from field: string entity_type = 7;
   */
  entityType: string;

  /**
   * @generated from field: float score = 8;
   */
  score: number;

  /**
   * @generated from field: string source = 9;
   */
  source: string;

  /**
   * @generated from field: string field_path = 10;
   */
  fieldPath: string;

  /**
   * value_hash is a SHA-256 hash of the value. The length is 32 bytes (64 characters).
   *
   * @generated from field: string value_hash = 11;
   */
  valueHash: string;

  /**
   * @generated from field: string request_method = 12;
   */
  requestMethod: string;

  /**
   * @generated from field: string request_path = 13;
   */
  requestPath: string;
};

/**
 * Describes the message qpoint.type.v1.PIIEntity.
 * Use `create(PIIEntitySchema)` to create a new message.
 */
export const PIIEntitySchema: GenMessage<PIIEntity> = /*@__PURE__*/
  messageDesc(file_qpoint_type_v1_pii, 0);

