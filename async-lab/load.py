import asyncio
import sys
import httpx
import time

async def main():
    endpoint = sys.argv[1]
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 10

    limits = httpx.Limits(max_connections=1000)
    async with httpx.AsyncClient(base_url="http://127.0.0.1:8000", timeout=None, limits=limits) as client:
        start = time.perf_counter()
        await asyncio.gather(*(client.get(endpoint, params={"i": i}) for i in range(n)))
        print(f"{n} requests to {endpoint} took {time.perf_counter() - start:.2f}s")

asyncio.run(main())    