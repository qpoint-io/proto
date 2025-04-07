// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        (unknown)
// source: qpoint/type/v1/request.proto

package typev1

import (
	_ "buf.build/gen/go/bufbuild/protovalidate/protocolbuffers/go/buf/validate"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
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

type Request struct {
	state                    protoimpl.MessageState `protogen:"opaque.v1"`
	xxx_hidden_Timestamp     *timestamppb.Timestamp `protobuf:"bytes,1,opt,name=timestamp,proto3"`
	xxx_hidden_Direction     string                 `protobuf:"bytes,2,opt,name=direction,proto3"`
	xxx_hidden_ConnectionId  string                 `protobuf:"bytes,3,opt,name=connection_id,json=connectionId,proto3"`
	xxx_hidden_EndpointId    string                 `protobuf:"bytes,5,opt,name=endpoint_id,json=endpointId,proto3"`
	xxx_hidden_VendorId      string                 `protobuf:"bytes,6,opt,name=vendor_id,json=vendorId,proto3"`
	xxx_hidden_Id            string                 `protobuf:"bytes,7,opt,name=id,proto3"`
	xxx_hidden_Url           string                 `protobuf:"bytes,8,opt,name=url,proto3"`
	xxx_hidden_Path          string                 `protobuf:"bytes,9,opt,name=path,proto3"`
	xxx_hidden_Method        string                 `protobuf:"bytes,10,opt,name=method,proto3"`
	xxx_hidden_Status        uint32                 `protobuf:"varint,11,opt,name=status,proto3"`
	xxx_hidden_Duration      uint64                 `protobuf:"varint,12,opt,name=duration,proto3"`
	xxx_hidden_ContentType   string                 `protobuf:"bytes,13,opt,name=content_type,json=contentType,proto3"`
	xxx_hidden_Category      string                 `protobuf:"bytes,14,opt,name=category,proto3"`
	xxx_hidden_Agent         string                 `protobuf:"bytes,15,opt,name=agent,proto3"`
	xxx_hidden_Tags          []string               `protobuf:"bytes,16,rep,name=tags,proto3"`
	xxx_hidden_BytesReceived uint64                 `protobuf:"varint,21,opt,name=bytes_received,json=bytesReceived,proto3"`
	xxx_hidden_BytesSent     uint64                 `protobuf:"varint,22,opt,name=bytes_sent,json=bytesSent,proto3"`
	xxx_hidden_AuthToken     *Request_AuthToken     `protobuf:"bytes,23,opt,name=auth_token,json=authToken,proto3"`
	unknownFields            protoimpl.UnknownFields
	sizeCache                protoimpl.SizeCache
}

func (x *Request) Reset() {
	*x = Request{}
	mi := &file_qpoint_type_v1_request_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *Request) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Request) ProtoMessage() {}

