import requests

def status(url):
    response = requests.get(url)
    if response.status_code == 200:
        print('Web site is on/exists')
    else:
        print('Web site is not on/does not exist') 