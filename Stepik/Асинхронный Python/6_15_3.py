import asyncio
import random
number_open_ports = {}

async def scan_port(address, port):
    await asyncio.sleep(1)
    if random.random()<=0.01:
        number_open_ports[address] += 1
        print(f"Port {port} on {address} is open")
        return port


async def scan_range(address, start_port, end_port):
    number_open_ports[address] = 0
    print(f"Scanning ports {start_port}-{end_port} on {address}")
    tasks = [asyncio.create_task(scan_port(address, i)) for i in range(start_port, end_port + 1)]

    t = await asyncio.gather(*tasks)
    t=[i for i in t if i is not None]
    if t==[]:
        print(f"No open ports on {address}")
async def main():

    # список ip-адресов
    ip_addresses = [
        '192.168.0.1', '192.168.0.2', '192.168.0.3', '192.168.0.4',
        '192.168.0.5', '192.168.0.6', '192.168.0.7', '192.168.0.8',
        '192.168.0.9', '192.168.0.10', '192.168.1.1', '192.168.1.2',
        '192.168.1.3', '192.168.1.4', '192.168.1.5', '192.168.1.6',
        '192.168.1.7', '192.168.1.8', '192.168.1.9', '192.168.1.10',
        '192.168.2.1', '192.168.2.2', '192.168.2.3', '192.168.2.4',
        '192.168.2.5'
    ]

    start_port = 0 # Получение стартового порта из аргументов командной строки
    end_port = 300 # Получение конечного порта из аргументов командной строки
    for ip_adress in ip_addresses:
        await scan_range(ip_adress, start_port, end_port) # Выполнение асинхронной функции сканирования портов
    for ip_adress in ip_addresses:
        print(f"Всего найдено открытых портов {number_open_ports[ip_adress]} для ip: {ip_adress}")

asyncio.run(main()) # Запуск асинхронного приложения