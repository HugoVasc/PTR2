import threading
import socket
from random import randint

class client:
  clientId: 0b0
  produtor: False;
  consumo: 0b0
  valorCompra: 0b0
  producao: 0b0
  valorVenda: 0b0
  def __init__():
    self.clientId = bin(randint(0,1023))
    self.produtor = bool(randint(0,1))
    self.consumo = bin(randint(0,1023))
    self.valorCompra = bin(randint(0,1023))
    self.producao = bin(randint(0,1023))
    self.valorVenda = bin(randint(0,1023))

client1 = client()
print(client1)
def main():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(('localhost', 7777))
    except:
        return print('\nNão foi possívvel se conectar ao servidor!\n')

    username = input('Usuário> ')
    print('\nConectado')

    thread1 = threading.Thread(target=receiveMessages, args=[client])
    thread2 = threading.Thread(target=sendMessages, args=[client, username])

    thread1.start()
    thread2.start()


def receiveMessages(client):
    while True:
        try:
            msg = client.recv(2048).decode('utf-8')
            print(msg+'\n')
        except:
            print('\nNão foi possível permanecer conectado no servidor!\n')
            print('Pressione <Enter> Para continuar...')
            client.close()
            break
            

def sendMessages(client, username):
    while True:
        try:
            msg = input('\n')
            client.send(f'<{username}> {msg}'.encode('utf-8'))
        except:
            return


main()