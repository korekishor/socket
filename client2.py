import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='127.0.0.1'
port=1234
s.connect((host,port))

msg="hellow thos is client 1"
# s.send(bytes(msg))
# unocod estanderd  all charactor come in 
s.send(msg.encode("utf-8"))
s.close()

