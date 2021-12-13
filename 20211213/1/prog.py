import random 
import asyncio
from collections import defaultdict

L = eval(input())
LL = L.copy()


async def merge(begin0, begin1, end1, l_ev, r_ev, my_ev):
    await r_ev.wait()
    await l_ev.wait()

    end0 = begin1
    i = begin0
    begin = begin0

    while begin0 < end0 and begin1 < end1:
        if LL[begin0] < L[begin1]:
            LL[i] = L[begin0]
            begin0 += 1
        else:
            LL[i] = L[begin1]
            begin1 += 1
        i += 1

    await asyncio.sleep(0)

    LL[i:end1] = L[begin0:end0] + L[begin1:end1]
    L[begin:end1] = LL[begin:end1]
    my_ev.set()

async def joiner():

    events = defaultdict(asyncio.Event)
    tasks = []

    for p in range(4):
        b = 2 ** (p+1)
        for i in range(0, len(L), b):
            tasks.append(asyncio.create_task(merge(i, i+b // 2, i+b, events[f'{p}-{i}'], events[f'{p}-{i+b//2}'], events[f'{p+1}-{i}'])))

    for i in range(16):
        events[f'0-{i}'].set()

    await asyncio.gather(*tasks)


asyncio.run(joiner())
print(L)
