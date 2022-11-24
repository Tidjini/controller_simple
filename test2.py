import asyncio
from threading import Thread

loop = asyncio.new_event_loop()


def f(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


t = Thread(target=f, args=(loop,))
t.start()


@asyncio.coroutine
def g():
    yield from asyncio.sleep(1)
    print('Hello, world!')


loop.call_soon_threadsafe(asyncio.async, g())
