import socket

#create socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#convert string message into bytes
msg = "Hello".encode()

#view type of msg
type(msg)

#send msg to ip address: port no  wher the socket program is waiting for packet
s.sendto(msg,("192.168.43.237",1234))

