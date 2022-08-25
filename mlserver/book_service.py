import book_pb2
import book_pb2_grpc

import matplotlib.pyplot as plt

from io import BytesIO
import base64


class BookService(book_pb2_grpc.BookServiceServicer):

    def GetBooksByBookName(self, request, context):

        res = book_pb2.BookResponse(
            message="what the..."
        )
        return res

    def ExecPythonMLModel(self, request, context):

        fig, ax = plt.subplots()

        fruits = ['apple', 'blueberry', 'cherry', 'orange']
        counts = [40, 100, 30, 55]
        bar_labels = ['red', 'blue', '_red', 'orange']
        bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

        ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

        ax.set_ylabel('fruit supply')
        ax.set_title('Fruit supply by kind and color')
        ax.legend(title='Fruit color')

        buf = BytesIO()
        plt.savefig(buf, format="png")

        data = base64.b64encode(buf.getbuffer()).decode(("ascii"))

        res = book_pb2.SimpleResponse(
            message=f"<img src='data:image/png;base64,{data}' id='resultImage'/>"
        )
        return res