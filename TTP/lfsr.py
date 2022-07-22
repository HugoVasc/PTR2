from random import randint
def binToString(number:int, size:int):
  if(not(isinstance(number, int))):
    print("variable is not a number")
    raise ValueError("variable must be a number")
  else:
    bitString = (format(number, "0%db"%size))
    return bitString

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
  state = (state >> 1) | (newBit << 31)
  return state

def lfsr8 (seed):
  state = seed
  newBit = (state ^ (state >> 2) ^ (state >> 3) ^ (state >> 4)  ) & 1
  state = (state >> 1) | (newBit << 31)
  return state

def lfsr4 (seed):
  state = seed
  newBit = (state ^ (state >> 1) ) & 1
  state = (state >> 1) | (newBit << 31)
  return state

# first = seed = randint(0, (2^32)-1)
# print(str(seed) + " is " + binToString(seed) + " in binary" + " and it's size is " + str(len(binToString(seed))))
# count = 0
# while(1 != 0):
#   count += 1
#   if(not(isinstance(seed, int))):
#     int(seed)
#   seed = lfsr(seed, 10)
#   print(str(seed) + " is " + binToString(seed) + " in binary" + " and it's size is " + str(len(binToString(seed))))
#   if(seed == first): break
# print('O codigo se encerrou apos ' + str(count) + ' loops')