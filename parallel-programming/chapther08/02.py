import asyncio

@asyncio.coroutine
def sleep_coro(name, seconds=1):
    print("[%s] coroutine will sleep for %d seconds..." %(name, seconds))

    yield from asyncio.sleep(seconds)
    print("[%s] done !" % name)

if __name__ == '__main__':
    tasks = [asyncio.Task(sleep_coro('Task-A',10)),
            asyncio.Task(sleep_coro('Task-B')),
            asyncio.Task(sleep_coro('Task-C'))]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*tasks))