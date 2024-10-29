# -*- coding: utf-8 -*-
#valor = input().split()

#A = float(input())
#B = float(input())
#C = float(input())


A,B,C= map(float,input().split())

def area(A, B, C):
    area_triangle = (A * C / 2)
    pi = 3.14159
    area_circle = pi * (C ** 2) 
    area_trapezium = (1 / 2 * (A + B) * C)
    area_square = B ** 2
    area_rectangle = A * B
    return [area_triangle, area_circle, area_trapezium, area_square, area_rectangle]

# Calculer les aires
areas = area(A, B, C)

# Afficher les résultats
print(f"TRIANGULO: {areas[0]:.3f}")
print(f"CIRCULO: {areas[1]:.3f}")
print(f"TRAPEZIO: {areas[2]:.3f}")
print(f"QUADRADO: {areas[3]:.3f}")
print(f"RETANGULO: {areas[4]:.3f}")
