# socket() - It is used to create the socket object.
# bind() - It is used to bind-address to the socket. It takes two arguments hostname and port number.
# listen() - It is used to establish and start the TCP listener.
# accept() - It is used to TCP client connection until the connection is established.
# connect() - It is used to initiate TCP server connection.
# sendto() - It is used to send the UDP messages.
# send() - It is used to send the TCP messages.
# recv() - It is used to receive the TCP messages.
# close() - It is used to close a socket.


 
from pickle import TRUE
import socket
import os
import sys


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()    # '127.0.0.1' /  localhost

# connect mobile to server 
# host= '172.20.0.141'   # ip adress of mobile wifi

port=2256
s.bind((host,port))

# onlu can 5 take send data

s.listen(5)
# return socket client object and socket client address

socketclient,addres=s.accept()
print("got connection from ",addres)
con=True
while con:

    socketclient.send("You are connected to :".encode())
    msg=socketclient.recv(1024)

    msg=msg.decode("utf-8")
    print(msg)
    if int(msg) > 50:
        print("-------------",type(msg)," massage :",msg)
        # sys.exit()

    if msg=="quite":
        con=False
        s.close()
    
    if msg=="shutdown":
        os.system("shutdown -s -t 00")
        

 

# import psutil
# mem = psutil.virtual_memory()
# print(mem)

