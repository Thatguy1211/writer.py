import requests
import colorama
import time
from colorama import *
from time import sleep

init(convert=True)
def Menu():
    for i in range(50):
        print('')
    print(f'''{Fore.CYAN}
        Created by: {Fore.MAGENTA} that_guy1211.exe

    {Fore.MAGENTA}
        ▎  ██╗       ██╗██████╗ ██╗████████╗███████╗██████╗  ▎
        ▎  ██║  ██╗  ██║██╔══██╗██║╚══██╔══╝██╔════╝██╔══██╗ ▎
        ▎  ╚██╗████╗██╔╝██████╔╝██║   ██║   █████╗  ██████╔╝ ▎
        ▎   ████╔═████║ ██╔══██╗██║   ██║   ██╔══╝  ██╔══██╗ ▎
        ▎   ╚██╔╝ ╚██╔╝ ██║  ██║██║   ██║   ███████╗██║  ██║ ▎
        ▎    ╚═╝   ╚═╝  ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝ ▎ \n''')
    

def Main():
    print(f"        {Fore.MAGENTA}[|] {Fore.WHITE}Type here your text:{Fore.CYAN}")
    text = str(input('            '))
    print(f"        {Fore.MAGENTA}[|] {Fore.WHITE}Are you sure this is correct? [Y|N]{Fore.CYAN}")
    answer = str(input('            '))
    
    if answer == "Y" or answer == "y":
        print(f'        {Fore.MAGENTA}[|] {Fore.WHITE}Understood, writing to file...')
        time.sleep(5)
        with open('document.txt', 'a') as f:
            f.write(text + '\n')
            f.close
        print(f'        {Fore.MAGENTA}[|] {Fore.WHITE}Finished, restarting program....')
        time.sleep(1)
        for i in range(50):
            print('')
    else:
        print(f'        {Fore.MAGENTA}[|] {Fore.WHITE}Understood, restarting program....')
        time.sleep(5)
        return

while True:
    Menu()
    Main()




