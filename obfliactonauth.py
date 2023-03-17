import requests, os, uuid, hashlib
from colorama import Fore, init , Style
import subprocess


init()

def auth_process():
    hwid = hashlib.md5(subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip().encode()).hexdigest()
    url = 'https://pastebin.com/raw/9BZfTJby'

    print(f"{Fore.LIGHTBLUE_EX}HWID{Fore.RESET} {hwid}\n")


    if any(line.strip(',') == f"{hwid}" for line in requests.get(url).text.split(',')):
        print(f'{Fore.GREEN}[AUTH] {Fore.RESET}Successfully logged in')
    else:
        print(f'{Fore.RED}{Style.BRIGHT}[AUTH] {Style.RESET_ALL}{Fore.RESET}Your HWID is not in our database, \n   {Fore.RED}{Style.BRIGHT}[!]{Style.RESET_ALL}{Fore.RESET} Join Our Server [discord.gg/shearkeykingdom] and contact our support to get verified!')
        input(f'{Fore.RED}{Style.BRIGHT}[AUTH] {Style.RESET_ALL}{Fore.RESET}Enter to exit\n')
        os._exit(0)