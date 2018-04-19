import os 

#IPC model

named_pipe = "ipc_pipe"

if not os.path.exists(named_pipe):
    os.mkfifo(named_pipe)

def write_message(input_pipe, message):
    fd = os.open(input_pipe, os.O_WRONLY)
    os.write(fd, (message % str(os.getpid())))
    os.close(fd)



if __name__ == '__main__':
    write_message(named_pipe,"IPC Writing...")
    