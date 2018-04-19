import os

named_pipe = "ipc_pipe"

if not os.path.exists(named_pipe):
    os.mkfifo(named_pipe)


def read_message(input_pipe):
    fd = os.open(input_pipe, os.O_RDONLY)
    message = (" I pid [%d] recived a message => %s" %(os.getpid(),os.read(fd,22)))
    os.close()

    return message

if __name__ == '__main__':
    read_message(named_pipe)