# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_demo.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="grpc_demo.proto",
    package="seismo",
    syntax="proto3",
    serialized_options=b"\252\002\tSeismoSrv",
    serialized_pb=b'\n\x0fgrpc_demo.proto\x12\x06seismo"!\n\x11SeismoPingRequest\x12\x0c\n\x04name\x18\x01 \x01(\t""\n\x0fSeismoPingReply\x12\x0f\n\x07message\x18\x01 \x01(\t")\n\x19\x42iggestEventInDaysRequest\x12\x0c\n\x04\x64\x61ys\x18\x01 \x01(\x05"N\n\x14\x42iggestEventResponse\x12\x11\n\tmagnitude\x18\x01 \x01(\x02\x12\x10\n\x08latitude\x18\x02 \x01(\x02\x12\x11\n\tlongitude\x18\x03 \x01(\x02"A\n\x15\x42iggestEventOnRequest\x12\x0b\n\x03\x64\x61y\x18\x01 \x01(\x05\x12\r\n\x05month\x18\x02 \x01(\x05\x12\x0c\n\x04year\x18\x03 \x01(\x05\x32\xfd\x01\n\rSeismoService\x12\x42\n\nSeismoPing\x12\x19.seismo.SeismoPingRequest\x1a\x17.seismo.SeismoPingReply"\x00\x12W\n\x12\x42iggestEventInDays\x12!.seismo.BiggestEventInDaysRequest\x1a\x1c.seismo.BiggestEventResponse"\x00\x12O\n\x0e\x42iggestEventOn\x12\x1d.seismo.BiggestEventOnRequest\x1a\x1c.seismo.BiggestEventResponse"\x00\x42\x0c\xaa\x02\tSeismoSrvb\x06proto3',
)


_SEISMOPINGREQUEST = _descriptor.Descriptor(
    name="SeismoPingRequest",
    full_name="seismo.SeismoPingRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="seismo.SeismoPingRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=27,
    serialized_end=60,
)


_SEISMOPINGREPLY = _descriptor.Descriptor(
    name="SeismoPingReply",
    full_name="seismo.SeismoPingReply",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="message",
            full_name="seismo.SeismoPingReply.message",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=62,
    serialized_end=96,
)


_BIGGESTEVENTINDAYSREQUEST = _descriptor.Descriptor(
    name="BiggestEventInDaysRequest",
    full_name="seismo.BiggestEventInDaysRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="days",
            full_name="seismo.BiggestEventInDaysRequest.days",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=98,
    serialized_end=139,
)


_BIGGESTEVENTRESPONSE = _descriptor.Descriptor(
    name="BiggestEventResponse",
    full_name="seismo.BiggestEventResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="magnitude",
            full_name="seismo.BiggestEventResponse.magnitude",
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="latitude",
            full_name="seismo.BiggestEventResponse.latitude",
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="longitude",
            full_name="seismo.BiggestEventResponse.longitude",
            index=2,
            number=3,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=141,
    serialized_end=219,
)


_BIGGESTEVENTONREQUEST = _descriptor.Descriptor(
    name="BiggestEventOnRequest",
    full_name="seismo.BiggestEventOnRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="day",
            full_name="seismo.BiggestEventOnRequest.day",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="month",
            full_name="seismo.BiggestEventOnRequest.month",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="year",
            full_name="seismo.BiggestEventOnRequest.year",
            index=2,
            number=3,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=221,
    serialized_end=286,
)

DESCRIPTOR.message_types_by_name["SeismoPingRequest"] = _SEISMOPINGREQUEST
DESCRIPTOR.message_types_by_name["SeismoPingReply"] = _SEISMOPINGREPLY
DESCRIPTOR.message_types_by_name[
    "BiggestEventInDaysRequest"
] = _BIGGESTEVENTINDAYSREQUEST
DESCRIPTOR.message_types_by_name["BiggestEventResponse"] = _BIGGESTEVENTRESPONSE
DESCRIPTOR.message_types_by_name["BiggestEventOnRequest"] = _BIGGESTEVENTONREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SeismoPingRequest = _reflection.GeneratedProtocolMessageType(
    "SeismoPingRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _SEISMOPINGREQUEST,
        "__module__": "grpc_demo_pb2"
        # @@protoc_insertion_point(class_scope:seismo.SeismoPingRequest)
    },
)
_sym_db.RegisterMessage(SeismoPingRequest)

SeismoPingReply = _reflection.GeneratedProtocolMessageType(
    "SeismoPingReply",
    (_message.Message,),
    {
        "DESCRIPTOR": _SEISMOPINGREPLY,
        "__module__": "grpc_demo_pb2"
        # @@protoc_insertion_point(class_scope:seismo.SeismoPingReply)
    },
)
_sym_db.RegisterMessage(SeismoPingReply)

BiggestEventInDaysRequest = _reflection.GeneratedProtocolMessageType(
    "BiggestEventInDaysRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _BIGGESTEVENTINDAYSREQUEST,
        "__module__": "grpc_demo_pb2"
        # @@protoc_insertion_point(class_scope:seismo.BiggestEventInDaysRequest)
    },
)
_sym_db.RegisterMessage(BiggestEventInDaysRequest)

BiggestEventResponse = _reflection.GeneratedProtocolMessageType(
    "BiggestEventResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _BIGGESTEVENTRESPONSE,
        "__module__": "grpc_demo_pb2"
        # @@protoc_insertion_point(class_scope:seismo.BiggestEventResponse)
    },
)
_sym_db.RegisterMessage(BiggestEventResponse)

BiggestEventOnRequest = _reflection.GeneratedProtocolMessageType(
    "BiggestEventOnRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _BIGGESTEVENTONREQUEST,
        "__module__": "grpc_demo_pb2"
        # @@protoc_insertion_point(class_scope:seismo.BiggestEventOnRequest)
    },
)
_sym_db.RegisterMessage(BiggestEventOnRequest)


DESCRIPTOR._options = None

_SEISMOSERVICE = _descriptor.ServiceDescriptor(
    name="SeismoService",
    full_name="seismo.SeismoService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    serialized_start=289,
    serialized_end=542,
    methods=[
        _descriptor.MethodDescriptor(
            name="SeismoPing",
            full_name="seismo.SeismoService.SeismoPing",
            index=0,
            containing_service=None,
            input_type=_SEISMOPINGREQUEST,
            output_type=_SEISMOPINGREPLY,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name="BiggestEventInDays",
            full_name="seismo.SeismoService.BiggestEventInDays",
            index=1,
            containing_service=None,
            input_type=_BIGGESTEVENTINDAYSREQUEST,
            output_type=_BIGGESTEVENTRESPONSE,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name="BiggestEventOn",
            full_name="seismo.SeismoService.BiggestEventOn",
            index=2,
            containing_service=None,
            input_type=_BIGGESTEVENTONREQUEST,
            output_type=_BIGGESTEVENTRESPONSE,
            serialized_options=None,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_SEISMOSERVICE)

DESCRIPTOR.services_by_name["SeismoService"] = _SEISMOSERVICE

# @@protoc_insertion_point(module_scope)
