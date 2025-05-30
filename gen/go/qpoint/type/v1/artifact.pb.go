// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        (unknown)
// source: qpoint/type/v1/artifact.proto

package typev1

import (
	_ "buf.build/gen/go/bufbuild/protovalidate/protocolbuffers/go/buf/validate"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	structpb "google.golang.org/protobuf/types/known/structpb"
	timestamppb "google.golang.org/protobuf/types/known/timestamppb"
	reflect "reflect"
	unsafe "unsafe"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type Artifact struct {
	state                   protoimpl.MessageState `protogen:"opaque.v1"`
	xxx_hidden_Timestamp    *timestamppb.Timestamp `protobuf:"bytes,1,opt,name=timestamp,proto3"`
	xxx_hidden_ConnectionId string                 `protobuf:"bytes,2,opt,name=connection_id,json=connectionId,proto3"`
	xxx_hidden_RequestId    string                 `protobuf:"bytes,3,opt,name=request_id,json=requestId,proto3"`
	xxx_hidden_Type         string                 `protobuf:"bytes,4,opt,name=type,proto3"`
	xxx_hidden_EndpointId   string                 `protobuf:"bytes,5,opt,name=endpoint_id,json=endpointId,proto3"`
	xxx_hidden_VendorId     string                 `protobuf:"bytes,6,opt,name=vendor_id,json=vendorId,proto3"`
	xxx_hidden_Digest       string                 `protobuf:"bytes,7,opt,name=digest,proto3"`
	xxx_hidden_Url          string                 `protobuf:"bytes,8,opt,name=url,proto3"`
	xxx_hidden_Summary      *structpb.Struct       `protobuf:"bytes,9,opt,name=summary,proto3"`
	unknownFields           protoimpl.UnknownFields
	sizeCache               protoimpl.SizeCache
}

func (x *Artifact) Reset() {
	*x = Artifact{}
	mi := &file_qpoint_type_v1_artifact_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *Artifact) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Artifact) ProtoMessage() {}

