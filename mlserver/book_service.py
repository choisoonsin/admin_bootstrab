import book_pb2
import book_pb2_grpc

class BookService(book_pb2_grpc.BookServiceServicer):

    def GetBooksByBookName(self, request, context):

        res = book_pb2.BookResponse(
            message="what the..."
        )
        return res
