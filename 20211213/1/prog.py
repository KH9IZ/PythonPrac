import random 
import asyncio
from collections import defaultdict

L = list(range(16))
random.shuffle(L)
LL = L.copy()


async def merge(b0, b1, e1, n, el, er, myev):
    e0 = b1
    i = b0
    b = b0
    await el.wait()
    await er.wait()

    while b0 < e0 and b1 < e1:
        if L[b0] < L[b1]:
            LL[i] = L[b0]
            b0 += 1
        else:
            LL[i] = L[b1]
            b1 += 1
        i += 1
    await asyncio.sleep(0.1)
    print("-> ",n)
    LL[i:e1] = L[b0:e0] + L[b1:e1]
    L[b:e1] = LL[b:e1]
    myev.set()

async def joiner():
    events = defaultdict(asyncio.Event)
    tasks = []
    n = 0
    for p in range(4):
        b = 2 ** (p+1)
        for i in range(0, len(L), b):
            tasks.append(asyncio.create_task(merge(i, i+b // 2, i+b, n, events[f'{p}-{i}'], events[f'{p}-{i+b//2}'], events[f'{p+1}-{i}'])))
            n += 1
    for i in range(16):
        events[f'0-{i}'].set()
    await asyncio.gather(*tasks)
asyncio.run(joiner())
print(L)