func (x *Artifact) ProtoReflect() protoreflect.Message {
	mi := &file_qpoint_type_v1_artifact_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

func (x *Artifact) GetTimestamp() *timestamppb.Timestamp {
	if x != nil {
		return x.xxx_hidden_Timestamp
	}
	return nil
}

func (x *Artifact) GetConnectionId() string {
	if x != nil {
		return x.xxx_hidden_ConnectionId
	}
	return ""
}

func (x *Artifact) GetRequestId() string {
	if x != nil {
		return x.xxx_hidden_RequestId
	}
	return ""
}

func (x *Artifact) GetType() string {
	if x != nil {
		return x.xxx_hidden_Type
	}
	return ""
}

func (x *Artifact) GetEndpointId() string {
	if x != nil {
		return x.xxx_hidden_EndpointId
	}
	return ""
}

func (x *Artifact) GetVendorId() string {
	if x != nil {
		return x.xxx_hidden_VendorId
	}
	return ""
}

func (x *Artifact) GetDigest() string {
	if x != nil {
		return x.xxx_hidden_Digest
	}
	return ""
}

func (x *Artifact) GetUrl() string {
	if x != nil {
		return x.xxx_hidden_Url
	}
	return ""
}

func (x *Artifact) GetSummary() *structpb.Struct {
	if x != nil {
		return x.xxx_hidden_Summary
	}
	return nil
}

func (x *Artifact) SetTimestamp(v *timestamppb.Timestamp) {
	x.xxx_hidden_Timestamp = v
}

func (x *Artifact) SetConnectionId(v string) {
	x.xxx_hidden_ConnectionId = v
}

func (x *Artifact) SetRequestId(v string) {
	x.xxx_hidden_RequestId = v
}

func (x *Artifact) SetType(v string) {
	x.xxx_hidden_Type = v
}

func (x *Artifact) SetEndpointId(v string) {
	x.xxx_hidden_EndpointId = v
}

func (x *Artifact) SetVendorId(v string) {
	x.xxx_hidden_VendorId = v
}

func (x *Artifact) SetDigest(v string) {
	x.xxx_hidden_Digest = v
}

func (x *Artifact) SetUrl(v string) {
	x.xxx_hidden_Url = v
}

func (x *Artifact) SetSummary(v *structpb.Struct) {
	x.xxx_hidden_Summary = v
}

func (x *Artifact) HasTimestamp() bool {
	if x == nil {
		return false
	}
	return x.xxx_hidden_Timestamp != nil
}

func (x *Artifact) HasSummary() bool {
	if x == nil {
		return false
	}
	return x.xxx_hidden_Summary != nil
}

func (x *Artifact) ClearTimestamp() {
	x.xxx_hidden_Timestamp = nil
}

func (x *Artifact) ClearSummary() {
	x.xxx_hidden_Summary = nil
}

type Artifact_builder struct {
	_ [0]func() // Prevents comparability and use of unkeyed literals for the builder.

	Timestamp    *timestamppb.Timestamp
	ConnectionId string
	RequestId    string
	Type         string
	EndpointId   string
	VendorId     string
	Digest       string
	Url          string
	Summary      *structpb.Struct
}

func (b0 Artifact_builder) Build() *Artifact {
	m0 := &Artifact{}
	b, x := &b0, m0
	_, _ = b, x
	x.xxx_hidden_Timestamp = b.Timestamp
	x.xxx_hidden_ConnectionId = b.ConnectionId
	x.xxx_hidden_RequestId = b.RequestId
	x.xxx_hidden_Type = b.Type
	x.xxx_hidden_EndpointId = b.EndpointId
	x.xxx_hidden_VendorId = b.VendorId
	x.xxx_hidden_Digest = b.Digest
	x.xxx_hidden_Url = b.Url
	x.xxx_hidden_Summary = b.Summary
	return m0
}

var File_qpoint_type_v1_artifact_proto protoreflect.FileDescriptor

const file_qpoint_type_v1_artifact_proto_rawDesc = "" +
	"\n" +
	"\x1dqpoint/type/v1/artifact.proto\x12\x0eqpoint.type.v1\x1a\x1bbuf/validate/validate.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xd7\x02\n" +
	"\bArtifact\x12@\n" +
	"\ttimestamp\x18\x01 \x01(\v2\x1a.google.protobuf.TimestampB\x06\xbaH\x03\xc8\x01\x01R\ttimestamp\x12+\n" +
	"\rconnection_id\x18\x02 \x01(\tB\x06\xbaH\x03\xc8\x01\x01R\fconnectionId\x12%\n" +
	"\n" +
	"request_id\x18\x03 \x01(\tB\x06\xbaH\x03\xc8\x01\x01R\trequestId\x12\x1a\n" +
	"\x04type\x18\x04 \x01(\tB\x06\xbaH\x03\xc8\x01\x01R\x04type\x12\x1f\n" +
	"\vendpoint_id\x18\x05 \x01(\tR\n" +
	"endpointId\x12\x1b\n" +
	"\tvendor_id\x18\x06 \x01(\tR\bvendorId\x12\x16\n" +
	"\x06digest\x18\a \x01(\tR\x06digest\x12\x10\n" +
	"\x03url\x18\b \x01(\tR\x03url\x121\n" +
	"\asummary\x18\t \x01(\v2\x17.google.protobuf.StructR\asummaryB\xb6\x01\n" +
	"\x12com.qpoint.type.v1B\rArtifactProtoP\x01Z7github.com/qpoint-io/proto/gen/go/qpoint/type/v1;typev1\xa2\x02\x03QTX\xaa\x02\x0eQpoint.Type.V1\xca\x02\x0eQpoint\\Type\\V1\xe2\x02\x1aQpoint\\Type\\V1\\GPBMetadata\xea\x02\x10Qpoint::Type::V1b\x06proto3"

var file_qpoint_type_v1_artifact_proto_msgTypes = make([]protoimpl.MessageInfo, 1)
var file_qpoint_type_v1_artifact_proto_goTypes = []any{
	(*Artifact)(nil),              // 0: qpoint.type.v1.Artifact
	(*timestamppb.Timestamp)(nil), // 1: google.protobuf.Timestamp
	(*structpb.Struct)(nil),       // 2: google.protobuf.Struct
}
var file_qpoint_type_v1_artifact_proto_depIdxs = []int32{
	1, // 0: qpoint.type.v1.Artifact.timestamp:type_name -> google.protobuf.Timestamp
	2, // 1: qpoint.type.v1.Artifact.summary:type_name -> google.protobuf.Struct
	2, // [2:2] is the sub-list for method output_type
	2, // [2:2] is the sub-list for method input_type
	2, // [2:2] is the sub-list for extension type_name
	2, // [2:2] is the sub-list for extension extendee
	0, // [0:2] is the sub-list for field type_name
}

func init() { file_qpoint_type_v1_artifact_proto_init() }
func file_qpoint_type_v1_artifact_proto_init() {
	if File_qpoint_type_v1_artifact_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_qpoint_type_v1_artifact_proto_rawDesc), len(file_qpoint_type_v1_artifact_proto_rawDesc)),
			NumEnums:      0,
			NumMessages:   1,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_qpoint_type_v1_artifact_proto_goTypes,
		DependencyIndexes: file_qpoint_type_v1_artifact_proto_depIdxs,
		MessageInfos:      file_qpoint_type_v1_artifact_proto_msgTypes,
	}.Build()
	File_qpoint_type_v1_artifact_proto = out.File
	file_qpoint_type_v1_artifact_proto_goTypes = nil
	file_qpoint_type_v1_artifact_proto_depIdxs = nil
}
