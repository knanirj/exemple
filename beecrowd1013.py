# coding: utf-8
#beecrowd1006
import math
# Lecture des trois valeurs entières
a, b, c = map(int, input().split())
print(a, b, c)

# Calcul du plus grand entre a et b
maiorAB = (a + b + abs(a - b)) // 2

# Calcul du plus grand entre maiorAB et c
maior = (maiorAB + c + abs(maiorAB - c)) // 2

# Affichage du résultat
print(f"{maior} eh o maior")