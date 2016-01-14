import socket
import os
from threading import Thread

os.system('cls')

print("\n")
print("\t\t\t############PYTHON###########")
print("\t\t\t##     Client && Server    ##")
print("\t\t\t##     Author: Kristof     ##")
print("\t\t\t###########CODECOOL##########")
print("\n\n\n")


#---------------------------#
#----Connection Handler-----#
#------------AND------------#
#----Get And Send Message---#
#---------------------------#

def ConnectionHandler():
    c,  address = server_socket.accept()
    data = c.recv(1024)
    get_nickname = str(data.decode(encoding='utf-8', errors='strict'))
    nicknames = []
    if get_nickname not in nicknames:
        nicknames.append(get_nickname)
        print(str(data.decode(encoding='utf-8', errors='strict')) + " CONNECTED TO THE SERVER!")
    while True:
        try:
            data = c.recv(1024)
            print(str(data.decode(encoding='utf-8', errors='strict')))
            if not data:
                break
            msg = input("SERVER MESSAGE: ")
            c.sendall("Kristof: ".encode('utf-8') + msg.encode('utf-8'))
        except socket.error as e:
            print("Disconnect by user...")
            break
    c.close()


#----------------------------#
#----Connection Settings-----#
#----------------------------#
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_name = ''
server_port =  8080

server_socket.bind((server_name, server_port))
server_socket.listen(5)


for i in range(5):
    Thread(target=ConnectionHandler).start()
