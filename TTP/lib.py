import random
import string
from tokenize import String

n_clientes = 5

### Binary and String ###
def binToString(number:int, size:int):
  if(not(isinstance(number, int))):
    print("variable is not a number")
    raise ValueError("variable must be a number")
  else:
    bitString = (format(number, "0%db"%size))
    return bitString

def stringToBinary(number:String):
    number = '0b'+number
    number = int(number,2)
    return number

#################################################

### LFSRs ###

def lfsr64 (seed):
  state = seed
  newBit = (state ^ (state >> 1) ^ (state >> 3) ^ (state >> 4)  ) & 1
  state = (state >> 1) | (newBit << 63)
  return state

def lfsr32 (seed):
  state = seed
  newBit = (state ^ (state >> 10) ^ (state >> 30) ^ (state >> 31) ) & 1
  state = (state >> 1) | (newBit << 31)
  return state

def lfsr16 (seed):
  state = seed
  newBit = (state ^ (state >> 1) ^ (state >> 3) ^ (state >> 12)  ) & 1
  state = (state >> 1) | (newBit << 15)
  return state

def lfsr8 (seed):
  state = seed
  newBit = (state ^ (state >> 2) ^ (state >> 3) ^ (state >> 4)  ) & 1
  state = (state >> 1) | (newBit << 7)
  return state

def lfsr4 (seed):
  state = seed
  newBit = (state ^ (state >> 1) ) & 1
  state = (state >> 1) | (newBit << 3)
  return state

################ Matriz K #######################

def getRandomLFSR (value:int):
    match value:
        case 0:
            seed = random.randint(1, (pow(2,4)-1))
            line = lfsr4(seed)
            return binToString(line,4), seed, 4
        case 1:
            seed = random.randint(1, (pow(2,8)-1))
            line = lfsr8(seed)
            return binToString(line,8), seed, 8
        case 2:
            seed = random.randint(1, (pow(2,16)-1))
            line = lfsr16(seed)
            return binToString(line,16), seed, 16
        case 3:
            seed = random.randint(1, (pow(2,32)-1))
            line = lfsr32(seed)
            return binToString(line,32), seed, 32
        case 4:
            seed = random.randint(1, (pow(2,64)-1))
            line = lfsr64(seed)
            return binToString(line,64), seed, 64
        

########### Gerar matrizLFSR e matriz de Seeds #############
def SeedsAndTaps(n_clients):
    x = n_clients * 32
    line = ''
    kn = []
    matrizLFSR = []
    matrizSeed = []
    while (x >=0 ):
        pedacinhoLinha, seed, tamanhoLFSR = getRandomLFSR(random.randint(0,4))
        if((len(line)+len(pedacinhoLinha))<32):
            line = line + (pedacinhoLinha)
        else:
            tamanho = 32 - len(line)
            line = line + (pedacinhoLinha[0:tamanho])
            pedacinhoLinha = pedacinhoLinha[tamanho:]
            kn.append(line)
            line = ''
            if(len(pedacinhoLinha)>=32):
                tamanho = len(pedacinhoLinha) - (len(pedacinhoLinha) - 32)
                line = pedacinhoLinha[0:tamanho]
                kn.append(line)
                line = pedacinhoLinha[tamanho:]
        x = x - tamanhoLFSR
        matrizLFSR.append(tamanhoLFSR)
        matrizSeed.append(seed)
    if(len(kn) > n_clientes):
        popped = kn.pop()
    return matrizLFSR, matrizSeed;
#################################################

def __MountaLinhaMatrizK (value:int, seed:int):
    match value:
        case 4:
            line = lfsr4(seed)
            return binToString(line,4)
        case 8:
            line = lfsr8(seed)
            return binToString(line,8)
        case 16:
            line = lfsr16(seed)
            return binToString(line,16)
        case 32:
            line = lfsr32(seed)
            return binToString(line,32)
        case 64:
            line = lfsr64(seed)
            return binToString(line,64)

def MontaMatrizK (matrizLFSR:list, matrizSeed:list):
    line = '';
    K=[]
    for i in range(len(matrizLFSR)-1):
        line = __MountaLinhaMatrizK(matrizLFSR[i], matrizSeed[i])
        K.append(line)  
    return K

matrizLFSR, matrizSeed = SeedsAndTaps(n_clientes)

################# Valida Ordem #######################
def validaOrdem (bid:string): # Retorna True se a ordem é válida
    bidType = bid[0] # 0 -> Venda; 1 -> Compra
    bidDuration = bid[1]
    price1 = bid[2:11]
    price2 = bid[12:21]
    quant = bid[22:31]
    price1 = int(lib.stringToBinary(price1))
    price2 = int(lib.stringToBinary(price2))
    if(bidType == '0'):
        if(price1 > price2):
            return True
        else:
            return False
    elif(bidType == '1'):
        if(price1 < price2):
            return True
        else:
            return False

    

#Testes
# k1_teste = MontaMatrizK(matrizLFSR, matrizSeed)
# k1_prova = MontaMatrizK(matrizLFSR, matrizSeed)

# print(k1_teste)
# print(k1_prova)
# print('\n')
# if (k1_teste == k1_prova):
#     print("Sucesso, K1 = K1 Prova\n")
# else:
#     print('\nFalha matrizes K1_teste e K1_prova divergem!!\n')


# # Gerar P
# line = '01010011111010000000001101100010'
# posicao = random.randint(0,31)
# p = []
# for i in range(0,31):
#     if (i == posicao):
#         p.append(line)
#     else:
#         randomBit = random.randint(1,pow(2,32)-1)
#         p.append(binToString(randomBit, 32))
#
# def getRandomPositions(cliente:client):
#   def positionZero(): 
#         line = bitarray(str(cliente.clientId)[2:] + str(cliente.consumo)[2:] + str(cliente.valorCompra)[2:])
#         return line
#   def positionOne(): 
#         line = bitarray(str(cliente.clientId)[2:] + str(cliente.valorCompra)[2:] + str(cliente.consumo)[2:])
#         return line
#   def positionTwo(): 
#         line = bitarray(str(cliente.valorCompra)[2:] + str(cliente.consumo)[2:] + str(cliente.clientId)[2:])
#         return line
#   def positionThree(): 
#         line = bitarray(str(cliente.valorCompra)[2:] + str(cliente.clientId)[2:] + str(cliente.consumo)[2:])
#         return line
#   def positionFour(): 
#         line = bitarray(str(cliente.consumo)[2:] + str(cliente.clientId)[2:] + str(cliente.valorCompra)[2:])
#         return line
#   def positionFive(): 
#         line = bitarray(str(cliente.consumo)[2:] + str(cliente.valorCompra)[2:] + str(cliente.clientId)[2:])
#         return line
#   positions = {0:positionZero, 1:positionOne, 2:positionTwo, 3:positionThree, 4:positionFour, 5:positionFive}
#   position = randint(0,5)
#   line = positions.get(position)()
#   return line
# def createMatrix(line:bitarray):
#   matrix = [line]
#   for i in range(0,30):
#     a = format(bin(randint(0,1023)), "010b")
#     b = format(bin(randint(0,1023)), "010b")
#     c = format(bin(randint(0,1023)), "010b")
#     newLine = bitarray(a + b + c)
#     matrix.append(newLine)
#   return matrix
