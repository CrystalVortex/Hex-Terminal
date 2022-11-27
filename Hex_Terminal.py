build_version = "build 1.1"

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
                                           
                                           
                                  
{build_version}

""")

print("Loading....")

from imports import *



sys.path.insert(0, "plugins")



print("Done...")




def invalid():
  log.log_r("Invalid command or syntax!")


log.log_g("Loading complete!")

while True:
    cmd = input('User@Hex: ')
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

