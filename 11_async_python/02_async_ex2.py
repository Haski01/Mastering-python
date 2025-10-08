import asyncio

async def boil_water():
    print("Boiling water...")
    await asyncio.sleep(2)
    print("Water boiled!")

async def make_tea():
    print("Making tea...")
    await asyncio.sleep(3)
    print("chai is ready!")

async def main():
    await asyncio.gather(
        boil_water(),
        make_tea()
    )

# asyncio.run(main())

# example 2

async def brew(name):
    print(f"Brewing {name}...")
    await asyncio.sleep(3)
    print(f"{name} is ready!")

async def main():
    await asyncio.gather(
        brew("Masala chai"),
        brew("Ginger chai"),
        brew("Cardmom")
    )

asyncio.run(main())