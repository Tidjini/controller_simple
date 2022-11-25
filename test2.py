'''threading'''

from threading import Thread
import time

start = time.perf_counter()


def task(name):
    print(f'Task {name} started')
    time.sleep(2)
    print(f'TASK {name} DONE')
    # raise Exception('ThreadException')


t1 = Thread(target=task, args=('A',))
t2 = Thread(target=task, args=('B',))
# task(name='A')
# task(name='B')
t1.start()
t2.start()

t1.join()
t2.join()

end = time.perf_counter()


# run() method called when start is called
# is_alive() to check thread execution, if it is still execute the run() method, start() < is_alive() < join()
# daemon to run as application daemon
# main thread
# exception hook -> threading.exceptionhook = custom_hook


print("\n\nRuninig Time = {:.2f} second(s)".format(end-start))
input('Enter your name')
