
# Hex-Terminal 

An alternative to your default CLI


# Features

Plugins which can extend the functionality of Hex Terminal. This can be made fully in python. </br>
For any OS that supports python ( Macos, Windows, Linux ).</br>
A package manager called Midnight.</br>
Constant new features and updates. </br>
Full wiki for every single command </br>

# Help ❓
See the wiki tab for help or open an issue.
If you find a bug just report it in issues. (99.99% impossible)

       
        
        
 # Requesting new features 🆕
 
 You can request new features in issues.
 
 # Using plugins 🔌
 All you have to do is open up the file called "imports.py" and add the plugin name. For example: You put a file called things.py in the plugins folder, then, you go into the imports.py file and type "from plugins import things" (you dont need to add the .py part)
 
        
# Additonal notes 🗒️
Hex Terminal is usable although there isn't much features yet and no build instructions.
        
        
        
        


# Installation - Windows 🪟


Install [python](https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe). </br>
At the top of the repository, click code, download zip. </br>
Unzip it into a folder and open it. </br>
in the top bar, right click then click copy adress. </br>
Open up command promt or Windows Powershell </br>
type in cd then paste in the adress. Eg: (cd "C:\users\username\desktop\Best_Terminal_ever") </br>
then type in 

```pip install -r requirements.txt``` 

</br>
When its done you can close your terminal and open Hex_Terminal.py

# Installation - Linux ( Ubuntu ) 🟠
At the top of the repository, click code, download zip. </br>
Unzip it into a folder and open it. </br>
Open up a terminal in root. </br>
type in the following commands: </br>
```
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa
```
It will ask you to press enter to confirm. Run these commands after that: </br>
```
sudo apt update
sudo apt install python3.11 -y
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.11 1
sudo apt install pip -y
```
inside the folder where you unzipped this, right click and open in terminal. </br>
Type in:

```
pip install -r requirements.txt
```
Then you can close the terminal and open Hex_Terminal.py, and you're done. </br>

# Latest updates ⬆️
Build 1.3 (Latest)
- Packages now have descriptions
- Fixed wiki

Build 1.2 (Old)
- When getting a permission error it now says "[Permission denied] [PermissionError]"
- When opening the terminal it no longer says pre-1
- removed terminal.py from /lib/ and from imports.py
- You can now zip up a file using file.zip("filename")
- Changed the command and message from ping.web(name) to ping.site(website)
- New pip.exec(cmd) command
- Default run test plugin command has changed from test.do() to test.run()
- New file (settings/settings.json) more on that on the next version

