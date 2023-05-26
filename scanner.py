!/bin/python3

import sys
import socket
from datetime import datetime

# add some input validation for the ip address argument
def validate_ip_address(ip_address):
	try:
		socket.inet_aton(ip_address)
		return True
	except socket.error:
		return False

# determine if there is an argument provided		
if len(sys.argv) == 2:
	ip_address = sys.argv[1]
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")
	exit()

# determine if ip address is valid and define target
if validate_ip_address(ip_address):
	target = ip_address
else:
	print("Not a valid IP address")
	exit()
	
#add a banner
print("-" * 50)
print("Scanning target " + target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print(f"Port {port} is open.")
		s.close()

except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()

except socket.error:
	print("Could not connect to the server.")
	sys.exit()
