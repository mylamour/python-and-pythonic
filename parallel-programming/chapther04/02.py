import requests
import re
import sys
import logging
import threading
import queue 
import concurrent
import multiprocessing

from concurrent.futures import ThreadPoolExecutor
# if use concurrent.futures.ThreadPoolExectuor, it's would be error, but not this.

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

html_link_regex = re.compile('<a\s(?:.*?\s)*?href=[\'"](.*?)[\'"].*?>')

urls = queue.Queue()

urls.put('http://baidu.com')
urls.put('http://bing.com')
urls.put('http://github.com')
urls.put('http://forensix.cn')


result_dict = {}

def group_urls_task(urls):
    try:
        url = urls.get(True, 0.05)
        result_dict[url] = None
        logger.info("[%s] putting url [%s] in dictionary..." % (threading.current_thread().name,url))


    except queue.Empty:
        logging.error("Nothing to be done, queue is empty")


def crawle_task(url):
    links = []
    try:
        requests_data = requests.get(url)
        logger.info("[%s] putting url [%s] in dictionary..." % (threading.current_thread().name,url))

        links = html_link_regex.findall(requests_data.text)
    except:
        logger.error(sys.exc_info()[0])
        raise

    finally:
        return (url, links)

with ThreadPoolExecutor(max_workers=3) as group_link_threads:
    for i in range(urls.qsize()):
        group_link_threads.submit(group_urls_task,urls)


with ThreadPoolExecutor(max_workers=3) as crawler_link_threads:
    future_tasks = {crawler_link_threads.submit(crawle_task,url): url for url in result_dict.keys()}

