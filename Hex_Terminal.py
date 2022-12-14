version = "Version 1.3"

def about():
    print(f"""
    _    _                                   
    | |  | |                                  
    | |__| | _____  __                        
    |  __  |/ _ \ \/ /                        
    | |  | |  __/>  <                         
    |_|__|_|\___/_/\_\        _             _ 
    |__   __|                (_)           | |
        | | ___ _ __ _ __ ___  _ _ __   __ _| |
        | |/ _ \ '__| '_ ` _ \| | '_ \ / _` | |
        | |  __/ |  | | | | | | | | | | (_| | |
        |_|\___|_|  |_| |_| |_|_|_| |_|\__,_|_|
                                            
                                                                                
    [{version}] 

    """)

about()

print("Loading....")

from imports import *

def clear():
    for i in range(100):
        print("      ")

log.log_g("Loading complete!")

while True:
    cmd = input('User@Hex ~ $: ')
    def invalid():
        log.log_r("Invalid command or syntax! >>> " + cmd)
    if cmd == "::exit":
        print("Are you sure you want to close this terminal? (y,n)")
        ans = input()
        if ans == "y":
            log.log_r("Closing terminal...")
            time.sleep(0.1)
            exit()
    if cmd == "::clear":
        clear()
    try:
      exec(cmd)
    except SyntaxError as error:
        invalid()
    except NameError as error:
        invalid()
    except AttributeError as error:
        invalid()
    except ModuleNotFoundError as error:
        invalid()
    except ImportError as error:
        invalid()
    except FileNotFoundError as error:
        invalid()
    except MemoryError as error:
        invalid()      
    except IndexError as error:
        invalid()
    except TypeError as error:
        invalid()
    except ValueError as error:
        invalid()
    except LookupError as error:
        invalid()
    except FileExistsError as error:
        invalid()
    except EOFError as error:
        invalid()
    except TimeoutError as error:
        print("TimeoutError...")
    except RuntimeError as error:
        invalid()
    except shutil.Error as error:
        invalid()
        print("If you're trying to install a package it might already be installed.")
    except ConnectionAbortedError as error:
        print("Connection Aborted Error")
    except InterruptedError as error:
        invalid()
    except NotADirectoryError as error:
        invalid()
    except requests.exceptions.ConnectionError as error:
        print("No internet connection!")
    except PermissionError as error:
        print("[Permission denied] [PermissionError]")
    except OSError as error:
        print("[OSError] If you are trying to connect to ssh you might have typed in the details wrong")