#!/usr/bin/env python

import socket

botSocket = socket.socket()

botSocket.connect(("localhost",12222))
botSocket.close()

