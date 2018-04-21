import logging
import threading
import time

def wait_for_event(e):
    logging.debug('Waiting fot event starting')
    event_is_set = e.wait()
    logging.debug('Event set: {}'.format(event_is_set))

def wait_for_event_timeout(e,t):
    while not e.is_set():
        logging.debug('Waiting for event timeout starting')
        event_is_set = e.wait(t)
        logging.debug('Event set: {}'.format(event_is_set))

        if event_is_set:
            logging.debug('Processing Event')
        else:
            logging.debug('Doing other work')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)


e = threading.Event()
t1 = threading.Thread(
    name='block',
    target=wait_for_event,
    args=(e,),
)

t1.start()

t2 = threading.Thread(
    name='nonblock',
    target=wait_for_event_timeout,
    args=(e,2),
)

t2.start()

logging.debug('Waiting before calling Event.set()')
time.sleep(3)

e.set()
logging.debug('Event is et')