

# [] Criar matriz de lfsrs que irão criar a matriz K1 e K2
# [] Gerar seeds com tamanho apropriado para cada lfsr
# [] Criar as matrizes K1 e K2
# [] Receber o dado do cliente
# [] Gerar matriz P
# [] Gerar matriz M1 a partir de P e K1
# [] Fazer broadcast de M1

import threading
import socket

clients = [] #lista de clientes

def main():


    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #objeto socket ipv4 e tcp

    try:
        server.bind(('localhost', 7777))  #vamos tentar fazer uma ligação com o host e a porta
        server.listen() #poderia limitar o numero de conexoes exemplo server.listen(10) com 10 conexoes
    except:
        return print('\nNão foi possível iniciar o servidor!\n') #se der ruim na hora de escutar

    while True: #laco que aceita conexoes
        client, addr = server.accept()
        clients.append(client) #adicionando clientes na lista

        thread = threading.Thread(target=messagesTreatment, args=[client]) #vamos tratar de receber a mensagem de cada usuario
        thread.start()

  


  

def messagesTreatment(client):
    while True:
        try:
            msg = client.recv(2048) #recebo os bytes da msg 
            print(msg)
        except:
            deleteClient(client)
            break


def broadcast(msg, client): #funçao de broadcast
    for clientItem in clients:
        if clientItem != client:
            try:
                clientItem.send(msg)
            except:
                deleteClient(clientItem)


def deleteClient(client): #se quiser deletar cliente
    clients.remove(client)

main()