from socket import *

serverIP = ""
serverPort = 27315
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP, serverPort))
