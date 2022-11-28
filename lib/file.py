import os

def md(foldername):
    print(f"Creating folder {foldername}...")
    os.mkdir(foldername)
    print(f"folder {foldername} created...")

def delete(filename):
    print(f"Are you sure to want to delete {filename}? y,n")
    opt = input()
    if opt == "y" : 
        print(f"deleting file {filename}...")
        os.remove(filename)
        print(f"file {filename} has been deleted...")

def delete_confirm(filename):
    print(f"deleting file {filename}...")
    os.remove(filename)
    print(f"file {filename} has been deleted...")

def delete_dir(filename):
    print(f"Are you sure to want to delete {filename}? y,n")
    opt = input()
    if opt == "y" : 
        print(f"deleting Directory {filename}...")
        os.rmdir(filename)
        print(f"Directory {filename} has been deleted...")

def new(filename):
    print(f"Creating file {filename}...")
    file_object  = open(filename, "w+")
    print(f"File {filename} has been created...")
