#!/usr/bin/python3

# Developing a TCP server

import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname()
port = 4444

serverSocket.bind((host, port))
# server listens for a maxiumum of 3 connections
serverSocket.listen(3)

while True:
    clientSocket, address = serverSocket.accept()
    print ('received connection from ' % str(address))

    message = 'Trank you for connecting to the server' + '\r\n'
    clientSocket.send(message)

    clientSocket.close()
