from socket import *

serverIP = ""
serverPort = 8080
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP, serverPort))
