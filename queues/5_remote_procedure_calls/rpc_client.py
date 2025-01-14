import os
import pika
import sys
import uuid


class FibonacciRpcClient:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="localhost"))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue="", exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

        self.response = None
        self.corr_id = None

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange="",
            routing_key="rpc_queue",
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=str(n))
        while self.response is None:
            self.connection.process_data_events(time_limit=None)
        return int(self.response)


def main():
    try:
        n = sys.argv[1]
    except IndexError:
        sys.stderr.write(f"Usage: {sys.argv[0]} [n: int] \n")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
            raise
    fibonacci_rpc = FibonacciRpcClient()
    print(f" [x] Requesting fib({n})")
    response = fibonacci_rpc.call(n)
    print(f" [.] Got {response}")


if __name__ == "__main__":
    main()
