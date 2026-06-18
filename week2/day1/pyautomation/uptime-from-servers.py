import subprocess


SERVERS_INFO: dict = {
    '10.10.11.128': {
        'username': 'maria',
        'port': 22,
        'uptime': None
    },
    '10.10.11.24': {
        'username': 'jake',
        'port': 22,
        'uptime': None
    },
    '10.10.11.44': {
        'username': 'julio',
        'port': 987,
        'uptime': None
    },
    '10.10.11.4': {
        'username': 'requp',
        'port': 832,
        'uptime': None
    },
}


def get_uptime(hostname: str, command: str) -> str:
    '''
    Get uptime from the given linux server by ssh.
    Manual typing password in the terminal requeired
    ''' 
    command: str = f'ssh -p {port} {username}@{hostname}\n'
    proc: subprocess.Popen = subprocess.Popen(
        ['bash'], text=True, bufsize=1,
        stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE
        )
    # First time type 'yes' in the terminal then it just a password from the servers
    proc.stdin.write(command) 
    for _ in range(20): # To skhostname all information in the beggining 
        proc.stdin.write('uptime\n')
        proc.stdin.flush()
        proc.stdout.readline()
    proc.stdin.write('uptime\n')
    uptime = proc.stdout.readline() 
    proc.stdin.close()
    return uptime


for hostname in SERVERS_INFO.keys():
    # Loop for all hostnames in SERVERS_INFO
    port = SERVERS_INFO[hostname]['port']
    username = SERVERS_INFO[hostname]['username']
    command: str = f'ssh -p {port} {username}@{hostname}\n'
    uptime: str = get_uptime(hostname=hostname, command=command)
    SERVERS_INFO[hostname]['uptime'] = uptime 


for hostname in SERVERS_INFO.keys():
    print(f'Server {hostname} uptime is:')
    print(SERVERS_INFO[hostname]['uptime'])
    print('--------------------')