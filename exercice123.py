# coding: utf-8
#ex1
lista = [x for x in range(2, 11, 2)]
print(lista)
lista2 = [x for x in range(1, 11) if x % 2 == 0]
print(lista2)

#ex2

cores = ["vermelho", "azul", "verde", "amarelo", "rosa", "preto"]
lista_numerada = [f"{i+1} - {j}" for i, j in enumerate(cores)]
print(lista_numerada)

participantes = ["joel", "jessica", "maria", "cris", "Larissa", "rafael", "marcus", "john"]
pagamento_realizado = ["joel", "jessica", "maria", "cris"]
#ex3
# Concatène " PAGO" aux noms qui figurent dans pagamento_realizado
resultado = [f"{i} PAGO" if i in pagamento_realizado else i for i in participantes]
print(resultado)
