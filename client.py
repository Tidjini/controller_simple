from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from threading import Thread, Event
import asyncio
import socketio

sio = socketio.AsyncClient()
main_event = Event()

# some changes
async def chatting():
    message = None
    while message != "quit":
        message = input("Enter your message:\n")
        try:
            await sio.emit("message", message)
        except:
            pass


@sio.event
async def connect():
    print("connection established")


@sio.event
async def disconnect():
    print("disconnected from server")


@sio.event
async def message(data):
    print("data ", data)


async def main():
    await sio.connect("http://localhost:5000")
    await sio.wait()
    # event.set()


async def timer():
    x = 0
    while True:
        x += 1
        await asyncio.sleep(1)
        print("Time", x)


async def chat():
    # await asyncio.sleep(20)
    # await sio.emit('message', 'I m out')
    # print('Chat Complete')
    # return
    pass


async def principle():
    loop = asyncio.new_event_loop()
    t = await main()
    loop.run_until_complete(t)
    await chat()
    # print('default thread pool', result)
    # t = asyncio.create_task(main())
    # d = asyncio.create_task(chat())

    # await t
    # # await d


if __name__ == "__main__":

    # asyncio.run(principle())
    # m = Thread(target=asyncio.run, args=(main(),))
    # t = Thread(target=asyncio.run, args=(chatting(),))

    # m.start()
    # t.start()

    # with ThreadPoolExecutor(max_workers=1) as e:
    #     # main_socket = e.submit(asyncio.run, main())
    #     c = e.submit(asyncio.run, main())
    # c.result()
    # t = Thread(target=asyncio.run, args=(main(),))
    # t.start()
    # asyncio.run(main())
    t = Thread(target=asyncio.run, args=(main(),), daemon=True)
    t.start()
    print("start my program")
    input("Enter something")
    # c = Thread(target=asyncio.run, args=(chatting(),))
    # c.start()

    # asyncio.run(main())
