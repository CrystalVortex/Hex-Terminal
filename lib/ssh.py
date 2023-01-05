import paramiko

def connect(ip,user,passw):
    global client
    client = paramiko.SSHClient()
    client.connect(ip, user, passw)

def exec(cmd):
    global stdin,stdout,stderr
    stdin, stdout, stderr = client.exec_command('ls')
    print(stdout.read())

def close():
    client.close()
