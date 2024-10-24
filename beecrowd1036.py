# coding: utf-8
#beecrowd1036
a, b, c = map(float, input("Entrez les coefficients a, b et c : ").split())
# Calcul du discriminant
delta = b**2 - 4*a*c
while a!=0:
    if delta<0:
        print("nao e possivel")
    elif delta==0:
        x=(-b)/(2*a)
        print(f"A raiz é: {x:.5f}") 

    else:
         # Calcul des racines
         x1 = (-b + math.sqrt(delta)) / (2 * a)
         x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"As raízes são: R1 = {x1:.5f} e R2 = {x2:.5f}")