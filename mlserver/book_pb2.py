# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: book.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nbook.proto\x12\x04\x62ook\" \n\rSimpleRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"!\n\x0eSimpleResponse\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x1e\n\x0b\x42ookRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1f\n\x0c\x42ookResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\x8e\x01\n\x0b\x42ookService\x12=\n\x12GetBooksByBookName\x12\x11.book.BookRequest\x1a\x12.book.BookResponse\"\x00\x12@\n\x11\x45xecPythonMLModel\x12\x13.book.SimpleRequest\x1a\x14.book.SimpleResponse\"\x00\x42!\n\x1f\x63om.example.adminjsp.rpcserviceb\x06proto3')



_SIMPLEREQUEST = DESCRIPTOR.message_types_by_name['SimpleRequest']
_SIMPLERESPONSE = DESCRIPTOR.message_types_by_name['SimpleResponse']
_BOOKREQUEST = DESCRIPTOR.message_types_by_name['BookRequest']
_BOOKRESPONSE = DESCRIPTOR.message_types_by_name['BookResponse']
SimpleRequest = _reflection.GeneratedProtocolMessageType('SimpleRequest', (_message.Message,), {
  'DESCRIPTOR' : _SIMPLEREQUEST,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:book.SimpleRequest)
  })
_sym_db.RegisterMessage(SimpleRequest)

SimpleResponse = _reflection.GeneratedProtocolMessageType('SimpleResponse', (_message.Message,), {
  'DESCRIPTOR' : _SIMPLERESPONSE,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:book.SimpleResponse)
  })
_sym_db.RegisterMessage(SimpleResponse)

BookRequest = _reflection.GeneratedProtocolMessageType('BookRequest', (_message.Message,), {
  'DESCRIPTOR' : _BOOKREQUEST,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:book.BookRequest)
  })
_sym_db.RegisterMessage(BookRequest)

BookResponse = _reflection.GeneratedProtocolMessageType('BookResponse', (_message.Message,), {
  'DESCRIPTOR' : _BOOKRESPONSE,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:book.BookResponse)
  })
_sym_db.RegisterMessage(BookResponse)

_BOOKSERVICE = DESCRIPTOR.services_by_name['BookService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037com.example.adminjsp.rpcservice'
  _SIMPLEREQUEST._serialized_start=20
  _SIMPLEREQUEST._serialized_end=52
  _SIMPLERESPONSE._serialized_start=54
  _SIMPLERESPONSE._serialized_end=87
  _BOOKREQUEST._serialized_start=89
  _BOOKREQUEST._serialized_end=119
  _BOOKRESPONSE._serialized_start=121
  _BOOKRESPONSE._serialized_end=152
  _BOOKSERVICE._serialized_start=155
  _BOOKSERVICE._serialized_end=297
# @@protoc_insertion_point(module_scope)
