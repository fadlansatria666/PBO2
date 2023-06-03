import asyncio

class AsyncCounter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current
        else:
            raise StopAsyncIteration

async def async_iteration():
    async for num in AsyncCounter(5):
        print(num)

asyncio.run(async_iteration())
