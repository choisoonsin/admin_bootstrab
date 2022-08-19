# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import book_pb2 as book__pb2


class BookServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetBooksByBookName = channel.unary_unary(
                '/book.BookService/GetBooksByBookName',
                request_serializer=book__pb2.BookRequest.SerializeToString,
                response_deserializer=book__pb2.BookResponse.FromString,
                )


class BookServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetBooksByBookName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BookServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetBooksByBookName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBooksByBookName,
                    request_deserializer=book__pb2.BookRequest.FromString,
                    response_serializer=book__pb2.BookResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'book.BookService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BookService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetBooksByBookName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/book.BookService/GetBooksByBookName',
            book__pb2.BookRequest.SerializeToString,
            book__pb2.BookResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
