
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import threading
import asyncio
import socketio

login_ok = None
event = threading.Event()
sio = socketio.AsyncClient()


@sio.on('wrong username')
def print_message():
    global login_ok
    print("this username is not exist")
    login_ok = False
    event.set()


@sio.on('wrong password')
def print_message():
    global login_ok
    print("your password is wrong please try again")
    login_ok = False
    event.set()


@sio.on('connected')
def print_message():
    global index
    global login_ok
    index = 1
    print("LOGIN OK")
    login_ok = True
    event.set()


def login():
    global index
    index = 0
    while index == 0:
        username = input("please enter your username\n")
        password = input("please enter your password\n")
        sio.emit('send user name and password', {
                 "username": username, "password": password})

        event.wait()
        event.clear()
        if login_ok:
            break
