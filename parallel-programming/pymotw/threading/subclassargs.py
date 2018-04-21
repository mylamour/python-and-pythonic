import threading
import logging

class MThreadWithArgs(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
        args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name, daemon=daemon)
        self.args = args
        self.kwargs = kwargs

    def run(self):
        logging.debug("Runing with {} and {}"
            .format(self.args, self.kwargs)
        )

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName) -10s) %(message)s',
)

for i in range(5):
    t = MThreadWithArgs(args=(i,), kwargs={
        'a':'A',
        'b':'B'
    })
    t.start()
    