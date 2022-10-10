#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import socket

def askinput():
    #change to raw_input for python 2.7
    c = input("1: add mail 1 pr \n2: rm mail 1 pr \n3: add mail 4 pr \n4: show queue \n5: print next cmd \nelse: exit\n ->: ")
    global choice
    if c == "1":
        choice = 1
        return 1
    elif c == "2":
        choice = 2
        return 1
    elif c == "3":
        choice = 3
        return 1
    elif c == "4":
        choice = 4
        return 1
    elif c == "5":
        choice = 5
        return 1
    else:
        return 0



# context = zmq.Context()

#  Socket to talk to server
# print("Connecting to hello world server…")
# socket = context.socket(zmq.REQ)
# socket.connect("tcp://localhost:5555")

host = socket.gethostname()  # as both code is running on same pc
port = 5000  # socket server port number

client_socket = socket.socket()  # instantiate
client_socket.connect((host, port))  # connect to the server
print("Connecting to server...")
choice = 0
while askinput():
    print("Sending request %s ..." % choice)
    client_socket.send(bytes(str(choice), 'utf8'))

    #  Get the reply.
    message = client_socket.recv(1024).decode()
    print("Received reply %s [ %s ]" % (choice, message))

client_socket.close()
print("Connection with server closed.")


