import requests
import wget
import zipfile
import os
import json



def install(pkg):
    print(f"Searching for package {pkg}...")
    response = requests.get("https://github.com/CrystalVortex/Hex-Terminal/tree/main/packages/" + pkg + ".zip")
    if response.status_code == 200:
        print(f'Package {pkg} was found, installing...')
        filename = wget.download(f"https://github.com/CrystalVortex/Hex-Terminal/raw/main/packages/{pkg}.zip")
        with zipfile.ZipFile(f"{pkg}.zip", 'r') as zip_ref:
            os.mkdir(pkg)
            zip_ref.extractall(pkg)
            f = open(f"{pkg}/{pkg}/{pkg}")
            data = json.load(f)
            get = wget.download(data["url"])
            f.close()
    else:
        print(f'Package {pkg} was not found.') 


