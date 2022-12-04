from termcolor import colored

from colorama import Fore, Back, Style

from colorama import init

init(strip=False)

def log(t):
    print(f"LOG: {t}")

def log_g(t):
    text = colored('LOG: ' + t, 'green')
    print(text)

def log_r(t):
    text = colored('LOG: ' + t, 'red')
    print(text)