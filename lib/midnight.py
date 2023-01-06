import requests
import wget
import os
import shutil
from bs4 import BeautifulSoup


def install(pkg):
    print(f"Searching for package {pkg}...")
    response = requests.get(f"https://github.com/CrystalVortex/HexTerminalPackages/raw/main/{pkg}.zip")
    if response.status_code == 200:
            print(f'Package {pkg} was found, installing...')
            ispkg = os.path.isfile(f"lib/{pkg}/{pkg}.py")
            if ispkg == "True":
                print("Package Already Installed!")
                
            else:
                r = open("lib/sources/sources.txt", "r")
                src = r.read()
                print(src)    
                get = wget.download(f"{src}/{pkg}.zip")
                shutil.unpack_archive(f"{pkg}.zip", f"lib/{pkg}")
                shutil.move(f"lib/{pkg}/{pkg}.py", "lib")
                file_object = open('imports.py', 'a')
                file_object.write("\n")
                file_object.write(f'from lib import {pkg} # Installed automatically by running "midnight.install("{pkg}")"')
                print("[Midnight]: Install complete... you might have to restart this terminal.")
    else:
            print('Package Does not exist...') 

def info(pkg):
    print(f"Searching for package {pkg}...")
    response = requests.get(f"https://github.com/CrystalVortex/HexTerminalPackages/raw/main/{pkg}.zip")
    if response.status_code == 200:
            print(f'Package {pkg} was found, fetching...')


            url = f'https://raw.githubusercontent.com/CrystalVortex/HexTerminalPackages/main/{pkg}.txt'
            html_content = requests.get(url).text

            soup = BeautifulSoup(html_content, 'html.parser')

            text = soup.get_text()

            print(text)
            r = open("lib/sources/sources.txt", "r")
            src = r.read()
            print("Packages managed by: " + src)
    else:
        print("package not found...")


