import sys
import socket
from datetime import datetime

if (len(sys.argv) != 2):
    sys.exit('Invalid number of arguments')

print(50*'-')
print((20*' ')+'Port scanner')
print(50*'-')

ipAdress = socket.gethostbyname(sys.argv[1])

print(50*'-')
print('Scanning ip address: '+ipAdress)
print('Start scanning at: '+str(datetime.now()))
print(50*'-')

try:
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((ipAdress, port))
        if result == 0:
            print('Port '+str(port)+' is open.')
        s.close

except KeyboardInterrupt:
    sys.exit('\nScanning open port stoped!')

except Exception:

    sys.exit('Exception while scanning '+ipAdress)

print(50*'*')
print('Scanning finished successffully')
print(50*'*')
