from random import randint
from bitarray import bitarray
from numpy import matrix


class client:
  clientId: 0b0
  produtor: False;
  consumo: 0b0
  valorCompra: 0b0
  producao: 0b0
  valorVenda: 0b0

def lfsr(seed, mask):
    result = seed
    nbits = mask.bit_length()-1
    while True:
        result = (result << 1)
        xor = result >> nbits
        if xor != 0:
            result ^= mask

        yield xor, result
      

def getRandomValues():
  cliente = client()
  cliente.clientId = bin(randint(0,1023))
  cliente.produtor = bool(randint(0,1))
  cliente.consumo = bin(randint(0,1023))
  cliente.valorCompra = bin(randint(0,1023))
  cliente.producao = bin(randint(0,1023))
  cliente.valorVenda = bin(randint(0,1023))
  return cliente

def getRandomPositions(cliente:client):
  def positionZero(): 
        line = bitarray(str(cliente.clientId)[2:] + str(cliente.consumo)[2:] + str(cliente.valorCompra)[2:])
        return line
  def positionOne(): 
        line = bitarray(str(cliente.clientId)[2:] + str(cliente.valorCompra)[2:] + str(cliente.consumo)[2:])
        return line
  def positionTwo(): 
        line = bitarray(str(cliente.valorCompra)[2:] + str(cliente.consumo)[2:] + str(cliente.clientId)[2:])
        return line
  def positionThree(): 
        line = bitarray(str(cliente.valorCompra)[2:] + str(cliente.clientId)[2:] + str(cliente.consumo)[2:])
        return line
  def positionFour(): 
        line = bitarray(str(cliente.consumo)[2:] + str(cliente.clientId)[2:] + str(cliente.valorCompra)[2:])
        return line
  def positionFive(): 
        line = bitarray(str(cliente.consumo)[2:] + str(cliente.valorCompra)[2:] + str(cliente.clientId)[2:])
        return line
  positions = {0:positionZero, 1:positionOne, 2:positionTwo, 3:positionThree, 4:positionFour, 5:positionFive}
  position = randint(0,5)
  line = positions.get(position)()
  return line

def createMatrix(line:bitarray):
  matrix = [line]
  for i in range(0,30):
    a = format(bin(randint(0,1023)), "010b")
    b = format(bin(randint(0,1023)), "010b")
    c = format(bin(randint(0,1023)), "010b")
    newLine = bitarray(a + b + c)
    matrix.append(newLine)
  return matrix
  

casa = getRandomValues()
line = getRandomPositions(casa)

print('O cliente ' + casa.clientId + ' consumiu ' + casa.consumo + ' e vai pagar ' + casa.valorCompra + ' por esse consumo.')
print('O cliente ' + str(int(casa.clientId, 2)) + ' consumiu ' + str(int(casa.consumo, 2)) + ' e vai pagar ' + str(int(casa.valorCompra, 2)) + ' por esse consumo.')

#print (line)

matrix = createMatrix(line)
for i in range(len(matrix)):
      print(matrix[i])