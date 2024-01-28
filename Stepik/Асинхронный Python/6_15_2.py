import asyncio
import random


async def scan_port(address, port):
    await asyncio.sleep(1)
    n = random.choice([0, 1])
    if n:
        print(f'Порт {port} на адресе {address} открыт')
        return port


async def scan_range(address, start_port, end_port):
    print(f'Сканирование портов с {start_port} по {end_port} на адресе {address}')
    tasks = [asyncio.create_task(scan_port(address, i)) for i in range(start_port, end_port + 1)]

    t = await asyncio.gather(*tasks)
    t=[i for i in t if i is not None]
    print(f'Открытые порты на адресе {address}: {t}')


asyncio.run(scan_range('192.168.0.1', 80, 85))
