#-*- coding: utf-8 -*-
import random as rd
def eq2grau(a, b, c):
    Delta = b**2-4*a*c
    x1 = (-b-Delta**0.5)/(2*a)
    x2 = (-b+Delta**0.5)/(2*a)
    return x1, x2, Delta
for _ in range(10):
    a = rd.randint(1,10) #Gera aleatório entre 0 e 10.
    b = rd.randint(-5,5) #Gera aleatório entre -5 e 5.
    c = rd.randint(-2,7) #Gera aleatório entre -2 e 7.
    res = eq2grau(a, b, c)
    print(res)
    print("Coeficientes: {0}, {1}, {2}, soluções: {3:.2f},  {4:.2f}. ".format(a, b, c, res[0], res[1]))
