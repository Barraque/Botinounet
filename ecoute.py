
#!/usr/bin/env python

import socket
import threading


def ajout(addr):
    print "new bot ", addr
    fichier = open("lstbot","r")
    with open("lstbot","r") as f:
        lines = f.readlines()
    with open("lstbot","w") as f:
        for line in lines:
            if line.split(' ')[0] != addr[0]:
                f.write(line)
        f.write(addr[0]+" "+str(addr[1])+"\n")
        
ecoute  = socket.socket()
ecoute.setsockopt(\
         socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ecoute.bind(('',12222))
while (1):
    ecoute.listen(1)
    connection, addr = ecoute.accept()
    t = threading.Thread(target = ajout,args=(addr,))
    t.start()
