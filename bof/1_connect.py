# Import files
import socket
import sys

# Target
rhost = "192.168."
rport = 110


# Error Handling
try:
	# TCP socket connection
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((rhost,rport))
	
	# Send/receive buffer
	print s.recv(1024)
	s.send('USER test\r\n')
	print s.recv(1024)
	s.send('PASS asdf\r\n')
	print s.recv(1024)
	s.send('QUIT\r\n')
	
	# Close connection
	s.close()
except:
	# On error, perform following:
	print "Oops! Something went wrong!"
	sys.exit()

	
