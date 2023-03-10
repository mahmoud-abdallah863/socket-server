import websockets
import asyncio

PORT = 44445
print("Server is listening on port " + str(PORT))


connected_clients = set()


async def echo(client_socket, path):
    print("A new client connected")
    connected_clients.add(client_socket)
    try:
        async for message in client_socket:
            print(f'received message from client {message}')
            for socket in connected_clients:
                await socket.send(f'Message: {message}')
    except websockets.exceptions.ConnectionClosed as e:
        connected_clients.remove(client_socket)
        print("Client disconnected")

start_server = websockets.serve(echo, "192.168.1.103", PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
