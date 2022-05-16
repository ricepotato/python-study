import asyncio
import time


async def main():
    print(f"{time.ctime()} Hello!")
    await asyncio.sleep(1)
    print(f"{time.ctime()} Good bye!")


asyncio.run(main())
