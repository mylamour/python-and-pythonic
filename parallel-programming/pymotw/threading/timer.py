import threading
import time
import logging

def delayed():
    logging.debug('Worker running')

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName) -10s) %(message)s ',
)

t1 = threading.Timer(0.1 ,delayed)
t1.setName('T1')
t2 = threading.Timer(0.1 ,delayed)
t2.setName('T2')

logging.debug('starting Timers')
t1.start()
t2.start()

logging.debug('Waiting before canceling {}'.format(t2.getName()))
time.sleep(0.4)
logging.debug('Caceling {}'.format(t2.getName()))
t2.cancel()
logging.debug('Done')
