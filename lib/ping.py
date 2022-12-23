import os

def site(name):
    print("[Warning] This command will only work on certain Operating systems which have the ping command...")
    os.system("ping " + name)        

