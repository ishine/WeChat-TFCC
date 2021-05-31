# Copyright 2021 Wechat Group, Tencent
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tfcc_runtime/proto/data.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tfcc_runtime.proto import common_pb2 as tfcc__runtime_dot_proto_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="tfcc_runtime/proto/data.proto",
    package="tfcc.runtime.data",
    syntax="proto3",
    serialized_pb=_b(
        '\n\x1dtfcc_runtime/proto/data.proto\x12\x11tfcc.runtime.data\x1a\x1ftfcc_runtime/proto/common.proto"c\n\x08\x44\x61taItem\x12\x0c\n\x04name\x18\x01 \x01(\t\x12,\n\x05\x64type\x18\x02 \x01(\x0e\x32\x1d.tfcc.runtime.common.DataType\x12\r\n\x05shape\x18\x03 \x03(\r\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c"4\n\x06Inputs\x12*\n\x05items\x18\x01 \x03(\x0b\x32\x1b.tfcc.runtime.data.DataItem"5\n\x07Outputs\x12*\n\x05items\x18\x02 \x03(\x0b\x32\x1b.tfcc.runtime.data.DataItemb\x06proto3'
    ),
    dependencies=[
        tfcc__runtime_dot_proto_dot_common__pb2.DESCRIPTOR,
    ],
)


_DATAITEM = _descriptor.Descriptor(
    name="DataItem",
    full_name="tfcc.runtime.data.DataItem",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="tfcc.runtime.data.DataItem.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="dtype",
            full_name="tfcc.runtime.data.DataItem.dtype",
            index=1,
            number=2,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="shape",
            full_name="tfcc.runtime.data.DataItem.shape",
            index=2,
            number=3,
            type=13,
            cpp_type=3,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="data",
            full_name="tfcc.runtime.data.DataItem.data",
            index=3,
            number=4,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=85,
    serialized_end=184,
)


_INPUTS = _descriptor.Descriptor(
    name="Inputs",
    full_name="tfcc.runtime.data.Inputs",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="items",
            full_name="tfcc.runtime.data.Inputs.items",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=186,
    serialized_end=238,
)


_OUTPUTS = _descriptor.Descriptor(
    name="Outputs",
    full_name="tfcc.runtime.data.Outputs",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="items",
            full_name="tfcc.runtime.data.Outputs.items",
            index=0,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=240,
    serialized_end=293,
)

_DATAITEM.fields_by_name[
    "dtype"
].enum_type = tfcc__runtime_dot_proto_dot_common__pb2._DATATYPE
_INPUTS.fields_by_name["items"].message_type = _DATAITEM
_OUTPUTS.fields_by_name["items"].message_type = _DATAITEM
DESCRIPTOR.message_types_by_name["DataItem"] = _DATAITEM
DESCRIPTOR.message_types_by_name["Inputs"] = _INPUTS
DESCRIPTOR.message_types_by_name["Outputs"] = _OUTPUTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataItem = _reflection.GeneratedProtocolMessageType(
    "DataItem",
    (_message.Message,),
    dict(
        DESCRIPTOR=_DATAITEM,
        __module__="tfcc_runtime.proto.data_pb2"
        # @@protoc_insertion_point(class_scope:tfcc.runtime.data.DataItem)
    ),
)
_sym_db.RegisterMessage(DataItem)

Inputs = _reflection.GeneratedProtocolMessageType(
    "Inputs",
    (_message.Message,),
    dict(
        DESCRIPTOR=_INPUTS,
        __module__="tfcc_runtime.proto.data_pb2"
        # @@protoc_insertion_point(class_scope:tfcc.runtime.data.Inputs)
    ),
)
_sym_db.RegisterMessage(Inputs)

Outputs = _reflection.GeneratedProtocolMessageType(
    "Outputs",
    (_message.Message,),
    dict(
        DESCRIPTOR=_OUTPUTS,
        __module__="tfcc_runtime.proto.data_pb2"
        # @@protoc_insertion_point(class_scope:tfcc.runtime.data.Outputs)
    ),
)
_sym_db.RegisterMessage(Outputs)


# @@protoc_insertion_point(module_scope)
