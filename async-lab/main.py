import asyncio
import threading
import time

from fastapi import FastAPI
from fastapi.concurrency import run_in_threadpool

app = FastAPI()

def log(msg):
    t = threading.current_thread()
    now = time.strftime("%H:%M:%S") + f".{int(time.time() * 1000) % 1000}"
    print(f"[{now}] [{t.name} id={t.ident % 10000}] {msg}")

@app.get("/health")
async def health():
    return {"status": "alive"}

# 1. async def + non-blocking wait
@app.get("/async-good")
async def async_good(i: int = 0):
    log(f"start {i}")
    await asyncio.sleep(1)
    log(f"end {i}")
    return {"i": i}

# 2. def + blocking wait
@app.get("/sync-ok")
def sync_ok(i: int = 0):
    log(f"start {i}")
    time.sleep(1)
    log(f"end {i}")
    return {"i": i}

# 3. async def + blocking wait (the BUG)
@app.get("/async-bad")
async def async_bad(i: int = 0):
    log(f"start {i}")
    time.sleep(1)
    log(f"end {i}")
    return {"i": i}

