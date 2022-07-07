from random import randint



class cliente:
  clientId: 0b0000000000
  produtor: False;
  consumo: 0b0000000000
  valorCompra: 0b0000000000
  producao: 0b0000000000
  valorVenda: 0b0000000000

casa = cliente()

casa.clientId = bin(randint(0,1023))
casa.produtor = bool(randint(0,1))
casa.consumo = bin(randint(0,1023))
casa.valorCompra = bin(randint(0,1023))
casa.producao = bin(randint(0,1023))
casa.valorVenda = bin(randint(0,1023))

print('O cliente ' + casa.clientId + ' consumiu ' + casa.consumo + ' e vai pagar ' + casa.valorCompra + ' por esse consumo.')
print('O cliente ' + str(int(casa.clientId, 2)) + ' consumiu ' + str(int(casa.consumo, 2)) + ' e vai pagar ' + str(int(casa.valorCompra, 2)) + ' por esse consumo.')