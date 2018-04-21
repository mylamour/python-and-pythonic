import threading
import logging


class MThread(threading.Thread):
    def run(self):
        logging.debug('Running')


logging.basicConfig(
    level = logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)


def worker(num):
    print('Worker: {}'.format(num))

threads = []

for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for i in range(5):
    t = MThread()
    t.start()