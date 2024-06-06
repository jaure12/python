

import socket

HOST = '127.0.0.1'

PORT = 7777 #picking a non standard port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #af_inet is ipv4, sock_stream is a port

s.connect((HOST, PORT))

#kali linux
#nc -nvlp 7777
#netcat lp in -nvlp is a listener port being opened

