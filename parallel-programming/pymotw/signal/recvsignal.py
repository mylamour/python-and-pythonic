import signal
import os
import time


def recv_signal(signum, stack):
    print("Received: ",signum)


signal.signal(signal.SIGUSR1, recv_signal)
signal.signal(signal.SIGUSR2, recv_signal)

print('MY PID IS: ',os.getpid())

while True:
    print('Waiting...')
    time.sleep(3)