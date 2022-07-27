import lfsr
import random

n_clientes = 5

matriz = []

for i in range(n_clientes):
    seed = random.randint(1, (pow(2,32)-1))
    line = lfsr.lfsr32(seed)
    line = lfsr.binToString(line, 32)
    matriz.append(line)
print (matriz)


