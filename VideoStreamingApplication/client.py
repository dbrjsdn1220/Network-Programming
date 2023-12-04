import asyncio


async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 2355)

    print(f"Send: {message!r}")
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(10)
    print(f"Received: {data.decode()!r}")

    print("Close the connection")
    writer.close()
    await writer.wait_closed()


asyncio.run(tcp_echo_client("Hello, world!"))
