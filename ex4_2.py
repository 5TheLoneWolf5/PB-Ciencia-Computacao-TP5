"""

Resultado:

$ python3 ex5_2.py 127.0.0.1

Starting Nmap 7.92 ( https://nmap.org ) at 2025-03-29 21:55 -03
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00016s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT    STATE SERVICE VERSION
22/tcp  open  ssh     OpenSSH 9.9 (protocol 2.0)
631/tcp open  ipp     CUPS 2.4

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 6.48 seconds

"""

import subprocess
import shlex
import sys

command = shlex.split(f"nmap -sV {sys.argv[1]}")
process = subprocess.run(command, capture_output=True, text=True, check=True)
print(process.stdout.strip())