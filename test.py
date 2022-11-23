import asyncio
from random import randint


async def get_message():
    message = randint(0, 1_000)
    print(f'{message} got')
    return message


async def process_message(message):
    await asyncio.sleep(randint(1, 5))
    print(f'{message} processed')
    return message


async def deal_with_message(message):
    await asyncio.sleep(randint(1, 5))
    print(f'{message} dealt')


async def utilize_message():
    message = await get_message()
    message = await process_message(message)
    await deal_with_message(message)


parallel_max = 5  # don't utilize more than 5 msgs parallely
parallel_now = 0


def populate_tasks():
    global parallel_now
    for _ in range(parallel_max - parallel_now):
        parallel_now += 1
        task = asyncio.ensure_future(utilize_message())
        task.add_done_callback(on_utilized)


def on_utilized(_):
    global parallel_now
    parallel_now -= 1
    populate_tasks()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        populate_tasks()
        loop.run_forever()
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()
