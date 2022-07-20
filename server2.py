from operator import add
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='127.0.0.1'
port=1234
s.bind((host,port))
s.listen(5)
socketclient,address=s.accept()
print("got connected from ",address)
msg=socketclient.recv(1024)
msg=msg.decode("utf-8")
print(msg)


