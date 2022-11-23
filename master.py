import asyncio
import socketio
from threading import Thread

sio = socketio.AsyncClient()


@sio.event
async def connect():
    print('connected')


@sio.event
async def disconnect():
    print('disconnected')


async def main():
    await sio.connect('http://localhost:8564')


async def listen():
    await sio.wait()


async def handler():
    await sio.sleep(1)
    while True:
        name = input('Entre your name: ')
        await sio.emit('tidjini', {'response': name})


def program():
    asyncio.ensure_future(main())
    # task = asyncio.create_task(main())
    asyncio.ensure_future(listen())
    asyncio.ensure_future(handler())
    # task.add_done_callback(handler())

    # taskc.add_done_callback(handler())

    # await sio.emit('passage', {'response': name})


def get_or_create_eventloop():
    try:
        return asyncio.get_event_loop()
    except RuntimeError as ex:
        if "There is no current event loop in thread" in str(ex):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            return asyncio.get_event_loop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        program()
        loop.run_forever()
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()

        # t = Thread(target=asyncio.run, args=(program(),), daemon=True)
        # t.start()

        # asyncio.run(main())
