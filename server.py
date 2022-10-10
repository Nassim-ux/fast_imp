#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

from pynput import keyboard
from threading import Thread, Lock
from get_mails import fetch, init_service
from imp_mails import print_mail
from queue import Queue
import time
import os
import socket

class globalVars():
    pass

G = globalVars() #empty object to pass around global state
G.lock = Lock()
stop = 0

# get the hostname
host = socket.gethostname()
port = 5000  # initiate port no above 1024

server_socket = socket.socket() # get instance
server_socket.settimeout(60) # 1min
# look closely. The bind() function takes tuple as argument
server_socket.bind((host, port))  # bind host address and port together

# configure how many client the server can listen simultaneously
server_socket.listen(2)

def fetching_work(service, save_location):
    global stop
    q = []
    while not stop:
        # with G.lock:
        if not G.data_in.empty():
            q = G.data_in.get()
            
        q = fetch(service, q, save_location)
        if len(q) > 0:
            G.data_out.put(q)
            
        print('----------------------------------')
    
        print('Sleeping...')
        time.sleep(30)
        # data_in.put(q)
        # if stop == 1:
        #     exit()
        #     break 


def client_work(service, printer, save_location):
    
    stopped = False
    while not stopped:
        try: 
            print("\nWaiting for connection... \n")
            conn, address = server_socket.accept()  # accept new connection
            print("Connection from: " + str(address))
        except socket.timeout:
            stopped = True
            print("\nNo connection found: socket shuted down. \n")
            pass
        except:
            raise
        else:
            while 1:
                #  Wait for next request from client
                message = conn.recv(1024).decode()
                print("Received request: %s" % message)
                opt = str(message)
                if not message:
                    # if data is not received break
                    break
                # operation.put(opt)
                
                if opt == "4":
                    # with G.lock:
                    if not G.data_out.empty():
                        # mailsQ = G.data_out.get()
                        mailsQ = G.data_out.queue[0]
                        conn.send(bytes(str(mailsQ), 'utf8'))
                        G.data_in.put(mailsQ)
                    else:
                        print("******* Queue is empty.")
                        conn.send(bytes("Queue is empty.", 'utf8'))
                        
                elif opt == "5":
                    # with G.lock:
                    if not G.data_out.empty():
                        # mailsQ = G.data_out.get()
                        mailsQ = G.data_out.queue[0]
                        if len(mailsQ) > 0:
                            mail = mailsQ[0]
                            response = print_mail(service, mail, printer, save_location)
                            
                            if response == "success":
                                mailsQ.pop(0)
                            
                            conn.send(bytes(response, 'utf8'))
                            G.data_in.put(mailsQ)
                            G.data_out.put(mailsQ)
                        else:
                            print("******* Queue is empty.")
                            conn.send(bytes("Queue is empty.", 'utf8'))
                    else:
                        print("******* Queue is empty.")
                        conn.send(bytes("Queue is empty.", 'utf8'))
                    
                
                elif opt == "1":
                    # with G.lock:
                    if not G.data_out.empty():
                        # mailsQ = G.data_out.get()
                        mailsQ = G.data_out.queue[0]
                        for m in mailsQ:
                            if str(m._id) == "1":
                                m.addPriority()
                                mailsQ.sort(key= lambda x: ( x._priority, x._maildetail._date))

                        conn.send(bytes(str(mailsQ), 'utf8'))
                        G.data_in.put(mailsQ)
                        
                    else:
                        print("******** Queue is empty.")
                        conn.send(bytes("Queue is empty.", 'utf8'))
                
                elif opt == "2":
                    # with G.lock:
                    if not G.data_out.empty():
                        # mailsQ = G.data_out.get()
                        mailsQ = G.data_out.queue[0]
                        for m in mailsQ:
                            if str(m._id) == "1":
                                m.removePriority()
                                mailsQ.sort(key= lambda x: ( x._priority, x._maildetail._date))

                        conn.send(bytes(str(mailsQ), 'utf8'))
                        G.data_in.put(mailsQ)
                        
                    else:
                        print("******** Queue is empty.")
                        conn.send(bytes("Queue is empty.", 'utf8'))
                
                time.sleep(1)
                # if stop == 1:
                #     exit()
                #     break 
            conn.close()
            print("\n Connection closed. \n")
                    
    

G.data_in = Queue()
G.data_out = Queue()

printer = "Microsoft Print to PDF"
save_location = os.getcwd() + "\\files"

if not os.path.exists(save_location):
    os.makedirs('files')

service = init_service()  
mailsQ = []



def press_callback(key):
    global stop
    
    if key == keyboard.Key.esc:
        def stop_loop():
            global stop
            stop = 1
            # t1.do_run = False
            # t1.join()
            # t2.do_run = False
            # t2.join()
            # exitS.put(stop)
            # exitC.put(stop)
            return stop
        print('\nShutting down the server. \n')
        stop = stop_loop()
     

    return stop

if __name__ == "__main__":
    l = keyboard.Listener(on_press=press_callback)
    l.start()

    # with G.lock:
    G.data_in.put(mailsQ)

    t1 = Thread(target= fetching_work, args=(service, save_location))
    t1.start()

    t2 = Thread(target= client_work, args=(service, printer, save_location))
    t2.start()
