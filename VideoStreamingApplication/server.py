import asyncio


async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Received {message!r} from {addr!r}")
    print(f"Send: {message!r}")
    writer.write(data)
    await writer.drain()


async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 2355)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f"Serving on {addrs}")

    async with server:
        await server.serve_forever()

asyncio.run(main())
