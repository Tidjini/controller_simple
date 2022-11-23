from socketIO_client import SocketIO, LoggingNamespace

with SocketIO('localhost', 8564, LoggingNamespace) as socketIO:
    socketIO.emit('aaa')
    socketIO.wait(seconds=1)
