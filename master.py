#!/usr/bin/env python

import socket
import time

botSocket = socket.socket()

botSocket.connect(("localhost",12345))
botSocket.send("dos 000.000.000.000 80")
botSocket.close()

