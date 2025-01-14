import asyncio
from rstream import Producer


STREAM_NAME = "hello-world-python-stream"
STREAM_RETENTION = 500_000_000 # ~0.5GB


async def send():
    async with Producer(
        host="localhost",
        username="guest",
        password="guest",
    ) as producer:
        await producer.create_stream(
            STREAM_NAME, exists_ok=True, arguments={"max-length-bytes": STREAM_RETENTION}
        )

        await producer.send(stream=STREAM_NAME, message=b"Hello, World!")

        print(" [x] Hello, World! message sent")

        input(" [x] Press Enter to close the producer  ...")


with asyncio.Runner() as runner:
    runner.run(send())