import os
import json

def install(name):
    print(f"Installing package {name}...")
    os.system("pip install " + name)

def exec(cmd):
    print("Tip: use the pip comand as you normally would but you dont need to start with pip. Eg:pip.exec('install flask')")
    os.system(f"pip3 {cmd}")
