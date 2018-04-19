import multiprocessing
import logging
import sys

def work():
    print("I am working...")
    sys.stdout.flush()
    # sys.exit(1)         # exitcode


if __name__ == '__main__':
    multiprocessing.log_to_stderr(logging.DEBUG)
    p = multiprocessing.Process(target=work)
    
    p.start()
    p.join()

    print(p.exitcode)
    