func (x *Request) ProtoReflect() protoreflect.Message {
	mi := &file_qpoint_type_v1_request_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

func (x *Request) GetTimestamp() *timestamppb.Timestamp {
	if x != nil {
		return x.xxx_hidden_Timestamp
	}
	return nil
}

func (x *Request) GetDirection() string {
	if x != nil {
		return x.xxx_hidden_Direction
	}
	return ""
}

func (x *Request) GetConnectionId() string {
	if x != nil {
		return x.xxx_hidden_ConnectionId
	}
	return ""
}

func (x *Request) GetEndpointId() string {
	if x != nil {
		return x.xxx_hidden_EndpointId
	}
	return ""
}

func (x *Request) GetVendorId() string {
	if x != nil {
		return x.xxx_hidden_VendorId
	}
	return ""
}

func (x *Request) GetId() string {
	if x != nil {
		return x.xxx_hidden_Id
	}
	return ""
}

func (x *Request) GetUrl() string {
	if x != nil {
		return x.xxx_hidden_Url
	}
	return ""
}

func (x *Request) GetPath() string {
	if x != nil {
		return x.xxx_hidden_Path
	}
	return ""
}

func (x *Request) GetMethod() string {
	if x != nil {
		return x.xxx_hidden_Method
	}
	return ""
}

func (x *Request) GetStatus() uint32 {
	if x != nil {
		return x.xxx_hidden_Status
	}
	return 0
}

func (x *Request) GetDuration() uint64 {
	if x != nil {
		return x.xxx_hidden_Duration
	}
	return 0
}

func (x *Request) GetContentType() string {
	if x != nil {
		return x.xxx_hidden_ContentType
	}
	return ""
}

func (x *Request) GetCategory() string {
	if x != nil {
		return x.xxx_hidden_Category
	}
	return ""
}

func (x *Request) GetAgent() string {
	if x != nil {
		return x.xxx_hidden_Agent
	}
	return ""
}

func (x *Request) GetTags() []string {
	if x != nil {
		return x.xxx_hidden_Tags
	}
	return nil
}

func (x *Request) GetBytesReceived() uint64 {
	if x != nil {
		return x.xxx_hidden_BytesReceived
	}
	return 0
}

func (x *Request) GetBytesSent() uint64 {
	if x != nil {
		return x.xxx_hidden_BytesSent
	}
	return 0
}

func (x *Request) GetAuthToken() *Request_AuthToken {
	if x != nil {
		return x.xxx_hidden_AuthToken
	}
	return nil
}

func (x *Request) SetTimestamp(v *timestamppb.Timestamp) {
	x.xxx_hidden_Timestamp = v
}

func (x *Request) SetDirection(v string) {
	x.xxx_hidden_Direction = v
}

func (x *Request) SetConnectionId(v string) {
	x.xxx_hidden_ConnectionId = v
}

func (x *Request) SetEndpointId(v string) {
	x.xxx_hidden_EndpointId = v
}

func (x *Request) SetVendorId(v string) {
	x.xxx_hidden_VendorId = v
}

func (x *Request) SetId(v string) {
	x.xxx_hidden_Id = v
}

func (x *Request) SetUrl(v string) {
	x.xxx_hidden_Url = v
}

func (x *Request) SetPath(v string) {
	x.xxx_hidden_Path = v
}

func (x *Request) SetMethod(v string) {
	x.xxx_hidden_Method = v
}

func (x *Request) SetStatus(v uint32) {
	x.xxx_hidden_Status = v
}

func (x *Request) SetDuration(v uint64) {
	x.xxx_hidden_Duration = v
}

func (x *Request) SetContentType(v string) {
	x.xxx_hidden_ContentType = v
}

func (x *Request) SetCategory(v string) {
	x.xxx_hidden_Category = v
}

func (x *Request) SetAgent(v string) {
	x.xxx_hidden_Agent = v
}

func (x *Request) SetTags(v []string) {
	x.xxx_hidden_Tags = v
}

func (x *Request) SetBytesReceived(v uint64) {
	x.xxx_hidden_BytesReceived = v
}

func (x *Request) SetBytesSent(v uint64) {
	x.xxx_hidden_BytesSent = v
}

func (x *Request) SetAuthToken(v *Request_AuthToken) {
	x.xxx_hidden_AuthToken = v
}

func (x *Request) HasTimestamp() bool {
	if x == nil {
		return false
	}
	return x.xxx_hidden_Timestamp != nil
}

func (x *Request) HasAuthToken() bool {
	if x == nil {
		return false
	}
	return x.xxx_hidden_AuthToken != nil
}

func (x *Request) ClearTimestamp() {
	x.xxx_hidden_Timestamp = nil
}

func (x *Request) ClearAuthToken() {
	x.xxx_hidden_AuthToken = nil
}

type Request_builder struct {
	_ [0]func() // Prevents comparability and use of unkeyed literals for the builder.

	Timestamp     *timestamppb.Timestamp
	Direction     string
	ConnectionId  string
	EndpointId    string
	VendorId      string
	Id            string
	Url           string
	Path          string
	Method        string
	Status        uint32
	Duration      uint64
	ContentType   string
	Category      string
	Agent         string
	Tags          []string
	BytesReceived uint64
	BytesSent     uint64
	AuthToken     *Request_AuthToken
}

func (b0 Request_builder) Build() *Request {
	m0 := &Request{}
	b, x := &b0, m0
	_, _ = b, x
	x.xxx_hidden_Timestamp = b.Timestamp
	x.xxx_hidden_Direction = b.Direction
	x.xxx_hidden_ConnectionId = b.ConnectionId
	x.xxx_hidden_EndpointId = b.EndpointId
	x.xxx_hidden_VendorId = b.VendorId
	x.xxx_hidden_Id = b.Id
	x.xxx_hidden_Url = b.Url
	x.xxx_hidden_Path = b.Path
	x.xxx_hidden_Method = b.Method
	x.xxx_hidden_Status = b.Status
	x.xxx_hidden_Duration = b.Duration
	x.xxx_hidden_ContentType = b.ContentType
	x.xxx_hidden_Category = b.Category
	x.xxx_hidden_Agent = b.Agent
	x.xxx_hidden_Tags = b.Tags
	x.xxx_hidden_BytesReceived = b.BytesReceived
	x.xxx_hidden_BytesSent = b.BytesSent
	x.xxx_hidden_AuthToken = b.AuthToken
	return m0
}

type Request_AuthToken struct {
	state             protoimpl.MessageState `protogen:"opaque.v1"`
	xxx_hidden_Mask   string                 `protobuf:"bytes,1,opt,name=mask,proto3"`
	xxx_hidden_Hash   string                 `protobuf:"bytes,2,opt,name=hash,proto3"`
	xxx_hidden_Source string                 `protobuf:"bytes,3,opt,name=source,proto3"`
	xxx_hidden_Type   string                 `protobuf:"bytes,4,opt,name=type,proto3"`
	unknownFields     protoimpl.UnknownFields
	sizeCache         protoimpl.SizeCache
}

func (x *Request_AuthToken) Reset() {
	*x = Request_AuthToken{}
	mi := &file_qpoint_type_v1_request_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *Request_AuthToken) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Request_AuthToken) ProtoMessage() {}

