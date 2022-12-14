import requests
import wget
import zipfile
import os
import json
import shutil


def install(pkg):
    print(f"Searching for package {pkg}...")
    response = requests.get(f"https://github.com/CrystalVortex/HexTerminalPackages/raw/main/{pkg}.zip")
    if response.status_code == 200:
            print(f'Package {pkg} was found, installing...')
            ispkg = os.path.isfile(f"lib/{pkg}/{pkg}.py")
            if ispkg == "True":
                print("Package Already Installed!")
                
            else:      
                get = wget.download(f"https://github.com/CrystalVortex/HexTerminalPackages/raw/main/{pkg}.zip")
                shutil.unpack_archive(f"{pkg}.zip", f"lib/{pkg}")
                shutil.move(f"lib/{pkg}/{pkg}.py", "lib")
                file_object = open('imports.py', 'a')
                file_object.write("\n")
                file_object.write(f'from lib import {pkg}')
                print("[Midnight]: Install complete... you might have to restart this terminal.")
    else:
            print('Package Does not exist...') 