from socket import socket,SOCK_STREAM,AF_INET
from threading import Thread

clients={}
address={}

HOST=""
PORT=8080
BUFSIZE=1024
ADDR=(HOST,PORT)
SERVER=socket(AF_INET,SOCK_STREAM)
SERVER.bind(ADDR)


def accept_client():
    while True:
        client,client_address=SERVER.accept()
        print("%s has connected"%client_address)
        client.send(bytes("Greeting from the cave"+"Now type your name","utf8"))
        address[client]=client_address
        Thread(target=handle_client,args=(client,)).start()
        

def handle_client(client):
    name=client.recv(BUFSIZ).decode("utf8")
    welcome="Welcome %s! if you want to quit type {quit}"
    client.send(bytes(welcome,"utf8"))
    msg="%s has joined the chat "%name
    broadcast(bytes(msg,"utf8"))
    clients[client]=name
    while True:
            msg=client.recv(BUFSIZE)
            if msg!=bytes("{quit}","utf8"):
                broadcast(msg,name+": ")
            else:
                client.send(bytes("{quit}","utf8"))
                client.close()
                del clients[client]
                broadcast(bytes("%s has left the chat "%name,"utf8"))
                break


def broadcast(msg,prefix=""):
    for socks in client:
        sock.send(bytes(prefix,"utf8")+msg)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_client)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
