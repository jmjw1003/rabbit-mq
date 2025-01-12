import pika

def main():
    # Connect to queue & get chanel
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    # Create a channel for our messages
    channel.queue_declare(queue="hello")

    # Publish a message to the exchange
    msg = "Hello World!"
    channel.basic_publish(
        exchange="",
        routing_key="hello",
        body=msg
    )

    print(" [x] Sent '{msg}'")

    # Finally, close the connection
    connection.close()


if __name__ == "__main__":
    main()
