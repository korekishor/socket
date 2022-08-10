import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=socket.gethostname()
# if want to connect your mobile 
# host= '172.20.0.141'  # ip adress of mobile wifi

port=2256
s.connect((host,port))
con=True


while con:
    import psutil
    from psutil._common import BatteryTime

    massage=s.recv(1024)
    print("-----------",massage)
    
    batarydata=psutil.sensors_battery()
    print(psutil.cpu_percent(1))
    print(batarydata)
    s.send(str(batarydata.percent).encode("utf-8"))

    msg=input("enter the msg : ")
    s.send(msg.encode("utf-8"))
    if msg=="quite":
        con=False
        s.close()



        