import os

def install(name):
    print(f"Installing package {name}...")
    os.system("pip install " + name)
