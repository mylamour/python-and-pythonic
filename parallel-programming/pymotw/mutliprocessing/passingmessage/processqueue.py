import multiprocessing
import random
import string

class Fun:
    def __init__(self, name):
        self.name = name

    def do_it(self):
        name = multiprocessing.current_process().name
        print("{} Just Do it; Fun {}".format(name, self.name))


def worker(q):
    obj = q.get()
    obj.do_it()



if __name__ == '__main__':
    queue = multiprocessing.Queue()

    p = multiprocessing.Process(target=worker, args=(queue,))
    p.start()

    queue.put(Fun("{}".format(random.choice(string.ascii_uppercase))))
    
    queue.close()
    queue.join_thread()
    p.join()
    