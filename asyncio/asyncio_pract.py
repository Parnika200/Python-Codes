"""
async = used to define async function
await = waits for async fun
coroutine = fun that is executes
event loop= heart of asyncio, decides which task runs
"""
import asyncio

# asyncio.gather executes all tasks at same time
async def task1():
    print("Task 1 started")
    await asyncio.sleep(3)
    print("Task 1 completed")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(2)
    print("Task 2 completed")

async def main():
    await asyncio.gather(task1(),task2())

asyncio.run(main())


#
import asyncio

async def task():
    await asyncio.sleep(5)
    print("Task completed")

async def main():
    try:
        await asyncio.wait_for(task(), timeout=2) # max wait for
    except asyncio.TimeoutError:
        print("Time limit exceeded")

asyncio.run(main())


#create task create_task() tells Python: "Schedule this coroutine to run while I continue doing other things."

import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(3)
    print("Task 1 completed")

async def main():

    t1 = asyncio.create_task(task1())

    print("Main function running")

    await t1

asyncio.run(main())