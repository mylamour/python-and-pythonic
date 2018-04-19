import sys, time, random, re, requests
import concurrent.futures
import logging

from multiprocessing import cpu_count, current_process, Manager, Queue, Process


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)


# Manager : This is a type of object that allows sharing Python objects 
# among different processes by means of proxies

def producer_task(q, fibo_dict):
    for i in range(15):
        value = random.randint(1, 20)
        fibo_dict[value] = None

        logger.info("Producer [%s] putting value [%d] into queue... " %(current_process().name, value))

        q.put(value)

def consumer_task(q, fibo_dict):
    while not q.empty():
        value = q.get(True, 0.05)
        a, b = 0, 1
        for item in range(value):
            a, b = b, a + b
            fibo_dict[value] = a 

        logger.info("Consumer [%s] getting value [%d] from queue... " % (current_process().name, value))

data_queue = Queue()
fibo_dict = {}

producer = Process(target = producer_task, args=(data_queue,fibo_dict))
producer.start()
producer.join()

consumer_list = []

for i in range(cpu_count()):
    consumer = Process(target=consumer_task, args=(data_queue,fibo_dict))
    consumer.start()
    consumer_list.append(consumer)
[consumer.join() for consumer in consumer_list]


