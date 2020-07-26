import socket
import sys

rhost = "192.168."
rport = 110


try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((rhost,rport))
	print s.recv(1024)
	s.send('USER test\r\n')
	print s.recv(1024)
	s.send('PASS asdf\r\n')
	print s.recv(1024)
	s.send('QUIT\r\n')
	s.close()
except:
	print "Oops! Something went wrong!"
	sys.exit()

	