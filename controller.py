from aiohttp import web
import socketio


HOST = "127.0.0.1"
PORT = 8564

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)


async def index(request):
    """Serve the client-side application."""
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')


@sio.event
async def connect(sid, environ):
    print("connect ", sid)


@sio.on('chat_message')
def at_message(sid, data):
    print("data ", sid, data)


@sio.on('tidjini')
def passage(sid, data):
    print("data ", sid, data)
# @sio.event
# async def chat_message(sid, data):
#     print("message ", data)
#     await sio.emit('reply', room=sid)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


# @sio.on('pass')
# def catch_all(sid, data):
#     print('data-> ', sid, data)


app.router.add_static('/static', 'static')
app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app, host=HOST, port=PORT)
