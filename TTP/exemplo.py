import lfsr
import random

n_clientes = 5

# for i in range(n_clientes):
#     seed = random.randint(1, (pow(2,32)-1))
#     line = lfsr.lfsr32(seed)
#     line = lfsr.binToString(line, 32)
#     matriz.append(line)
# print (matriz)


def getRandomLFSR (value:int):
    match value:
        case 0:
            seed = random.randint(1, (pow(2,4)-1))
            line = lfsr.lfsr4(seed)
            return lfsr.binToString(line,4), seed, 4
        case 1:
            seed = random.randint(1, (pow(2,8)-1))
            line = lfsr.lfsr8(seed)
            return lfsr.binToString(line,8), seed, 8
        case 2:
            seed = random.randint(1, (pow(2,16)-1))
            line = lfsr.lfsr16(seed)
            return lfsr.binToString(line,16), seed, 16
        case 3:
            seed = random.randint(1, (pow(2,32)-1))
            line = lfsr.lfsr32(seed)
            return lfsr.binToString(line,32), seed, 32
        case 4:
            seed = random.randint(1, (pow(2,64)-1))
            line = lfsr.lfsr64(seed)
            return lfsr.binToString(line,64), seed, 64
        

#Gerar matrizLFSR e matriz de Seeds
def createMatrix(n_clients):
    x = n_clients * 32
    line = ''
    k1 = []
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
            k1.append(line)
            line = ''
            if(len(pedacinhoLinha)>=32):
                tamanho = len(pedacinhoLinha) - (len(pedacinhoLinha) - 32)
                line = pedacinhoLinha[0:tamanho]
                k1.append(line)
                line = pedacinhoLinha[tamanho:]
        x = x - tamanhoLFSR
        matrizLFSR.append(tamanhoLFSR)
        matrizSeed.append(seed)
    if(len(k1) > n_clientes):
        k1.pop()
        print('popped')
    return matrizLFSR, matrizSeed, k1;

matrizLFSR, matrizSeed, k1 = createMatrix(n_clientes)
print(matrizLFSR, matrizSeed, k1)

# x = 32
# generatorRange = 3
# line = ""
# while( x != 0 ):
#     if((x < 32) & (x > 16)):
#         generatorRange = 2
#     elif((x < 16) & (x > 8)):
#         generatorRange = 1
#     else:
#         generatorRange = 0
#     pedacinhoLinha, valor  = randomLFSR(random.randint(0,generatorRange))
#     line = line.append(pedacinhoLinha)
#     x - valor;



# lfsr32 -> 32
# lfsr16 -> 16
# lfsr8 -> 8
# lfsr4 -> 4
# [ [16,8,4,4], [8,16,4,4] ]

# Gerar P
line = '01010011111010000000001101100010'
posicao = random.randint(0,31)
p = []
for i in range(0,31):
    if (i == posicao):
        p.append(line)
    else:
        randomBit = random.randint(1,pow(2,32)-1)
        p.append(lfsr.binToString(randomBit))
