# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SecDbKeychainSerializedAKSWrappedKey.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='SecDbKeychainSerializedAKSWrappedKey.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n*SecDbKeychainSerializedAKSWrappedKey.proto\"\\\n$SecDbKeychainSerializedAKSWrappedKey\x12\x12\n\nwrappedKey\x18\x01 \x02(\x0c\x12\x12\n\nrefKeyBlob\x18\x02 \x01(\x0c\x12\x0c\n\x04type\x18\x03 \x02(\r'
)




_SECDBKEYCHAINSERIALIZEDAKSWRAPPEDKEY = _descriptor.Descriptor(
  name='SecDbKeychainSerializedAKSWrappedKey',
  full_name='SecDbKeychainSerializedAKSWrappedKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='wrappedKey', full_name='SecDbKeychainSerializedAKSWrappedKey.wrappedKey', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='refKeyBlob', full_name='SecDbKeychainSerializedAKSWrappedKey.refKeyBlob', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='SecDbKeychainSerializedAKSWrappedKey.type', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=138,
)

DESCRIPTOR.message_types_by_name['SecDbKeychainSerializedAKSWrappedKey'] = _SECDBKEYCHAINSERIALIZEDAKSWRAPPEDKEY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SecDbKeychainSerializedAKSWrappedKey = _reflection.GeneratedProtocolMessageType('SecDbKeychainSerializedAKSWrappedKey', (_message.Message,), {
  'DESCRIPTOR' : _SECDBKEYCHAINSERIALIZEDAKSWRAPPEDKEY,
  '__module__' : 'SecDbKeychainSerializedAKSWrappedKey_pb2'
  # @@protoc_insertion_point(class_scope:SecDbKeychainSerializedAKSWrappedKey)
  })
_sym_db.RegisterMessage(SecDbKeychainSerializedAKSWrappedKey)


# @@protoc_insertion_point(module_scope)
