from concurrent.futures import ThreadPoolExecutor
import asyncio
import socketio

sio = socketio.AsyncClient()


@sio.event
async def connect():
    print("connection established")


@sio.event
async def my_message(data):
    print("message received with ", data)
    await sio.emit("my response", {"response": "my response"})


@sio.event
async def disconnect():
    print("disconnected from server")


async def main():
    await sio.connect("http://127.0.0.1:5666")
    await sio.wait()


def program():
    while True:
        name = input("Enter name")
        sio.emit("my_message", {"name": name})


with ThreadPoolExecutor(max_workers=2) as e:
    s = e.submit(asyncio.run, main())
    p = e.submit(program)

    s.result()
    p.result()
