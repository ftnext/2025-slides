import asyncio


async def say_hello(second: int):
    await asyncio.sleep(second)
    print(f"Hello from {second} later")


async def sequential():
    await say_hello(3)
    await say_hello(1)
    await say_hello(2)


async def concurrent():
    await asyncio.gather(
        say_hello(3),
        say_hello(1),
        say_hello(2),
    )


if __name__ == "__main__":
    print("Concurrent:")
    asyncio.run(concurrent())
    print()

    print("Sequential:")
    asyncio.run(sequential())

"""
Concurrent:
Hello from 1 later
Hello from 2 later
Hello from 3 later

Sequential:
Hello from 3 later
Hello from 1 later
Hello from 2 later
"""
