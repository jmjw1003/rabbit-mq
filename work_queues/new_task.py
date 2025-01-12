import pika
import sys


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    channel.queue_declare(queue="task_queue", durable=True)

    msg = " ".join(sys.argv[1:]) or "Hello World!"
    channel.basic_publish(
        exchange="",
        routing_key="task_queue",
        body=msg,
        properties=pika.BasicProperties(
            delivery_mode=pika.DeliveryMode.Persistent
        )
    )

    print(" [x] Sent '{msg}'")

    connection.close()


if __name__ == "__main__":
    main()
