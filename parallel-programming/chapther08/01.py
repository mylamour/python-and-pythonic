import asyncio

@asyncio.coroutine
def sleep_coroutin(f):
    yield from asyncio.sleep(2)
    f.set_result("Done")

if __name__ == '__main__':
    future = asyncio.Future()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(sleep_coroutin(future))
    