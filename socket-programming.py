import socket

# UDP protocol
myp = socket.SOCK_DGRAM

#Network address family: IPv4
afn = socket.AF_INET

#create socket
s = socket.socket(afn,myp)

#mention ip address and port no
ip = "192.168.43.237"
port = 1234

#bind ip and port no
s.bind((ip,port))

#Recieve the signal/packet from sender
x = s.recvfrom(1024)

#print the output that is recieved from sender
print(x)
