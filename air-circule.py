import math

# Lire le rayon du cercle
rayon = float(input("Entrez le rayon du cercle: "))

# Calculer l'aire (Aire = π * r^2)
aire = math.pi * rayon ** 2

# Afficher le résultat avec 2 décimales
print(f"L'aire du cercle est: {aire:.2f}")
