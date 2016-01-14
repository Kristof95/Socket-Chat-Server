import socket
import os

os.system('cls')


#---------------------------#
#-------Chat Nickname-------#
#---------------------------#
nickname = input("Choose a nickname: ")


#---------------------------#
#----Connection Settings----#
#---------------------------#
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ''
server_port = 8080
client_socket.connect((server_address, server_port))
client_socket.send(nickname.encode('utf-8'))



#---------------------------#
#-----Send Data Handler-----#
#---------------------------#
def Main():
    while True:
        try:
            user_msg = input("To:~# ")
            msg = nickname+ ": " +user_msg
            client_socket.send(msg.encode('utf-8'))
            data = client_socket.recv(1024)
            print(str(data.decode(encoding='utf-8',errors='strict')))
        except client_socket.error as e:
            print(e)
            break
    client_socket.close()
if __name__ == "__main__":
    Main()

