

# [X] Criar matriz de lfsrs que irão criar a matriz K1 e K2
# [X] Gerar seeds com tamanho apropriado para cada lfsr
# [X] Criar as matrizes K1 e K2
# [] Receber o dado do cliente
# [] Gerar matriz P
# [] Gerar matriz M1 a partir de P e K1
# [] Fazer broadcast de M1

from operator import concat
import threading
import socket
import lib
import json

clients = [] #lista de clientes
LFSR_K1, Seeds_K1 = lib.SeedsAndTaps(5)
LFSR_K2, Seeds_K2 = lib.SeedsAndTaps(5)
def main():

    slot = 0

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    try:
        server.bind(('localhost', 7777))  
        server.listen() 
    except:
        return print('\nNão foi possível iniciar o servidor!\n') 

    while True: 
        client, addr = server.accept()
        clients.append(client) 

        thread = threading.Thread(target=messagesTreatment, args=[client]) 
        thread.start()
        if(slot == 0): broadcastSlot0()
        elif(slot == 96): slot = 0
        else: slot += 1

def messagesTreatment(client):
    while True:
        try:
            msg = client.recv(2048) 
            print(msg)
            broadcast(msg,client)
        except:
            deleteClient(client)
            break

def broadcast(msg, client): 
    for clientItem in clients:
        if clientItem != client:
            try:
                clientItem.send(msg)
            except:
                deleteClient(clientItem)

def broadcastSlot0 ():
    for clientItem in clients:
        clientItem.send(LFSR_K1)
        clientItem.send(Seeds_K1)
        clientItem.send(LFSR_K2)
        clientItem.send(Seeds_K2)


def deleteClient(client): 
    clients.remove(client)

main()