func (x *Request_AuthToken) ProtoReflect() protoreflect.Message {
	mi := &file_qpoint_type_v1_request_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

func (x *Request_AuthToken) GetMask() string {
	if x != nil {
		return x.xxx_hidden_Mask
	}
	return ""
}

func (x *Request_AuthToken) GetHash() string {
	if x != nil {
		return x.xxx_hidden_Hash
	}
	return ""
}

func (x *Request_AuthToken) GetSource() string {
	if x != nil {
		return x.xxx_hidden_Source
	}
	return ""
}

func (x *Request_AuthToken) GetType() string {
	if x != nil {
		return x.xxx_hidden_Type
	}
	return ""
}

func (x *Request_AuthToken) SetMask(v string) {
	x.xxx_hidden_Mask = v
}

func (x *Request_AuthToken) SetHash(v string) {
	x.xxx_hidden_Hash = v
}

func (x *Request_AuthToken) SetSource(v string) {
	x.xxx_hidden_Source = v
}

func (x *Request_AuthToken) SetType(v string) {
	x.xxx_hidden_Type = v
}

type Request_AuthToken_builder struct {
	_ [0]func() // Prevents comparability and use of unkeyed literals for the builder.

	Mask string
	// hash is a 32-byte SHA-256 hash of the auth token.
	Hash   string
	Source string
	Type   string
}

func (b0 Request_AuthToken_builder) Build() *Request_AuthToken {
	m0 := &Request_AuthToken{}
	b, x := &b0, m0
	_, _ = b, x
	x.xxx_hidden_Mask = b.Mask
	x.xxx_hidden_Hash = b.Hash
	x.xxx_hidden_Source = b.Source
	x.xxx_hidden_Type = b.Type
	return m0
}

var File_qpoint_type_v1_request_proto protoreflect.FileDescriptor

const file_qpoint_type_v1_request_proto_rawDesc = "" +
	"\n" +
	"\x1cqpoint/type/v1/request.proto\x12\x0eqpoint.type.v1\x1a\x1bbuf/validate/validate.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc4\x05\n" +
	"\aRequest\x12@\n" +
	"\ttimestamp\x18\x01 \x01(\v2\x1a.google.protobuf.TimestampB\x06\xbaH\x03\xc8\x01\x01R\ttimestamp\x12$\n" +
	"\tdirection\x18\x02 \x01(\tB\x06\xbaH\x03\xc8\x01\x01R\tdirection\x12+\n" +
	"\rconnection_id\x18\x03 \x01(\tB\x06\xbaH\x03\xc8\x01\x01R\fconnectionId\x12\x1f\n" +
	"\vendpoint_id\x18\x05 \x01(\tR\n" +
	"endpointId\x12\x1b\n" +
	"\tvendor_id\x18\x06 \x01(\tR\bvendorId\x12\x16\n" +
	"\x02id\x18\a \x01(\tB\x06\xbaH\x03\xc8\x01\x01R\x02id\x12\x10\n" +
	"\x03url\x18\b \x01(\tR\x03url\x12\x12\n" +
	"\x04path\x18\t \x01(\tR\x04path\x12\x16\n" +
	"\x06method\x18\n" +
	" \x01(\tR\x06method\x12\x16\n" +
	"\x06status\x18\v \x01(\rR\x06status\x12\x1a\n" +
	"\bduration\x18\f \x01(\x04R\bduration\x12!\n" +
	"\fcontent_type\x18\r \x01(\tR\vcontentType\x12\x1a\n" +
	"\bcategory\x18\x0e \x01(\tR\bcategory\x12\x14\n" +
	"\x05agent\x18\x0f \x01(\tR\x05agent\x12\x12\n" +
	"\x04tags\x18\x10 \x03(\tR\x04tags\x12%\n" +
	"\x0ebytes_received\x18\x15 \x01(\x04R\rbytesReceived\x12\x1d\n" +
	"\n" +
	"bytes_sent\x18\x16 \x01(\x04R\tbytesSent\x12@\n" +
	"\n" +
	"auth_token\x18\x17 \x01(\v2!.qpoint.type.v1.Request.AuthTokenR\tauthToken\x1a_\n" +
	"\tAuthToken\x12\x12\n" +
	"\x04mask\x18\x01 \x01(\tR\x04mask\x12\x12\n" +
	"\x04hash\x18\x02 \x01(\tR\x04hash\x12\x16\n" +
	"\x06source\x18\x03 \x01(\tR\x06source\x12\x12\n" +
	"\x04type\x18\x04 \x01(\tR\x04typeJ\x04\b\x04\x10\x05J\x04\b\x11\x10\x15B\xb5\x01\n" +
	"\x12com.qpoint.type.v1B\fRequestProtoP\x01Z7github.com/qpoint-io/proto/gen/go/qpoint/type/v1;typev1\xa2\x02\x03QTX\xaa\x02\x0eQpoint.Type.V1\xca\x02\x0eQpoint\\Type\\V1\xe2\x02\x1aQpoint\\Type\\V1\\GPBMetadata\xea\x02\x10Qpoint::Type::V1b\x06proto3"

var file_qpoint_type_v1_request_proto_msgTypes = make([]protoimpl.MessageInfo, 2)
var file_qpoint_type_v1_request_proto_goTypes = []any{
	(*Request)(nil),               // 0: qpoint.type.v1.Request
	(*Request_AuthToken)(nil),     // 1: qpoint.type.v1.Request.AuthToken
	(*timestamppb.Timestamp)(nil), // 2: google.protobuf.Timestamp
}
var file_qpoint_type_v1_request_proto_depIdxs = []int32{
	2, // 0: qpoint.type.v1.Request.timestamp:type_name -> google.protobuf.Timestamp
	1, // 1: qpoint.type.v1.Request.auth_token:type_name -> qpoint.type.v1.Request.AuthToken
	2, // [2:2] is the sub-list for method output_type
	2, // [2:2] is the sub-list for method input_type
	2, // [2:2] is the sub-list for extension type_name
	2, // [2:2] is the sub-list for extension extendee
	0, // [0:2] is the sub-list for field type_name
}

func init() { file_qpoint_type_v1_request_proto_init() }
func file_qpoint_type_v1_request_proto_init() {
	if File_qpoint_type_v1_request_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_qpoint_type_v1_request_proto_rawDesc), len(file_qpoint_type_v1_request_proto_rawDesc)),
			NumEnums:      0,
			NumMessages:   2,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_qpoint_type_v1_request_proto_goTypes,
		DependencyIndexes: file_qpoint_type_v1_request_proto_depIdxs,
		MessageInfos:      file_qpoint_type_v1_request_proto_msgTypes,
	}.Build()
	File_qpoint_type_v1_request_proto = out.File
	file_qpoint_type_v1_request_proto_goTypes = nil
	file_qpoint_type_v1_request_proto_depIdxs = nil
}
