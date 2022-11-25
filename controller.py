from aiohttp import web
import socketio
import time


HOST = "127.0.0.1"
PORT = 5000

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)


async def index(request):
    """Serve the client-side application."""
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')


async def notify(request):
    """Serve the client-side application."""
    # print('request', request.body())
    await sio.emit('message', 'hi their')
    return web.Response(text="Hello, their")


@sio.event
async def connect(sid, environ):
    print("connect ", sid)


@sio.on('server_message')
async def get_message(sid, data):
    print("data ", sid, data)
    # await sio.emit('message', 'hi their')


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


# @sio.on('pass')
# def catch_all(sid, data):
#     print('data-> ', sid, data)


app.router.add_static('/static', 'static')
app.router.add_post('/', notify)

if __name__ == '__main__':
    web.run_app(app, host=HOST, port=PORT)
