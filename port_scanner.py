

import sys
import socket
from datetime import datetime


if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #translate host name to ipv4

else:
    print("Invalid amount of arguments.")
    print("Syntax Python3 port_scanner.py <ip>.")

"""argv is the amount of arguments we are giving
the argument will be python port_scanner.py <ip>
python is program used [0], port_scanner.py is argument [0], <ip> is argument [1]"""

#make a pretty banner

print("-" * 50)

print("Scanning target: " + target)
print("Time started: "+ str(datetime.now()))
print("-" * 50)

try:
    for port in range (2,100):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
except KeyboardInterrupt:
    print("exiting program")
    sys.exit
except socket.gaierror:
    print("hostname could not be resolved")
except socket.error:
    print("could not connect to server")